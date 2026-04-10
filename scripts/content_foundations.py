from __future__ import annotations

from note_blueprints import callout, page_blueprint, section, visual


FOUNDATIONS_CONTENT: dict[str, dict] = {
    "course_overview": page_blueprint(
        template_type="concept",
        page_intro_zh="这页先帮你看清整门课的主线：HFE 不是把错误归给人，而是研究人在复杂系统里怎样被设计、任务、组织和环境共同塑形。",
        page_intro_en="This page establishes the course arc: HFE is not about pinning failure on people, but about understanding how design, task demands, organization, and environment shape human performance in complex systems.",
        core_question_zh="如果后面的方法页和案例页要读得顺，这一页必须先回答一个问题：这门课到底在分析什么对象，是单个人，还是人在系统里的位置？",
        core_question_en="If the later method pages and case pages are going to make sense, this page has to answer one prior question: what is the unit of analysis in this course, the individual, or the person embedded in a system?",
        must_learn_points_zh=[
            "这门课的分析单位不是“某个人做错了什么”，而是“人在系统中承担什么角色、被什么条件约束”。",
            "课程主线是：先建共同语言，再学分析方法，再进应用场景，最后回到案例与伦理。",
            "后续所有方法页其实都在回答同一组问题：任务是什么、哪里可能失败、系统怎样拦截或放大失败。",
            "如果导论页没看懂，后面的 Swiss Cheese、URRA、CRM 和案例页都会显得像碎片。",
        ],
        must_learn_points_en=[
            "The recurring unit of analysis is not “what one person did wrong,” but the person-in-system relationship.",
            "The course arc is language first, methods second, application domains third, and cases plus ethics last.",
            "Later method pages keep answering the same questions: what the task is, where failure can emerge, and how the system blocks or amplifies it.",
            "Without this frame, Swiss Cheese, URRA, CRM, and the case pages feel disconnected.",
        ],
        memory_anchor_zh="把这门课先记成一句话：它研究的不是“人很容易出错”，而是“系统怎样让正确行为变得更容易，让错误更难穿透防线”。",
        memory_anchor_en="Remember the course this way: it is not about proving that people are error-prone, but about understanding how systems make correct action easier and prevent failure from piercing defenses.",
        sections=[
            section(
                "arc",
                "## 课程主线",
                "## Course Arc",
                body_zh="""
先把课程骨架记住，后面很多页就能自动归位：

1. 先用 `human factors`、`human error`、`Swiss Cheese` 这些基础页建立共同语言。
2. 再用 `error analysis`、`task analysis`、`URRA` 这些方法页，把“问题”写成可分析、可追踪的结构。
3. 然后进入航空、自动化和医疗器械等应用场景，看同一套分析逻辑怎样落到不同系统。
4. 最后通过 operational risk、Cardosi、737 Max 等案例，把分析扩展到组织、监管和伦理层。
""",
                body_en="""
Keep the course arc in mind:

1. Build shared language through `human factors`, `human error`, and `Swiss Cheese`.
2. Turn that language into structure through `error analysis`, `task analysis`, and `URRA`.
3. Apply the logic in aviation, automation, and medical-device settings.
4. End with cases such as operational risk, Cardosi, and the 737 Max, where organizational and ethical issues become unavoidable.
""",
            ),
            section(
                "unit",
                "## 这门课真正分析的对象是什么",
                "## What the Course Actually Analyzes",
                body_zh="""
课程并不是把“一次失误”当成终点，而是把失误当作入口。真正要分析的是：

- 人当时承担什么任务
- 系统提供了什么信息和工具
- 环境、组织和时间压力如何影响判断
- 防线为什么没有把错误挡住

所以这门课里几乎没有哪一页是在单独研究“人的毛病”。更准确地说，它研究的是人在系统里如何被支持，或如何被逼到容易出错的位置。
""",
                body_en="""
The course does not stop at the visible mistake. It treats the mistake as an entry point into a larger analysis:

- what task the person was performing
- what information and tools the system provided
- how environment, organization, and time pressure shaped judgment
- why defenses failed to intercept the problem

That is why almost no page in the course is really about “human weakness” in isolation. It is about how people are supported or set up to fail inside systems.
""",
            ),
            section(
                "map",
                "## 怎样用这张学习地图读后面的页",
                "## How to Use This Learning Map",
                body_zh="""
读后面内容时，可以持续用一条固定主线来串：

- 基础页回答：系统应该怎样看人。
- 方法页回答：怎样把问题写成分析对象。
- 应用页回答：同一套问题在不同行业里如何出现。
- 案例页回答：当事故真的发生时，哪些系统层因素一起起作用。

只要一直沿着这条线走，后面的内容就不会变成概念堆积。
""",
                body_en="""
Use a single reading line for the rest of the site:

- foundation pages explain how to see the human inside the system
- method pages explain how to turn that view into an analyzable structure
- application pages show how the same logic appears in different industries
- case pages show which system-layer factors interact when events actually unfold

Following that line keeps the site from turning into a pile of disconnected terms.
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="这门课最值得带走的不是一串术语，而是一种视角：别只问谁错了，要问系统为什么让这个错误出现、扩大、或者没被拦住。",
                note_body_en="The real takeaway is not a set of terms but a stance: do not stop at who failed; ask why the system allowed the failure to appear, expand, or pass through defenses.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "map",
                "最容易走偏的读法",
                "The Most Common Reading Trap",
                body_zh="不要把课程读成“每页一个新名词”。如果只记名词而不记主线，你会在后面的案例页里不知道该把哪个概念放到哪里。",
                body_en="Do not read the course as “one new term per page.” If the terms are memorized without the logic, the later case pages will feel unstructured and hard to analyze.",
            )
        ],
        examples=[
            callout(
                "example",
                "unit",
                "案例：为什么同一个错误可以被两门课读出完全不同的结论",
                "Example: Why the Same Error Can Produce Two Very Different Lessons",
                body_zh="如果只从“谁犯错了”出发，一次药物配置错误可能只会被总结成“护士不够仔细”。但这门课会继续问：标签是否清楚、容器是否易混、核对流程是否现实、工作负荷是否超标。导论页的价值，就是先把这种分析习惯建立起来。",
                body_en="If analysis starts and ends with “who made the mistake,” a medication-preparation error turns into “the nurse was not careful enough.” This course keeps going: were the labels clear, were the containers confusable, was the verification process realistic, and was workload excessive? The overview matters because it establishes that habit before anything else.",
            )
        ],
        inline_visuals=[
            visual(
                "arc",
                "Course intro 1-14-26.pdf",
                "这张预览图要看懂的是：整门课并不是按行业拆开讲，而是按“基础语言 -> 方法 -> 应用 -> 案例”逐层推进。",
                "This preview should make the course architecture visible: the site is not split by industry first, but by language, methods, applications, and then cases.",
                index=0,
            ),
            visual(
                "map",
                "Course intro 1-14-26.pdf",
                "这张预览图要看懂的是：课程后半段虽然进入航空和医疗器械场景，但它们都在回收前面学过的同一套 HFE 分析框架。",
                "This preview should make one point clear: even when the course moves into aviation and medical-device contexts, it keeps reusing the same HFE logic introduced earlier.",
                index=1,
            ),
        ],
        summary_points_zh=[
            "课程先建语言，再建方法，再进入场景和案例。",
            "分析单位始终是“人在系统中的位置”，不是脱离环境的个人。",
            "后续每一页都可以用“任务、失败点、防线”这条主线来读。",
            "导论页的作用是给整站提供一个不会丢线的阅读地图。",
        ],
        summary_points_en=[
            "The course builds language first, methods second, and applications plus cases afterward.",
            "The recurring unit of analysis is the person in the system, not the isolated individual.",
            "Later pages can all be read through the same line: task, failure point, and defense.",
            "The overview page exists to provide a reading map for the entire site.",
        ],
    ),
    "human_factors_intro": page_blueprint(
        template_type="concept",
        page_intro_zh="这一页先回答最基础的问题：human factors 到底是什么。它不是“研究人类缺点”的学科，而是把人的能力与限制真正带回设计里。",
        page_intro_en="This page answers the foundational question: what is human factors? It is not a catalog of human weakness, but a discipline that deliberately brings real human capabilities and limits back into design.",
        core_question_zh="如果系统最后总是要靠人来使用、监控、判断和恢复，那么设计时应该怎样把人的能力、限制和工作现实纳入系统？",
        core_question_en="If systems ultimately depend on people to use, monitor, judge, and recover, how should design account for human capabilities, limits, and the reality of work?",
        must_learn_points_zh=[
            "人因工程同时追求人的福祉与系统绩效，不是只偏向“效率”或“舒服”。",
            "它研究的不是抽象的人，而是真实情境中的使用者：会疲劳、会分心、会受时间压力影响。",
            "好设计不是让专家勉强能用，而是让普通用户在压力下也不容易走错。",
            "培训很重要，但人因工程优先改系统，而不是先把责任压给使用者。",
        ],
        must_learn_points_en=[
            "Human factors pursues both human well-being and system performance.",
            "It studies real users in context, not abstract ideal users.",
            "Good design is not merely expert-usable; it remains usable under pressure and distraction.",
            "Training matters, but human factors starts by improving the system rather than blaming the user.",
        ],
        memory_anchor_zh="记这一页最简单的方法是：人因工程不是让人去迁就系统，而是让系统尽量贴近真实的人。",
        memory_anchor_en="The shortest way to remember this page is that human factors does not ask people to adapt endlessly to systems; it asks systems to fit real people better.",
        sections=[
            section(
                "definition",
                "## 人因工程到底在做什么",
                "## What Human Factors Actually Does",
                body_zh="""
课件里的定义看起来很正式，但学生读这页时先抓住一句人话就够了：人因工程是在研究人和系统中其他要素怎样相互作用，然后把这种理解再用回设计。

这件事之所以重要，是因为系统最后总要落到真实的人手里。界面、硬件、软件、说明、环境和流程，只要有一个环节不匹配，最终都会变成使用负担、出错机会或恢复困难。
""",
                body_en="""
The formal definition is broad, but the student-level reading is simple: human factors studies how people interact with the rest of the system and then feeds that understanding back into design.

That matters because every interface, hardware element, software workflow, instruction set, and environment ultimately lands in the hands of a real user. Any mismatch becomes burden, error opportunity, or recovery difficulty.
""",
            ),
            section(
                "goals",
                "## 为什么它同时关心福祉和绩效",
                "## Why It Cares About Well-Being and Performance Together",
                body_zh="""
很多人直觉上会把“人的福祉”和“系统绩效”看成两件互相冲突的事，但人因工程把它们放在一起看。原因很直接：

- 一个让人持续费力、困惑、易疲劳的系统，长期绩效通常不会好。
- 一个只追求表面效率、却把恢复和检查机会拿掉的系统，安全性通常也会变差。

所以这门学科追求的不是“谁让步”，而是怎样通过设计让两者一起变好。
""",
                body_en="""
Students often assume that human well-being and system performance pull in opposite directions, but human factors treats them as linked.

- systems that are exhausting, confusing, and cognitively expensive usually perform poorly over time
- systems that chase surface efficiency by removing recovery and checking opportunities usually become less safe

The discipline therefore asks how design can improve both rather than force a tradeoff by default.
""",
            ),
            section(
                "application",
                "## 人因工程在设计里具体落到哪里",
                "## Where Human Factors Lands in Design",
                body_zh="""
这页真正想把你从“概念理解”推进到“设计理解”。如果说人因工程是系统设计的一部分，那么它具体会落到：

- 信息是否在正确时间出现
- 界面是否支持快速辨识和正确映射
- 步骤顺序是否符合人的认知流程
- 系统是否给了检查、纠错和恢复空间

也就是说，它不是只存在于实验室或培训课里，而是直接写进产品、流程和环境本身。
""",
                body_en="""
This page should move the reader from abstract definition to design consequence. If human factors is part of system design, it lands in questions such as:

- whether information appears at the right time
- whether the interface supports fast recognition and correct mapping
- whether step order matches human cognition
- whether the system preserves checking, correction, and recovery space

In other words, it lives in the product, workflow, and environment, not only in research labs or training rooms.
""",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "application",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把人因工程缩成“培训再加强一点”。如果界面、流程和环境本身在制造困难，那么单靠培训很难稳定抵消这些设计缺陷。",
                body_en="Do not collapse human factors into “better training.” If the interface, workflow, and environment are generating difficulty, training alone rarely cancels that risk in a stable way.",
            )
        ],
        examples=[
            callout(
                "example",
                "application",
                "案例：为什么输液泵的人因问题不只是“护士再仔细一点”",
                "Example: Why an Infusion-Pump Problem Is Not Solved by Telling the Nurse to Be More Careful",
                body_zh="如果输液泵的按钮名称相近、剂量确认流程长、关键状态字小而不显眼，那么即使使用者接受过培训，仍然可能在繁忙病区里误选或漏看。人因工程在这里关心的不是“再多提醒一遍”，而是界面本身有没有把正确操作变容易。",
                body_en="If an infusion pump uses similar button labels, a long confirmation flow, and low-salience status information, a trained user may still mis-select or overlook critical information in a busy ward. Human factors is not asking for one more reminder; it is asking whether the interface itself makes correct action easier.",
            )
        ],
        summary_points_zh=[
            "人因工程研究的是人和系统其他要素的相互作用。",
            "它追求人的福祉与系统绩效同时优化。",
            "真实用户的疲劳、分心和工作现实必须被带回设计。",
            "培训是补充，系统设计才是首要抓手。",
        ],
        summary_points_en=[
            "Human factors studies the interaction between people and the rest of the system.",
            "It aims to optimize well-being and performance together.",
            "Fatigue, distraction, and real work conditions must be designed for rather than ignored.",
            "Training is supportive; system design remains the primary lever.",
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
        page_intro_zh="这页把课程里的系统视角再往前推一步：事故不是因为某一个人突然犯了大错，而是因为多层防线同时出现漏洞，并在某个时刻被串成了一条穿透路径。",
        page_intro_en="This page pushes the systems view one step further: accidents do not emerge only because one person suddenly makes a dramatic mistake, but because multiple defenses contain weaknesses that align into a path of penetration.",
        core_question_zh="为什么高风险系统明明有很多防线，事故还是会发生？这些防线的漏洞又为什么会在同一个时刻被串起来？",
        core_question_en="Why do accidents still happen in high-risk systems that appear to have many defenses, and how do the weaknesses in those defenses align at the same time?",
        must_learn_points_zh=[
            "Swiss Cheese 模型把事故看成“多层防线被穿透”，而不是“单个人失手”。",
            "每一层防线都可能既有保护作用，也有漏洞。",
            "真正危险的不是某一个洞存在，而是多个洞在时空上对齐。",
            "这套模型的价值，是把注意力从 blame 拉回 barrier design 和 system resilience。",
        ],
        must_learn_points_en=[
            "The Swiss Cheese model treats accidents as penetrations of multiple defenses rather than as isolated individual failures.",
            "Each layer can provide protection while still containing vulnerabilities.",
            "The deepest danger is not one hole by itself, but several holes aligning in time and circumstance.",
            "The value of the model is that it redirects attention from blame to barrier design and system resilience.",
        ],
        memory_anchor_zh="记这页时先抓一句话：事故往往不是因为“最后一个人太差”，而是因为系统里的多层保护在同一时刻都没能把问题挡住。",
        memory_anchor_en="The shortest memory line for this page is that accidents usually do not happen because the final operator was uniquely weak, but because several layers of protection failed to stop the problem at the same time.",
        sections=[
            section(
                "model",
                "## Swiss Cheese 模型到底在解释什么",
                "## What the Swiss Cheese Model Explains",
                body_zh="""
这套模型的核心不是“奶酪上有洞”这个比喻本身，而是它背后的解释逻辑：任何高风险系统都不会只靠一层保护，而是靠多层屏障、程序、检查、人员配合和组织控制共同维持安全。

一旦你接受这个前提，事故就不再是“某个点突然失败”，而更像是一条本来应该被多次拦截的问题链，最终一路穿透到了结果层。
""",
                body_en="""
The core of the model is not the cheese metaphor itself, but the logic underneath it: high-risk systems are protected by multiple barriers, procedures, checks, people, and organizational controls rather than a single safeguard.

Once that is clear, an accident no longer looks like a single-point collapse. It looks like a failure path that should have been intercepted several times but instead passed through each layer.
""",
            ),
            section(
                "holes",
                "## 防线和漏洞为什么会同时存在",
                "## Why Barriers and Holes Coexist",
                body_zh="""
课程用这页提醒你一个很关键的现实：有防线，并不等于防线总是有效。

- 有些漏洞是长期存在的设计弱点、资源不足、流程不合理或组织容忍。
- 有些漏洞是短时出现的，例如疲劳、分心、时间压力、天气、沟通失误。

真正危险的时刻，是这些长期条件和短时触发在同一时间叠在一起。
""",
                body_en="""
The lecture uses this model to emphasize one practical reality: having a barrier does not mean the barrier is always effective.

- some holes are latent and persistent, such as weak design, low resources, unrealistic procedure, or organizational tolerance
- some holes are active and temporary, such as fatigue, distraction, time pressure, weather, or communication breakdown

The dangerous moment is when the latent conditions and active triggers line up at once.
""",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="系统防线不是“有了就行”，而是要持续问：它们在真实运行条件下还挡得住吗？",
                note_body_en="Barriers are not safe merely because they exist. The real question is whether they still work under real operating conditions.",
            ),
            section(
                "design",
                "## 这套模型为什么会把分析拉回系统设计",
                "## Why the Model Redirects Analysis to System Design",
                body_zh="""
如果事故被理解成防线穿透，那改进方向就不会只剩下“提醒人更小心”。更成熟的追问会变成：

- 哪一层防线原本应该拦住问题
- 为什么那一层防线没有起作用
- 有没有哪一层本来就设计得太脆弱
- 多层防线之间是不是留下了彼此都以为对方会负责的空白

这也是为什么 Swiss Cheese 模型在课程里不是一个独立比喻，而是后面 risk methods、operational risk 和案例页的共同底板。
""",
                body_en="""
Once an accident is understood as barrier penetration, the improvement path cannot stop at “be more careful.” The stronger questions become:

- which layer should have intercepted the problem
- why that layer failed in real conditions
- whether any layer was designed too weakly from the start
- whether the boundaries between layers created responsibility gaps

That is why Swiss Cheese is not an isolated metaphor in the course. It becomes the base layer for later risk methods, operational risk, and case analysis.
""",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "holes",
                "最容易误读的地方",
                "The Most Common Misreading",
                body_zh="不要把模型读成“只要多加几层防线就一定更安全”。如果新增的层级本身很弱、彼此冲突，或者和真实工作脱节，层数增加并不等于韧性增加。",
                body_en="Do not read the model as “more layers always mean more safety.” If the added layers are weak, conflicting, or detached from real work, more layers do not automatically produce more resilience.",
            )
        ],
        examples=[
            callout(
                "example",
                "design",
                "案例：一条事故路径是怎样穿透多层防线的",
                "Example: How One Accident Path Penetrates Several Layers",
                body_zh="想象一台医疗设备在夜班里被错误设定剂量。最后那一下输入错误只是 `sharp end`。更上游可能已经同时存在：界面字段易混、标签不清、双人核对流于形式、工作负荷过高、培训把重点放错。单看最后一步，很像“某个人输错了”；从 Swiss Cheese 看，真正的问题是多层防线一起失守。",
                body_en="Imagine a medical device receiving an incorrect dose setting during a night shift. The final wrong entry is only the `sharp end`. Upstream there may already be a confusable interface, unclear labeling, a superficial double-check process, excessive workload, and training that emphasized the wrong cues. If only the final action is inspected, the story becomes “someone typed it incorrectly.” Through Swiss Cheese, the deeper story is that several defenses failed together.",
            )
        ],
        inline_visuals=[
            visual(
                "model",
                "05 Swiss Cheese Model.pdf",
                "这张图要看懂的是：事故不是绕过一层防线，而是沿着多层漏洞被连续放行。",
                "This figure should make one idea visible: accidents do not bypass only one barrier; they pass through a chain of weaknesses across several layers.",
                index=0,
            ),
            visual(
                "holes",
                "05 Swiss Cheese Model.pdf",
                "这张图要看懂的是：漏洞既可能来自长期潜伏条件，也可能来自当下触发因素，真正危险的是两者在同一时刻重合。",
                "This figure should make clear that holes may come from latent conditions or immediate triggers, and the real hazard appears when they overlap.",
                index=1,
            ),
        ],
        summary_points_zh=[
            "Swiss Cheese 模型把事故理解成多层防线穿透。",
            "每一层屏障都可能同时具有保护作用和漏洞。",
            "长期潜伏条件和短时触发叠加时，事故路径最容易形成。",
            "这套模型的真正价值是把改进方向拉回 barrier design 和 system resilience。",
        ],
        summary_points_en=[
            "The Swiss Cheese model reads accidents as penetration of multiple defenses.",
            "Each barrier can protect while still containing vulnerabilities.",
            "Accident paths form most easily when latent conditions overlap with immediate triggers.",
            "The real value of the model is that it redirects improvement toward barrier design and resilience.",
        ],
    ),
}
