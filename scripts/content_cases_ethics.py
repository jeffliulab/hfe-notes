from __future__ import annotations

from textwrap import dedent


def pair(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": dedent(zh).strip(),
        "en": dedent(en).strip(),
    }


CASES_ETHICS_CONTENT: dict[str, dict[str, str]] = {
    "operational_risk": pair(
        """
        ## 一眼看懂

        Operational risk 这页要你看到的是：风险不只发生在一次错误动作里，而是长期藏在运行条件里。班次、时间压力、环境变化、组织约束和一线应对方式，都会把系统推向更脆弱或更稳健的状态。

        ## 核心逻辑

        - 任务风险会随着场景变化而波动，不是固定值。
        - work as imagined 和 work as done 往往存在差距。
        - 如果管理层只看程序上的“应该怎样做”，却不看一线实际怎样完成任务，就会低估真实运行风险。

        ## 这页为什么很重要

        它把前面很多分散主题拉到一起：

        - Swiss Cheese 讲的是多层防线
        - error analysis 讲的是事件怎么展开
        - fatigue、stress、checklists 讲的是操作者怎样受到条件约束

        operational risk 则把这些都放回日常运行系统里，去看风险如何持续生成。

        ## 难点讲解

        最容易犯的错，是把 operational risk 理解成“又一个风险清单”。更准确的理解应该是：它是一种看系统的视角，提醒你不断追问现实运行条件是不是正在侵蚀原本设计好的安全边界。
        """,
        """
        ## At a Glance

        Operational risk is about seeing risk as something embedded in ongoing operating conditions rather than in a single visible error.

        ## Core Logic

        - risk varies with context rather than remaining fixed
        - work as imagined often differs from work as done
        - organizations that only inspect the formal procedure tend to underestimate real operating risk

        ## Why It Matters

        This topic reconnects many earlier themes by placing defenses, event analysis, fatigue, stress, and procedures back into the everyday operating system.

        ## Common Difficulty

        Operational risk is not just another checklist. It is a way of asking whether real conditions are gradually eroding the safety boundary that formal design assumes.
        """,
    ),
    "cardosi_case": pair(
        """
        ## 一眼看懂

        Cardosi 案例这一页的价值，在于把抽象原则重新拉回一个具体事件里。你会看到显示、沟通、程序、注意和情境理解不是分开的主题，而是在真实案例里同时起作用。

        ## 读案例时要抓什么

        - 事件里哪些信息本来应该支持正确判断
        - 哪些界面或程序因素让判断变难
        - 团队沟通在关键时刻是补位了，还是失效了
        - 如果从 HFE 角度回看，这个系统本来可以在哪些地方更早拦住问题

        ## 为什么案例页重要

        课程不是希望你把概念背下来，而是希望你能在案例里识别它们。Cardosi 这样的材料正好训练一种能力：

        - 看到局部现象时，能联想到背后的 HFE 结构
        - 看到事故经过时，能把 attention、display、procedure、CRM 串成解释链

        ## 难点讲解

        很多人做案例分析时会掉进“事后看一切都很明显”的陷阱。更成熟的读法是尽量回到当事人在那个时刻能看到什么、理解什么、误判什么，然后再讨论系统还能如何设计得更好。
        """,
        """
        ## At a Glance

        The Cardosi case matters because it turns abstract principles back into a concrete event where displays, communication, procedure, attention, and understanding interact at once.

        ## What To Look For

        - what information should have supported correct judgment
        - what interface or procedural features made judgment harder
        - whether team communication corrected or amplified the problem
        - where the system could have intercepted the issue earlier

        ## Why Case Pages Matter

        The goal is not memorizing concepts but recognizing them inside an event. A case trains the ability to translate visible details into human-factors structure.

        ## Common Difficulty

        Hindsight makes everything look obvious. Better analysis tries to reconstruct what was visible, interpretable, and misleading to the people in the moment.
        """,
    ),
    "f16_analysis_prompts": pair(
        """
        ## 一眼看懂

        F16 prompts 这一页本质上是一个“怎么分析案例”的脚手架。它的作用不是直接给你答案，而是帮你把课程概念转换成一组系统化提问。

        ## 这页真正有用的地方

        - 避免案例分析只停在表面叙述
        - 让你从多个维度同时看同一个事件
        - 帮助团队在讨论时保持结构，而不是想到哪里说到哪里

        ## 一般可以怎么用这些 prompts

        1. 先描述事件和任务背景。
        2. 再问信息、界面、程序、团队和组织因素分别起了什么作用。
        3. 然后区分直接触发因素与更深层条件。
        4. 最后把分析收束成改进建议。

        ## 难点讲解

        很多 prompts 看起来像“问题列表”，但它们真正的价值是迫使分析者跳出单因解释。也就是说，prompt 的意义不在于问得多，而在于把你的视角从个人错误扩展到整个系统。
        """,
        """
        ## At a Glance

        The F16 prompts are a scaffold for case analysis. They do not provide the answer; they organize how to ask better questions.

        ## Why They Help

        - they prevent case analysis from collapsing into simple storytelling
        - they force multiple dimensions of the event into view
        - they give teams a shared structure for discussion

        ## A Useful Sequence

        1. describe the event and task context
        2. examine information, interface, procedure, team, and organizational contributors
        3. separate triggers from deeper conditions
        4. turn the analysis into recommendations

        ## Common Difficulty

        Prompts matter not because they produce more questions, but because they widen the frame beyond a single-cause explanation.
        """,
    ),
    "boeing_737max_and_ethics": pair(
        """
        ## 一眼看懂

        737 Max 这一页最重要的点，是它不是单纯的“一个设计缺陷案例”。课程把它放在伦理部分，是因为这里同时出现了系统设计、培训、传感器/告警、组织决策、认证过程和专业责任的交织。

        ## 这页要你看到的几层问题

        - 技术层：系统状态可见性、自动化逻辑、单点失效、告警和飞行员理解之间是否匹配。
        - 运行层：飞行员在时间压力、高工作负荷和异常状态下是否还有足够认知空间做出正确判断。
        - 组织层：制造商、运营方、维护和监管者分别承担了什么风险管理责任。
        - 伦理层：当设计与培训假设不足时，谁有义务更早提出、修正、阻止风险扩散。

        ## 为什么它是 HFE 案例

        这不是一个“技术”和“人”的二选一案例。恰恰相反，课程借它说明：

        - 设计问题会改变人的判断条件
        - 训练和程序决定人是否能在异常中恢复
        - 监管与组织选择会决定缺陷能否长期存在

        所以 HFE 在这里不是边角料，而是解释系统为何失效的核心视角之一。

        ## 难点讲解

        伦理讨论最容易流于空泛。更好的方式是回到具体工程决策：有没有充分揭示系统行为、有没有把风险转嫁给飞行员、有没有让认证与培训假设脱离真实运行条件。只有落回这些具体点，伦理才不会变成抽象口号。
        """,
        """
        ## At a Glance

        The 737 Max topic is not just a design-defect story. It belongs in ethics because system design, training, alerting, organizational decisions, certification, and professional responsibility are intertwined.

        ## The Layers To See

        - technical: visibility of system state, automation logic, single-failure vulnerability, and alerting
        - operational: whether crews had enough cognitive room under time pressure and abnormal conditions
        - organizational: how manufacturer, operator, maintenance, and regulator responsibilities were distributed
        - ethical: who had the obligation to surface, correct, or stop the spread of risk

        ## Why It Is An HFE Case

        This is not a choice between technology and humans. Design shapes human judgment conditions, training shapes recovery, and organizational choices shape whether defects persist.

        ## Common Difficulty

        Ethics becomes empty if it stays abstract. The stronger approach is to tie it back to concrete engineering decisions about disclosure, training assumptions, failure tolerance, and responsibility transfer.
        """,
    ),
}
