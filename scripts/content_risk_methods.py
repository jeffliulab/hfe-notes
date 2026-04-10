from __future__ import annotations

from note_blueprints import callout, formalize_blueprint, page_blueprint, section


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

RISK_METHODS_CONTENT = {
    slug: formalize_blueprint(blueprint) for slug, blueprint in RISK_METHODS_CONTENT.items()
}
