from __future__ import annotations

from note_blueprints import callout, page_blueprint, section


MEDICAL_DEVICES_CONTENT: dict[str, dict] = {
    "iso_14971": page_blueprint(
        template_type="method",
        page_intro_zh="ISO 14971 这一页讲的不是单张表，而是一套贯穿医疗器械全生命周期的风险管理语言和流程。",
        page_intro_en="This page treats ISO 14971 not as a single worksheet, but as the language and process framework for risk management across the medical-device lifecycle.",
        core_question_zh="ISO 14971 怎样把 hazard、hazardous situation、harm、control 和上市后反馈组织成一个闭环风险管理过程？",
        core_question_en="How does ISO 14971 organize hazard, hazardous situation, harm, control, and post-market feedback into a closed-loop risk-management process?",
        must_learn_points_zh=[
            "ISO 14971 的重点不是填表，而是用一致语言管理风险。",
            "`hazard`、`hazardous situation`、`harm` 必须严格分开。",
            "风险管理不是一次性动作，而是计划、识别、控制、验证和上市后回看的连续过程。",
            "人因工作在这里的重要性，是很多 hazardous situation 都经由使用路径触发。",
        ],
        must_learn_points_en=[
            "The point of ISO 14971 is not paperwork; it is a consistent language for managing risk.",
            "`hazard`, `hazardous situation`, and `harm` must stay clearly separated.",
            "Risk management is not a one-time activity but a continuous process of planning, identification, control, verification, and post-market review.",
            "Human-factors work matters here because many hazardous situations arise through use.",
        ],
        memory_anchor_zh="先记住这个标准的定位：它不是替代设计，而是逼团队把设计风险、使用风险和伤害后果放到同一个闭环里。",
        memory_anchor_en="Remember the role of the standard this way: it does not replace design work; it forces the team to place design risk, use risk, and harm consequence inside one closed loop.",
        sections=[
            section(
                "terms",
                "## 这个方法解决什么问题",
                "## What Problem This Method Solves",
                body_zh="ISO 14971 解决的是团队对风险对象说不清楚的问题。它要求大家用同一套语言去区分潜在伤害源、暴露情境和真正发生的伤害，从而让设计、临床、法规和人因讨论能接起来。",
                body_en="ISO 14971 solves the problem of teams talking about risk imprecisely. It forces a shared language that separates sources of harm, exposure situations, and actual harm so design, clinical, regulatory, and human-factors discussions can connect.",
            ),
            section(
                "io",
                "## 输入与输出是什么",
                "## What the Inputs and Outputs Are",
                body_zh="""
输入包括：设计信息、预期用途、用户场景、危害识别、测试信息和上市后反馈。

输出至少包括：

- 风险管理计划
- 风险分析条目
- 控制与剩余风险判断
- 上市后信息回流机制
""",
                body_en="""
Inputs include design information, intended use, user scenarios, hazard identification, testing information, and post-market feedback.

Outputs include at least:

- a risk-management plan
- risk-analysis entries
- control and residual-risk judgments
- a mechanism for feeding post-market information back into the system
""",
            ),
            section(
                "steps",
                "## 操作步骤怎么走",
                "## How the Method Proceeds",
                body_zh="""
可以把标准流程记成六步：

1. 建风险管理计划。
2. 识别 hazard 和 foreseeable use situation。
3. 估计并评价风险。
4. 实施风险控制。
5. 判断剩余风险和整体可接受性。
6. 用生产和上市后信息持续回看。
""",
                body_en="""
The process can be remembered in six steps:

1. establish the risk-management plan
2. identify hazards and foreseeable use situations
3. estimate and evaluate risk
4. implement risk controls
5. judge residual risk and overall acceptability
6. feed production and post-market information back into the process
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="ISO 14971 的强项，是让团队始终用同一套结构去看风险，而不是每个部门各说各话。",
                note_body_en="The strength of ISO 14971 is that it keeps the team using one shared risk structure instead of letting each function describe risk in its own language.",
            ),
            section(
                "relation",
                "## 和人因工作是什么关系",
                "## How It Connects to Human Factors",
                body_zh="人因工作不是标准外的附加项。很多 hazardous situation 正是通过使用错误、界面诱发、标签误读和任务环境限制出现的，所以 medical-device URRA 和 use-error 页会继续把这条线展开。",
                body_en="Human factors is not an external add-on to the standard. Many hazardous situations appear through use error, interface-induced confusion, labeling issues, and task-context limits, which is why the later medical-device URRA and use-error pages continue the same line.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "terms",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最常见的错误，是把 `hazard`、`hazardous situation` 和 `harm` 混写成同一个层级。一旦这三个词没分清，后面的控制和验证就会一起变乱。",
                body_en="The most common error is collapsing `hazard`, `hazardous situation`, and `harm` into the same layer. Once those three are blurred, later controls and verification logic drift with them.",
            )
        ],
        examples=[
            callout(
                "example",
                "steps",
                "worked example：一个注射器风险链怎样写清楚",
                "Worked Example: How to Write a Syringe Risk Chain Clearly",
                body_zh="如果装置的剂量窗口难读，`hazard` 可能是药物输送能力本身，`hazardous situation` 是用户把剂量读错并完成过量给药，`harm` 则是患者受到不良生理后果。把这三层分开后，控制措施才能分别落到窗口设计、确认流程和验证测试上。",
                body_en="If a dose window is hard to read, the `hazard` may be the drug-delivery capability itself, the `hazardous situation` is the user misreading the dose and delivering too much, and the `harm` is the patient’s adverse physiological outcome. Once those layers are separated, controls can be assigned correctly to display design, confirmation workflow, and validation testing.",
            )
        ],
        summary_points_zh=[
            "ISO 14971 提供的是统一风险语言和闭环流程。",
            "hazard、hazardous situation、harm 必须严格区分。",
            "风险管理贯穿计划、控制、验证和上市后反馈。",
            "人因工作在医疗器械风险链里不是附属品。",
        ],
        summary_points_en=[
            "ISO 14971 provides a common risk language and a closed-loop process.",
            "`hazard`, `hazardous situation`, and `harm` must remain distinct.",
            "Risk management spans planning, control, verification, and post-market feedback.",
            "Human factors is not peripheral inside the medical-device risk chain.",
        ],
    ),
    "medical_device_urra": page_blueprint(
        template_type="method",
        page_intro_zh="这一页把 URRA 放到医疗器械监管语境里：同样是 use-related risk，这里更强调 patient harm、critical task 和可追踪控制。",
        page_intro_en="This page places URRA inside the medical-device regulatory context, where use-related risk is tied more explicitly to patient harm, critical tasks, and traceable controls.",
        core_question_zh="在医疗器械场景里，URRA 和一般任务风险分析相比，究竟多了哪些判断要求？",
        core_question_en="Inside medical devices, what additional judgment demands does URRA impose beyond a generic task-risk analysis?",
        must_learn_points_zh=[
            "医疗器械 URRA 更强调可预见 use scenario、critical task 和 patient harm 路径。",
            "控制措施不能只停在培训，必须优先考虑界面、标签、IFU 和物理设计。",
            "监管语境要求风险链条可追踪、可验证、可回看。",
            "这页是 ISO 14971 和具体 use error 工作之间的桥。",
        ],
        must_learn_points_en=[
            "Medical-device URRA places stronger emphasis on foreseeable use scenarios, critical tasks, and patient-harm pathways.",
            "Controls cannot stop at training; interface, labeling, IFU, and physical design changes take priority.",
            "The regulatory context requires the risk chain to be traceable, verifiable, and reviewable.",
            "This page bridges ISO 14971 and concrete use-error work.",
        ],
        memory_anchor_zh="先记住这个方法的定位：医疗器械 URRA 不是普通风险表，它必须写到足以证明团队真的知道病人会怎样受伤、设计又该怎样改。",
        memory_anchor_en="Remember the purpose of medical-device URRA this way: it is not a generic risk table; it must be written clearly enough to show how patients may be harmed and how design should respond.",
        sections=[
            section(
                "problem",
                "## 这个方法解决什么问题",
                "## What Problem This Method Solves",
                body_zh="医疗器械 URRA 解决的是“使用风险怎么被写成监管上可接受的证据”这个问题。它要求团队把 use scenario、critical task、use error、hazardous situation、harm 和 control 写成一条完整链条。",
                body_en="Medical-device URRA solves the problem of turning use risk into evidence that is acceptable in a regulated setting. It requires the team to write use scenario, critical task, use error, hazardous situation, harm, and control as one complete chain.",
            ),
            section(
                "io",
                "## 输入与输出是什么",
                "## What the Inputs and Outputs Are",
                body_zh="""
输入通常包括：任务分析、用户群体、使用环境、器械设计、标签/IFU、已知问题和伤害后果判断。

输出则应让团队明确：

- 哪些步骤是 critical task
- 哪些错误会直通 patient harm
- 哪些控制需要在设计里体现
- 哪些点必须进入 validation
""",
                body_en="""
Typical inputs include task analysis, user groups, use environment, device design, labeling and IFU, known issues, and harm assessment.

The output should make it clear:

- which steps are critical tasks
- which errors can lead directly to patient harm
- which controls must appear in design
- which points must enter validation
""",
            ),
            section(
                "steps",
                "## 操作步骤怎么走",
                "## How the Method Proceeds",
                body_zh="做法上和一般 URRA 相同，但要求更严格：从 use scenario 开始，明确 critical task，写出具体 use error，再推进到 hazardous situation、harm 和 control，最后把这些条目回接到 validation 计划。",
                body_en="The logic is similar to generic URRA but held to a stricter standard: begin with the use scenario, identify the critical task, define the concrete use error, push the chain into hazardous situation, harm, and control, and then feed the row back into validation planning.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="医疗器械 URRA 的关键，不是把“风险存在”写出来，而是把“病人可能怎样受伤、系统准备怎样拦住它”写具体。",
                note_body_en="The key move in medical-device URRA is not simply stating that risk exists, but specifying how the patient may be harmed and how the system intends to intercept that path.",
            ),
            section(
                "relation",
                "## 和前后页面是什么关系",
                "## How It Connects to the Neighboring Pages",
                body_zh="它前接 ISO 14971 的标准语言，后接 use-error 分析和 EpiPen workbook 的具体文档写法，是医疗器械分区里最像“中枢枢纽”的一页。",
                body_en="This page inherits the standardized language of ISO 14971 and feeds forward into use-error analysis and the EpiPen workbook. It is the hub page inside the medical-device section.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "steps",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最容易出现的弱控制，是凡事都写成“加强培训”。如果界面、反馈、标签或物理形态本身可以改，主要风险不应该压给培训和注意力。",
                body_en="The weakest recurring control is to write everything as “better training.” If interface, feedback, labeling, or physical form can be redesigned, the primary risk should not be left to training and attention.",
            )
        ],
        examples=[
            callout(
                "example",
                "steps",
                "worked example：critical task 为什么必须被单独标出来",
                "Worked Example: Why a Critical Task Must Be Marked Explicitly",
                body_zh="例如注射器“设定剂量”这一步，一旦错误就可能直接进入 patient harm 路径，所以它必须被标成 critical task。只有这样，团队才会在设计评审和 validation 里对这一步给出更高等级的控制和测试关注。",
                body_en="Suppose the syringe step is “set dose.” If failure there can lead directly to patient harm, that step must be marked as a critical task. Only then will the design review and validation plan allocate the higher level of control and testing attention it deserves.",
            )
        ],
        summary_points_zh=[
            "医疗器械 URRA 更强调 critical task 和 patient harm。",
            "输入包括任务流、用户情境、设计和标签信息。",
            "输出必须能反推控制和 validation 计划。",
            "培训不能成为默认主控制。",
        ],
        summary_points_en=[
            "Medical-device URRA places stronger emphasis on critical tasks and patient harm.",
            "Its inputs include task flow, user context, design, and labeling information.",
            "Its outputs must support both controls and validation planning.",
            "Training cannot become the default primary control.",
        ],
    ),
    "medical_device_use_errors": page_blueprint(
        template_type="concept",
        page_intro_zh="这一页专门解决“用错了到底算什么”的问题：device failure、无意 use error、异常使用和故意偏离规则，不能混成一个桶。",
        page_intro_en="This page is about classifying what “used incorrectly” really means. Device failure, unintended use error, abnormal use, and deliberate deviation cannot all be thrown into one bucket.",
        core_question_zh="当医疗器械使用出了问题时，我们怎样区分设计诱发的 use error、器械本身失效、异常使用和故意违规？",
        core_question_en="When medical-device use goes wrong, how do we distinguish design-induced use error from device failure, abnormal use, and deliberate rule deviation?",
        must_learn_points_zh=[
            "不是所有不良使用都叫 use error。",
            "判断时必须看行为是否在可预见使用范围内、设计是否放大了错误机会、恢复空间是否存在。",
            "use error 分析的重点，是把问题重新拉回具体任务和具体情境。",
            "如果问题类型定义错了，后面的控制措施也会跑偏。",
        ],
        must_learn_points_en=[
            "Not every bad use episode is a use error.",
            "The classification depends on foreseeability, design contribution, and whether recovery opportunities existed.",
            "Good use-error analysis pushes the discussion back to specific tasks and contexts.",
            "If the problem type is misclassified, the later controls will drift as well.",
        ],
        memory_anchor_zh="记这一页最简单的方法是：先别急着说“用户用错了”，先问设计、环境和情境是不是已经把正确操作变得很难。",
        memory_anchor_en="The shortest way to remember this page is: before saying “the user used it incorrectly,” ask whether design, environment, and context already made correct use unusually hard.",
        sections=[
            section(
                "definition",
                "## 什么叫医疗器械中的 use error",
                "## What Use Error Means in Medical Devices",
                body_zh="这页不是在扩大 blame，而是在缩小误判。它要求团队把“错误行为”放回可预见使用场景里，看它到底是无意偏差、器械失效、异常使用，还是故意偏离规则。",
                body_en="This page is not broadening blame; it is reducing misclassification. It asks the team to place the visible behavior back into the foreseeable use context and judge whether it reflects unintended deviation, device failure, abnormal use, or deliberate rule departure.",
            ),
            section(
                "importance",
                "## 为什么这个区分会直接影响控制策略",
                "## Why the Distinction Directly Changes the Control Strategy",
                body_zh="""
一旦定义错了，改法就会跟着错：

- 明明是界面诱发错误，却只补培训，风险会回来。
- 明明是异常使用，却按普通 use error 写，控制会失焦。
- 明明是器械失效，却把责任压给用户，设计问题就被遮掉了。
""",
                body_en="""
Once the classification is wrong, the response drifts with it:

- if an interface-induced error is treated as a training problem, the risk returns
- if abnormal use is treated as ordinary use error, controls lose focus
- if device failure is pushed onto the user, the design problem is hidden
""",
            ),
            section(
                "application",
                "## 这页真正想建立的分析习惯",
                "## The Analytical Habit This Page Tries to Build",
                body_zh="看到错误行为时，不要立刻贴标签。先回到具体 use step、具体场景、具体信息显示和具体环境条件，再问设计有没有让误选、漏做、误判或顺序错误变得更容易。",
                body_en="When a visible error appears, do not label it immediately. Return first to the specific use step, scenario, display context, and environment, and then ask whether design made mis-selection, omission, misjudgment, or sequence error easier.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="医疗器械里的 use error 分析，本质上是在判断系统有没有把使用者推到容易出错的位置。",
                note_body_en="Medical-device use-error analysis is fundamentally about judging whether the system pushed the user into an error-prone position.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "importance",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最常见的误区，是把所有不良后果都收成一句“user error”。这样一来，界面、标签、环境和组织条件都会从视野里消失。",
                body_en="The most common mistake is compressing every bad outcome into the phrase “user error.” Once that happens, interface, labeling, environment, and organizational conditions disappear from view.",
            )
        ],
        examples=[
            callout(
                "example",
                "application",
                "案例：明明看起来像“用错了”，其实是界面在诱发错误",
                "Example: It Looks Like “Wrong Use,” but the Interface Is Doing the Pushing",
                body_zh="如果两种给药模式在界面上只用细小字母区分，用户在紧急场景中选错模式后，表面上像是“user selected the wrong mode”。但更重要的分析结论可能是：系统把高后果选择设计得过于难辨认。",
                body_en="If two dosing modes are separated only by small textual labels, and the user selects the wrong mode in an urgent setting, the surface description is “the user selected the wrong mode.” The more important conclusion may be that the system made a high-consequence choice too difficult to discriminate.",
            )
        ],
        summary_points_zh=[
            "不是所有不良使用都等于 use error。",
            "分类时要看可预见性、设计诱发和恢复空间。",
            "如果问题定义错了，控制策略也会错。",
            "分析必须回到具体任务和具体情境。",
        ],
        summary_points_en=[
            "Not every poor use episode is a use error.",
            "Classification depends on foreseeability, design contribution, and recovery opportunity.",
            "If the problem definition is wrong, the control strategy will also be wrong.",
            "Analysis must return to the concrete task and context.",
        ],
    ),
    "epipen_workbook": page_blueprint(
        template_type="case",
        page_intro_zh="EpiPen workbook 这一页不是新理论，而是把前面讲过的 task analysis、critical task 和 URRA 写法压缩进一个具体工作底稿里。",
        page_intro_en="The EpiPen workbook page is not a new theory page. It compresses task analysis, critical tasks, and URRA writing into one concrete working document.",
        core_question_zh="一张 workbook 表怎样把抽象概念翻译成团队真的能写、能审、能验证的风险条目？",
        core_question_en="How does one workbook translate abstract concepts into risk entries that a team can actually write, review, and validate?",
        must_learn_points_zh=[
            "样例页的价值，在于让你看到“好的一行 URRA”到底长什么样。",
            "workbook 会把任务步骤、critical task、use error、harm 和 mitigation 压成可协作的表格语言。",
            "读样例时要分清哪些栏位在描述事实，哪些栏位在做风险判断。",
            "它不是标准答案模板，而是写法顺序的示范。",
        ],
        must_learn_points_en=[
            "The value of the example is that it shows what a strong URRA row actually looks like.",
            "The workbook compresses task steps, critical tasks, use errors, harms, and mitigation into collaborative table language.",
            "When reading it, distinguish descriptive fields from evaluative risk-judgment fields.",
            "It is not an answer key template; it is a demonstration of writing order and discipline.",
        ],
        memory_anchor_zh="先记住这个案例页的一句话判断：样例的真正价值，不在于抄格式，而在于学会“先任务、再错误、再伤害、最后控制”的书写顺序。",
        memory_anchor_en="Keep this case-level judgment in mind: the example matters not because its format can be copied blindly, but because it teaches the writing order of task first, error second, harm third, and control last.",
        sections=[
            section(
                "background",
                "## 背景与 stakes",
                "## Background and Stakes",
                body_zh="EpiPen 这类产品的风险文档之所以重要，是因为使用往往发生在紧急场景下，用户可能不是专业人员，时间压力高，错误后果又直接落到患者身上。所以 workbook 不是文书练习，而是把风险判断提前写实。",
                body_en="For a product such as the EpiPen, risk documentation matters because use often occurs in urgent settings, the user may not be a professional, time pressure is high, and the consequence lands directly on the patient. The workbook is therefore not paperwork rehearsal; it is an attempt to write the risk judgment realistically in advance.",
            ),
            section(
                "chain",
                "## 这张表到底在串什么",
                "## What the Workbook Actually Connects",
                body_zh="workbook 会把 use step、potential use error、hazard、harm、severity、critical task 和 mitigation 串成一行。它的好处，是让团队在一页里看到“这一步如果错了，会沿什么路径走向后果，以及准备怎样拦住它”。",
                body_en="The workbook connects use step, potential use error, hazard, harm, severity, critical task, and mitigation into a single row. Its value is that the team can see, in one place, how one step may fail, where the consequence path goes, and how the design intends to stop it.",
            ),
            section(
                "application",
                "## 读样例时应该怎样下手",
                "## How to Read the Example Effectively",
                body_zh="""
读这种 workbook 时，建议顺着下面这条线走：

1. 先看任务步骤是否拆得够细。
2. 再看哪些步骤被标成 critical task。
3. 接着看 error、hazard、harm 有没有真的连成链。
4. 最后看 mitigation 是不是回到了设计、说明、流程或验证上。
""",
                body_en="""
When reading a workbook like this, use a fixed sequence:

1. check whether the task steps are decomposed finely enough
2. identify which steps are marked as critical tasks
3. inspect whether error, hazard, and harm truly form a chain
4. judge whether mitigation comes back to design, instructions, workflow, or validation
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="这页不是让你背 workbook 栏位名称，而是让你学会如何把抽象 HFE 概念翻译成可执行文档。",
                note_body_en="This page is not about memorizing workbook column names. It is about learning how to translate abstract HFE concepts into executable documentation.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "application",
                "最容易做错的地方",
                "The Most Common Failure Mode",
                body_zh="最容易出现的误解，是把样例当成可直接照抄的模板。真正该学的是它背后的顺序和约束，而不是句式表面。",
                body_en="The most common misunderstanding is to treat the example as a template to copy line by line. What matters is the sequence and discipline behind it, not the surface phrasing.",
            )
        ],
        examples=[
            callout(
                "example",
                "chain",
                "案例：为什么“一行写得好”比“整张表写满”更重要",
                "Example: Why One Strong Row Matters More than a Fully Filled Sheet",
                body_zh="如果某一行能把任务步骤、具体 error、患者 harm 和 mitigation 写得非常清楚，团队就能据此设计验证场景。反过来，如果整张表都只是“使用不当”“可能伤害”“需要培训”这种泛词，表填满了也没有真正分析价值。",
                body_en="If one row clearly links the task step, the concrete error, the patient harm, and the mitigation, the team can design a meaningful validation scenario from it. If the entire sheet is filled with vague phrases such as “improper use,” “possible harm,” and “training required,” the workbook looks complete but adds little analytic value.",
            )
        ],
        summary_points_zh=[
            "workbook 页的重点是看“好的一行 URRA”长什么样。",
            "它把任务流、critical task、harm 和 mitigation 压成团队可协作的文档语言。",
            "读样例时要区分描述字段和判断字段。",
            "真正该学的是写法顺序，而不是抄格式。",
        ],
        summary_points_en=[
            "The workbook page is about seeing what a strong URRA row actually looks like.",
            "It compresses task flow, critical task, harm, and mitigation into collaborative document language.",
            "When reading the example, separate descriptive fields from evaluative fields.",
            "What matters most is the writing order, not blind format copying.",
        ],
    ),
}

MEDICAL_DEVICES_CONTENT["iso_14971"]["sections"].extend(
    [
        section(
            "controls",
            "## 风险控制在这个标准里为什么不是“想到什么就补什么”",
            "## Why Risk Control in This Standard Is Not “Add Whatever Control Comes to Mind”",
            body_zh="""
            ISO 14971 真正强调的，不是风险列得够不够多，而是控制有没有逻辑顺序。课程里反复暗示的一条判断是：如果危险可以通过设计本身被消掉，就不应该先把希望寄托在标签提醒或培训上。

            这背后其实是在建立一个控制层级：

            - 先改设计本身，尽量从源头降低风险
            - 再看 protective measure 或系统层防线
            - 最后才是信息、说明、培训和告警

            这样做不是因为后面的手段没用，而是因为越靠近源头的控制，通常越稳定、越不依赖用户在高压下始终做对。
            """,
            body_en="""
            ISO 14971 does not mainly reward the team for listing many risks. It rewards the team for thinking clearly about control logic. One recurring course judgment is that if a hazard can be reduced through design itself, the analysis should not start by relying on labeling or training.

            That creates a control hierarchy:

            - redesign the source of risk where possible
            - then add protective measures or system defenses
            - only then depend on information, instructions, training, or alerts

            The reason is not that the later methods never help. It is that source-level controls are usually more stable and less dependent on perfect user behavior under pressure.
            """,
        ),
        section(
            "language",
            "## 为什么标准语言必须这么严格",
            "## Why the Standard’s Language Has to Be So Strict",
            body_zh="""
            很多人第一次看 ISO 14971 会觉得定义太细、太烦。但这恰恰是标准有用的原因。只要团队在 `hazard`、`hazardous situation`、`harm` 之间说混了，后面就会出现三个连锁问题：

            - 控制措施不知道该控哪一层
            - 验证活动不知道要证明什么
            - 剩余风险讨论会变成不同部门各说各话

            所以标准语言看起来像术语要求，本质上其实是在保护团队的因果结构不被写乱。
            """,
            body_en="""
            Many people see ISO 14971 for the first time and feel the definitions are overly fine-grained. That precision is exactly why the standard is useful. Once the team blurs `hazard`, `hazardous situation`, and `harm`, three problems appear quickly:

            - controls no longer target the right layer
            - verification no longer knows what it is supposed to demonstrate
            - residual-risk discussion turns into several departments speaking past each other

            The language rule therefore looks like terminology discipline, but in practice it protects the causal structure of the analysis from collapsing.
            """,
        ),
    ]
)
MEDICAL_DEVICES_CONTENT["iso_14971"]["examples"].append(
    callout(
        "example",
        "controls",
        "案例：为什么“说明书里写清楚了”通常不能算第一层主控制",
        "Example: Why “It Is Clearly Stated in the IFU” Usually Cannot Be the Primary Control",
        body_zh="如果一个高风险误用本来就可以通过窗口设计、结构限制、接口区分或强制确认来降低，那么把主控制写成“在 IFU 中提醒用户注意”通常不够。这不是否定 IFU，而是说明标准更关心稳定控制，而不是事后把风险交给阅读和记忆。",
        body_en="If a high-risk misuse can already be reduced through display design, physical constraint, interface separation, or forced confirmation, then writing the primary control as “warn the user in the IFU” is usually weak. This does not mean the IFU is useless; it means the standard prefers stable controls over handing risk back to reading and memory.",
    )
)

MEDICAL_DEVICES_CONTENT["medical_device_urra"]["sections"].extend(
    [
        section(
            "critical",
            "## 为什么医疗器械 URRA 特别强调 critical task",
            "## Why Medical-Device URRA Puts Special Weight on Critical Tasks",
            body_zh="""
            在医疗器械里，critical task 不是“重要步骤”的口语说法，而是风险管理里的分水岭。因为一旦某一步做错就可能直接影响 patient safety 或 treatment effectiveness，这一步就必须被放大看。

            这会直接影响后面的三个动作：

            - 设计时是否要给更强的防错或确认机制
            - 说明书、标签和界面是不是需要更明确地支持这一步
            - validation 时是否必须把这一步放进高优先级观察情境
            """,
            body_en="""
            In medical devices, a critical task is not just an “important step” in everyday language. It is a threshold inside risk management. If performing the step incorrectly could directly affect patient safety or treatment effectiveness, the step must be elevated analytically.

            That changes at least three later decisions:

            - whether design needs stronger error-prevention or confirmation logic
            - whether IFU, labeling, and interface need stronger support around that step
            - whether validation must observe that step as a high-priority use scenario
            """,
        ),
        section(
            "regulatory",
            "## 为什么这页比一般 URRA 更强调可追踪性",
            "## Why This Page Cares More About Traceability Than Generic URRA",
            body_zh="""
            一般风险分析如果写得粗糙，问题已经不小；医疗器械场景里再写得粗糙，就会同时影响设计决策、验证计划和监管沟通。正因为如此，这页特别强调 traceability。

            团队必须能顺着一条链回看：

            - 这个步骤为什么被视为 critical
            - 这个 use error 是从哪个任务和场景推出的
            - 这个 control 是否真的对应这条风险链
            - 这个 control 又在哪里被验证
            """,
            body_en="""
            When generic risk analysis is weak, the consequences are already serious. In medical devices, weak analysis also distorts design decisions, validation planning, and regulatory communication. That is why this page cares so much about traceability.

            The team has to be able to trace one chain backward:

            - why the step was judged critical
            - which task and scenario the use error came from
            - whether the control really answers that risk path
            - where the control was later validated
            """,
        ),
    ]
)
MEDICAL_DEVICES_CONTENT["medical_device_urra"]["examples"].append(
    callout(
        "example",
        "critical",
        "案例：为什么“拔帽”和“确认方向”有时会比真正注射动作更关键",
        "Example: Why “Remove the Cap” and “Confirm Orientation” Can Matter More Than the Injection Itself",
        body_zh="在自注射装置里，真正高风险的节点未必是最后按压那一下。更早的方向确认、端部识别、拔帽顺序和装置朝向，往往一旦做错就会把后续所有动作带偏。这也是为什么医疗器械 URRA 不能只盯最显眼的使用动作。",
        body_en="In self-injection devices, the highest-risk node is not always the final act of pressing. Earlier actions such as orientation confirmation, end recognition, cap-removal sequence, and device alignment may matter more because once they fail, every later action is pulled off track. That is why medical-device URRA cannot focus only on the most visible use action.",
    )
)

MEDICAL_DEVICES_CONTENT["medical_device_use_errors"]["sections"].extend(
    [
        section(
            "boundary",
            "## 为什么这页真正难的是划清边界",
            "## Why the Hard Part of This Page Is Drawing the Boundaries Correctly",
            body_zh="""
            医疗器械 use error 分析最容易被写浅的地方，就是团队太快把所有坏结果都装进“user error”这个桶里。真正的分析难点在于区分：

            - 是器械自己没有按设计工作
            - 还是用户在可预见场景里被设计推向了错误
            - 还是发生了明显超出预期的 abnormal use
            - 还是操作者明知规则却故意偏离

            这几个边界一旦没划清，后面的控制、责任判断和验证重点都会跟着乱掉。
            """,
            body_en="""
            The easiest way to write medical-device use-error analysis badly is to place every bad outcome into one bucket called “user error.” The real difficulty is drawing the boundary between:

            - device malfunction
            - design-induced error inside foreseeable use
            - clearly abnormal use beyond the intended context
            - deliberate rule departure

            Once those boundaries are blurred, later controls, accountability judgments, and validation priorities also become blurred.
            """,
        ),
        section(
            "control_logic",
            "## 为什么分类会直接改变你最后改什么",
            "## Why Classification Directly Changes What Gets Redesigned",
            body_zh="""
            这页最实用的价值在这里：不同类型的问题，对应的控制策略完全不同。

            - 如果是 device failure，重点回到 engineering reliability
            - 如果是 design-induced use error，重点回到界面、标签、流程和可恢复性
            - 如果是 abnormal use，重点回到边界说明和风险沟通
            - 如果是 violation，重点还要看激励、文化和程序现实性

            所以分类不是学术洁癖，而是决定后面到底改哪里。
            """,
            body_en="""
            The most practical value of this page is that different problem types lead to different control strategies.

            - device failure pushes the response toward engineering reliability
            - design-induced use error pushes toward interface, labeling, workflow, and recoverability
            - abnormal use shifts attention toward boundary communication and foreseeable misuse management
            - violation forces the analysis to examine incentives, culture, and procedure realism

            Classification therefore is not academic purity. It determines what gets changed next.
            """,
        ),
    ]
)
MEDICAL_DEVICES_CONTENT["medical_device_use_errors"]["examples"].append(
    callout(
        "example",
        "control_logic",
        "案例：同样是“剂量不对”，为什么可能导向完全不同的改进",
        "Example: Why the Same “Wrong Dose” Outcome Can Lead to Completely Different Fixes",
        body_zh="如果剂量错误来自设备内部故障，改进重点应是硬件或软件可靠性；如果来自用户把 1.0 读成 10，重点就应回到显示、对比度、标记和确认流程；如果来自故意跳过检查，则还要看流程是不是过于脱离现实。结果一样，但控制路径完全不同。",
        body_en="If the wrong dose comes from internal device failure, the redesign focus belongs to hardware or software reliability. If it comes from reading 1.0 as 10, the focus belongs to display, contrast, marking, and confirmation workflow. If it comes from deliberately bypassing a check, the procedure may also be unrealistic. The outcome looks the same, but the control path is completely different.",
    )
)

MEDICAL_DEVICES_CONTENT["epipen_workbook"]["sections"].extend(
    [
        section(
            "translation",
            "## workbook 真正训练的是“翻译能力”",
            "## The Workbook Is Really Training Translation",
            body_zh="""
            这页的核心价值，不是让你认识表头，而是让你练习把前面学过的抽象概念翻译成工作文件。很多学生到了这里才会真正发现：知道 `critical task`、`hazardous situation` 和 `mitigation` 的定义，不等于会把它们写成一行清楚、能被团队继续使用的记录。

            workbook 的作用，就是逼你完成这一步翻译。
            """,
            body_en="""
            The core value of the workbook is not recognizing column headers. It is practicing translation from abstract concepts into working documentation. Many students only realize at this point that knowing the definitions of `critical task`, `hazardous situation`, and `mitigation` is not the same as writing them into one clear row that a team can actually use.

            The workbook forces that translation step to happen.
            """,
        ),
        section(
            "review",
            "## 一张 workbook 应该怎样被团队拿来审",
            "## How a Team Should Review a Workbook",
            body_zh="""
            一张好的 workbook 不是个人作业，而应该能支持多人审读。设计、人因、法规和临床如果一起看同一行，至少应该能对四件事达成共识：

            - 这一步到底在做什么
            - 错误路径写得是否具体
            - patient harm 有没有被写到位
            - 这个 mitigation 是不是足够强

            如果一行写出来后没人能稳定复述这四点，那它通常还不够好。
            """,
            body_en="""
            A strong workbook is not a private note. It should support multi-role review. If design, human factors, regulatory, and clinical reviewers look at the same row, they should at least be able to align on four things:

            - what the step actually is
            - whether the error path is specific enough
            - whether patient harm has been written clearly enough
            - whether the mitigation is strong enough

            If the row cannot support shared understanding on those points, it is usually still weak.
            """,
        ),
    ]
)
MEDICAL_DEVICES_CONTENT["epipen_workbook"]["examples"].append(
    callout(
        "example",
        "review",
        "案例：为什么 workbook 里最怕出现“表面完整、实质空心”的行",
        "Example: Why the Most Dangerous Workbook Row Is the One That Looks Complete but Says Very Little",
        body_zh="有些条目看起来每一列都填了，但 error 写成“improper use”，harm 写成“injury”，mitigation 写成“training”。这种行表面完整，实际上既不能指导设计，也不能指导验证。真正好的 workbook 行应该让团队一眼就知道下一步该改什么、该测什么。",
        body_en="Some rows look complete because every column contains text, but the error is written as “improper use,” the harm as “injury,” and the mitigation as “training.” Such rows are complete on the surface but analytically hollow. A strong row should let the team see immediately what must be redesigned and what must be tested next.",
    )
)
