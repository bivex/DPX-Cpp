"""Open/Closed Principle (OCP) Detection Rule for C++."""

from __future__ import annotations

import re

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternCategory, PatternType

_DYNAMIC_CAST_RE = re.compile(r"\bdynamic_cast\s*<\s*([A-Za-z0-9_:]+)\s*[\*&]\s*>\s*\(")
_TYPEID_RE = re.compile(r"\btypeid\s*\([^)]+\)")


class OpenClosedPrincipleRule(BasePatternRule):
    """Detects violations and adherences to the Open/Closed Principle (OCP) in C++.

    Indicators:
    - OCP Violation (RTTI / Type-testing cascade): Method body containing cascades of `dynamic_cast`
      or `typeid` checks instead of polymorphic virtual dispatch.
    - OCP Adherence: Extensible polymorphic pure virtual interface design with clean implementations.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.OPEN_CLOSED

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Detect dynamic_cast / typeid cascades inside method bodies (OCP Violations)
        for fn in model.all_functions():
            simple_name = fn.name.split("::")[-1]
            if simple_name in ("operator==", "operator!=", "operator<", "operator="):
                continue
            body = fn.body_text or ""
            cast_matches = _DYNAMIC_CAST_RE.findall(body)
            typeid_matches = _TYPEID_RE.findall(body)
            total_type_checks = len(cast_matches) + len(typeid_matches)

            if total_type_checks >= 2:
                types_str = ", ".join(cast_matches) if cast_matches else "typeid inspections"
                evidences: list[Evidence] = [
                    self.evidence(
                        description=f"Method '{fn.name}' performs explicit RTTI type inspection ({types_str}) using dynamic_cast cascades, violating OCP",
                        weight=min(0.65, 0.40 + 0.10 * total_type_checks),
                        location=fn.location,
                        code_suffix="OCP_DYNAMIC_CAST_CASCADE",
                    ),
                    self.evidence(
                        description="Adding new types requires modifying this method rather than extending via virtual polymorphic dispatch",
                        weight=0.35,
                        location=fn.location,
                        code_suffix="OCP_FRAGILE_MODIFICATION",
                    ),
                ]

                detection = self.create_detection(
                    target_name=fn.name,
                    target_kind="ocp_dynamic_cast_violation",
                    evidences=evidences,
                    primary_location=fn.location,
                    summary=f"OCP Violation: Method '{fn.name}' uses {total_type_checks} RTTI/dynamic_cast checks instead of virtual dispatch",
                    base_score=0.35,
                )
                detection.pattern_category = PatternCategory.PRINCIPLE
                detections.append(detection)

        # 2. Detect OCP Adherence (Polymorphic Interface + Concrete Specializations)
        for proto in model.all_protocols():
            implementing_classes = model.find_records_implementing(proto.name)
            if len(implementing_classes) >= 2:
                impl_names = ", ".join(r.name for r in implementing_classes[:4])
                evidences = [
                    self.evidence(
                        description=f"Abstract interface '{proto.name}' enables open extension through {len(implementing_classes)} polymorphic implementations: {impl_names}",
                        weight=min(0.70, 0.40 + 0.10 * len(implementing_classes)),
                        location=proto.location,
                        code_suffix="OCP_POLYMORPHIC_ABSTRACTION",
                    ),
                    self.evidence(
                        description="New behaviors can be added by implementing the interface without modifying existing consumers",
                        weight=0.35,
                        location=proto.location,
                        code_suffix="OCP_EXTENSIBLE_DESIGN",
                    ),
                ]

                detection = self.create_detection(
                    target_name=proto.name,
                    target_kind="ocp_polymorphic_hierarchy",
                    evidences=evidences,
                    primary_location=proto.location,
                    related_locations=[r.location for r in implementing_classes],
                    summary=f"OCP Adherence: Interface '{proto.name}' supports open extension with {len(implementing_classes)} implementations",
                    base_score=0.35,
                )
                detection.pattern_category = PatternCategory.PRINCIPLE
                detections.append(detection)

        return detections
