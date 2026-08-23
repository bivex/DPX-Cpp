"""Data Flow Analysis Service (SciTools Understand Parity)."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.data_flow import (
    DataFlowDirection,
    DataFlowGraph,
    DataFlowVariant,
    NodeKind,
)


class DataFlowService:
    """Domain Service for computing Forward (Data Flow Out) and Backward (Data Flow In) graphs."""

    def trace_data_flow_out(
        self,
        model: CodeModel,
        root_variable: str,
        variant: DataFlowVariant = DataFlowVariant.SIMPLIFIED,
        max_depth: int = 15,
    ) -> DataFlowGraph:
        """Trace forward data flow: what reads and propagates root_variable."""
        graph = DataFlowGraph(
            root_id=root_variable,
            direction=DataFlowDirection.OUT,
            variant=variant,
        )

        # Register root variable
        graph.add_node(
            node_id=root_variable,
            name=root_variable,
            kind=NodeKind.VARIABLE,
            is_root=True,
        )

        visited_vars: set[str] = set()
        queue: list[tuple[str, int]] = [(root_variable, 0)]

        while queue:
            var_name, depth = queue.pop(0)
            if depth >= max_depth:
                continue

            if var_name in visited_vars and depth > 0:
                continue
            visited_vars.add(var_name)

            # 1. Find all functions that read/use var_name
            reader_functions = [
                fn for fn in model.all_functions()
                if var_name in fn.reads_variables or var_name in fn.body_text
            ]

            for fn in reader_functions:
                fn_id = f"fn_{fn.name}"
                cluster_name = fn.namespace or fn.location.file_path.split("/")[-1] if fn.location else "global"
                graph.add_node(
                    node_id=fn_id,
                    name=fn.name,
                    kind=NodeKind.FUNCTION,
                    cluster=cluster_name,
                    file_path=fn.location.file_path if fn.location else "",
                    line=fn.location.line if fn.location else 1,
                )
                graph.add_edge(from_id=var_name, to_id=fn_id, kind="READS", location=fn.location)

                # 2. Check what variables this function writes or modifies
                written_vars = list(dict.fromkeys(fn.writes_variables + fn.modifies_variables))
                # If no explicit parsed writes, infer from body assignments
                if not written_vars:
                    for other_state in model.all_states():
                        if other_state.name != var_name and other_state.name in fn.body_text and f"{other_state.name} =" in fn.body_text:
                            written_vars.append(other_state.name)

                for w_var in written_vars:
                    w_kind = "MODIFIES" if w_var in fn.modifies_variables or (w_var == var_name) else "WRITES"
                    graph.add_node(
                        node_id=w_var,
                        name=w_var,
                        kind=NodeKind.VARIABLE,
                        cluster=cluster_name,
                    )
                    graph.add_edge(from_id=fn_id, to_id=w_var, kind=w_kind, location=fn.location)

                    if w_var != var_name and w_var not in visited_vars:
                        queue.append((w_var, depth + 1))

        return graph

    def trace_data_flow_in(
        self,
        model: CodeModel,
        root_variable: str,
        variant: DataFlowVariant = DataFlowVariant.SIMPLIFIED,
        max_depth: int = 15,
    ) -> DataFlowGraph:
        """Trace backward data flow: what produces/modifies root_variable."""
        graph = DataFlowGraph(
            root_id=root_variable,
            direction=DataFlowDirection.IN,
            variant=variant,
        )

        graph.add_node(
            node_id=root_variable,
            name=root_variable,
            kind=NodeKind.VARIABLE,
            is_root=True,
        )

        visited_vars: set[str] = set()
        queue: list[tuple[str, int]] = [(root_variable, 0)]

        while queue:
            var_name, depth = queue.pop(0)
            if depth >= max_depth:
                continue

            if var_name in visited_vars and depth > 0:
                continue
            visited_vars.add(var_name)

            # 1. Find all functions that write/modify var_name
            writer_functions = [
                fn for fn in model.all_functions()
                if var_name in fn.writes_variables or var_name in fn.modifies_variables
            ]

            for fn in writer_functions:
                fn_id = f"fn_{fn.name}"
                cluster_name = fn.namespace or fn.location.file_path.split("/")[-1] if fn.location else "global"
                graph.add_node(
                    node_id=fn_id,
                    name=fn.name,
                    kind=NodeKind.FUNCTION,
                    cluster=cluster_name,
                    file_path=fn.location.file_path if fn.location else "",
                    line=fn.location.line if fn.location else 1,
                )
                w_kind = "MODIFIED_BY" if var_name in fn.modifies_variables else "WRITTEN_BY"
                graph.add_edge(from_id=var_name, to_id=fn_id, kind=w_kind, location=fn.location)

                # 2. Find variables that this function reads
                for r_var in fn.reads_variables:
                    graph.add_node(
                        node_id=r_var,
                        name=r_var,
                        kind=NodeKind.VARIABLE,
                        cluster=cluster_name,
                    )
                    graph.add_edge(from_id=fn_id, to_id=r_var, kind="READS_FROM", location=fn.location)

                    if r_var != var_name and r_var not in visited_vars:
                        queue.append((r_var, depth + 1))

        return graph

    def trace_relationship(
        self,
        model: CodeModel,
        source: str,
        target: str,
        max_depth: int = 15,
    ) -> DataFlowGraph:
        """Trace paths specifically connecting source and target entities (Relationship variant)."""
        full_out_graph = self.trace_data_flow_out(model, source, variant=DataFlowVariant.RELATIONSHIP, max_depth=max_depth)

        # Filter nodes and edges to only those that lie on paths from source to target
        adj: dict[str, list[str]] = {}
        for edge in full_out_graph.edges:
            adj.setdefault(edge.from_id, []).append(edge.to_id)

        target_nodes = {target, f"fn_{target}"}

        # Backtrack DFS to find all reachable nodes to target
        reachable_to_target: set[str] = set()

        def can_reach(u: str, path: list[str]) -> bool:
            if u in target_nodes:
                reachable_to_target.update(path + [u])
                return True
            found = False
            for v in adj.get(u, []):
                if v not in path:
                    if can_reach(v, path + [u]):
                        found = True
            return found

        can_reach(source, [])

        filtered_graph = DataFlowGraph(
            root_id=source,
            direction=DataFlowDirection.OUT,
            variant=DataFlowVariant.RELATIONSHIP,
        )

        for node_id in reachable_to_target:
            if node_id in full_out_graph.nodes:
                node = full_out_graph.nodes[node_id]
                filtered_graph.add_node(
                    node_id=node.id,
                    name=node.name,
                    kind=node.kind,
                    cluster=node.cluster,
                    file_path=node.file_path,
                    line=node.line,
                    is_root=node.is_root,
                )

        for edge in full_out_graph.edges:
            if edge.from_id in reachable_to_target and edge.to_id in reachable_to_target:
                filtered_graph.add_edge(edge.from_id, edge.to_id, edge.kind, edge.location)

        return filtered_graph
