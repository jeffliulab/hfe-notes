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


def formalize_blueprint(blueprint: dict) -> dict:
    """Append one extra lecture-style section so first-pass pages read more like full notes."""
    result = dict(blueprint)
    sections = list(result.get("sections", []))
    existing_keys = {section_block.get("key") for section_block in sections}
    template_type = result.get("template_type")

    if template_type == "concept" and "formal_use" not in existing_keys:
        sections.append(
            section(
                "formal_use",
                "## 这套概念怎么真正拿来判断问题",
                "## How to Actually Use This Concept to Judge a Real Problem",
                body_zh="""
把概念页真正用起来时，不要停在定义。更实用的读法是固定沿着三步走：

1. 先定位当前任务和场景是什么。
2. 再问这页讲的限制、机制或风险，在这个场景里会怎样出现。
3. 最后把判断落回设计、流程、训练或组织改进。

这样概念才不会停在“知道术语”，而会变成“会分析问题”。
""",
                body_en="""
To use a concept page well, do not stop at the definition. A stronger reading follows three steps:

1. identify the task and context
2. ask how the mechanism, limit, or risk described on the page appears in that context
3. translate the judgment back into design, workflow, training, or organizational change

That is how the concept moves from “knowing the term” to “analyzing the problem.”
""",
            )
        )

    if template_type == "method" and "formal_quality" not in existing_keys:
        sections.append(
            section(
                "formal_quality",
                "## 怎样判断这个方法有没有真正写到位",
                "## How to Tell Whether This Method Has Actually Been Applied Well",
                body_zh="""
判断一个方法页有没有真正落地，可以固定看四件事：

- 输入是不是具体，而不是泛泛收材料
- 条目或步骤是不是回到了具体任务和具体场景
- 输出有没有把错误、后果和控制对应起来
- 结果能不能直接支持设计修改、验证、复盘或风险沟通

如果这四点里缺了几项，方法通常还是停在表面流程，没有变成真正可执行的分析。
""",
                body_en="""
You can judge whether a method has actually been applied by checking four things:

- are the inputs concrete rather than generic
- do the rows or steps return to specific tasks and contexts
- does the output connect error, consequence, and control clearly
- can the result directly support redesign, validation, review, or risk communication

If several of these are missing, the method usually remains a surface process rather than an executable analysis.
""",
            )
        )

    if template_type == "case" and "formal_review" not in existing_keys:
        sections.append(
            section(
                "formal_review",
                "## 复盘这个案例时固定看哪几层",
                "## Which Layers to Review Every Time in a Case",
                body_zh="""
复盘案例时，可以固定从四层往回看：

1. 事件链是怎样展开的。
2. 信息、界面和程序在哪些节点让局面变差。
3. 团队、组织和运行条件怎样放大了风险。
4. 如果要改，应该改设计、程序、训练、资源还是治理。

这样案例页就不会只剩“事故故事”，而会回到课程真正要训练的系统分析。
""",
                body_en="""
When reviewing a case, work backward through four layers:

1. how the event chain unfolded
2. where information, interface, and procedure worsened the situation
3. how team, organization, and operating conditions amplified the risk
4. whether improvement belongs in design, procedure, training, resources, or governance

That keeps the case from collapsing into a story and brings it back to the systems analysis the course is actually teaching.
""",
            )
        )

    result["sections"] = sections
    return result
