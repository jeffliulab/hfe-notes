from __future__ import annotations

from textwrap import dedent


def _clean_text(value: str | None) -> str:
    return dedent(value or "").strip()


def _clean_lines(values: list[str] | None) -> list[str]:
    return [item for item in (_clean_text(value) for value in (values or [])) if item]


def localized_text(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": _clean_text(zh),
        "en": _clean_text(en),
    }


def localized_lines(zh: list[str] | None, en: list[str] | None) -> dict[str, list[str]]:
    return {
        "zh": _clean_lines(zh),
        "en": _clean_lines(en),
    }


def callout(
    kind: str,
    after_section: str,
    title_zh: str,
    title_en: str,
    body_zh: str = "",
    body_en: str = "",
    bullets_zh: list[str] | None = None,
    bullets_en: list[str] | None = None,
) -> dict:
    return {
        "kind": kind,
        "after_section": after_section,
        "title": localized_text(title_zh, title_en),
        "body": localized_text(body_zh, body_en),
        "bullets": localized_lines(bullets_zh, bullets_en),
    }


def section(
    key: str,
    title_zh: str,
    title_en: str,
    body_zh: str = "",
    body_en: str = "",
    bullets_zh: list[str] | None = None,
    bullets_en: list[str] | None = None,
    note_title_zh: str | None = None,
    note_title_en: str | None = None,
    note_body_zh: str = "",
    note_body_en: str = "",
    note_bullets_zh: list[str] | None = None,
    note_bullets_en: list[str] | None = None,
) -> dict:
    note = None
    if note_title_zh and note_title_en:
        note = callout(
            "note",
            key,
            note_title_zh,
            note_title_en,
            note_body_zh,
            note_body_en,
            note_bullets_zh,
            note_bullets_en,
        )
    return {
        "key": key,
        "title": localized_text(title_zh, title_en),
        "body": localized_text(body_zh, body_en),
        "bullets": localized_lines(bullets_zh, bullets_en),
        "note": note,
    }


def visual(
    after_section: str,
    source_file: str,
    caption_zh: str,
    caption_en: str,
    index: int = 0,
    alt_zh: str | None = None,
    alt_en: str | None = None,
    asset_name_contains: str | None = None,
    locator_contains: str | None = None,
) -> dict:
    return {
        "after_section": after_section,
        "source_file": source_file,
        "index": index,
        "caption": localized_text(caption_zh, caption_en),
        "alt": localized_text(alt_zh or caption_zh, alt_en or caption_en),
        "asset_name_contains": asset_name_contains,
        "locator_contains": locator_contains,
    }


def page_blueprint(
    template_type: str,
    page_intro_zh: str,
    page_intro_en: str,
    core_question_zh: str,
    core_question_en: str,
    must_learn_points_zh: list[str],
    must_learn_points_en: list[str],
    memory_anchor_zh: str,
    memory_anchor_en: str,
    sections: list[dict],
    examples: list[dict] | None = None,
    warnings: list[dict] | None = None,
    inline_visuals: list[dict] | None = None,
    summary_points_zh: list[str] | None = None,
    summary_points_en: list[str] | None = None,
) -> dict:
    return {
        "template_type": template_type,
        "page_intro": localized_text(page_intro_zh, page_intro_en),
        "core_question": localized_text(core_question_zh, core_question_en),
        "must_learn_points": localized_lines(must_learn_points_zh, must_learn_points_en),
        "memory_anchor": localized_text(memory_anchor_zh, memory_anchor_en),
        "sections": sections,
        "examples": examples or [],
        "warnings": warnings or [],
        "inline_visuals": inline_visuals or [],
        "summary_points": localized_lines(summary_points_zh, summary_points_en),
    }
