from __future__ import annotations

from textwrap import dedent


def pair(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": dedent(zh).strip(),
        "en": dedent(en).strip(),
    }


AVIATION_AUTOMATION_CONTENT: dict[str, dict[str, str]] = {
    "aviation_automation_intro": pair(
        """
        ## 一眼看懂

        航空与自动化导论这一页，讲的不是“自动化越来越先进”这么简单，而是一个更关键的问题：当机器承担更多功能后，人到底还剩下什么工作，这些工作会不会反而更难。

        ## 核心逻辑

        - 自动化的第一层收益通常是减轻重复负担、提高精度、稳定流程。
        - 但自动化也会把人的角色推向监控、接管、模式理解和异常处置，这些工作平时少做，一出问题却要求很高。
        - 所以自动化不是把人拿掉，而是重写了人的任务结构。

        ## 真正要学会的判断

        读这页时要反复问三件事：

        1. 自动化接管了什么。
        2. 人保留了什么。
        3. 剩下的人类任务是否仍然可行。

        如果第三个问题答不上来，自动化往往只是把风险从“手动操作错误”转移成“监控失败、模式混淆或接管失败”。

        ## 难点讲解

        很多人直觉上会觉得“自动化越多越安全”。课程其实想纠正这个直觉。真正决定安全的，不是自动化数量，而是：

        - 系统状态是否可见
        - 自动化模式是否好理解
        - 人在接管前是否还有足够时间和信息恢复情境意识
        """,
        """
        ## At a Glance

        This topic is not just about automation becoming more advanced. It is about how automation changes the human role and whether the remaining human tasks become harder rather than easier.

        ## Core Logic

        - Automation often reduces repetitive workload and improves consistency.
        - But it also pushes people toward monitoring, mode understanding, takeover, and exception handling.
        - Those residual human tasks may be infrequent, but they become critical when things go wrong.

        ## What To Ask

        1. What did automation take over?
        2. What did the human retain?
        3. Are the remaining human tasks still realistically doable?

        If the third question has no good answer, risk has often shifted rather than disappeared.

        ## Common Difficulty

        More automation is not automatically more safety. Safety depends on visibility of system state, clarity of automation mode, and whether the human can recover enough understanding to intervene effectively.
        """,
    ),
    "crew_resource_management": pair(
        """
        ## 一眼看懂

        CRM 不是“大家相处好一点”的软技能课，而是一套把团队资源真正转化成安全防线的工作方法。它要解决的是：在高负荷和高风险环境里，团队怎样沟通、分工、纠错和相互补位。

        ## 这页最重要的主线

        - CRM 把安全从“个人技术是否足够好”扩展到“团队是否会一起工作”。
        - 它强调的不只是 communication，还包括 leadership、followership、assertiveness、briefing、debriefing、workload management 和 situational awareness。
        - 团队里最危险的情况，往往不是没人发现问题，而是有人看见了却没有说出来，或说出来后没有被团队吸收。

        ## 课件里真正强调的点

        从 Tenerife、Eastern 401、United 173 这类事故到后来的 CRM 训练，课程想强调的是：

        - authority gradient 过陡时，副驾驶和工程师即使看见问题，也可能不敢有效挑战
        - 一线成员如果不共享 mental model，就会出现“同一架飞机上每个人理解的局面不一样”
        - 团队监控和交叉检查，本质上是在用多人系统抵消单个人的注意和判断局限

        ## 难点讲解

        CRM 容易被误解成“出了问题时大家多说几句”。但好的 CRM 其实发生在问题出现之前：

        - brief 把预期状态先对齐
        - workload management 防止关键时刻所有人盯同一件事
        - inquiry 和 advocacy 让质疑成为团队规范
        - debrief 让经验被沉淀成下一次更好的协作
        """,
        """
        ## At a Glance

        CRM is not just a soft-skills topic about getting along. It is a way of turning team resources into a real safety barrier in high-workload operations.

        ## Core Message

        - CRM extends safety from individual skill to collective performance.
        - Communication matters, but so do leadership, followership, assertiveness, briefing, debriefing, workload management, and shared situational awareness.
        - A major failure mode is not that nobody noticed the problem, but that someone noticed and the team failed to absorb the signal.

        ## What The Course Emphasizes

        Historical accidents show how steep authority gradients, weak challenge behavior, and unshared mental models can defeat an otherwise technically capable crew.

        ## Common Difficulty

        CRM is not only what happens during an emergency. Strong CRM starts earlier through aligned plans, explicit workload distribution, and a team climate where questioning is normal and useful.
        """,
    ),
    "displays_and_alerts": pair(
        """
        ## 一眼看懂

        显示与告警设计的核心矛盾是：你必须让关键信息足够显眼，但又不能把操作者淹没在噪声里。真正好的告警系统，不是“更响、更亮”，而是“更可判断、更可信”。

        ## 这页的分析主轴

        - `display` 负责把系统状态变得可见、可比较、可推断。
        - `alert` 负责在时机关键时把注意力拉到该看的地方。
        - 两者如果分开设计，就容易出现看得见但看不懂，或者听得见却不知道要怎么做。

        ## 读这页时要抓的三个判断

        1. 这条告警是否真的代表高优先级风险。
        2. 告警出现时，操作者能不能立刻知道系统处于什么状态。
        3. 告警之后，是否有清晰的下一步动作。

        如果其中任何一个环节缺失，告警就可能只会增加 workload。

        ## 难点讲解

        课程里一个很重要的点是 false alarm 和 trust erosion。告警并不是越多越安全，因为：

        - 过多低价值告警会造成 alarm fatigue
        - 操作者会逐渐学会忽略、延迟响应或降低信任
        - 一旦真正关键的告警出现，系统可能已经失去“被立刻认真对待”的资格

        所以显示与告警设计，本质上是在做注意资源管理。
        """,
        """
        ## At a Glance

        The central challenge in displays and alerts is making critical information noticeable without drowning the operator in noise.

        ## Core Structure

        - displays make system state visible and interpretable
        - alerts redirect attention at the right moment
        - if these are poorly coordinated, operators may notice a signal without understanding what it means or what to do next

        ## Three Useful Questions

        1. Does this alert truly represent a high-priority condition?
        2. When it appears, can the operator quickly understand system state?
        3. Is the next action clear?

        ## Common Difficulty

        More alerts do not necessarily produce more safety. Frequent low-value alerts can create alarm fatigue and trust erosion, which makes later critical alerts less effective.
        """,
    ),
    "checklists_and_procedures": pair(
        """
        ## 一眼看懂

        检查单与程序的价值，不是把人变成机械执行者，而是把那些最容易被遗忘、跳步或顺序错乱的动作，外化成可共享、可核对、可复现的工作结构。

        ## 这页最关键的理解

        - checklist 是认知支架，不只是记忆备忘录。
        - procedure 是组织对“正常情况下应该如何做”的稳定承诺。
        - 当团队共用同一套程序语言时，协调成本会下降，交接和复盘也更清楚。

        ## 好的程序设计在做什么

        - 把关键步骤摆在最可执行的顺序上
        - 让检查点能被看见、读出、回应和确认
        - 让异常情况有升级路径，而不是逼着操作者在模糊地带硬撑

        ## 难点讲解

        这页最容易产生误解的地方，是把程序化理解成“越死板越好”。其实课程更想表达的是：

        - 标准化能减轻记忆负担
        - 但程序也必须和真实工作节奏匹配
        - 如果程序脱离 work as done，一线人员就会为了完成任务自行绕开它

        所以真正的人因问题不是“有没有 checklist”，而是“checklist 是否真能支持实际工作”。
        """,
        """
        ## At a Glance

        Checklists and procedures do not exist to make people mechanical. They externalize vulnerable steps so the work becomes shared, checkable, and repeatable.

        ## Core Logic

        - a checklist is a cognitive scaffold, not just a memory aid
        - a procedure is an organizational commitment about how normal work should be performed
        - shared procedural language reduces coordination cost and improves handoff and review

        ## What Good Design Does

        Good procedures put critical steps in usable order, make checkpoints visible and confirmable, and provide escalation paths for abnormal situations.

        ## Common Difficulty

        Standardization helps, but only if it fits real work. When procedures diverge from work as done, operators begin to route around them.
        """,
    ),
    "automated_vehicles": pair(
        """
        ## 一眼看懂

        自动化车辆这一页不是在重复航空自动化，而是在问一个迁移问题：当自动化从驾驶辅助走向更高等级时，人类驾驶员会不会被放进一个“平时太闲、出事时又来不及”的危险位置。

        ## 核心逻辑

        - 自动化车辆最难的不是正常巡航，而是 `handoff`。
        - 系统让人退出主任务后，再要求人突然接管，会遇到监控衰退、情境意识不足和反应迟滞。
        - 因此，信任校准比“让用户更相信系统”更重要，关键是让用户既不盲信，也不过度不用。

        ## 这页和航空自动化的连接

        课程把 automated vehicles 放进来，是因为很多问题高度相似：

        - automation surprise
        - mode confusion
        - 低参与度监控
        - 接管窗口太短
        - 责任划分模糊

        也就是说，技术平台不同，但人因矛盾非常接近。

        ## 难点讲解

        自动化车辆领域很容易把问题说成“驾驶员不够专注”。但如果系统设计本身长期让人不需要主动控制，那么在关键时刻要求人立即恢复高质量控制，本身就可能是不现实的设计假设。
        """,
        """
        ## At a Glance

        Automated vehicles extend the automation discussion into a takeover problem: people are often disengaged during routine operation and then expected to resume high-quality control with little warning.

        ## Core Logic

        - the hardest problem is often handoff, not steady-state automation
        - low-engagement monitoring weakens readiness, situation awareness, and response timing
        - trust calibration matters more than simply increasing trust

        ## Connection To Aviation

        The course uses automated vehicles because they inherit familiar automation challenges: surprise, mode confusion, monitoring decay, short takeover windows, and ambiguous responsibility.

        ## Common Difficulty

        It is too easy to say the driver should pay more attention. If system design encourages long periods of disengagement, the expectation of instant high-quality takeover may itself be unrealistic.
        """,
    ),
}
