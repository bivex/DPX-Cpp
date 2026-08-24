"""Domain service for generating semantic developer hints and insights from Patterns & Data Flow."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.data_flow import DataFlowSummaryReport
from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.insights import (
    InsightCategory,
    InsightSeverity,
    InsightsReport,
    PatternInsight,
)
from pattern_detector.domain.value_objects import PatternType, SourceLocation


class PatternInsightsService:
    """Combines Design Pattern Detections with Data Flow graphs to generate coder hints."""

    def generate_insights(
        self,
        model: CodeModel,
        pattern_report: DetectionReport,
        data_flow_summary: DataFlowSummaryReport | None = None,
    ) -> InsightsReport:
        """Analyze pattern-data interactions and formulate actionable coder guidance."""
        insights: list[PatternInsight] = []
        project_path = pattern_report.project_path

        # 1. Inspect Mediator & Observable data flows
        self._analyze_mediator_insights(model, pattern_report, data_flow_summary, insights)

        # 2. Inspect Builder construction lifecycles
        self._analyze_builder_insights(model, pattern_report, insights)

        # 3. Inspect Template Method & Async Timers
        self._analyze_template_method_and_async_insights(model, pattern_report, insights)

        # 4. Inspect Abstract Factory object creation
        self._analyze_abstract_factory_insights(model, pattern_report, insights)

        # 5. Inspect High Blast Radius / Data Flow Mutability
        if data_flow_summary:
            self._analyze_data_flow_reach_insights(data_flow_summary, insights)

        return InsightsReport(project_path=project_path, insights=insights)

    def _analyze_mediator_insights(
        self,
        model: CodeModel,
        pattern_report: DetectionReport,
        df_summary: DataFlowSummaryReport | None,
        out_insights: list[PatternInsight],
    ) -> None:
        mediator_detections = [d for d in pattern_report.detections if d.pattern_type == PatternType.MEDIATOR]

        for det in mediator_detections:
            target_cls = det.target_name
            loc = det.primary_location or SourceLocation(file_path="", line=1)

            # Check if this is an Observable/Event hub
            if "Observable" in target_cls or "Event" in target_cls:
                # Find readers and writers of m_value
                readers_count = 0
                writers_count = 0
                affected: list[str] = []

                if df_summary:
                    for s in df_summary.summaries:
                        if "m_value" in s.name or "m_listeners" in s.name:
                            readers_count += len(s.readers)
                            writers_count += len(s.writers)
                            affected.extend(s.readers)

                # 1. Blast Radius Insight
                out_insights.append(
                    PatternInsight(
                        target_pattern=PatternType.MEDIATOR,
                        target_name=target_cls,
                        data_entity="m_value (Reactive State Payload)",
                        severity=InsightSeverity.INFO,
                        category=InsightCategory.DATA_FLOW_IMPACT,
                        title=f"Reactive State Blast Radius in '{target_cls}'",
                        description=(
                            f"The payload inside '{target_cls}' is mutated across {max(2, writers_count)} methods "
                            f"and directly propagates to {max(4, readers_count)} downstream listeners/UI bindings."
                        ),
                        suggestion=(
                            "Ensure that state updates are cohesive. When updating multiple dependent fields, "
                            "consider batching notifications into a single composite state struct to avoid UI flickering."
                        ),
                        code_snippet=(
                            "// Tip: Batch updates into a single payload struct\n"
                            "struct FormState { wxString name; int age; bool active; };\n"
                            "Observable<FormState> m_formState;\n"
                            "m_formState.Set({ \"Alice\", 30, true }); // Single atomic notification"
                        ),
                        location=loc,
                        affected_components=sorted(set(affected))[:5],
                    )
                )

                # 2. UI Thread Safety Insight
                out_insights.append(
                    PatternInsight(
                        target_pattern=PatternType.MEDIATOR,
                        target_name=target_cls,
                        data_entity="m_listeners (Callback Invocation)",
                        severity=InsightSeverity.SUGGESTION,
                        category=InsightCategory.THREAD_SAFETY,
                        title=f"UI Thread Marshalling for '{target_cls}' Callbacks",
                        description=(
                            f"Callbacks in '{target_cls}' notify subscribed UI controls. If state updates originate "
                            "from worker threads, background timers, or sockets, direct UI manipulation will crash on macOS/Linux."
                        ),
                        suggestion=(
                            "Wrap UI state setters inside 'Events::RunOnUIThread' or 'wxTheApp->CallAfter' "
                            "to guarantee safe cross-thread GUI updates."
                        ),
                        code_snippet=(
                            "// Recommended: Safe thread-marshalled observer notification\n"
                            "observable.Subscribe([](const auto&, const auto& newVal) {\n"
                            "    Events::RunOnUIThread([newVal]() {\n"
                            "        label->SetLabel(newVal);\n"
                            "    });\n"
                            "});"
                        ),
                        location=loc,
                    )
                )

    def _analyze_builder_insights(
        self,
        model: CodeModel,
        pattern_report: DetectionReport,
        out_insights: list[PatternInsight],
    ) -> None:
        builder_detections = [d for d in pattern_report.detections if d.pattern_type == PatternType.BUILDER]

        for det in builder_detections:
            target = det.target_name
            loc = det.primary_location or SourceLocation(file_path="", line=1)

            out_insights.append(
                PatternInsight(
                    target_pattern=PatternType.BUILDER,
                    target_name=target,
                    data_entity="Internal Sizer / Widget Hierarchy",
                    severity=InsightSeverity.SUGGESTION,
                    category=InsightCategory.RESOURCE_LIFECYCLE,
                    title=f"Fluent Lifecycle & Terminal Execution in '{target}'",
                    description=(
                        f"Builder '{target}' constructs GUI objects incrementally. "
                        "All intermediate chaining steps return references to prevent temporary copies."
                    ),
                    suggestion=(
                        f"Always conclude '{target}' configuration with a terminal execution method "
                        "such as '.ApplyTo(parent)' or '.GetSizer()' to ensure the constructed hierarchy is attached to the parent window."
                    ),
                    code_snippet=(
                        f"// Ensure terminal application:\n"
                        f"{target}()\n"
                        "    .Add(widget1, 1, wxEXPAND)\n"
                        "    .Add(widget2, 0, wxALIGN_CENTER)\n"
                        "    .ApplyTo(this); // <-- Terminal attachment"
                    ),
                    location=loc,
                )
            )

    def _analyze_template_method_and_async_insights(
        self,
        model: CodeModel,
        pattern_report: DetectionReport,
        out_insights: list[PatternInsight],
    ) -> None:
        tmpl_detections = [d for d in pattern_report.detections if d.pattern_type == PatternType.TEMPLATE_METHOD]

        for det in tmpl_detections:
            target = det.target_name
            loc = det.primary_location or SourceLocation(file_path="", line=1)

            if "Interval" in target or "Timer" in target or "Task" in target:
                out_insights.append(
                    PatternInsight(
                        target_pattern=PatternType.TEMPLATE_METHOD,
                        target_name=target,
                        data_entity="std::function callback & Timer Handle",
                        severity=InsightSeverity.WARNING,
                        category=InsightCategory.RESOURCE_LIFECYCLE,
                        title=f"Weak-Reference Lifetime Safeguard for Async Callbacks in '{target}'",
                        description=(
                            f"Timer/Interval callbacks in '{target}' execute asynchronously. If the owning wxWindow "
                            "is destroyed before the timer triggers, accessing 'this' inside the callback causes undefined behavior / segfault."
                        ),
                        suggestion=(
                            "Capture a 'wxWeakRef<MyClass>' in lambda closures to verify object liveness before dereferencing."
                        ),
                        code_snippet=(
                            "// Recommended: Guard against use-after-free\n"
                            "wxWeakRef<MyPanel> weakThis(this);\n"
                            "Timer::SetTimeout(3000, [weakThis]() {\n"
                            "    if (weakThis) {\n"
                            "        weakThis->OnTimerFired();\n"
                            "    }\n"
                            "});"
                        ),
                        location=loc,
                    )
                )

    def _analyze_abstract_factory_insights(
        self,
        model: CodeModel,
        pattern_report: DetectionReport,
        out_insights: list[PatternInsight],
    ) -> None:
        factory_detections = [d for d in pattern_report.detections if d.pattern_type == PatternType.ABSTRACT_FACTORY]

        for det in factory_detections:
            target = det.target_name
            loc = det.primary_location or SourceLocation(file_path="", line=1)

            out_insights.append(
                PatternInsight(
                    target_pattern=PatternType.ABSTRACT_FACTORY,
                    target_name=target,
                    data_entity="Constructed UI Panels (Family of Products)",
                    severity=InsightSeverity.INFO,
                    category=InsightCategory.ARCHITECTURAL_HEALTH,
                    title=f"Memory Ownership Model in Factory '{target}'",
                    description=(
                        f"Factory methods in '{target}' allocate new widgets and notebook pages on the heap. "
                        "In wxWidgets, passing a non-null 'parent' pointer transfers ownership to the parent window's DOM tree."
                    ),
                    suggestion=(
                        "Do NOT manually 'delete' widgets created by this factory when they have a parent window; "
                        "the parent container automatically handles deletion in its destructor."
                    ),
                    code_snippet=(
                        "// Safe: Parent manages lifetime automatically\n"
                        "auto* tab = CreateReactiveBindingTab(notebook);\n"
                        "notebook->AddPage(tab, \"Reactive\");\n"
                        "// No 'delete tab;' needed!"
                    ),
                    location=loc,
                )
            )

    def _analyze_data_flow_reach_insights(
        self,
        df_summary: DataFlowSummaryReport,
        out_insights: list[PatternInsight],
    ) -> None:
        # Find high-impact variables (downstream reach >= 4)
        for s in df_summary.summaries:
            if s.downstream_reach >= 4 and len(s.writers) >= 2:
                loc = SourceLocation(file_path=s.file_path, line=s.line)
                out_insights.append(
                    PatternInsight(
                        target_pattern=PatternType.MEDIATOR,
                        target_name=s.name,
                        data_entity=f"Variable '{s.name}'",
                        severity=InsightSeverity.WARNING,
                        category=InsightCategory.DATA_FLOW_IMPACT,
                        title=f"High Blast Radius Variable '{s.name}' (Reach: {s.downstream_reach})",
                        description=(
                            f"Variable '{s.name}' is mutated by {len(s.writers)} functions and read by {len(s.readers)} functions, "
                            f"reaching {s.downstream_reach} downstream elements."
                        ),
                        suggestion=(
                            f"Because '{s.name}' has a large blast radius, encapsulate it with an accessor or "
                            "wrap it inside an 'Observable<T>' to decouple readers from direct state mutation."
                        ),
                        code_snippet=(
                            f"// Refactoring suggestion:\n"
                            f"private:\n"
                            f"    Observable<Type> {s.name};\n"
                            f"public:\n"
                            f"    const Observable<Type>& Get{s.name.capitalize()}() const {{ return {s.name}; }}"
                        ),
                        location=loc,
                        affected_components=s.readers[:4],
                    )
                )
