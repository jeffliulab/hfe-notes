from __future__ import annotations

from note_blueprints import callout, page_blueprint, section, visual


FOUNDATIONS_CONTENT: dict[str, dict] = {
    "course_overview": page_blueprint(
        template_type="concept",
        page_intro_zh="本章重点是先把整门课读成一张地图：这不是一门背术语的课，而是一门用系统视角解释事故、分析失效并提出改进的课。",
        page_intro_en="This chapter establishes the course map first: the course is not mainly about memorizing terminology, but about using a systems lens to explain accidents, analyze breakdowns, and propose mitigations.",
        core_question_zh="这门课到底在训练什么能力？为什么后面的方法页、应用页和案例页，其实都在回答同一组问题？",
        core_question_en="What capability is this course really training, and why do the later method pages, application pages, and case pages keep answering the same set of questions?",
        must_learn_points_zh=[
            "这门课研究的不是“谁犯错了”，而是“人在系统里怎样和任务、工具、环境、组织一起作用”。",
            "课程主线是：先建立共同语言，再学习分析方法，再进入行业场景，最后回到事故、责任和伦理。",
            "后面的很多页虽然主题不同，但都在追问同一件事：失败是怎样产生的，为什么没被拦住，以及应该改哪里。",
            "这门课训练的不只是解释事故，更包括提出可操作的 mitigation。",
            "如果导论页没读明白，后面的名词会很多，但彼此很难连成线。",
        ],
        must_learn_points_en=[
            "The course is not centered on “who made the mistake,” but on how the person interacts with task, tools, environment, and organization.",
            "The course arc is shared language first, analytic methods second, domain applications third, and accident plus ethics analysis last.",
            "Many later pages look different on the surface, but they keep asking the same thing: how failure emerged, why it was not intercepted, and what should be changed.",
            "The course trains not only explanation of events, but also the ability to propose workable mitigations.",
            "Without the overview, the later terminology becomes harder to connect into one line of reasoning.",
        ],
        memory_anchor_zh="把整门课先记成一句话：看到事故时，不要停在“谁错了”，而要继续追问系统怎样让错误出现、扩大，或者没被拦住。",
        memory_anchor_en="The shortest memory line for the course is this: when an event happens, do not stop at who failed; keep asking how the system allowed the failure to appear, expand, or slip past defenses.",
        sections=[
            section(
                "forensic",
                "## 这门课为什么带有 `forensic` 的味道",
                "## Why the Course Has a Forensic Flavor",
                body_zh="""
这里的 `forensic` 不是让课程变成法庭流程课，而是强调一种分析姿态：面对伤害、险情或事故，不能只停在表面结果，而要把事件拆成一连串可追问的问题。

这套追问通常包括：

- 发生了什么
- 为什么会发生
- 原本哪几层防线应该拦住它
- 为什么这些防线没有起作用
- 后续 mitigation 应该改设计、改流程、改组织，还是一起改

所以这门课虽然会接触案例、责任和事故调查，但核心仍然是工程分析，而不是法律术语本身。
""",
                body_en="""
The word `forensic` does not turn the course into a courtroom-process class. It signals an analytic stance: when harm, near misses, or accidents occur, the analysis should not stop at the visible outcome.

The recurring questions are:

- what happened
- why it happened
- which defenses should have intercepted it
- why those defenses failed
- whether mitigation belongs in design, process, organization, or some combination

That is why the course touches cases, responsibility, and investigation while still remaining fundamentally an engineering-analysis course.
""",
            ),
            section(
                "architecture",
                "## 课程主线是怎样串起来的",
                "## How the Course Architecture Hangs Together",
                body_zh="""
这门课最容易被误读成“每周换一个主题”。其实课件已经把四个组件摆出来了：`issues / theory`、`analysis methods and frameworks`、`mitigations`、`cases`。

把这四块连起来，课程结构就很清楚：

1. 基础页先告诉你该怎样看人和系统。
2. 方法页把这种视角变成可操作的分析步骤。
3. 应用页让你看到同一套逻辑在航空、自动化和医疗器械里怎样落地。
4. 案例页再把前面的框架拉回真实事故和伦理判断。
""",
                body_en="""
The easiest misreading is to treat the course as “a new topic every week.” The lecture materials actually present four recurring elements: `issues / theory`, `analysis methods and frameworks`, `mitigations`, and `cases`.

Once those are linked, the structure becomes clear:

1. foundation pages explain how to see the human in the system
2. method pages turn that view into concrete analytic steps
3. application pages show how the same logic operates in aviation, automation, and medical devices
4. case pages pull the earlier frameworks back into real events and ethical judgment
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="整门课不是按行业拆散来讲，而是把“理论 - 方法 - 改进 - 案例”反复套在不同场景上。",
                note_body_en="The course is not split into disconnected industries; it keeps reapplying the sequence of theory, methods, mitigation, and cases across different contexts.",
            ),
            section(
                "goals",
                "## 学到最后到底要会什么",
                "## What You Are Supposed to Be Able to Do by the End",
                body_zh="""
从导论课件列出的 goals 看，这门课最终训练的是四种能力：

- 能把 incident 的 causes 用标准 HFE 语言讲清楚
- 能把系统中的 hazard 和 use-related risk 解释得简洁、准确
- 能提出 corrective actions 和 countermeasures，而不是只会复述问题
- 能判断设计 tradeoff 对 safety 和 performance 的影响

换句话说，这门课不是只训练“会看案例”，而是训练你把案例讲清楚、拆清楚，并给出有逻辑的改进方向。
""",
                body_en="""
The course goals point to four practical capabilities:

- explaining incident causes in clear human-factors language
- describing hazards and use-related risks accurately and concisely
- proposing corrective actions and countermeasures rather than only restating the problem
- evaluating how design tradeoffs influence safety and performance

So the course is not just about “reading cases.” It is about explaining them well, structuring them clearly, and turning them into defensible improvement paths.
""",
            ),
            section(
                "study",
                "## 这门课应该怎么学才不会散",
                "## How to Study the Course Without Losing the Thread",
                body_zh="""
比较有效的读法不是按周次被动跟着跑，而是始终带着同一条问题链去看每一页：

- 这页讲的是哪一种失败或限制
- 这页提供了什么分析工具
- 这页最后落到哪些 mitigation
- 这和前面的基础概念怎么连起来

如果一直沿着这条线读，`Swiss Cheese` 不会只是一个比喻，`URRA` 不会只是一个模板，案例页也不会只剩故事。
""",
                body_en="""
The most effective reading strategy is not simply following the weekly order. Instead, keep the same question chain active on every page:

- what kind of failure or limitation is this page about
- what analytic tool does it introduce
- what mitigation path does it imply
- how does it connect back to the earlier foundations

If that line is preserved, `Swiss Cheese` stops being only a metaphor, `URRA` stops being only a form, and the case pages stop being only stories.
""",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "study",
                "最容易走偏的读法",
                "The Most Common Reading Trap",
                body_zh="不要把课程读成“每页一个新名词”。如果只收集名词、不记主线，后面的事故分析就会变成概念拼盘。",
                body_en="Do not read the course as “one new term per page.” If the terms are collected without the logic, later accident analysis turns into an unstructured pile of concepts.",
            )
        ],
        examples=[
            callout(
                "example",
                "goals",
                "案例：同一个药物错误，整门课会怎样把它拆开",
                "Example: How the Course Would Unpack the Same Medication Error",
                body_zh="一次给药错误，导论页先要求你别急着下结论。基础页会让你区分 human error 和 system conditions；方法页会要求你写任务步骤、失败点和 risk controls；应用页会让你看设备、标签、工作环境和流程；案例页再把责任、组织和伦理层面加回来。也就是说，整门课不是反复看“一个故事”，而是反复训练你用不同层级把同一个问题拆开。",
                body_en="A medication error is not supposed to produce an immediate conclusion. The foundation pages separate human error from system conditions; the method pages ask for task steps, failure points, and risk controls; the application pages pull in device design, labeling, environment, and workflow; the case pages add organization, responsibility, and ethics. The course is therefore not repeatedly retelling one story. It is training you to decompose the same event across several layers.",
            )
        ],
        inline_visuals=[
            visual(
                "architecture",
                "Course intro 1-14-26.pdf",
                "这张图要看懂的是：课程的四个元素不是彼此分开的模块，而是理论、方法、改进和案例互相支撑的结构。",
                "This figure should make one thing visible: theory, methods, mitigation, and cases are not separate silos but mutually supporting elements of the course.",
                asset_name_contains="page-07",
            ),
        ],
        summary_points_zh=[
            "这门课带有 forensic 的味道，是因为它要求你对事故保持连续追问，而不是停在结论。",
            "课程骨架始终是：基础语言、分析方法、应用场景、案例与伦理。",
            "最终训练的能力包括解释 causes、提出 mitigation、评估 tradeoff。",
            "读整站时要始终带着同一条问题链：失败怎么出现、怎么扩散、怎么拦截、怎么改进。",
        ],
        summary_points_en=[
            "The course has a forensic flavor because it demands sustained questioning rather than a quick conclusion.",
            "Its architecture remains stable: foundational language, analytic methods, application contexts, and cases plus ethics.",
            "The target capability includes explaining causes, proposing mitigation, and evaluating tradeoffs.",
            "Read the whole site through one line: how failure emerged, how it spread, how it should have been intercepted, and what should change.",
        ],
    ),
    "human_factors_intro": page_blueprint(
        template_type="concept",
        page_intro_zh="本章重点是先把 `human factors` 读成设计学，而不是读成人的缺点清单。它关心的是：真实的人怎样和系统互动，以及系统应当怎样反过来适配真实的人。",
        page_intro_en="This chapter should first be read as a design discipline rather than a catalog of human weakness. It asks how real people interact with systems and how systems should be adapted to real people in return.",
        core_question_zh="如果系统最终总要由真实的人来感知、理解、判断、执行和恢复，那么设计时到底该把哪些人的特点与限制带回系统？",
        core_question_en="If systems are ultimately perceived, interpreted, judged, executed, and recovered by real people, which human characteristics and limits must be brought back into design?",
        must_learn_points_zh=[
            "人因工程研究的是人和系统其他要素的相互作用，而不是只研究“人本身”。",
            "它同时追求人的福祉和系统绩效，因为两者在真实系统里往往是一体两面。",
            "这门学科的发展方向经历了从“让人适应任务”到“让任务和设备更适应人”的转向。",
            "真正要被带回设计的，不只是身高和力量，也包括注意、感知、记忆、判断和习惯。",
            "培训是补充措施，好的系统设计才是第一道 mitigation。",
        ],
        must_learn_points_en=[
            "Human factors studies the interaction between people and the rest of the system rather than studying the person alone.",
            "It cares about well-being and performance together because those two often move together in real systems.",
            "The field shifted from “fit the human to the task” toward “fit the task and equipment to the human.”",
            "Design must account not only for body size and strength but also for attention, perception, memory, judgment, and habit.",
            "Training is supportive, but good system design is the primary mitigation layer.",
        ],
        memory_anchor_zh="记这一页最简单的方法是：人因工程不是要求人不断迁就系统，而是要求系统尽量贴近真实人的能力、限制和工作现实。",
        memory_anchor_en="The shortest memory line is this: human factors does not ask people to keep adapting endlessly to the system; it asks the system to fit real human capabilities, limits, and work conditions.",
        sections=[
            section(
                "definition",
                "## 人因工程到底在研究什么",
                "## What Human Factors Actually Studies",
                body_zh="""
先把定义翻成人话：`human factors` 研究的是人怎样和系统中的其他要素互动，然后把这些认识再用回设计。

这里的“系统其他要素”至少包括：

- 硬件和界面
- 软件和信息流
- 说明书、培训和流程
- 环境、时间压力和组织约束

所以人因工程不是孤立地研究“人”，而是在研究人放进真实系统以后，会遇到什么支持、什么摩擦、什么易错点。
""",
                body_en="""
In plain language, `human factors` studies how people interact with the other parts of a system and then feeds that understanding back into design.

Those “other parts” include at least:

- hardware and interfaces
- software and information flow
- instructions, training, and procedures
- environment, time pressure, and organizational constraints

Human factors therefore does not study “the human” in isolation. It studies what happens when a real person is placed inside a real system.
""",
            ),
            section(
                "history",
                "## 为什么人因工程后来开始强调“让系统适配人”",
                "## Why the Field Shifted Toward Fitting the System to the Human",
                body_zh="""
课件里有一条很重要的历史线索：早期很多工作都偏向 `fit the human to the task`，也就是通过选拔和训练，让人去适应工作。

这个思路后来遇到一个现实问题：设备越来越复杂，光靠挑更合适的人、做更多训练，也无法稳定解决界面差、信息差、控制逻辑差的问题。于是人因工程逐渐转向另一个核心判断：

系统、设备和任务设计本身，必须适配人的能力边界。

这条转向非常关键，因为它决定了后面的分析不会把培训当成默认答案，而会继续追问设计是不是已经把人推到吃力的位置。
""",
                body_en="""
The lecture highlights an important historical shift. Early work often followed a `fit the human to the task` model, relying on selection and training to make people adapt to work demands.

That approach eventually ran into a practical limit: as equipment became more complex, selection and training could not reliably compensate for poor interfaces, weak information design, or bad control logic. The field therefore moved toward a stronger position:

the system, equipment, and task design must fit human capabilities and boundaries.

That shift matters because it prevents later analysis from treating training as the default answer. It pushes the analysis back toward design quality.
""",
            ),
            section(
                "layers",
                "## 看“人”时，至少要看哪几层",
                "## Which Layers of the Human Matter in Design",
                body_zh="""
课件把人因工程的观察入口分成了三层：`physical`、`cognitive`、`behavioral`。这是一个很有用的读图方式。

- `physical`：身高、力量、可达性、视听能力、操作姿势等身体层约束
- `cognitive`：感知、注意、记忆、判断、决策等认知层约束
- `behavioral`：人在流程中会形成的习惯、捷径、协作方式和实际工作策略

只看其中一层通常不够。一个系统可能在物理尺寸上合格，却在认知上极难使用；也可能界面看似清楚，但实际工作中会诱发错误习惯。
""",
                body_en="""
The lecture divides the human-factors lens into three useful layers: `physical`, `cognitive`, and `behavioral`.

- `physical`: body size, strength, reach, sensory capability, and posture
- `cognitive`: perception, attention, memory, judgment, and decision making
- `behavioral`: habits, shortcuts, coordination patterns, and real work strategies

Design problems often appear when one of these layers is ignored. A system may satisfy physical requirements while remaining cognitively difficult to use, or it may look clear on paper while inducing risky habits in real work.
""",
                note_title_zh="这一节最重要的结论",
                note_title_en="The Main Conclusion of This Section",
                note_body_zh="人因工程不是只看“人体尺寸”，也不是只看“认知心理学”，而是把身体、认知和行为一起放回真实使用情境里。",
                note_body_en="Human factors is neither only body measurement nor only cognitive psychology. It brings body, cognition, and behavior back into real use conditions together.",
            ),
            section(
                "perception",
                "## 为什么感知和注意会直接变成设计问题",
                "## Why Perception and Attention Become Design Problems",
                body_zh="""
这一页后半段其实在铺垫一个重要事实：人不是被动、完整、稳定地接收信息的。

- 人会受颜色辨识能力限制影响
- 人会因为 habituation 对重复刺激逐渐不敏感
- 人的理解既受输入驱动，也受期待驱动

这意味着“信息已经显示出来了”并不等于“用户一定会看见并理解”。如果颜色、对比、布局、提示方式或默认期望设计得不好，系统就会在感知层和认知层同时埋下问题。
""",
                body_en="""
The second half of the lecture lays groundwork for a crucial fact: humans do not receive information in a passive, complete, or stable way.

- color discrimination varies across users
- repeated stimuli lose salience through habituation
- interpretation is shaped by both incoming signals and prior expectation

That means “the information was shown” is not the same as “the user saw and understood it.” Poor color choice, weak contrast, weak layout, or expectation mismatches create problems at both the perceptual and cognitive levels.
""",
            ),
            section(
                "application",
                "## 人因工程在设计里到底落到哪里",
                "## Where Human Factors Lands in Design",
                body_zh="""
把前面的内容收起来，真正落地时通常会变成这些设计问题：

- 关键信息是不是在对的时间、对的位置出现
- 控件和结果之间的 mapping 是否自然
- 警示是不是只靠一种脆弱线索，例如只靠颜色
- 使用流程有没有给检查、纠错和恢复留下空间
- 说明、标签和界面是否互相支持，而不是互相打架

所以人因工程不是停在“理解人”，而是要把理解变成更稳的设计、流程和环境。
""",
                body_en="""
When the earlier ideas are translated into practice, they become design questions such as:

- whether critical information appears at the right time and in the right place
- whether control-to-outcome mapping feels natural
- whether warnings depend on a single fragile cue such as color alone
- whether the workflow preserves checking, correction, and recovery space
- whether instructions, labels, and interface elements support one another

Human factors therefore does not stop at “understanding people.” It converts that understanding into more reliable design, workflow, and environment decisions.
""",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "history",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把人因工程缩成“培训再加强一点”。如果界面、流程和环境本身在制造困难，培训只能部分补洞，不能长期替代设计修正。",
                body_en="Do not reduce human factors to “better training.” If the interface, workflow, and environment are generating difficulty, training can only patch some of the gap and cannot replace design correction over time.",
            ),
            callout(
                "warning",
                "perception",
                "另一种常见误判",
                "Another Common Misjudgment",
                body_zh="不要默认“我能看懂，用户就一定能看懂”。颜色、对比度、字体、布局和期望都可能让同一信息被完全不同地接收。",
                body_en="Do not assume that “if I can read it, every user can read it.” Color, contrast, type, layout, and expectation can radically change how the same information is perceived.",
            ),
        ],
        examples=[
            callout(
                "example",
                "application",
                "案例：为什么输液泵的人因问题不只是“护士再仔细一点”",
                "Example: Why an Infusion-Pump Problem Is Not Solved by Telling the Nurse to Be More Careful",
                body_zh="如果输液泵的按钮名称相近、剂量确认流程过长、关键状态字小而不显眼，那么即使使用者接受过培训，仍然可能在繁忙病区里误选或漏看。人因工程在这里关心的不是“再多提醒一遍”，而是界面本身有没有把正确操作变容易。",
                body_en="If an infusion pump uses similar button labels, an overlong confirmation flow, and low-salience status information, a trained user may still mis-select or overlook critical information in a busy ward. Human factors is not asking for one more reminder; it is asking whether the interface itself makes correct action easier.",
            ),
            callout(
                "example",
                "perception",
                "案例：为什么不能只用颜色做关键告警",
                "Example: Why a Critical Warning Should Not Depend on Color Alone",
                body_zh="如果某个高风险状态只靠红绿区分来提示，那么色觉差异用户、低照度环境或高压力情境下的普通用户都可能把它读错。设计上更稳的做法是让颜色和文字、位置、形状、优先级层级一起工作。",
                body_en="If a high-risk state is communicated only through red-versus-green coding, users with color-vision differences, users in low-light conditions, and even ordinary users under pressure may misread it. The stronger design move is to combine color with text, position, shape, and clear priority cues.",
            ),
        ],
        inline_visuals=[
            visual(
                "perception",
                "01 Intro to HF and Risk (1).pptx",
                "这张图要看懂的是：同一组颜色在不同色觉条件下会被读成不同信息，所以关键设计不能只押在颜色一个线索上。",
                "This figure should make one point obvious: the same colors can be interpreted very differently across visual conditions, so critical design cannot rely on color as the only cue.",
                asset_name_contains="slide-24-image7",
            ),
            visual(
                "perception",
                "01 Intro to HF and Risk (1).pptx",
                "这张图要看懂的是：感知不是纯输入驱动，人的期待会影响自己“看见”什么，这会直接进入判断和操作。",
                "This figure should show that perception is not purely stimulus-driven; expectation changes what people think they are seeing, which then feeds into judgment and action.",
                asset_name_contains="slide-33-image11",
            ),
            visual(
                "application",
                "01 Intro to HF and Risk (1).pptx",
                "这张图要看懂的是：一个好的界面会通过外观和布局暗示使用方式，设计本身就在“教”用户怎么操作。",
                "This figure should make clear that a strong interface suggests how it should be used through appearance and layout; the design itself teaches the interaction.",
                asset_name_contains="slide-36-image14",
            ),
        ],
        summary_points_zh=[
            "人因工程研究的是人和系统其他要素的相互作用，而不是孤立的人。",
            "这门学科的重要转向是：不能只让人适应任务，也要让任务和设备适应人的边界。",
            "身体、认知和行为三层都要被带回设计。",
            "设计时不能假设用户一定会看见、记住、理解所有信息。",
            "培训是补充，界面、流程和环境设计才是第一道 mitigation。",
        ],
        summary_points_en=[
            "Human factors studies the interaction between people and the rest of the system rather than the isolated person.",
            "A key shift in the field is that tasks and equipment must fit human limits, not only the other way around.",
            "Body, cognition, and behavior all have to be brought back into design.",
            "Design cannot assume users will always see, remember, or understand every cue.",
            "Training is supportive; interface, workflow, and environmental design remain the first mitigation layer.",
        ],
    ),
    "human_error_frameworks": page_blueprint(
        template_type="concept",
        page_intro_zh="本章重点是看懂两件事：人为什么会出错，以及为什么分析错误时不能只盯着出错的人。",
        page_intro_en="This chapter focuses on two questions: why people make errors and why error analysis cannot stop at the individual who happened to fail.",
        core_question_zh="为什么人会出错，为什么不能把错误简单归咎于人，以及这套框架如何帮助我们找到真正该改的地方？",
        core_question_en="Why do people make errors, why can we not simply blame the individual, and how does this framework help us identify what should actually be fixed?",
        must_learn_points_zh=[
            "人会出错，不等于问题只在人身上。",
            "`slip`、`lapse`、`mistake`、`violation` 都像“出错”，但性质不同，后面的改法也不同。",
            "错误分析的终点不是贴标签，而是找到 root cause 和 mitigation。",
            "同一个表面错误，可能来自感知、认知或动作执行的不同环节。",
            "如果只看到“是谁错了”，通常会漏掉更重要的系统原因。",
        ],
        must_learn_points_en=[
            "People making errors does not mean the whole problem sits inside the person.",
            "`slip`, `lapse`, `mistake`, and `violation` all look like failure, but they are not the same type of failure.",
            "The goal of classification is not labeling; it is finding root cause and mitigation.",
            "The same surface error may emerge from perception, cognition, or action failure.",
            "If analysis stops at who failed, the larger system causes are usually missed.",
        ],
        memory_anchor_zh="""
人会出错，不是因为“人很差”，而是因为人的注意、记忆、判断都有边界；当系统设计不好、信息不清楚、流程不合理时，这些边界就会被放大，最后表现成错误。

接下来这页只回答一个问题：面对一次错误，我们到底应该怎么看，才能真正找到该改的地方。
""",
        memory_anchor_en="""
People do not err simply because they are “bad operators.” Attention, memory, and judgment all have limits, and poor design, unclear information, and weak workflows magnify those limits into visible failure.

This page therefore answers a single question: how should we read an error if we actually want to improve the system?
""",
        sections=[
            section(
                "definition",
                "## 什么叫人为失误",
                "## What Counts as Human Error",
                body_zh="""
先用最简单的话说，`human error` 指的是：人原本想把事情做对，但最后没有得到预期结果。

这个定义有两个关键信息：

- 它强调的是“原本想做对”，所以首先讨论的是无意偏差。
- 它讨论的不只是结果错了，还包括动作、顺序、时间、判断这些环节出了问题。

课件里给了两个常见定义，合起来读就够了：

- `Reason (1990)`：原本计划好的心理或身体活动，没有实现预期结果。
- `Hagen & Mays (1981)`：人在 `accuracy`、`sequence`、`time` 这些限制上没有把动作完成好。
""",
                body_en="""
In plain language, `human error` means a person intended to do the task correctly but failed to produce the intended result.

Two parts matter:

- the person was trying to do the task correctly, so the framework begins with unintended deviation
- the problem may sit in action, sequence, timing, or judgment rather than only in the final outcome

The two course definitions are enough to carry forward:

- `Reason (1990)`: a planned mental or physical activity fails to achieve the intended result
- `Hagen & Mays (1981)`: the action fails under constraints such as `accuracy`, `sequence`, or `time`
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="人为失误不是骂人的词，而是分析问题的词。它的价值在于把一次失败拆开看：动作做错了、漏做了、判断错了，还是系统把人推到了容易出错的位置。",
                note_body_en="Human error is not mainly a blame term; it is an analytic term. Its value lies in separating wrong action, omitted action, wrong judgment, and system-created error opportunity.",
            ),
            section(
                "system_view",
                "## 为什么不能简单怪人",
                "## Why We Cannot Stop at Blaming the Person",
                body_zh="""
如果一开始就认定“问题只在这个人身上”，那后面的所有分类最后都会变成更精细的责怪。

这也是为什么课件要把 `old view / new view`、`internal / external`、`sharp end / blunt end` 串成一条线：

- `old view`：系统基本是好的，出错主要是因为操作者粗心、能力差、没按要求做。
- `new view`：人会出错是事实，但更重要的问题是系统为什么让这个错误这么容易发生，或为什么没有把它拦住。
- `internal`：人的注意、记忆、疲劳和判断限制。
- `external`：界面、说明、环境、工作负荷和组织压力。
- `sharp end`：前线操作那一刻看得见的错误。
- `blunt end`：更上游的设计、制度、资源和组织决策。
""",
                body_en="""
If analysis starts with “the whole problem is inside the person,” every later category becomes a more refined version of blame.

That is why the lecture connects `old view / new view`, `internal / external`, and `sharp end / blunt end` in one line:

- `old view`: the system is basically fine and failure mainly reflects operator carelessness or weakness
- `new view`: people do err, but the deeper question is why the system made the error easy to produce or hard to stop
- `internal`: limits of attention, memory, fatigue, and judgment
- `external`: interface, instructions, environment, workload, and organizational pressure
- `sharp end`: the visible frontline action
- `blunt end`: the upstream design, policy, resource, and organizational decisions
""",
                note_title_zh="这一节最重要的结论",
                note_title_en="The Main Conclusion of This Section",
                note_body_zh="表面上看是人出错，深层上常常是系统在制造易错条件。",
                note_body_en="The visible failure may belong to the person, but the deeper vulnerability often belongs to the system creating error-prone conditions.",
            ),
            section(
                "taxonomy",
                "## 四类错误怎么区分",
                "## How to Distinguish the Four Error Types",
                body_zh="""
明白“不能只怪人”之后，下一步才是分类。分类不是为了显得专业，而是因为不同类型的错误，后面的改法根本不一样。

### 1. `slip`
一句话定义：计划是对的，但动作做错了。  
最典型的例子：想按 A，结果碰到了 B。

### 2. `lapse`
一句话定义：计划是对的，但该做的动作没有做出来。  
最典型的例子：漏掉检查步骤、该确认却没有确认。

### 3. `mistake`
一句话定义：动作执行得没问题，但前面的理解、判断或计划本身就是错的。  
最典型的例子：按照错误理解做出完全一致但错误的决策。

### 4. `violation`
一句话定义：知道规则，却仍然故意偏离规则。  
最典型的例子：为了赶时间明知不该跳步却还是跳步。

四类放在一起时，可以用这一组最短的句子去记：

- `slip`：想对了，手做错了。
- `lapse`：想对了，但漏做了。
- `mistake`：做得很一致，但一开始就想错了。
- `violation`：知道规则，但故意偏离了。
""",
                body_en="""
Once the analysis stops blaming the person, the next step is classification. Classification matters because different failure types require different fixes.

### 1. `slip`
The plan is correct, but the action execution goes wrong.  
Typical example: intending to press A but touching B.

### 2. `lapse`
The plan is correct, but the needed action never happens.  
Typical example: omitting a check or forgetting a confirmation.

### 3. `mistake`
Execution is smooth, but the understanding, judgment, or plan is wrong from the start.  
Typical example: consistently acting on the wrong interpretation.

### 4. `violation`
The rule is known, but the operator deliberately departs from it.  
Typical example: skipping a step to save time.

The shortest memory line is:

- `slip`: the intention was right, the hand was wrong
- `lapse`: the intention was right, but the action was omitted
- `mistake`: the execution was consistent, but the plan was wrong
- `violation`: the rule was known, but deliberately bypassed
""",
            ),
            section(
                "pca",
                "## PCA 模型为什么重要",
                "## Why the PCA Model Matters",
                body_zh="""
上一节解决的是“错误属于哪一类”，这一节继续往下追：同样一个表面错误，到底是在哪个环节开始出问题的。

`PCA` 指的是 `Perception - Cognition - Action`，也就是：

- `Perception`：有没有看到、听到、感觉到关键信息。
- `Cognition`：有没有理解对、记住、判断对。
- `Action`：最后的动作有没有正确做出来。

这一步重要，是因为“表面上一样”的错误，根因可能完全不同。

| 表面错误 | 实际可能错在什么地方 | 更合理的改进方向 |
| --- | --- | --- |
| 不小心按错按钮 | `Action`：知道按钮在哪里，但动作误触了 | 改按钮布局、间距、护罩、反馈 |
| 没看见隐藏按钮 | `Perception`：根本没看见或没感觉到按钮存在 | 改可见性、显著性、对比度 |
| 提前松开注射器推杆 | `Cognition`：把操作要求记错或理解错了 | 改说明、时间反馈、任务引导 |
""",
                body_en="""
The previous section answers “what kind of error is this?” The PCA model asks a deeper question: where did the problem start to grow?

`PCA` stands for `Perception - Cognition - Action`:

- `Perception`: was the critical cue seen, heard, or sensed?
- `Cognition`: was it understood, remembered, and judged correctly?
- `Action`: was the final action executed correctly?

That matters because the same surface failure can have completely different roots.

| Surface failure | Where the deeper problem may sit | Better design response |
| --- | --- | --- |
| pressing the wrong button | `Action`: the button was known, but execution slipped | change spacing, guards, and feedback |
| missing a hidden button | `Perception`: the cue was not seen or noticed | change visibility, salience, and contrast |
| releasing a syringe too early | `Cognition`: the user remembered or understood the rule incorrectly | change instructions, timing feedback, and task guidance |
""",
                note_title_zh="这一节最重要的结论",
                note_title_en="The Main Conclusion of This Section",
                note_body_zh="PCA 的价值不在于多记一个缩写，而在于提醒你：不要只看最后那一下动作，要看错误是从哪一段开始长出来的。",
                note_body_en="The value of PCA is not the acronym itself. It is the reminder not to stare only at the final action, but to ask where the error started to develop.",
            ),
            section(
                "application",
                "## 这套框架怎么用",
                "## How to Use the Framework",
                body_zh="""
真正分析一个错误时，可以按下面这条线走：

```mermaid
flowchart TD
    A[看到一次错误结果] --> B{是否故意偏离规则?}
    B -- 是 --> C[先按 violation 看]
    B -- 否 --> D{计划本身是否正确?}
    D -- 是 --> E[再区分 slip 或 lapse]
    D -- 否 --> F[按 mistake 看]
    E --> G[继续追动作、记忆、界面、负荷]
    F --> H[继续追理解、规则、信息、心智模型]
    C --> I[继续追流程压力、组织环境、系统约束]
    G --> J[找到 root cause]
    H --> J
    I --> J
    J --> K[对应设计 mitigation]
```

这个流程最重要的意义是：不要一上来就说“加强培训”。先分类型，再追根因，最后再决定是该改界面、改流程、改提示、改说明，还是改组织安排。
""",
                body_en="""
When analyzing a real event, walk the framework in order:

```mermaid
flowchart TD
    A[Observe a visible failure] --> B{Was there a deliberate rule deviation?}
    B -- Yes --> C[Start from violation]
    B -- No --> D{Was the plan itself correct?}
    D -- Yes --> E[Differentiate slip vs lapse]
    D -- No --> F[Classify as mistake]
    E --> G[Trace action, memory, interface, and workload]
    F --> H[Trace understanding, rules, information, and mental model]
    C --> I[Trace workflow pressure, organization, and constraints]
    G --> J[Identify root cause]
    H --> J
    I --> J
    J --> K[Design the mitigation]
```

The practical point is simple: do not jump straight to “more training.” Classify first, trace the deeper cause second, and only then decide whether the right response is interface change, workflow change, prompting, documentation, or organizational redesign.
""",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "taxonomy",
                "最容易混淆的点",
                "The Most Common Confusions",
                bullets_zh=[
                    "`slip` 不是“不知道该怎么做”，而是“知道怎么做，却在动作执行时出偏差”。",
                    "`lapse` 不是动作做错，而是动作根本没发生，常常和记忆、注意脱落有关。",
                    "`mistake` 看起来也可能很流畅，因为执行阶段并没有乱，错的是更前面的规则理解、知识使用或心智模型。",
                    "`violation` 带有意图，所以它和前三类无意失误不一样；但分析到这里也还不能停止。",
                ],
                bullets_en=[
                    "`slip` is not not knowing what to do; it is knowing what to do and still deviating during execution.",
                    "`lapse` is not a wrong action; it is an omitted action, usually tied to memory or attention dropout.",
                    "`mistake` can look smooth because execution itself may be consistent; the problem sits earlier in rule use or mental model.",
                    "`violation` carries intent, so it differs from the other three, but that does not mean the analysis ends there.",
                ],
            )
        ],
        examples=[
            callout(
                "example",
                "system_view",
                "案例：为什么不能只怪拿错药的人",
                "Example: Why the Wrong-Medication Event Cannot Stop at Blaming the Nurse",
                body_zh="医院把外包装非常相似的药物放在相邻位置，平时一直没有出事；直到某次值班里，一名疲劳中的护士拿错了药，最后造成患者伤害。这个案例最容易被写成一句话：“护士拿错药了。”但真正更有价值的问题是：为什么两种药会放在一起？为什么包装相似到足以混淆？为什么疲劳状态下还要承担高风险识别任务？为什么前面没有更强的核对和拦截？",
                body_en="A hospital stores two look-alike medications next to each other. Nothing happens for a while, until a fatigued nurse selects the wrong one during a shift and the patient is harmed. The shallow summary is “the nurse picked the wrong drug.” The better questions are why the medications were stored together, why the packaging was so confusable, why a fatigued operator had to perform the high-risk discrimination, and why stronger checks failed to intercept the error.",
            ),
            callout(
                "example",
                "taxonomy",
                "四个迷你案例",
                "Four Mini Cases",
                bullets_zh=[
                    "`slip`：护士本来想按“静音报警”，手却碰到了旁边的“停止输注”。",
                    "`lapse`：值班人员知道要做双人核对，但处理完前一个任务后直接进入下一步，把核对动作漏掉了。",
                    "`mistake`：医生根据错误理解把病情判断成另一种情况，后面的动作都做得很一致，但整个处理建立在错误判断上。",
                    "`violation`：操作员知道要扫码确认，却因为高峰期赶进度直接跳过。",
                ],
                bullets_en=[
                    "`slip`: a nurse intends to press “silence alarm” but hits “stop infusion” instead.",
                    "`lapse`: the operator knows a double-check is required but moves on after the previous task and omits it entirely.",
                    "`mistake`: a physician interprets the situation incorrectly and then acts consistently on that wrong understanding.",
                    "`violation`: an operator knows scanning is required but skips it during a rush.",
                ],
            ),
            callout(
                "example",
                "pca",
                "案例：同样是“提前结束注射”，根因可能完全不同",
                "Example: The Same Early Injection Stop Can Have Different Roots",
                bullets_zh=[
                    "如果是手指无意打滑，那更接近 `Action` 问题。",
                    "如果是使用者误以为推杆已经到底，那更接近 `Perception` 问题。",
                    "如果是使用者把“按压 10 秒”记成了“按压 6 秒”，那更接近 `Cognition` 问题。",
                ],
                bullets_en=[
                    "If the finger slips unintentionally, the root is closer to `Action`.",
                    "If the user wrongly perceives that the plunger is already fully depressed, the root is closer to `Perception`.",
                    "If the user remembers “hold for 10 seconds” as “hold for 6 seconds,” the root is closer to `Cognition`.",
                ],
            ),
        ],
        inline_visuals=[
            visual(
                "system_view",
                "02 Intro to Human Error (1).pptx",
                "这张图要你看懂的不是“有人是坏苹果”，而是如果默认系统没有问题，分析就会自动滑向 blame，而不是 redesign。",
                "The point of this figure is not that some people are “bad apples,” but that once the system is presumed healthy, analysis slides automatically toward blame instead of redesign.",
                asset_name_contains="slide-11-image2",
            ),
            visual(
                "taxonomy",
                "02 Intro to Human Error (1).pptx",
                "这张图要你看懂的是：表面上都叫“出错”，但 slip、lapse、mistake、violation 发生在不同层次，所以不能用同一种补救办法处理。",
                "This figure should make one point visible: slip, lapse, mistake, and violation all look like failure on the surface, but they occur at different layers and should not trigger the same fix.",
                asset_name_contains="slide-16-image4",
            ),
            visual(
                "pca",
                "03 HE Frameworks (2).pptx",
                "这张图要你看懂的是：同一个表面错误，可能来自感知、认知、动作执行的不同环节，所以 root cause 和 mitigation 也会不同。",
                "This figure should make clear that the same surface failure may come from perception, cognition, or action, which means root cause and mitigation will also differ.",
                asset_name_contains="slide-14-image2",
            ),
        ],
        summary_points_zh=[
            "人为失误讨论的不是“谁烂”，而是错误为什么发生。",
            "只盯着出错的人，很容易漏掉真正重要的系统原因。",
            "`slip`、`lapse`、`mistake`、`violation` 必须分开看，因为后面的改法不同。",
            "`old view` 容易把问题收缩成 blame，`new view` 更关注系统怎样制造或放大风险。",
            "PCA 模型提醒我们：同一个表面错误，根因可能在感知、认知或动作的不同环节。",
            "给错误分类的终点不是分类本身，而是找到更有效的 root cause 和 mitigation。",
        ],
        summary_points_en=[
            "Human error analysis is about why failure happened, not about who is “bad.”",
            "Stopping at the failing individual usually misses the larger system causes.",
            "`slip`, `lapse`, `mistake`, and `violation` must be separated because they lead to different mitigations.",
            "The `old view` compresses failure into blame; the `new view` asks how the system created or amplified the risk.",
            "The PCA model reminds us that the same surface error may begin in perception, cognition, or action.",
            "Classification is only useful if it leads to better root-cause analysis and mitigation.",
        ],
    ),
    "swiss_cheese": page_blueprint(
        template_type="concept",
        page_intro_zh="本章重点是把“事故为什么会发生”从单点失误，推进到多层防线如何一起失守。Swiss Cheese 模型最重要的价值，不是那个比喻本身，而是它把注意力重新拉回系统屏障和漏洞对齐。",
        page_intro_en="This chapter pushes accident explanation from single-point failure toward the way multiple defenses fail together. The value of the Swiss Cheese model is not the metaphor itself, but the way it redirects attention to barriers and aligned vulnerabilities.",
        core_question_zh="为什么高风险系统明明有很多防线，事故还是会发生？真正危险的到底是一层失效，还是多层屏障在同一时刻同时失守？",
        core_question_en="Why do accidents still happen in high-risk systems that appear to have many defenses, and is the real danger one failed layer or multiple defenses failing together at the same time?",
        must_learn_points_zh=[
            "Swiss Cheese 模型把事故看成多层防线被穿透，而不是最后一个人突然犯了大错。",
            "每一层防线都可能同时具有保护作用和漏洞，所以“有屏障”不等于“屏障可靠”。",
            "真正危险的不是某一个洞存在，而是多个洞在时间和条件上对齐。",
            "这套模型的价值，是把 blame 转回 barrier design、latent conditions 和 system resilience。",
            "它很好用，但不能被当成完整终点，还要结合动态变化和更深层根因分析。",
        ],
        must_learn_points_en=[
            "The Swiss Cheese model treats accidents as penetration of multiple defenses rather than a single dramatic personal failure.",
            "Each layer can protect while still containing vulnerabilities, so the existence of a barrier does not guarantee dependable protection.",
            "The real danger is not one hole by itself, but several holes aligning across time and conditions.",
            "The model redirects blame-oriented thinking toward barrier design, latent conditions, and system resilience.",
            "It is useful, but it should not be treated as the full endpoint of analysis; dynamic change and deeper causal analysis still matter.",
        ],
        memory_anchor_zh="记这页时先抓一句话：事故通常不是因为最后一个人太差，而是因为多层本来应该拦截问题的防线，在同一时刻都没有起作用。",
        memory_anchor_en="The shortest memory line is this: accidents usually do not happen because the last operator was uniquely weak, but because several defenses that should have intercepted the problem failed at the same time.",
        sections=[
            section(
                "model",
                "## Swiss Cheese 模型到底在解释什么",
                "## What the Swiss Cheese Model Explains",
                body_zh="""
这套模型真正解释的是：复杂系统里的 harm path 往往不是“一步到位”形成的，而是一路穿过屏障、程序、检查、人和组织控制，最后才落到结果层。

一旦接受这个前提，事故就不再像一个孤立爆点，而像一条原本应该被多次拦住的问题链。也正因为如此，模型的关注点天然不是“谁最后按错了”，而是“为什么前面那么多层都没有拦住”。
""",
                body_en="""
What the model really explains is that harm paths in complex systems rarely emerge in one step. They move through barriers, procedures, checks, people, and organizational controls before reaching the outcome layer.

Once that is accepted, an accident no longer looks like an isolated explosion point. It looks like a problem chain that should have been intercepted several times. The natural focus therefore shifts from “who made the final wrong move” to “why so many prior layers failed to intercept it.”
""",
            ),
            section(
                "holes",
                "## 防线为什么会一边保护、一边带着漏洞",
                "## Why Defenses Protect and Still Contain Holes",
                body_zh="""
这页最重要的现实感在这里：防线从来不是绝对防线。

- 有些漏洞是长期潜伏的，例如设计弱点、资源不足、流程不现实、组织容忍或错误激励。
- 有些漏洞是当下触发的，例如疲劳、分心、沟通断裂、时间压力、天气和工作负荷。

真正危险的时候，不是某一个洞单独存在，而是长期潜伏条件和短时触发恰好叠在一起，让一条原本不该贯通的路径被打通。
""",
                body_en="""
This is where the model becomes concrete: defenses are never absolute.

- some holes are latent and persistent, such as design weakness, limited resources, unrealistic procedure, organizational tolerance, or poor incentives
- some holes are immediate triggers, such as fatigue, distraction, communication breakdown, time pressure, weather, or workload

The dangerous moment is not the existence of one hole alone, but the overlap between latent conditions and active triggers that opens a path which should never have been continuous.
""",
                note_title_zh="这一节最重要的结论",
                note_title_en="The Main Conclusion of This Section",
                note_body_zh="系统防线不能只问“有没有”，而要问“在真实运行条件下还能不能挡得住”。",
                note_body_en="The right question for a barrier is not only whether it exists, but whether it still works under real operating conditions.",
            ),
            section(
                "benefits",
                "## 这套模型为什么这么常用",
                "## Why This Model Is Used So Widely",
                body_zh="""
Swiss Cheese 模型之所以流行，不只是因为图好记，而是因为它把复杂风险快速讲清楚了：

- 它让人一眼看到安全不是靠单一屏障，而是靠 layered defense。
- 它能把 risk reduction 讲成很具体的问题：加一层、补一层、缩小洞、减少对齐机会。
- 它适用于航空、核电、医疗等多种高风险系统，因为这些系统都依赖多层拦截。

所以这套模型非常适合做第一层讲解，也非常适合在跨专业团队里建立共同语言。
""",
                body_en="""
The model is widely used not just because the graphic is memorable, but because it makes complex risk legible very quickly:

- it shows that safety depends on layered defense rather than a single barrier
- it turns risk reduction into concrete questions: add a layer, strengthen a layer, shrink holes, reduce alignment
- it transfers well across aviation, nuclear power, healthcare, and other high-risk domains because all of them rely on multiple interception layers

That makes the model highly effective as a first explanatory tool and as a shared language across mixed teams.
""",
            ),
            section(
                "limits",
                "## 这套模型也有什么局限",
                "## What the Model Cannot Do on Its Own",
                body_zh="""
课件没有把 Swiss Cheese 当成完美答案，而是专门列了 criticism。这个提醒很重要：

- 模型容易让人误以为各层屏障彼此独立、系统基本静态
- 它强调 barriers，却可能让人忽略“洞为什么会不断长出来”
- 如果只停在图示层面，分析会显得很 generic，不够贴近真实工作

这也是后来会出现 `Hot Cheese Model` 这类更新的原因：真实系统是动态变化的，新增 mitigation 甚至可能自己再引入新风险。
""",
                body_en="""
The lecture does not treat Swiss Cheese as a perfect answer. Its listed criticisms matter:

- the model can imply that barriers are independent and the system is relatively static
- it emphasizes barriers, but may hide the deeper question of why holes keep appearing
- if the analysis stops at the graphic, it becomes too generic and too detached from real work

That is why later updates such as the `Hot Cheese Model` matter: real systems change over time, and even a new mitigation can introduce fresh risk.
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="Swiss Cheese 很适合当起点，但不能代替动态系统分析和更深层的 causal analysis。",
                note_body_en="Swiss Cheese is a strong starting point, but it cannot replace dynamic systems thinking or deeper causal analysis.",
            ),
            section(
                "design",
                "## 这套框架怎么真正拿来分析事故",
                "## How to Actually Use the Framework in Accident Analysis",
                body_zh="""
把这页真正用起来时，可以按一条很实用的分析顺序走：

1. 先找 harm vector，也就是最后伤害是怎样形成的。
2. 再往回找原本应该拦截它的屏障有哪些。
3. 对每一层继续追问：它是不存在、失效了，还是看似存在但在真实条件下无效。
4. 最后区分哪些是 latent conditions，哪些是 active failures，并把 mitigation 对应回具体层级。

这样做的结果是，事故分析就不会只剩一个“最后责任人”，而会变成一张系统漏洞地图。
""",
                body_en="""
To actually use the framework, a practical sequence is:

1. identify the harm vector, meaning how the final harm path formed
2. work backward through the barriers that should have intercepted it
3. ask for each layer whether it was absent, failed, or only looked effective on paper
4. separate latent conditions from active failures and map mitigation back to specific layers

The result is that the analysis no longer ends with a single “responsible operator.” It becomes a system vulnerability map.
""",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "holes",
                "最容易误读的地方",
                "The Most Common Misreading",
                body_zh="不要把模型读成“只要多加几层防线就一定更安全”。如果新增层级本身很弱、互相冲突，或者和真实工作脱节，层数增加并不等于韧性增加。",
                body_en="Do not read the model as “more layers always mean more safety.” If the added layers are weak, conflicting, or detached from real work, more layers do not automatically produce more resilience.",
            ),
            callout(
                "warning",
                "limits",
                "另一个常见陷阱",
                "Another Common Trap",
                body_zh="不要把 Swiss Cheese 画成图以后就以为分析结束了。图只是帮助你看到层和洞，真正困难的是解释这些洞为什么会持续存在、怎样被组织条件放大。",
                body_en="Do not assume that drawing the Swiss Cheese picture completes the analysis. The picture helps reveal layers and holes, but the hard part is still explaining why those holes persist and how organizational conditions magnify them.",
            ),
        ],
        examples=[
            callout(
                "example",
                "benefits",
                "案例：为什么 COVID 图示能把模型一下子讲明白",
                "Example: Why the COVID Illustration Explains the Model So Quickly",
                body_zh="口罩、社交距离、清洁消毒、洗手都不是完美屏障，但它们叠在一起时会显著降低 harm path 被打通的机会。这个例子好用，是因为它把“每层都有洞，但多层一起仍然有意义”直观地画出来了。",
                body_en="Masks, distancing, cleaning, and handwashing are not perfect barriers, but together they reduce the chance that a harm path remains open. The example works because it makes one idea intuitive: every layer can have holes and still contribute meaningfully when stacked with others.",
            ),
            callout(
                "example",
                "design",
                "案例：一条事故路径是怎样穿透多层防线的",
                "Example: How One Accident Path Penetrates Several Layers",
                body_zh="想象一台医疗设备在夜班里被错误设定剂量。最后那一下输入错误只是 `sharp end`。更上游可能已经同时存在：界面字段易混、标签不清、双人核对流于形式、工作负荷过高、培训把重点放错。单看最后一步，很像“某个人输错了”；从 Swiss Cheese 看，真正的问题是多层防线一起失守。",
                body_en="Imagine a medical device receiving an incorrect dose setting during a night shift. The final wrong entry is only the `sharp end`. Upstream there may already be a confusable interface, unclear labeling, a superficial double-check process, excessive workload, and training that emphasized the wrong cues. If only the final action is inspected, the story becomes “someone typed it incorrectly.” Through Swiss Cheese, the deeper story is that several defenses failed together.",
            ),
            callout(
                "example",
                "design",
                "案例：为什么 Deepwater Horizon 和 Challenger 都适合用这套框架读",
                "Example: Why Both Deepwater Horizon and Challenger Fit This Framework",
                body_zh="这两个案例都不是“一个零件坏了”这么简单。Deepwater Horizon 里既有数据误读、设备失效，也有时间和预算压力；Challenger 里既有材料和测试问题，也有 schedule pressure 和 oversight / culture 问题。Swiss Cheese 的作用，就是让这些看似分散的因素能被放回同一条穿透路径里。",
                body_en="Neither case reduces cleanly to “one part failed.” Deepwater Horizon involved data misinterpretation, equipment failure, and time or budget pressure; Challenger involved material and testing problems together with schedule pressure and oversight or culture failures. Swiss Cheese helps place those seemingly scattered factors back onto one penetration path.",
            ),
        ],
        inline_visuals=[
            visual(
                "model",
                "05 Swiss Cheese Model.pdf",
                "这张图要看懂的是：事故不是绕过一层防线，而是沿着多层漏洞被连续放行。",
                "This figure should make one idea visible: accidents do not bypass only one barrier; they pass through a chain of weaknesses across several layers.",
                asset_name_contains="page-06",
            ),
            visual(
                "benefits",
                "05 Swiss Cheese Model.pdf",
                "这张图要看懂的是：每一层措施都不完美，但多层叠加仍然能明显降低风险路径被打通的概率。",
                "This figure should show that each measure is imperfect on its own, yet layering still sharply reduces the chance that a risk path stays open.",
                asset_name_contains="page-07",
            ),
        ],
        summary_points_zh=[
            "Swiss Cheese 模型把事故解释成多层防线的连续穿透。",
            "真正危险的是 latent conditions 和 active triggers 在时间上重合。",
            "这套模型很适合建立共同语言和第一层事故解释。",
            "它的局限在于容易静态化、图像化，因此还需要更深层根因分析补上。",
            "真正用它时，要把 harm vector、barriers、holes 和 mitigation 一层一层对应起来。",
        ],
        summary_points_en=[
            "The Swiss Cheese model explains accidents as sequential penetration of multiple defenses.",
            "The deepest danger appears when latent conditions overlap with active triggers.",
            "The model is highly effective for building shared language and a first-pass accident explanation.",
            "Its limitation is that it can become too static and purely graphical, so deeper causal analysis still has to follow.",
            "To use it well, map the harm vector, barriers, holes, and mitigation layer by layer.",
        ],
    ),
}
