"""Open/Closed Principle (OCP) Detection Rule."""

from __future__ import annotations

import re

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternCategory, PatternType

_INSTANCEOF_RE = re.compile(r"\binstanceof\s+([A-Za-z0-9_]+)")


class OpenClosedPrincipleRule(BasePatternRule):
    """Detects violations and adherences to the Open/Closed Principle (OCP).

    Indicators:
    - OCP Violation (Type-testing cascade): Method body containing cascades of `instanceof`
      or switch-on-type checks instead of polymorphic dispatch.
    - OCP Adherence: Extensible polymorphic interface design with clean implementations.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.OPEN_CLOSED

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Detect instanceof cascades inside method bodies (OCP Violations)
        for fn in model.all_functions():
            if fn.name.split(".")[-1] in ("equals", "compareTo", "toString", "hashCode"):
                continue
            body = fn.body_text or ""
            instanceof_matches = _INSTANCEOF_RE.findall(body)
            if len(instanceof_matches) >= 2:
                types_str = ", ".join(instanceof_matches)
                evidences: list[Evidence] = [
                    self.evidence(
                        description=f"Method '{fn.name}' performs explicit type inspection on ({types_str}) using 'instanceof' cascades, violating OCP",
                        weight=min(0.65, 0.40 + 0.10 * len(instanceof_matches)),
                        location=fn.location,
                        code_suffix="OCP_INSTANCEOF_CASCADE",
                    ),
                    self.evidence(
                        description="Adding new types requires modifying this method rather than extending via polymorphism",
                        weight=0.35,
                        location=fn.location,
                        code_suffix="OCP_FRAGILE_MODIFICATION",
                    ),
                ]

                detection = self.create_detection(
                    target_name=fn.name,
                    target_kind="ocp_type_switch_violation",
                    evidences=evidences,
                    primary_location=fn.location,
                    summary=f"OCP Violation: Method '{fn.name}' uses {len(instanceof_matches)} instanceof checks instead of polymorphic dispatch",
                    base_score=0.35,
                )
                detection.pattern_category = PatternCategory.PRINCIPLE
                detections.append(detection)

        # 2. Detect OCP Adherence (Polymorphic extensibility point)
        for proto in model.all_protocols():
            rec_impls = model.find_records_implementing(proto.name)
            if len(rec_impls) >= 3 and len(proto.methods) >= 1:
                impls_str = ", ".join(r.name for r in rec_impls)
                evidences = [
                    self.evidence(
                        description=f"Interface '{proto.name}' is open for extension with {len(rec_impls)} polymorphic implementations: {impls_str}",
                        weight=0.55,
                        location=proto.location,
                        code_suffix="OCP_POLYMORPHIC_EXTENSION",
                    ),
                    self.evidence(
                        description=f"Standard contract defines {len(proto.methods)} methods without requiring caller modifications",
                        weight=0.30,
                        location=proto.location,
                        code_suffix="OCP_CLOSED_CONTRACT",
                    ),
                ]

                detection = self.create_detection(
                    target_name=proto.name,
                    target_kind="ocp_polymorphic_hierarchy",
                    evidences=evidences,
                    primary_location=proto.location,
                    related_locations=[r.location for r in rec_impls],
                    summary=f"OCP Adherence: Interface '{proto.name}' provides polymorphic extensibility across {len(rec_impls)} classes",
                    base_score=0.30,
                )
                detection.pattern_category = PatternCategory.PRINCIPLE
                detections.append(detection)

        return detections
