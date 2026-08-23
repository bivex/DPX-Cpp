"""Liskov Substitution Principle (LSP) Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternCategory, PatternType


class LiskovSubstitutionRule(BasePatternRule):
    """Detects violations of the Liskov Substitution Principle (LSP).

    Indicators:
    - Subclass/implementor throwing `UnsupportedOperationException`, `IllegalStateException`,
      or `NotImplementedException` in overridden methods of an interface/superclass.
    - Subclasses refusing or disabling parent contract behaviors.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.LISKOV_SUBSTITUTION

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for rec in model.all_records():
            if not rec.implemented_protocols:
                continue

            for method in rec.methods:
                body = method.body_text or ""
                # Check for refusal of parent contract
                has_unsupported_op = any(
                    exc in body
                    for exc in (
                        "UnsupportedOperationException",
                        "NotImplementedException",
                        "OperationNotSupportedException",
                    )
                )

                if has_unsupported_op:
                    evidences: list[Evidence] = [
                        self.evidence(
                            description=f"Class '{rec.name}' overrides method '{method.name}' throwing UnsupportedOperationException, violating LSP substitutability",
                            weight=0.70,
                            location=method.location,
                            code_suffix="LSP_UNSUPPORTED_OPERATION",
                        ),
                        self.evidence(
                            description=f"Client expecting base type ({', '.join(rec.implemented_protocols)}) cannot transparently substitute with '{rec.name}'",
                            weight=0.40,
                            location=rec.location,
                            code_suffix="LSP_CONTRACT_BREACH",
                        ),
                    ]

                    detection = self.create_detection(
                        target_name=f"{rec.name}.{method.name.split('.')[-1]}",
                        target_kind="lsp_contract_violation",
                        evidences=evidences,
                        primary_location=method.location,
                        summary=f"LSP Violation: '{rec.name}.{method.name.split('.')[-1]}' rejects base contract by throwing UnsupportedOperationException",
                        base_score=0.45,
                    )
                    detection.pattern_category = PatternCategory.PRINCIPLE
                    detections.append(detection)

        return detections
