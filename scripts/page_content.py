from __future__ import annotations

from content_aviation_automation import AVIATION_AUTOMATION_CONTENT
from content_cases_ethics import CASES_ETHICS_CONTENT
from content_foundations import FOUNDATIONS_CONTENT
from content_human_performance import HUMAN_PERFORMANCE_CONTENT
from content_medical_devices import MEDICAL_DEVICES_CONTENT
from content_risk_methods import RISK_METHODS_CONTENT


PAGE_CONTENT: dict[str, dict[str, str]] = {}

for content_group in (
    FOUNDATIONS_CONTENT,
    RISK_METHODS_CONTENT,
    MEDICAL_DEVICES_CONTENT,
    AVIATION_AUTOMATION_CONTENT,
    HUMAN_PERFORMANCE_CONTENT,
    CASES_ETHICS_CONTENT,
):
    overlap = set(PAGE_CONTENT).intersection(content_group)
    if overlap:
        raise ValueError(f"Duplicate page content keys: {sorted(overlap)}")
    PAGE_CONTENT.update(content_group)
