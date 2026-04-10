from __future__ import annotations

from textwrap import dedent


def pair(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": dedent(zh).strip(),
        "en": dedent(en).strip(),
    }


RISK_METHODS_CONTENT: dict[str, dict[str, str]] = {
    "error_analysis_methods": pair(
        """
        ## 一眼看懂

        错误分析与调查流程这一页，讲的是“如何把事故讲清楚”。重点不是写一段故事，而是把事实、时间线、因果链和改进行动拆开处理。

        ## 调查的基本顺序

        1. 先收集事实：发生了什么、谁在场、系统处于什么状态。
        2. 再建时间线：事件是如何一步步演化的。
        3. 然后区分直接触发因素、前置条件和更深层的组织/设计因素。
        4. 最后把分析结果翻译成能执行的改进措施。

        ## NTSB 风格的重要提醒

        - 先有事实，再谈原因
        - 不要把“结论”提前塞进证据描述里
        - 一个后果通常不只有一条原因线
        - 真正有价值的报告必须能让后续设计、训练、程序或监管发生变化

        ## 难点讲解

        事故分析最常见的错误，是过早收束到一个显眼原因。例如“飞行员失误”或“护士看错了”。这会让你错过：

        - 信息呈现是否误导
        - 任务顺序是否本身容易出错
        - 程序是否与真实工作负荷冲突
        - 组织是否长期容忍危险偏差
        """,
        """
        ## At a Glance

        Error analysis is about turning an event into an explainable structure: facts, timeline, causal layers, and actionable recommendations.

        ## Basic Investigation Flow

        1. Gather facts.
        2. Build the event sequence.
        3. Separate triggers, preconditions, and deeper organizational or design contributors.
        4. Translate findings into interventions.

        ## NTSB-Style Discipline

        - facts come before conclusions
        - evidence and interpretation should not be collapsed
        - one outcome usually has multiple contributing paths
        - good analysis ends in design, training, procedure, or policy change

        ## Common Difficulty

        Investigations often stop too early at the most visible human action. The deeper task is to explain why the system made that action likely, hard to detect, or hard to recover from.
        """,
    ),
    "task_analysis": pair(
        """
        ## 一眼看懂

        任务分析的价值，在于把“用户在用产品”这件看起来连续的事情，拆成可以观察、可以讨论、可以评估风险的步骤链。

        ## 做 task analysis 时到底在拆什么

        - 用户想达成的目标
        - 为了达成目标必须经过的步骤
        - 每一步需要看到什么、判断什么、操作什么
        - 哪一步如果失败，会直接影响安全、有效性或后续恢复

        ## 为什么它是后续风险分析的地基

        如果你连任务都没拆清楚，后面几乎所有问题都会变模糊：

        - use error 不知道是在哪一步发生
        - critical task 无法界定
        - risk control 不知道该改界面、标签、流程还是培训

        ## 难点讲解

        任务分析不是把说明书抄一遍。真正有用的 task analysis 会把“系统要求用户做什么”和“用户在现实里实际怎么做”都放进去。也就是说，你要同时看理想流程和真实流程之间的偏差。
        """,
        """
        ## At a Glance

        Task analysis turns a continuous use episode into observable, discussable, and risk-assessable steps.

        ## What Gets Decomposed

        - the user's goal
        - the steps required to reach that goal
        - the information, judgment, and action demands at each step
        - the points where failure would affect safety or recovery

        ## Why It Matters

        Task analysis is the foundation for later work. Without it, use errors, critical tasks, and controls remain vague.

        ## Common Difficulty

        A useful task analysis is not just a rewritten instruction manual. It compares the ideal flow with the real flow that users are likely to perform in context.
        """,
    ),
    "urra_methods": pair(
        """
        ## 一眼看懂

        URRA 的核心作用，是把“任务步骤”“可能的使用错误”“危险情境”“伤害后果”和“风险控制”串成一张可追踪的链，而不是只留下零散担忧。

        ## 一条 URRA 记录通常在回答什么

        - 用户在做哪一个 use step
        - 可能出现什么错误行为
        - 这个错误会把系统带到什么危险情境
        - 最终可能造成什么 harm
        - 现有控制是否足够，是否还要增加新的控制

        ## 写 URRA 时的逻辑顺序

        先从任务与场景出发，再写错误，再写后果，最后才讨论控制。顺序不能反过来。因为如果你先想控制措施，很容易把分析写成“已有设计说明书”，而不是对风险的真正展开。

        ## 难点讲解

        URRA 写得不好的常见原因有两个：

        - 把错误写得太笼统，例如“使用不当”
        - 把 harm 写得太近，例如只写“剂量错误”，却没有继续写到病人可能受到什么伤害

        好的 URRA 必须具体到足以支持后续验证。
        """,
        """
        ## At a Glance

        URRA links task steps, possible use errors, hazardous situations, harms, and controls into a traceable risk chain.

        ## What A URRA Row Answers

        - which use step is under analysis
        - what user error might occur
        - what hazardous situation could follow
        - what harm could result
        - whether current controls are sufficient

        ## Writing Logic

        Start from task and scenario, then describe error, then consequence, and only then discuss controls. Reversing that order often turns the document into a design justification rather than a risk analysis.

        ## Common Difficulty

        Weak URRAs use vague phrases such as “improper use” or stop too early at intermediate outcomes. Strong URRAs are specific enough to support validation planning.
        """,
    ),
    "known_problem_and_event_tree": pair(
        """
        ## 一眼看懂

        这一页把两种补盲方法放在一起：Known Problem Analysis 让你从历史问题反推今天还可能漏掉什么；Event Tree 则让你从一个起点事件往后展开，检查后果路径是否被低估。

        ## Known Problem Analysis 在补什么

        - 既往投诉、事故、CAPA、文献、竞品问题
        - 团队已经知道但还没系统写进风险文件的问题
        - 新设计可能重新引入的老问题

        ## Event Tree 在补什么

        - 某个起始事件发生之后，后续会不会被拦住
        - 如果没拦住，会沿哪些分支走向不同严重程度
        - 中间哪些防护层是真正关键节点

        ## 为什么这页重要

        只做主流程分析，很容易漏掉低频但高后果的情况。Known Problem Analysis 和 Event Tree 的共同作用，就是逼你从“主路径之外”再看一次系统。

        ## 难点讲解

        不要把 known problem 当成“旧项目遗留列表”，也不要把 event tree 当成只在核工业里才用的大工具。课程想强调的是：任何高风险系统都需要一个机制，提醒团队去看“我们还没想到的分支”。
        """,
        """
        ## At a Glance

        This page pairs two gap-finding methods. Known Problem Analysis looks backward to previously observed issues, while an Event Tree looks forward from an initiating event to possible downstream outcomes.

        ## What Each Method Adds

        - Known Problem Analysis surfaces recurring, historical, or already-recognized issues that may be missing from current risk files.
        - Event Trees expand what happens after an initiating event and test whether barriers actually interrupt the sequence.

        ## Why It Matters

        Main workflow analysis often misses low-frequency, high-consequence paths. These methods force the team to examine the edges of the system rather than only the expected path.
        """,
    ),
}
