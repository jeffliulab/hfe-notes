from __future__ import annotations

from note_blueprints import callout, page_blueprint, section, visual


RISK_METHODS_CONTENT: dict[str, dict] = {
    "error_analysis_methods": page_blueprint(
        template_type="method",
        page_intro_zh="这一页讲的是：当事故、事件或险情已经发生后，我们怎样把它分析清楚，而不是只写成一段带结论的故事。",
        page_intro_en="This page asks how to analyze an accident, incident, or near miss in a disciplined way instead of collapsing it into a story with a premature conclusion.",
        core_question_zh="错误分析和调查流程怎样把“发生了什么”转成“为什么会这样，以及下一步应该改什么”？",
        core_question_en="How do error analysis and investigation convert “what happened” into “why it happened and what should be changed next”?",
        must_learn_points_zh=[
            "调查先收事实，再建时间线，再追因果层级，最后落到改进措施。",
            "NTSB 风格的核心纪律是：先有证据，再谈解释。",
            "一个后果通常不只有一条原因线，分析不能太早收束到单一结论。",
            "好的错误分析要能回到设计、流程、培训或监管行动，而不只是写报告。",
        ],
        must_learn_points_en=[
            "Investigation moves from facts to timeline to causal layers to interventions.",
            "The NTSB-style discipline is evidence first, explanation second.",
            "One outcome usually has multiple contributing paths, so analysis cannot collapse too early.",
            "Strong error analysis ends in design, workflow, training, or policy change rather than in a report alone.",
        ],
        memory_anchor_zh="先记住这个方法的定位：调查不是为了尽快给出结论，而是为了把结论建立在可靠事实和可解释因果链上。",
        memory_anchor_en="Start with the purpose of the method: investigation is not about reaching a conclusion quickly, but about grounding the conclusion in reliable facts and an explainable causal chain.",
        sections=[
            section(
                "problem",
                "## 这个方法解决什么问题",
                "## What Problem This Method Solves",
                body_zh="""
错误分析和调查流程的价值，在于把一次复杂事件拆成可验证的结构。它不满足于“某人当时做错了什么”，而是追问：

- 系统当时处于什么状态
- 事件按什么顺序展开
- 哪些因素是直接触发，哪些因素是前置条件
- 哪些系统层问题让错误更可能发生或更难恢复
""",
                body_en="""
Error analysis and investigation are valuable because they turn a complex event into a verifiable structure. The method asks:

- what state the system was in
- how the event unfolded over time
- which factors were direct triggers and which were preconditions
- which system-level issues made the error more likely or harder to recover from
""",
            ),
            section(
                "io",
                "## 输入与输出是什么",
                "## What the Inputs and Outputs Are",
                body_zh="""
这个方法的输入通常包括：访谈、记录、日志、时间信息、程序文件、环境条件和设备状态。

它的输出不应该只是一个“最可能原因”，而应该至少包含：

- 清楚的时间线
- 事实与解释的区分
- 直接因素与更深层条件的区分
- 能落地的改进建议
""",
                body_en="""
Typical inputs include interviews, records, logs, timing information, procedures, environmental conditions, and equipment state.

The output should not be only a “most likely cause.” It should include:

- a clear timeline
- separation of fact from interpretation
- separation of triggers from deeper conditions
- actionable recommendations
""",
            ),
            section(
                "steps",
                "## 操作步骤怎么走",
                "## How the Method Proceeds",
                body_zh="""
可以把调查流程记成四步：

1. 收集事实，不要急着解释。
2. 建时间线，确保事件展开顺序清楚。
3. 分层找因果，把触发因素、前置条件和组织/设计问题区分开。
4. 把结果翻译成改进措施，回到界面、程序、训练、资源或监管层。
""",
                body_en="""
The flow can be remembered in four steps:

1. gather facts without rushing into explanation
2. build the timeline so the sequence is clear
3. separate triggers, preconditions, and organizational or design contributors
4. translate the findings into interventions across interface, procedure, training, resources, or policy
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="调查真正要避免的，不是“信息太多”，而是“过早觉得自己已经知道答案”。",
                note_body_en="The main thing an investigation must avoid is not too much information, but the premature feeling that the answer is already obvious.",
            ),
            section(
                "relation",
                "## 和后续方法是什么关系",
                "## How It Connects to Later Methods",
                body_zh="这页讲的是“已经发生的事件如何被解释”。后面的 task analysis、URRA 和 operational risk 页，则把这种解释能力往前推，用来在出事之前识别结构性风险。",
                body_en="This page explains how a completed event is interpreted. Later pages such as task analysis, URRA, and operational risk push the same logic forward so risk can be recognized before an event fully unfolds.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "steps",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最常见的失误，是看见一个显眼的人类动作后就直接把它写成“原因”。这样会把调查从解释系统，缩成描述最后一下动作。",
                body_en="The most common failure is to see one visible human action and immediately write it down as “the cause.” That collapses a system explanation into a description of the last visible move.",
            )
        ],
        examples=[
            callout(
                "example",
                "steps",
                "worked example：一次给药错误怎样被拆开",
                "Worked Example: How a Medication Error Gets Decomposed",
                body_zh="如果调查只写“护士选错了药”，输出就只有 blame。更成熟的调查会继续补上时间线、包装相似性、核对流程、工作负荷、班次疲劳和报警信息，把单一动作扩展成一条可解释的因果链。",
                body_en="If the report only says “the nurse selected the wrong medication,” the output is blame. A stronger investigation adds the timeline, packaging similarity, verification process, workload, shift fatigue, and alarm context, turning one visible action into an explainable causal chain.",
            )
        ],
        summary_points_zh=[
            "调查先做事实澄清，再做因果解释。",
            "一个结果通常有多条原因线，不能过早收束。",
            "真正有价值的输出是时间线、因果层级和改进措施。",
            "这套方法为后续更前置的风险分析页打底。",
        ],
        summary_points_en=[
            "Investigation clarifies facts before explaining causes.",
            "One outcome often has multiple causal paths, so early closure is dangerous.",
            "The strongest output combines timeline, layered causation, and intervention.",
            "This method provides the base logic for the more proactive risk-analysis pages that follow.",
        ],
    ),
    "task_analysis": page_blueprint(
        template_type="method",
        page_intro_zh="任务分析这一页的作用，是把一段连续使用过程拆成可观察、可讨论、可映射风险的步骤链。",
        page_intro_en="The job of task analysis is to decompose a continuous use episode into a sequence of observable, discussable, and risk-mappable steps.",
        core_question_zh="如果连任务本身都没拆清楚，我们又怎么知道错误会发生在哪一步、critical task 在哪里、控制措施该落到什么环节？",
        core_question_en="If the task itself is not decomposed clearly, how can we know where errors may arise, which steps are critical, or where controls should land?",
        must_learn_points_zh=[
            "任务分析的目标不是复述说明书，而是把真实任务需求拆成步骤、判断和信息需求。",
            "它是后续 critical task、use error 和 URRA 的前提。",
            "好的 task analysis 既看理想流程，也看真实工作中的偏差和替代路径。",
            "任务拆得越具体，后续风险分析越能落地。",
        ],
        must_learn_points_en=[
            "Task analysis does not rewrite the manual; it decomposes the real task into steps, judgments, and information demands.",
            "It is the prerequisite for critical tasks, use errors, and URRA.",
            "Strong task analysis compares ideal flow with real work and likely deviations.",
            "The more concrete the decomposition, the more actionable later risk analysis becomes.",
        ],
        memory_anchor_zh="先记住这个方法的定位：如果任务流没有被拆出来，后面的风险分析几乎都会漂在空中。",
        memory_anchor_en="Remember the purpose of the method this way: if the task flow has not been decomposed, the later risk analysis will float without anchors.",
        sections=[
            section(
                "problem",
                "## 这个方法解决什么问题",
                "## What Problem This Method Solves",
                body_zh="task analysis 把“用户在用产品”这件看起来连续的事，拆成一个个可分析的 use step、subtask、信息需求和操作要求。这样做的目的，是让后续所有讨论都能回到具体环节，而不是停留在抽象判断上。",
                body_en="Task analysis breaks the apparently continuous act of “using a product” into analyzable use steps, subtasks, information demands, and action requirements. That lets later discussion stay tied to concrete moments instead of vague judgments.",
            ),
            section(
                "io",
                "## 输入与输出是什么",
                "## What the Inputs and Outputs Are",
                body_zh="""
输入通常包括：目标任务、用户特征、使用环境、设备说明、现有流程和观察到的真实使用方式。

输出通常包括：

- 明确的任务步骤
- 每一步的信息、判断和动作要求
- 关键失败点
- 能进入 URRA 或 validation 的结构化任务表
""",
                body_en="""
Inputs usually include the task goal, user characteristics, use environment, device instructions, current workflow, and observed real behavior.

Outputs usually include:

- explicit task steps
- information, judgment, and action requirements at each step
- key failure points
- a structured task table that can feed URRA or validation work
""",
            ),
            section(
                "steps",
                "## 操作步骤怎么走",
                "## How the Method Proceeds",
                body_zh="""
可以按这条线做：

1. 先明确用户目标和起止条件。
2. 把任务拆成能被观察和讨论的 use step。
3. 为每一步补上需要看见什么、判断什么、操作什么。
4. 标出一旦失败就会影响安全或疗效的关键步骤。
5. 再把这些关键步骤带入 use error 和 risk analysis。
""",
                body_en="""
The method can be run in this order:

1. define the user goal and the task boundaries
2. decompose the flow into observable use steps
3. add what must be seen, judged, and done at each step
4. mark the steps whose failure would affect safety or effectiveness
5. carry those steps into use-error and risk analysis work
""",
            ),
            section(
                "relation",
                "## 和前后方法是什么关系",
                "## How It Connects to Earlier and Later Methods",
                body_zh="前面 human error 页告诉你怎样读错误类型，task analysis 则告诉你错误会落在哪个任务节点上。后面的 URRA、critical task 和 workbook 页面，都会直接把这里拆出来的任务流拿去继续写。",
                body_en="The human-error framework explains how to read failure types, while task analysis explains where in the task flow those failures can emerge. Later URRA, critical-task, and workbook pages directly reuse this decomposition.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="task analysis 的价值，不在于“列步骤”，而在于把风险分析绑到真实工作流上。",
                note_body_en="The value of task analysis is not merely listing steps; it is binding risk analysis to the real workflow.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "steps",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最常见的问题，是把说明书顺序原样抄下来，却没有问用户在真实环境里会不会跳步、补救、回退或走替代路径。",
                body_en="The most common mistake is to copy the instruction sequence verbatim without asking how users actually skip, recover, backtrack, or improvise in real conditions.",
            )
        ],
        examples=[
            callout(
                "example",
                "steps",
                "worked example：注射器任务为什么不能只写“给药”",
                "Worked Example: Why a Syringe Task Cannot Be Written as Simply “Deliver Dose”",
                body_zh="如果表里只写“给药”，后面就看不见装配、剂量设定、确认、按压保持和废弃处理这些不同失败点。把任务拆开后，critical task 和风险控制才有地方落脚。",
                body_en="If the worksheet only says “deliver dose,” later analysis cannot see assembly, dose setting, confirmation, hold time, and disposal as distinct failure points. Once the task is decomposed, critical tasks and controls finally have concrete landing points.",
            )
        ],
        summary_points_zh=[
            "task analysis 先把任务结构拆清楚，再谈风险。",
            "输入包括用户、环境、流程和真实使用方式。",
            "输出应该支持 critical task、URRA 和 validation。",
            "最怕把理想说明书当成真实工作流。",
        ],
        summary_points_en=[
            "Task analysis clarifies task structure before risk is discussed.",
            "Its inputs include users, environment, workflow, and real behavior.",
            "Its outputs should support critical tasks, URRA, and validation.",
            "The main trap is treating the ideal manual as if it were the real workflow.",
        ],
    ),
    "urra_methods": page_blueprint(
        template_type="method",
        page_intro_zh="URRA 这一页讲的不是一种表格格式，而是一条完整风险链：任务步骤、使用错误、危险情境、伤害后果和控制措施怎样被写到同一个结构里。",
        page_intro_en="URRA is not merely a table format. It is a full risk chain that links task steps, use errors, hazardous situations, harms, and controls in one structure.",
        core_question_zh="Use-Related Risk Analysis 怎样把任务、错误、危害和控制措施串成一条可追踪、可验证、可回看的链？",
        core_question_en="How does Use-Related Risk Analysis connect tasks, errors, hazards, and controls into a chain that is traceable, verifiable, and reviewable?",
        must_learn_points_zh=[
            "URRA 的中心作用，是把 use step、use error、hazardous situation、harm 和 control 连成一条链。",
            "书写顺序必须是任务与场景在前，错误与后果在后，控制措施最后。",
            "写得好的 URRA 足够具体，能直接支持验证活动。",
            "写得差的 URRA 往往只有笼统用语，既看不出真正风险，也支撑不了后续测试。",
        ],
        must_learn_points_en=[
            "The central job of URRA is linking use step, use error, hazardous situation, harm, and control in one chain.",
            "The writing order must keep task and scenario first, error and consequence next, and controls last.",
            "A strong URRA is specific enough to support validation work directly.",
            "A weak URRA uses vague language and supports neither real risk understanding nor later testing.",
        ],
        memory_anchor_zh="先记住这个方法的定位：URRA 不是“把风险写进表里”，而是把风险路径写清楚到足以支持设计和验证。",
        memory_anchor_en="Remember the purpose of URRA this way: it is not about putting risk into a table, but about writing the risk path clearly enough to support design and validation.",
        sections=[
            section(
                "problem",
                "## 这个方法解决什么问题",
                "## What Problem This Method Solves",
                body_zh="URRA 解决的是“风险信息分散在不同文件里”的问题。它把使用流程、潜在错误、危险情境、伤害和控制汇总到同一条链上，让团队能看见风险是怎样一步步长出来的。",
                body_en="URRA solves the problem of risk information being scattered across documents. It places the use flow, possible errors, hazardous situations, harms, and controls in one chain so the team can see how risk develops step by step.",
            ),
            section(
                "io",
                "## 输入与输出是什么",
                "## What the Inputs and Outputs Are",
                body_zh="""
URRA 的输入通常来自：

- task analysis
- user and use-environment assumptions
- 已知 use error 或投诉信息
- 设计特征、标签、IFU 和培训方案

输出则是一组可追踪条目，能回答：

- 哪一步可能出错
- 错后会进入什么危险情境
- 最终可能带来什么 harm
- 现有控制够不够
""",
                body_en="""
Typical URRA inputs come from:

- task analysis
- user and use-environment assumptions
- known use errors or complaint history
- design features, labeling, IFU, and training plans

The output is a set of traceable rows that answer:

- where error may occur
- what hazardous situation follows
- what harm may result
- whether current controls are sufficient
""",
            ),
            section(
                "steps",
                "## 操作步骤怎么走",
                "## How the Method Proceeds",
                body_zh="""
写 URRA 时，顺序非常关键：

1. 先从任务和 use scenario 出发。
2. 明确写出具体 use error，而不是“使用不当”这种大词。
3. 继续把错误推到 hazardous situation 和 harm。
4. 最后再看现有 control 是否足够，以及还要不要加设计或验证措施。
""",
                body_en="""
The order matters a lot when writing URRA:

1. start from the task and use scenario
2. write the specific use error rather than a vague label like “improper use”
3. push the error forward into hazardous situation and harm
4. only then assess whether current controls are sufficient and what more is needed
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="如果控制措施写在前面，URRA 很容易变成设计辩护；如果风险链写在前面，URRA 才像真正的风险分析。",
                note_body_en="If controls are written first, URRA becomes design justification. If the risk chain is written first, URRA behaves like real risk analysis.",
            ),
            section(
                "relation",
                "## 和前后方法是什么关系",
                "## How It Connects to Earlier and Later Methods",
                body_zh="task analysis 给 URRA 提供任务骨架；medical-device pages 会进一步把这套逻辑放到监管语境里；EpiPen workbook 页则展示一条 URRA 记录实际长什么样。",
                body_en="Task analysis provides the task skeleton for URRA; the medical-device pages place the same logic inside a regulatory context; the EpiPen workbook shows what a concrete URRA row looks like in practice.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "steps",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最常见的问题有两个：把 error 写得太泛，比如“误用”；以及把 harm 写得太近，只写“剂量错误”却没有继续写到患者伤害。",
                body_en="Two failures appear constantly: writing the error too vaguely, such as “misuse,” and stopping the harm too early, such as writing only “wrong dose” without the patient consequence.",
            )
        ],
        examples=[
            callout(
                "example",
                "steps",
                "worked example：一条 URRA 记录应该怎样写",
                "Worked Example: What One Strong URRA Row Looks Like",
                body_zh="例如某一步是“设定剂量”。好的 URRA 不会只写“可能出错”，而会写成：用户把 1.0 mL 读成 10 mL，导致危险情境是过量给药，潜在 harm 是低血糖或更严重不良反应；然后才回头讨论剂量窗口、视觉区分、确认步骤和验证测试。",
                body_en="Suppose the step is “set dose.” A strong URRA row does not stop at “possible user error.” It says the user reads 1.0 mL as 10 mL, leading to an overdose hazardous situation and harm such as hypoglycemia or more severe injury; only then does it return to dose-window design, visual differentiation, confirmation steps, and validation testing.",
            )
        ],
        summary_points_zh=[
            "URRA 的核心是写清风险链，而不是填表本身。",
            "输入来自任务流、用户场景和已知问题。",
            "写作顺序必须是任务/错误/后果/控制，而不是倒着来。",
            "越具体的 URRA，越能支持后续验证。",
        ],
        summary_points_en=[
            "URRA is about clarifying the risk chain, not about filling a table for its own sake.",
            "Its inputs come from task flow, user context, and known problems.",
            "The writing order must stay task/error/consequence/control rather than reversing that logic.",
            "The more specific the URRA, the stronger the later validation work becomes.",
        ],
    ),
    "known_problem_and_event_tree": page_blueprint(
        template_type="method",
        page_intro_zh="这一页把两种补盲方法放在一起：Known Problem Analysis 是向后看历史问题，Event Tree 是向前看起始事件的后果分支。",
        page_intro_en="This page pairs two gap-finding methods: Known Problem Analysis looks backward to historical issues, while Event Tree analysis looks forward from an initiating event into downstream consequence branches.",
        core_question_zh="当主流程分析已经做完之后，团队怎样继续问：我们还漏掉了哪些已知问题和后果分支？",
        core_question_en="Once the main workflow analysis is complete, how does the team continue asking what historical issues and downstream consequence branches may still be missing?",
        must_learn_points_zh=[
            "Known Problem Analysis 用历史问题提醒团队别把旧坑重新挖一遍。",
            "Event Tree 用分支展开提醒团队别低估一个起始事件后面的后果路径。",
            "两者共同作用，是把视角从主路径扩展到边缘路径和遗漏风险。",
            "这不是额外文书，而是补盲机制。",
        ],
        must_learn_points_en=[
            "Known Problem Analysis prevents the team from rediscovering old failure modes too late.",
            "Event Trees prevent the team from underestimating the downstream branches of an initiating event.",
            "Together they expand the view from the main path to edge paths and missed risk.",
            "These methods are not administrative extras; they are deliberate blind-spot checks.",
        ],
        memory_anchor_zh="先记住这个方法的定位：主流程分析负责把主路径看清，Known Problem 和 Event Tree 负责提醒你别忘了系统的边角和分支。",
        memory_anchor_en="Remember the role of these methods this way: main workflow analysis clarifies the main path, while Known Problem Analysis and Event Trees protect against forgetting the edges and branches of the system.",
        sections=[
            section(
                "problem",
                "## 这两个方法分别补什么",
                "## What Each Method Adds",
                body_zh="""
`Known Problem Analysis` 补的是团队“其实早就知道”的东西，例如历史投诉、事故、CAPA、文献或竞品问题。

`Event Tree` 补的是起始事件之后的后果展开：如果这一层没拦住，会往哪些分支继续走？哪些节点是真正的防线？
""",
                body_en="""
`Known Problem Analysis` captures what the team may already know through complaints, incidents, CAPA records, literature, or competitor history.

`Event Tree` expands what happens after an initiating event: if one barrier fails, what branches follow, and which nodes function as real defenses?
""",
            ),
            section(
                "steps",
                "## 操作步骤怎么走",
                "## How the Methods Proceed",
                body_zh="""
可以把它们分开记：

1. Known Problem：先扫历史问题，再判断哪些仍适用于当前设计。
2. Event Tree：先定起始事件，再往后画分支，看后果、拦截点和严重程度如何变化。

两者都不是凭空发散，而是为了逼团队回到证据和可预见路径。
""",
                body_en="""
The two methods can be remembered separately:

1. Known Problem: scan historical problems first, then decide which still apply to the current design.
2. Event Tree: define the initiating event first, then expand the downstream branches, intercept points, and consequence severity.

Neither method is about free-form brainstorming. Both force the team back toward evidence and foreseeable pathways.
""",
            ),
            section(
                "relation",
                "## 和主流程分析是什么关系",
                "## How They Relate to the Main Workflow Analysis",
                body_zh="主流程分析最擅长看正常任务流里的风险；这两个方法最擅长看主路径之外的已知隐患和分支后果。所以它们不是替代关系，而是补位关系。",
                body_en="Main workflow analysis is strongest on the normal task path. These two methods are strongest at exposing historical blind spots and branch consequences outside that main path. They complement rather than replace the main analysis.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="这页的真正价值，是逼团队从“我们已经分析完了”退一步，重新问“我们还可能漏了什么”。",
                note_body_en="The real value of this page is that it forces the team to step back from “we already analyzed it” and ask “what might still be missing?”",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "problem",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最容易出现的误解，是把 known problem 当作旧问题清单，把 event tree 当作画图练习。它们真正的作用，是改变团队对遗漏风险的敏感度。",
                body_en="The most common misunderstanding is to treat known problems as an old-issue list and event trees as a drawing exercise. Their real function is to change the team’s sensitivity to missed risk.",
            )
        ],
        examples=[
            callout(
                "example",
                "steps",
                "worked example：主路径没问题，边缘路径仍然可能出事",
                "Worked Example: The Main Path Looks Fine, but the Edge Path Still Fails",
                body_zh="例如某设备的正常使用流程已经分析清楚，但历史投诉显示用户在清洁后重新组装时经常装反部件。主流程分析可能没把这个低频分支放进去；Known Problem Analysis 会把它拉回来，而 Event Tree 会进一步展开“装反之后如果未被发现，会走向什么后果”。",
                body_en="Suppose the normal use flow of a device is well analyzed, but complaint history shows users often reverse a component after cleaning and reassembly. Main-path analysis may miss that low-frequency branch. Known Problem Analysis pulls it back into view, and Event Tree analysis then asks what happens if that reversed assembly is not detected.",
            )
        ],
        summary_points_zh=[
            "Known Problem 看历史问题，Event Tree 看后果分支。",
            "两者共同作用，是补盲而不是替代主流程分析。",
            "它们都要求团队回到证据和可预见路径。",
            "真正目标是发现“我们还漏了什么”。",
        ],
        summary_points_en=[
            "Known Problem Analysis looks backward to prior issues; Event Trees look forward to consequence branches.",
            "Together they fill gaps rather than replace main workflow analysis.",
            "Both methods force the team back to evidence and foreseeable paths.",
            "The true target is discovering what the team still missed.",
        ],
    ),
}

RISK_METHODS_CONTENT["error_analysis_methods"]["sections"].extend(
    [
        section(
            "timeline",
            "## 为什么时间线是错误分析里最不能省的一层",
            "## Why the Timeline Is the One Layer You Cannot Skip in Error Analysis",
            body_zh="""
            很多团队以为时间线只是“把事情按先后写出来”。实际上时间线的作用更深，它是后面所有因果判断的骨架。只要事件顺序没理清，团队就很容易把后果错当原因，把后见之明错当事前可见性。

            所以真正好的调查不会急着总结，而会先问：异常最早在哪里出现、谁最先接触到关键信息、哪一步本来有机会恢复、以及恢复窗口是什么时候真正关闭的。时间线一旦稳住，后面的 system conditions 才能被放回正确位置。
            """,
            body_en="""
            Many teams treat the timeline as merely putting events into chronological order. Its role is deeper than that. The timeline becomes the skeleton for every later causal judgment. Once the sequence is unclear, teams begin mistaking outcomes for causes and hindsight for real-time visibility.

            Strong investigation therefore does not rush into summary. It first asks where the anomaly appeared earliest, who encountered the critical information first, where recovery was still possible, and when that recovery window actually closed. Once the timeline is stable, the later system conditions can be placed correctly.
            """,
        ),
        section(
            "evidence",
            "## 真正好的调查为什么总是先守住证据纪律",
            "## Why Strong Investigation Always Starts with Evidence Discipline",
            body_zh="""
            这页真正难的地方，不是“知道该先收事实”，而是很多团队在压力下会不自觉跳过这一步。只要一个显眼动作先进入视野，整个调查就很容易被它带偏，后面收集到的材料也会被拿来支持这个先入结论。

            所以好的调查通常会刻意把材料分层：

            - 哪些是确认过的客观事实
            - 哪些是当事人的主观回忆
            - 哪些是调查者的解释与推断

            只有把这三层分开，时间线才会稳，后面的因果分析也才不会变成“先有答案，再去找支持”。
            """,
            body_en="""
            The hard part of investigation is not knowing that facts should come first. The hard part is that, under pressure, teams often stop honoring that rule. Once one visible action grabs attention, the rest of the investigation can get pulled toward it and later evidence is interpreted mainly as support for that early conclusion.

            Strong investigation therefore separates material into layers:

            - confirmed facts
            - subjective recall from participants
            - interpretation and causal inference from investigators

            Once those layers are separated, the timeline becomes more stable and later causal analysis is less likely to turn into “start with the answer and collect supporting material.”
            """,
        ),
        section(
            "quality",
            "## 怎样判断一份调查结果是不是只写了故事",
            "## How to Tell Whether an Investigation Output Is Only a Story",
            body_zh="""
            很多报告表面上看结构完整，但其实只是在讲一个更正式的故事。判断它有没有真正分析到位，可以看三个信号：

            - 报告里有没有把时间线、条件和动作拆开，而不是只写结论句
            - 有没有同时写 direct cause、contributing factors 和更上游的组织/设计条件
            - 改进建议是不是能直接对应回前面的因果链

            如果一份报告里只有“发生了什么”和“以后注意”，那通常还不是课程里要求的 error analysis，而只是带结论的复述。
            """,
            body_en="""
            Many reports look structured on the surface while still behaving like polished stories. Three signals help distinguish stronger analysis:

            - does the report separate timeline, conditions, and actions rather than writing only conclusion sentences
            - does it include direct causes, contributing factors, and upstream design or organizational conditions together
            - do the recommendations connect clearly back to the earlier causal chain

            If a report contains only “what happened” followed by “be more careful next time,” it is usually not the kind of error analysis this course is teaching.
            """,
        ),
    ]
)
RISK_METHODS_CONTENT["error_analysis_methods"]["examples"].append(
    callout(
        "example",
        "quality",
        "案例：为什么同一份材料会被写成“事故复述”和“系统分析”两种完全不同的东西",
        "Example: Why the Same Material Can Become Either an Event Retelling or a System Analysis",
        body_zh="同样是一次给药错误，弱调查会写成“护士误选药物，导致患者受到错误治疗”；强调查会继续拆出包装相似性、班次疲劳、核对程序是否现实、警示信息是否足够显眼，以及为什么这些因素没有在更早节点被拦住。两者材料来源可能一样，但分析质量完全不同。",
        body_en="The same medication event can be written weakly as “the nurse selected the wrong medication and the patient received the wrong treatment,” or strongly as an analysis of packaging similarity, shift fatigue, realism of verification procedure, salience of warnings, and why those factors were not intercepted earlier. The source material may be the same, but the analytic quality is completely different.",
    )
)
RISK_METHODS_CONTENT["error_analysis_methods"]["inline_visuals"].extend(
    [
        visual(
            "relation",
            "Sp26_ErrorAnalysisMethods_20260121.pdf",
            "这张图要看懂的是：错误分析不是独立存在的方法，它处在理论、案例和 mitigation 之间，调查输出必须最终回到改进动作。",
            "This figure should make one thing visible: error analysis does not stand alone. It sits between theory, cases, and mitigation, so the investigation output has to return to concrete change.",
            asset_name_contains="page-02",
        ),
    ]
)

RISK_METHODS_CONTENT["task_analysis"]["sections"].extend(
    [
        section(
            "granularity",
            "## 为什么 task analysis 的颗粒度会直接决定后面分析质量",
            "## Why the Granularity of Task Analysis Directly Determines Later Analysis Quality",
            body_zh="""
            task analysis 写得太粗时，后面所有风险判断都会被迫写粗。因为只要任务步骤仍然停在“准备设备”“完成给药”这种大块上，团队就看不见真正高风险的感知、确认、对齐、保持和恢复节点。

            所以这页真正要练的，不只是会拆步骤，而是会把步骤拆到足以支撑后续 use error、critical task 和 validation 的层级。颗粒度不是写得越碎越好，而是要碎到能支撑判断、但又不碎到失去任务结构。
            """,
            body_en="""
            When task analysis remains too coarse, every later risk judgment also becomes coarse. If the steps stay at the level of “prepare device” or “deliver medication,” the team cannot see the real high-risk moments of perception, confirmation, alignment, holding, and recovery.

            The practical skill on this page is therefore not just decomposing steps, but decomposing them to the level that can support later use-error analysis, critical-task identification, and validation. Granularity does not mean making the list as small as possible. It means going fine enough to support judgment without destroying the task structure.
            """,
        ),
        section(
            "critical",
            "## 为什么 task analysis 最后一定会走到 critical task",
            "## Why Task Analysis Eventually Has to Reach Critical Tasks",
            body_zh="""
            任务分析不能停在“步骤列完了”。真正有价值的地方，是在步骤表里继续问：哪一步一旦出错，就会直接影响安全、疗效、剂量、识别或恢复机会。

            这就是 critical task 的来源。它不是额外附加的一列，而是 task analysis 真正的落点。因为只有把关键步骤标出来，团队才知道哪些节点值得投入更强的界面设计、确认机制、培训和验证资源。
            """,
            body_en="""
            Task analysis cannot stop at “the steps have been listed.” Its real value appears when the team continues asking which steps, if performed incorrectly, would directly affect safety, effectiveness, dose, identification, or recovery opportunity.

            That is where critical tasks come from. They are not just one extra spreadsheet column. They are the practical landing point of the analysis because they tell the team where stronger interface design, confirmation logic, training, and validation attention belong.
            """,
        ),
        section(
            "reality",
            "## 为什么课堂里的 PB&J 例子其实很重要",
            "## Why the PB&J Example Actually Matters",
            body_zh="""
            课件里用 PB&J 不是为了讲一个轻松例子，而是为了证明一件事：只要任务开始被认真拆开，很多原本“理所当然”的隐含步骤就会浮出来。

            例如洗手、检查原料状态、准备顺序、清理和收尾，这些都不是装饰步骤。它们说明 task analysis 的核心不是“把主要动作写出来”，而是把真实完成任务所需要的全部支撑条件也写出来。医疗器械、航空程序和自动化系统里的任务分析，逻辑上完全一样。
            """,
            body_en="""
            The PB&J example is not there because the course wanted a casual illustration. It proves something important: once a task is decomposed seriously, many supposedly obvious but unstated steps become visible.

            Hand washing, checking ingredient condition, preparation order, and cleanup are not decorative details. They show that task analysis is not only about writing the main visible actions. It is about writing the full support conditions required to complete the task reliably. The same logic applies in medical devices, aviation procedures, and automation systems.
            """,
        ),
    ]
)
RISK_METHODS_CONTENT["task_analysis"]["examples"].append(
    callout(
        "example",
        "critical",
        "案例：为什么“确认针头已装好”这种步骤常常比“按压给药”更值得盯住",
        "Example: Why “Confirm the Needle Is Properly Assembled” May Matter More Than “Press to Deliver”",
        body_zh="很多团队天然会把最显眼的动作当成主步骤，但任务分析常常会发现，真正高风险的点在更早环节。例如装配确认、剂量核对、解锁顺序和使用前准备，一旦漏掉，后面的执行再熟练也救不回来。这正是为什么 task analysis 必须把前置步骤写细。",
        body_en="Teams often treat the most visible action as the main step, but task analysis frequently shows that the higher-risk point sits earlier. Assembly confirmation, dose verification, unlock sequence, and pre-use preparation may matter more because once they fail, later execution quality cannot fully recover the situation. That is why task analysis has to decompose the preparatory steps in detail.",
    )
)
RISK_METHODS_CONTENT["task_analysis"]["inline_visuals"].extend(
    [
        visual(
            "steps",
            "08 Task Analysis.pptx",
            "这张图要看懂的是：一张看似简单的操作说明，其实已经包含准备、姿态、方向、按压、保持和收尾等多个可拆分步骤。",
            "This figure should make one point concrete: even a simple-looking instruction poster already contains multiple analyzable steps such as preparation, orientation, posture, pressing, holding, and finish actions.",
            asset_name_contains="slide-08-image8",
        ),
    ]
)

RISK_METHODS_CONTENT["urra_methods"]["sections"].extend(
    [
        section(
            "rows",
            "## 为什么一条 URRA 行本身就应该读得出完整风险故事",
            "## Why One URRA Row Should Read Like a Complete Risk Story",
            body_zh="""
            写 URRA 时，一个常见问题是每一列都填了字，但合起来仍然看不出真正发生了什么。强的 URRA 行应该让人顺着一条线读下去：谁在什么场景下做哪一步、会错成什么、错后会进入什么 hazardous situation、最终伤害是什么、现在靠什么拦。

            如果一行读完后团队还看不见这条完整路径，通常说明场景、动作、错误或 harm 写得还不够具体。URRA 的质量，不是表有多满，而是链是否完整。
            """,
            body_en="""
            A common URRA problem is that every column contains text while the row still fails to show what actually happens. A strong row should read as one line: who is doing which step in which scenario, what goes wrong, which hazardous situation follows, what the harm is, and what now stands in the way.

            If the team still cannot see that full path after reading the row, the scenario, action, error, or harm is usually still too vague. URRA quality is not about how full the table is. It is about whether the chain is complete.
            """,
        ),
        section(
            "discipline",
            "## 为什么 URRA 最怕写成抽象大词",
            "## Why URRA Fails When It Stays at a Vague Level",
            body_zh="""
            URRA 一旦写成“误用”“使用不当”“可能受伤”这种大词，后面几乎所有栏位都会一起失焦。因为团队看不出到底是哪一步、哪种错误、哪条 harm path，也就不知道控制到底该落在哪个设计点上。

            所以一条好的 URRA 记录通常都有很强的具体性：具体场景、具体动作、具体误判、具体后果、具体控制。写到这个程度时，验证场景和风险沟通才会自然长出来。
            """,
            body_en="""
            Once URRA is written in vague labels such as “misuse,” “incorrect use,” or “possible injury,” nearly every later column loses focus. The team can no longer see which step is failing, what specific error is happening, or which harm path is in play, so controls also become vague.

            Strong URRA rows therefore stay concrete: concrete scenario, concrete action, concrete misjudgment, concrete consequence, and concrete control. At that level, validation scenarios and risk communication can emerge naturally from the analysis.
            """,
        ),
        section(
            "validation",
            "## 为什么 URRA 最终一定要回到验证",
            "## Why URRA Ultimately Has to Feed Validation",
            body_zh="""
            这门课不把 URRA 当成档案管理，而把它当成设计与验证的接口。原因很简单：如果一条风险链已经被写出来，团队就必须能回答“我们准备怎样证明控制真的有效”。

            这意味着 URRA 不是写完就结束，而是还要继续推动：

            - 哪些 risk control 需要在原型或正式产品里被体现
            - 哪些关键任务需要在 validation 中被专门观察
            - 哪些情境需要通过 representative user 和 representative use condition 去复现
            """,
            body_en="""
            The course does not treat URRA as archive management. It treats it as an interface between design and validation. The reason is simple: once a risk chain has been written, the team must be able to answer how it will demonstrate that the control is actually effective.

            That means URRA is not finished when the row is written. It should continue to drive:

            - which controls must appear in prototype or final design
            - which critical tasks need focused observation in validation
            - which scenarios need to be reproduced with representative users under representative conditions
            """,
        ),
    ]
)
RISK_METHODS_CONTENT["urra_methods"]["warnings"].append(
    callout(
        "warning",
        "validation",
        "另一个常见失误",
        "Another Common Failure",
        body_zh="有些团队会把 URRA 写得看起来很完整，但没有任何一条真正能转进验证。这通常说明条目还不够具体，或者控制写得太空泛。",
        body_en="Some teams produce URRA tables that look complete but do not yield a single usable validation scenario. That usually means the entries are still too vague or the controls are written at too abstract a level.",
    )
)
RISK_METHODS_CONTENT["urra_methods"]["inline_visuals"].extend(
    [
        visual(
            "validation",
            "10 Write URRA.pptx",
            "这张图要看懂的是：URRA 不是单向填表，它会在风险不可接受或引入新风险时反复回到控制和验证，直到链条站得住。",
            "This figure should make the loop visible: URRA is not one-way form filling. It keeps returning to controls and validation whenever risk remains unacceptable or a new risk has been introduced.",
            asset_name_contains="slide-02-image2",
        ),
    ]
)

RISK_METHODS_CONTENT["known_problem_and_event_tree"]["sections"].extend(
    [
        section(
            "selection",
            "## 为什么 known problem analysis 还要学会筛信号",
            "## Why Known Problem Analysis Also Has to Learn Signal Selection",
            body_zh="""
            已知问题来源很多，但并不是所有历史信息都同样重要。真正成熟的做法，是学会从投诉、召回、文献和竞品案例里分辨哪些只是零散噪声，哪些已经在重复指向同一类结构问题。

            所以这页除了教你“去哪里找历史问题”，还在训练另一件事：看到历史材料后，能不能把它重新压缩成可操作的风险线索，而不是只做资料堆积。
            """,
            body_en="""
            Known problems come from many places, but not every historical signal carries the same weight. A more mature practice is learning how to separate scattered noise from repeated signals that point to the same structural weakness across complaints, recalls, literature, and competitor events.

            This page therefore teaches more than where to look. It also trains you to compress historical material into actionable risk cues rather than accumulating sources without analytic direction.
            """,
        ),
        section(
            "history",
            "## 为什么 known problem analysis 能防止团队重复踩坑",
            "## Why Known Problem Analysis Prevents the Team from Repeating Old Failures",
            body_zh="""
            很多系统风险并不是第一次出现，而是曾经以投诉、CAPA、事故、文献或竞品失败的形式已经出现过。Known Problem Analysis 的价值，就是逼团队承认：历史本身就是风险证据，不能假装每个项目都从零开始。

            这一步做得好时，团队会更早看到那些“并不新，但这次环境里仍然可能复现”的问题。
            """,
            body_en="""
            Many system risks are not novel. They have already appeared as complaints, CAPA records, accidents, literature findings, or competitor failures. Known Problem Analysis matters because it forces the team to recognize that history is itself risk evidence; every project does not begin from zero.

            When done well, this step makes the team notice problems that are not new, but are still likely to recur in the present environment.
            """,
        ),
        section(
            "branching",
            "## 为什么 event tree 会把主路径外的风险拉回来",
            "## Why Event Trees Pull Side-Branch Risk Back into View",
            body_zh="""
            主流程分析往往盯着“最常见的一条路径”，但系统真正危险的时候，经常恰恰发生在分支上。Event Tree 的价值，就是从一个 initiating event 出发，继续往后问：

            - 这一层防线如果成功，会怎样
            - 如果失败，又会走向哪里
            - 哪些后果虽然不常见，但一旦发生代价极高

            所以 Event Tree 不只是预测结果，而是在逼团队重新认识防线分支的含义。
            """,
            body_en="""
            Main workflow analysis often stays focused on the most common path, but many serious system outcomes emerge on the branches. The value of an Event Tree is that it begins with one initiating event and keeps asking:

            - what happens if this defense succeeds
            - what happens if it fails
            - which outcomes are rare but extremely costly

            Event Trees therefore do more than predict consequences. They force the team to reinterpret what each defense branch actually means.
            """,
        ),
    ]
)
RISK_METHODS_CONTENT["known_problem_and_event_tree"]["examples"].append(
    callout(
        "example",
        "branching",
        "案例：为什么“警报出现”不是终点，而只是 event tree 的起点",
        "Example: Why “An Alarm Occurs” Is Not the End but the Start of an Event Tree",
        body_zh="一旦起始事件是“关键警报出现”，后面真正要展开的是：操作者有没有注意到、有没有理解、有没有采取正确动作、系统有没有继续恶化、以及备用防线有没有接上。这样一展开，团队就会发现真正的风险不只在告警本身，而在后面一连串防线分支。",
        body_en="If the initiating event is “a critical alarm occurs,” the real analysis begins afterward: was it noticed, was it understood, was the correct action taken, did the system continue degrading, and did backup defenses engage? Once expanded this way, the team sees that the real risk is not the alarm itself but the whole chain of later defense branches.",
    )
)
RISK_METHODS_CONTENT["known_problem_and_event_tree"]["inline_visuals"].extend(
    [
        visual(
            "history",
            "11 Known Problem Analysis.pptx",
            "这张图要看懂的是：known problem analysis 不是凭印象回忆旧问题，而是要进到像 MAUDE 这样的真实数据库里找重复出现的设备问题与投诉模式。",
            "This figure should show that known problem analysis is not casual memory. It requires going into real databases such as MAUDE to identify recurring device problems and complaint patterns.",
            asset_name_contains="slide-06-image17",
        ),
    ]
)

RISK_METHODS_CONTENT["task_analysis"]["sections"].extend(
    [
        section(
            "review_table",
            "## 怎样判断一张 task analysis 表已经能拿去做后续工作",
            "## How to Tell When a Task-Analysis Table Is Ready for Downstream Work",
            body_zh="""
            一张 task analysis 表真正可用时，团队至少能用它稳定回答四个问题：

            - 用户这一步到底要完成什么
            - 这一步必须看到、判断和操作什么
            - 一旦在这里出错，后果会往哪条风险链走
            - 这一行能不能继续支撑 critical task、URRA 和 validation

            如果表只能告诉你“步骤名称”，却回答不了这些问题，它通常还只是半成品。task analysis 不是目录，而是后续风险工作的骨架。
            """,
            body_en="""
            A task-analysis table is truly usable only when the team can reliably answer at least four questions from it:

            - what exactly the user is trying to accomplish at this step
            - what must be perceived, judged, and executed here
            - where the consequence path goes if this step fails
            - whether this row can support critical-task identification, URRA, and validation

            If the table only gives you a step label but cannot answer those questions, it is usually still incomplete. Task analysis is not a table of contents. It is the skeleton for later risk work.
            """,
        ),
        section(
            "worked_flow",
            "## 从 PB&J 到正式使用任务，课堂真正想让你学会什么",
            "## What the Course Really Wants You to Learn from PB&J Before Moving to Formal Use Tasks",
            body_zh="""
            PB&J 例子最有用的地方，在于它把“隐含步骤”硬生生拉到台面上。很多人一开始只会写“拿面包、抹花生酱、抹果酱、合上”，但课程故意提醒你：洗手、检查是否过期、准备位置、开封方式、清理收尾，这些都可能决定任务是否安全、干净、有效完成。

            这和正式产品任务没有本质区别。到了注射器、自动注射器或复杂设备场景，只是支持条件更多、后果更高而已。PB&J 练的不是食物流程，而是把“看起来理所当然”的任务支撑条件全部写出来的习惯。
            """,
            body_en="""
            The real value of the PB&J example is that it forces hidden steps into the open. Many people start by writing only “take bread, spread peanut butter, spread jelly, close sandwich,” but the course deliberately points to hand washing, expiration checking, setup position, opening sequence, and cleanup. Those supporting steps may determine whether the task is completed safely, cleanly, and effectively.

            Formal product tasks are not different in principle. Syringes, auto-injectors, and complex devices simply add more support conditions and higher consequences. PB&J is therefore not about food. It is about building the habit of writing out everything the task quietly depends on.
            """,
        ),
    ]
)
RISK_METHODS_CONTENT["task_analysis"]["examples"].append(
    callout(
        "example",
        "worked_flow",
        "案例：把 PB&J 改写成注射器任务表时，哪些隐藏步骤会突然变关键",
        "Example: Which Hidden Steps Suddenly Become Critical When PB&J Logic Is Translated into a Syringe Task",
        body_zh="一旦把 PB&J 的思路迁到注射器任务表里，隐藏步骤会迅速跳出来：确认药液与患者匹配、检查针头是否牢固、确认剂量窗口、保持注射时间、处理废弃物。这些都不是“附属细节”，而是决定 harm path 会不会被打开的关键节点。PB&J 之所以重要，就是因为它先用低风险例子把这种观察方式练熟。",
        body_en="Once the PB&J logic is translated into a syringe task table, hidden steps emerge immediately: matching medication to patient, checking needle attachment, verifying the dose window, holding for the required duration, and disposing safely. These are not decorative details. They are the nodes that determine whether the harm path opens. PB&J matters because it rehearses that way of seeing in a low-risk example first.",
    )
)
RISK_METHODS_CONTENT["task_analysis"]["inline_visuals"].append(
    visual(
        "worked_flow",
        "08 Task Analysis.pptx",
        "这张图要看懂的是：PB&J 被放进课件里不是为了轻松一下，而是为了提醒你，看似简单的任务也隐藏着大量没有被说出口的步骤与前提。",
        "This figure should make one point concrete: PB&J is not included as comic relief. It is there to show that even a simple task hides many unstated steps and preconditions.",
        asset_name_contains="slide-04-image2",
    )
)

RISK_METHODS_CONTENT["error_analysis_methods"]["sections"].extend(
    [
        section(
            "mission",
            "## 为什么 NTSB 式调查会刻意把“责任归属”放到后面",
            "## Why NTSB-Style Investigation Deliberately Pushes Liability Questions to the Background",
            body_zh="""
            课件里反复强调 NTSB 调查是 `fact-finding proceedings`，而不是为了先判定谁该承担法律责任。这个区别非常重要，因为一旦调查太早围着 blame 旋转，团队就更容易只找最后一个显眼动作，而不是继续往前追系统条件、恢复机会和组织约束。

            对这门课来说，这种证据纪律不是法律细节，而是分析质量的前提。只有当调查先把材料稳定组织成事实、时间线和条件结构，后面“为什么会这样”这件事才不会变成先入为主的判断。
            """,
            body_en="""
            The lecture repeatedly emphasizes that NTSB investigation is a `fact-finding proceeding`, not a process designed primarily to assign legal liability. The distinction matters because once investigation begins orbiting blame too early, teams become more likely to stop at the last visible human action rather than continuing into system conditions, recovery opportunity, and organizational constraint.

            For this course, that discipline is not a legal footnote. It is a prerequisite for analytic quality. Only when the material is first stabilized into facts, timeline, and condition structure can the later question of “why this happened” avoid becoming a premature judgment.
            """,
        ),
        section(
            "recommendations",
            "## 什么时候一份调查才算真正做完",
            "## When an Investigation Is Actually Finished",
            body_zh="""
            一份调查不是在写出一句 cause statement 时结束的，而是在团队已经能把发现稳定翻译成改进动作时才真正完成。也就是说，调查终点不是“找到解释”，而是“让解释能够改变系统”。

            这也是为什么课程会强调 recommendation quality。真正成熟的建议，应该能清楚落到界面、程序、培训、资源、监督或法规层，而且能让人看出它究竟是在回应时间线中的哪一段风险链。如果建议和前面的证据链接不上，调查其实还没有真正闭环。
            """,
            body_en="""
            An investigation is not finished when it produces one cause sentence. It is finished when the team can translate the findings reliably into changes. In other words, the endpoint is not merely “we found an explanation,” but “the explanation can now change the system.”

            That is why the course emphasizes recommendation quality. Mature recommendations should land clearly on interface, procedure, training, resources, oversight, or regulation, and it should be visible which portion of the risk chain they answer. If the recommendation cannot be tied back to the evidence chain, the investigation has not actually closed the loop.
            """,
        ),
    ]
)
RISK_METHODS_CONTENT["error_analysis_methods"]["examples"].append(
    callout(
        "example",
        "mission",
        "案例：为什么一句“pilot error”不会让调查真正结束",
        "Example: Why the Phrase “Pilot Error” Does Not Actually Finish an Investigation",
        body_zh="如果报告最后只写成“pilot error”，团队得到的只是一个标签，而不是一个可改的结构。真正成熟的调查会继续追问：当时哪些状态信息并不充分可见、哪些程序没有帮忙恢复、哪些组织或设计条件让机组更难察觉并改正偏差。只有这些层级被写出来，建议才会落地。",
        body_en="If the report ends with the phrase “pilot error,” the team receives a label rather than a structure it can change. A stronger investigation continues asking which state cues were not sufficiently visible, which procedures failed to support recovery, and which organizational or design conditions made it harder for the crew to detect and correct the deviation. Only when those layers are written can recommendations become actionable.",
    )
)
RISK_METHODS_CONTENT["error_analysis_methods"]["inline_visuals"].extend(
    [
        visual(
            "mission",
            "Sp26_Investigative Process-NTSB_20260121.pdf",
            "这张图要看懂的是：NTSB 调查强调 fact-finding 与独立性，意思不是“没有责任问题”，而是调查必须先守住事实和安全改进这条主线。",
            "This figure should show that NTSB investigation emphasizes fact-finding and independence. The point is not that responsibility never matters, but that investigation must first protect the facts-and-safety-improvement line.",
            asset_name_contains="page-02",
        ),
        visual(
            "recommendations",
            "Sp26_Investigative Process-NTSB_20260121.pdf",
            "这张图要看懂的是：调查的最终目标不是写一句原因，而是产出客观调查与可执行 safety recommendations。",
            "This figure should make clear that the final goal of investigation is not one cause sentence, but objective investigation tied to implementable safety recommendations.",
            asset_name_contains="page-03",
        ),
    ]
)
