from __future__ import annotations

from note_blueprints import callout, page_blueprint, section, visual


CASES_ETHICS_CONTENT: dict[str, dict] = {
    "operational_risk": page_blueprint(
        template_type="concept",
        page_intro_zh="Operational risk 这页要你看到的，是风险不只存在于某一次错误动作里，而是长期藏在运行条件、组织约束和 work as done 里。",
        page_intro_en="This page asks you to see that operational risk does not live only inside one visible error. It lives over time in operating conditions, organizational constraints, and work as done.",
        core_question_zh="为什么真正的运行风险往往不是一次事件才突然出现，而是系统在日常运行中慢慢积累出来的？",
        core_question_en="Why does real operational risk usually not appear only at the moment of one event, but accumulate gradually inside everyday operations?",
        must_learn_points_zh=[
            "operational risk 关注的是日常运行系统，而不只是单次失误。",
            "work as imagined 和 work as done 往往存在结构性差距。",
            "组织约束、时间压力、环境变化和一线补丁行为会持续重塑风险水平。",
            "这页把 Swiss Cheese、fatigue、stress、procedure 等页面重新拉回同一运行视角。",
        ],
        must_learn_points_en=[
            "Operational risk focuses on the ongoing operating system rather than on one isolated error.",
            "Work as imagined and work as done often diverge structurally.",
            "Organizational constraints, time pressure, environmental change, and frontline workaround behavior continuously reshape risk.",
            "This page pulls Swiss Cheese, fatigue, stress, and procedure pages back into one operating view.",
        ],
        memory_anchor_zh="先记住一句话：运行风险不是事故发生后才有的东西，它通常在事故前很久就已经存在于工作条件里。",
        memory_anchor_en="Keep one sentence in mind: operational risk does not begin when the accident happens; it usually lives in the work conditions long before the event surfaces.",
        sections=[
            section(
                "logic",
                "## operational risk 到底在看什么",
                "## What Operational Risk Actually Looks At",
                body_zh="这页关心的不是单个动作的对错，而是系统在持续运行时有没有逐步变脆。换句话说，它问的是：班次、资源、流程、组织目标和现场补救行为，是否正在侵蚀原本设计好的安全边界。",
                body_en="The page is not mainly about whether one isolated action was right or wrong. It asks whether the system is becoming more fragile while it operates continuously. In other words, are shifts, resources, procedures, organizational goals, and frontline adaptations eroding the safety boundary that design originally assumed?",
            ),
            section(
                "gap",
                "## 为什么 work as imagined 和 work as done 的差距会变成风险",
                "## Why the Gap Between Work as Imagined and Work as Done Becomes Risk",
                body_zh="管理和设计往往先写出一个理想流程，但一线工作会受到时间压力、设备状态、环境变化和资源限制影响。如果系统长期只检查“有没有按理想流程做”，却不看实际工作如何被挤压和变形，风险就会被低估。",
                body_en="Management and design often start with an ideal workflow, but frontline work is shaped by time pressure, equipment state, environmental change, and resource limits. If the system checks only whether the ideal procedure was followed and not how real work is being squeezed and reshaped, risk gets underestimated.",
            ),
            section(
                "application",
                "## 这页为什么会成为很多案例页的底板",
                "## Why This Page Becomes the Base Layer for Many Case Pages",
                body_zh="很多案例页最后都会回到 operational risk，因为一线错误很少是孤立的。背后常常已经累积了长期的组织张力、任务负荷和现实约束，而这些因素平时就已经在慢慢改变风险结构。",
                body_en="Many case pages eventually return to operational risk because frontline errors are rarely isolated. Behind them, there are often long-standing organizational tensions, workload patterns, and real-world constraints that have already been reshaping the risk structure over time.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="operational risk 的价值，是提醒你把事故看成运行系统的产物，而不是看成单次偶发偏差。",
                note_body_en="The value of operational risk is that it makes you read the event as a product of the operating system rather than as a one-off deviation.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "logic",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把 operational risk 理解成“又一个风险清单”。它更像是一种持续追问运行条件是否在侵蚀防线的视角。",
                body_en="Do not treat operational risk as just another checklist. It is better understood as a viewpoint that continuously asks whether operating conditions are eroding defenses.",
            )
        ],
        examples=[
            callout(
                "example",
                "gap",
                "案例：为什么长期 workaround 会变成运行风险信号",
                "Example: Why Persistent Workarounds Become an Operational-Risk Signal",
                body_zh="如果一线人员长期用临时补丁绕过某条程序，那通常不是“员工不守规矩”这么简单，而是一个更深的运行信号：程序可能已经不再适配真实任务节奏，系统正在靠脆弱补丁维持表面正常。",
                body_en="If frontline staff repeatedly rely on a workaround to bypass a procedure, the signal is usually deeper than “people are not following the rules.” It may mean the procedure no longer fits real task rhythm and the system is maintaining normality through fragile patches.",
            )
        ],
        inline_visuals=[
            visual(
                "logic",
                "Operational Risk 2-18-2026.pdf",
                "这张图要看懂的是：运行风险不是单点问题，而是随着运行条件持续变化的一组系统约束。",
                "This figure should make clear that operational risk is not a single-point problem but a set of system constraints that shift with operating conditions.",
                index=0,
            )
        ],
        summary_points_zh=[
            "operational risk 关注的是持续运行中的风险生成。",
            "理想流程和真实工作之间的差距会不断改变风险水平。",
            "组织约束和 workaround 是重要风险信号。",
            "这页为后面的案例分析提供系统运行视角。",
        ],
        summary_points_en=[
            "Operational risk is about how risk is generated during ongoing operations.",
            "The gap between ideal procedure and real work continually changes risk level.",
            "Organizational constraints and workarounds are important risk signals.",
            "This page gives later cases their operating-system perspective.",
        ],
    ),
    "cardosi_case": page_blueprint(
        template_type="case",
        page_intro_zh="Cardosi 这一页真正有价值的地方，是把 ATC / aviation 的具体问题重新拉回一个人因视角：通信、显示、程序和团队理解是怎样在同一个系统里交织的。",
        page_intro_en="The real value of the Cardosi page is that it brings concrete ATC and aviation issues back under a human-factors lens, showing how communication, displays, procedure, and shared understanding interact inside one system.",
        core_question_zh="在这个案例语境里，为什么“通信听起来像技术细节”，最后却会变成人因、程序和情境意识共同作用的系统问题？",
        core_question_en="In this case setting, why does something that seems like a technical communication detail become a system problem involving human factors, procedure, and situation awareness all at once?",
        must_learn_points_zh=[
            "Cardosi 案例的重点不是记住事故故事，而是学会把 ATC 场景拆成 communication、display、procedure 和 SA 问题。",
            "被遮挡、被踩话或不完整接收的通信，是典型的人因风险入口。",
            "案例页训练的是把抽象概念重新识别进真实事件的能力。",
            "事后看很明显，不代表当事人在当时也有同样信息条件。",
        ],
        must_learn_points_en=[
            "The point of the Cardosi page is not memorizing a story, but learning to decompose the ATC setting into communication, display, procedure, and SA problems.",
            "Blocked, stepped-on, or incompletely received communications are classic entry points for human-factors risk.",
            "Case pages train the ability to recognize abstract concepts inside real events.",
            "Hindsight clarity does not mean the people in the moment had the same information conditions.",
        ],
        memory_anchor_zh="先记住这个案例的一句话判断：在航空通信场景里，信息一旦被挡住、踩断或误解，后面的显示、程序和团队理解都会连锁受影响。",
        memory_anchor_en="Keep this case judgment in mind: in aviation communication settings, once information is blocked, stepped on, or misread, later displays, procedures, and team understanding are all affected in cascade.",
        sections=[
            section(
                "background",
                "## 背景与 stakes",
                "## Background and Stakes",
                body_zh="Cardosi 材料把注意力放在 ATC 环境中信息怎样被发出、接收、打断和误解。因为航空通信本来就是时间关键型任务，所以任何一段信息丢失都可能迅速影响后续判断和动作。",
                body_en="The Cardosi material focuses on how information is transmitted, received, interrupted, and misunderstood inside the ATC environment. Because aviation communication is already a time-critical task, any partial information loss can quickly affect later judgment and action.",
            ),
            section(
                "chain",
                "## 这个案例的事件链应该怎么读",
                "## How to Read the Event Chain in This Case",
                body_zh="这类案例不能只看“谁说错了”或“谁没听清”。更成熟的读法是把通信通道、显示支持、程序要求和团队心智模型放到一起看：信息在哪一层被削弱了，谁因此形成了错误局面理解，哪一层本来可以更早补位。",
                body_en="Cases like this cannot stop at “who misspoke” or “who did not hear correctly.” A stronger reading combines communication channel, display support, procedural requirements, and team mental model: where was the information weakened, who built the wrong picture because of that, and which layer could have recovered earlier?",
            ),
            section(
                "system",
                "## 这个案例教会我们的系统层问题",
                "## The System-Level Lesson of the Case",
                body_zh="Cardosi 案例之所以重要，是因为它把一个看似局部的通信问题，重新暴露成系统设计问题：通道本身是否易受阻断、关键内容是否有冗余表达、程序是否帮团队共享同一局面、显示和流程是否给了补救机会。",
                body_en="The importance of the Cardosi case lies in turning what looks like a local communication problem back into a system-design problem: how vulnerable is the channel to blockage, whether critical content has redundancy, whether procedure supports a shared team picture, and whether displays and workflow create recovery opportunities.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="Cardosi 这页要你学会的，不是一个结论，而是一种案例读法：从局部通信问题回推系统层的人因结构。",
                note_body_en="What the Cardosi page teaches is not one final answer, but a reading method: move from a local communication problem back to the system-level human-factors structure underneath it.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "system",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="最容易掉进的坑，是事后觉得“信息明明很清楚”。案例分析必须尽量回到当事人在当时真正看见、真正听到和真正理解到的局面。",
                body_en="The easiest trap is hindsight: it feels obvious after the fact. Case analysis has to return as closely as possible to what people actually saw, heard, and understood in the moment.",
            )
        ],
        examples=[
            callout(
                "example",
                "chain",
                "案例锚点：被踩话的通信为什么会放大后续风险",
                "Case Anchor: Why a Stepped-On Transmission Amplifies Later Risk",
                body_zh="Cardosi 材料里提到 blocked / stepped-on communication 的问题。危险并不只在于一段话没听完整，而在于后面所有显示判断、程序执行和团队理解，都可能建立在这段残缺信息上继续往前走。",
                body_en="The Cardosi material highlights blocked and stepped-on communication. The danger is not only that one message is incomplete, but that later display interpretation, procedure execution, and team understanding may all continue forward on top of that damaged information.",
            )
        ],
        inline_visuals=[
            visual(
                "background",
                "Cardosi 2-2-2026.pdf",
                "这张预览图要看懂的是：ATC 场景里的通信并不是背景噪声，而是直接塑造后续理解和行动的核心工作流。",
                "This preview should make clear that communication in the ATC setting is not background noise; it is the core workflow shaping later understanding and action.",
                index=0,
            ),
            visual(
                "chain",
                "Cardosi 2-2-2026.pdf",
                "这张预览图要看懂的是：一旦通信通道发生被遮挡或踩话，后续的人因问题会沿着整个链条继续扩散。",
                "This preview should show that once the communication channel is blocked or stepped on, the later human-factors problems propagate along the whole chain.",
                index=1,
            ),
        ],
        summary_points_zh=[
            "Cardosi 案例是 communication、display、procedure 和 SA 的交叉案例。",
            "被踩话或不完整接收的信息是重要风险入口。",
            "案例分析必须回到当事人的当时信息条件。",
            "重点是学会从局部问题回推系统结构。",
        ],
        summary_points_en=[
            "The Cardosi case sits at the intersection of communication, display, procedure, and SA.",
            "Stepped-on or incompletely received information is a major risk entry point.",
            "Case analysis must return to the information conditions available in the moment.",
            "The real skill is moving from a local issue back to the system structure underneath it.",
        ],
    ),
    "f16_analysis_prompts": page_blueprint(
        template_type="case",
        page_intro_zh="F16 prompts 这一页本质上是“怎么分析案例”的脚手架，它不是直接给答案，而是给你一套不会漏掉关键维度的提问路径。",
        page_intro_en="The F16 prompts page is essentially a scaffold for case analysis. It does not give the answer directly; it gives a questioning path that prevents the analyst from missing key dimensions.",
        core_question_zh="当面对一个复杂案例时，怎样用 prompts 把观察、解释和改进建议组织成一个结构，而不是想到哪里问到哪里？",
        core_question_en="When facing a complex case, how can prompts organize observation, explanation, and recommendation into a structure rather than a random list of thoughts?",
        must_learn_points_zh=[
            "prompts 的价值在于结构化提问，而不是提问数量本身。",
            "它能帮助分析者同时看信息、界面、程序、团队和组织因素。",
            "prompt 的本质，是把案例分析从单因解释拉回多层解释。",
            "这页教的是分析框架，不是单一案例答案。",
        ],
        must_learn_points_en=[
            "The value of prompts lies in structured questioning rather than in the sheer number of questions.",
            "They help analysts examine information, interface, procedure, team, and organizational factors together.",
            "The essence of prompting is moving case analysis away from single-cause explanation toward layered explanation.",
            "This page teaches an analysis framework rather than one case-specific answer.",
        ],
        memory_anchor_zh="先记住这个案例的一句话判断：好的 prompt 不是让你问更多问题，而是让你问更不容易漏层的问题。",
        memory_anchor_en="Keep this case judgment in mind: a good prompt does not simply make you ask more questions; it makes you ask questions that are less likely to miss important layers.",
        sections=[
            section(
                "background",
                "## 背景与 stakes",
                "## Background and Stakes",
                body_zh="复杂案例最怕的是分析没有结构，大家各说一段现象，最后却没有形成因果逻辑。prompts 的作用，就是让团队在讨论时共享同一套观察维度和展开顺序。",
                body_en="Complex cases are vulnerable to structureless analysis, where everyone contributes fragments of observation but no coherent causal logic emerges. Prompts help the team share one observation frame and one unfolding order during discussion.",
            ),
            section(
                "chain",
                "## 这些 prompts 真正帮助你做什么",
                "## What These Prompts Actually Help You Do",
                body_zh="它们把案例拆成若干稳定维度：事件背景、任务、信息、界面、程序、团队、组织和改进建议。这样一来，分析就不容易只围着最显眼的一条解释打转。",
                body_en="The prompts decompose the case into stable dimensions such as background, task, information, interface, procedure, team, organization, and recommendations. That prevents the analysis from circling only around the most visible explanation.",
            ),
            section(
                "system",
                "## 为什么这种结构会让复盘质量明显提高",
                "## Why This Structure Improves Review Quality",
                body_zh="一旦团队对提问路径达成一致，讨论就更容易从“谁对谁错”转到“哪些证据支持哪条因果链、哪些改进最有针对性”。这正是 prompts 真正的价值。",
                body_en="Once the team aligns on the questioning path, the discussion can move from “who was right or wrong” toward “which evidence supports which causal chain and which intervention is most targeted.” That is the real value of the prompts.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="F16 prompts 教你的，不是某个事件答案，而是如何把课程概念稳定地搬进复杂案例分析。",
                note_body_en="The F16 prompts do not teach one event answer; they teach how to move course concepts reliably into complex case analysis.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "chain",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把 prompts 当成“问题越多越好”的列表。没有结构的多问题，只会把讨论拉散；真正有用的是提问顺序和维度覆盖。",
                body_en="Do not treat prompts as a “more questions is better” list. A large number of unstructured questions only diffuses discussion; the useful part is the sequence and dimensional coverage.",
            )
        ],
        examples=[
            callout(
                "example",
                "system",
                "案例：为什么同一个案例用 prompt 分析会更像工程复盘",
                "Example: Why Prompted Analysis Looks More Like Engineering Review",
                body_zh="没有 prompt 时，团队很容易停留在“某人判断错了”。用了 prompt 之后，讨论会被迫补齐信息、界面、程序、团队和组织层，这时案例就从故事变成了可执行的工程复盘。",
                body_en="Without prompts, a team often stops at “someone made the wrong judgment.” With prompts, the discussion is forced to fill in information, interface, procedure, team, and organizational layers, so the case becomes an actionable engineering review rather than only a story.",
            )
        ],
        summary_points_zh=[
            "prompts 的核心价值是结构化提问。",
            "它帮助团队覆盖多个因果维度。",
            "这页教的是分析框架，而不是标准答案。",
            "真正效果是把讨论拉回工程复盘逻辑。",
        ],
        summary_points_en=[
            "The core value of prompts is structured questioning.",
            "They help teams cover multiple causal dimensions.",
            "This page teaches an analysis framework rather than a fixed answer.",
            "Their real effect is to pull discussion back toward engineering-review logic.",
        ],
    ),
    "boeing_737max_and_ethics": page_blueprint(
        template_type="case",
        page_intro_zh="737 Max 这一页之所以被放在伦理部分，不是因为它脱离技术，而是因为这里的技术、组织、培训、监管和责任分配根本无法被拆开。",
        page_intro_en="The 737 Max belongs in the ethics section not because it is separate from technology, but because technology, organization, training, regulation, and responsibility allocation are inseparable in this case.",
        core_question_zh="为什么 737 Max 不应被读成一个单纯的设计缺陷案例，而应被读成技术、人因、组织和伦理问题同时失配的系统案例？",
        core_question_en="Why should the 737 Max not be read as a mere design-defect case, but as a system case where technical, human-factors, organizational, and ethical failures are intertwined?",
        must_learn_points_zh=[
            "737 Max 案例同时包含技术设计、飞行员理解、培训假设、认证过程和组织责任问题。",
            "它说明 HFE 不能脱离治理和责任讨论。",
            "真正重要的不只是 MCAS 本身，而是系统状态可见性、告警、单点失效容忍和训练假设如何组合起来。",
            "伦理讨论只有回到具体工程决策才有意义。",
        ],
        must_learn_points_en=[
            "The 737 Max case combines technical design, pilot understanding, training assumptions, certification, and organizational responsibility.",
            "It shows that HFE cannot be separated from governance and responsibility.",
            "What matters is not only MCAS itself, but how state visibility, alerting, single-failure tolerance, and training assumptions combined.",
            "Ethics discussion becomes meaningful only when it returns to concrete engineering decisions.",
        ],
        memory_anchor_zh="先记住这个案例的一句话判断：737 Max 最大的问题，不是单一技术元件，而是多个系统假设同时把风险转嫁给了飞行员和运行系统。",
        memory_anchor_en="Keep this case judgment in mind: the deepest problem in the 737 Max was not one isolated technical component, but several interacting system assumptions that transferred risk to the flight crew and operating system.",
        sections=[
            section(
                "background",
                "## 背景与 stakes",
                "## Background and Stakes",
                body_zh="737 Max 材料里同时出现了事故背景、事故后技术评估、飞行员响应研究、认证反思和工程伦理。这说明课程不是把它当作单一技术事故，而是当作一个多层系统案例来读。",
                body_en="The 737 Max material combines accident background, post-accident technical assessment, studies of pilot response, certification reflection, and engineering ethics. That shows the course does not read it as a narrow technical accident, but as a multi-layer system case.",
            ),
            section(
                "chain",
                "## 事件链和失配链应该怎样读",
                "## How to Read the Event Chain and the Mismatch Chain",
                body_zh="读这页时，不能只看“技术出了什么故障”。还要继续看：系统状态有没有被充分揭示、单点信息有没有被赋予过高权重、飞行员是否拥有足够训练与认知空间来理解异常状态、组织和监管又如何放大或没能阻止这条链。",
                body_en="This page cannot stop at “what technical fault occurred.” It must continue into whether system state was sufficiently visible, whether a single information source carried too much weight, whether the crew had enough training and cognitive room to understand the abnormal state, and how organization and regulation amplified or failed to stop the chain.",
            ),
            section(
                "ethics",
                "## 这个案例里的伦理问题到底落在哪里",
                "## Where the Ethical Question Actually Lands",
                body_zh="这页的伦理讨论不是抽象地说“工程师应当负责”，而是回到具体决策：系统行为有没有被充分披露？培训假设是否贴近真实运行？是否把风险过度转交给一线飞行员？认证过程有没有识别并纠正这些偏差？",
                body_en="The ethics discussion here is not an abstract claim that “engineers should be responsible.” It returns to concrete decisions: was system behavior fully disclosed, did training assumptions match real operations, was too much risk transferred to frontline crews, and did certification adequately identify and correct those mismatches?",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="737 Max 这一页真正要你学会的，是如何把技术、人因和责任分配读成同一条系统失配链。",
                note_body_en="The deepest lesson of the 737 Max page is how to read technology, human factors, and responsibility allocation as one system mismatch chain.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "ethics",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="如果伦理讨论只停在价值判断，不回到具体设计和认证决策，它就会变成空话。这个案例要求伦理和工程细节一起被分析。",
                body_en="If ethics remains only at the level of value judgment and never returns to concrete design and certification decisions, it becomes empty rhetoric. This case demands that ethics and engineering detail be analyzed together.",
            )
        ],
        examples=[
            callout(
                "example",
                "chain",
                "案例锚点：为什么前一班次信息没有自动变成后一班次安全",
                "Case Anchor: Why Prior-Flight Information Did Not Automatically Become Later Safety",
                body_zh="材料里提到前一航班已经经历 stick shaker 和 trim 问题，但这些信息并没有稳定转化成后续机组的有效防线。这正好说明：系统里“信息曾经出现过”并不等于“风险已经被真正管理”。",
                body_en="The material notes that the previous flight had already experienced stick shaker and trim issues, yet that information did not reliably become a defense for the later crew. This illustrates a crucial lesson: information having appeared somewhere in the system does not mean the risk has actually been managed.",
            )
        ],
        inline_visuals=[
            visual(
                "background",
                "Boeing 737Max and Ethics 2-23-26.pdf",
                "这张预览图要看懂的是：这不是单纯技术页，而是从一开始就把事故、复盘和伦理并排摆在一起的系统案例。",
                "This preview should make clear that the page is not only a technical discussion; from the beginning it places accident context, review, and ethics side by side as one system case.",
                index=0,
            ),
            visual(
                "ethics",
                "Boeing 737Max and Ethics 2-23-26.pdf",
                "这张预览图要看懂的是：伦理讨论真正落脚点，是具体的失效分类、缓解措施和责任分配，而不是抽象口号。",
                "This preview should show that the real landing point of ethics discussion is concrete failure classification, mitigation, and responsibility allocation rather than abstract slogans.",
                index=1,
            ),
        ],
        summary_points_zh=[
            "737 Max 是技术、人因、组织和伦理交织的系统案例。",
            "关键不只在故障元件，也在状态可见性、训练假设和责任分配。",
            "伦理讨论必须回到具体工程决策。",
            "这页教你把系统失配链整体读出来。",
        ],
        summary_points_en=[
            "The 737 Max is a system case where technology, human factors, organization, and ethics intertwine.",
            "The key is not only the failed component, but also state visibility, training assumptions, and responsibility allocation.",
            "Ethics discussion must return to concrete engineering decisions.",
            "This page teaches how to read the whole system mismatch chain together.",
        ],
    ),
}

CASES_ETHICS_CONTENT["operational_risk"]["sections"].extend(
    [
        section(
            "drift",
            "## 为什么运行风险经常以“慢慢偏掉”的形式出现",
            "## Why Operational Risk Often Appears as Slow Drift Rather Than Sudden Collapse",
            body_zh="""
            operational risk 最值得注意的，不是灾难时刻本身，而是系统在灾难前已经偏了多久。很多风险不会突然生成，而是在日常运行中一点点被正常化：

            - workaround 变成默认做法
            - 时间压力逐渐吞掉缓冲
            - 资源紧张让团队接受更脆弱的运行方式
            - 原本只是例外的偏差开始被当成“正常现实”

            这种 drift 最危险的地方在于，它平时看起来还能工作，所以系统会越来越低估自己已经变脆了多少。
            """,
            body_en="""
            The most important feature of operational risk is not the disaster moment itself, but how long the system has already been drifting before the disaster. Many risks do not appear suddenly. They become normalized through daily operation:

            - workarounds become default practice
            - time pressure eats away the original buffer
            - resource strain makes the team accept more fragile operating modes
            - deviations that began as exceptions get reclassified as ordinary reality

            Drift is dangerous because the system still appears to function during the slide, and therefore underestimates how fragile it has already become.
            """,
        ),
        section(
            "management",
            "## 为什么 operational risk 最后会变成治理问题",
            "## Why Operational Risk Eventually Becomes a Governance Problem",
            body_zh="""
            运行风险不会只停留在一线层。只要资源配置、目标压力、排班、维护窗口和监督机制长期塑造了现场条件，那么 operational risk 本质上就已经进入治理层。

            这也是为什么这页在课程里位置很重要：它提醒你，很多一线失误如果反复出现，问题就不该再被看成 frontline discipline，而要被看成 management of operating conditions。
            """,
            body_en="""
            Operational risk does not remain only at the frontline. Once resource allocation, production pressure, scheduling, maintenance windows, and oversight mechanisms shape local conditions over time, the issue has already become a governance problem.

            That is why this page matters so much in the course. Repeated frontline failure should no longer be treated only as discipline failure. It should be treated as management of operating conditions.
            """,
        ),
    ]
)
CASES_ETHICS_CONTENT["operational_risk"]["examples"].append(
    callout(
        "example",
        "drift",
        "案例：为什么“大家都这么做”本身就可能是高风险信号",
        "Example: Why “Everyone Does It This Way” Can Itself Be a High-Risk Signal",
        body_zh="当一线人员普遍用某种 workaround 完成任务时，这并不自动说明他们不专业。更重要的解释可能是：正式流程已经长期不贴合 work as done，而系统正在依赖一套没有被正式承认的脆弱运行方式维持表面稳定。",
        body_en="When frontline staff widely rely on the same workaround, this does not automatically mean they are careless. A more important explanation may be that the formal process has long ceased to fit work as done and the system is relying on an unofficial but fragile operating mode to preserve apparent stability.",
    )
)
CASES_ETHICS_CONTENT["operational_risk"]["sections"].append(
    section(
        "signals",
        "## 运行风险真正该盯住哪些早期信号",
        "## Which Early Signals Actually Matter in Operational Risk",
        body_zh="""
        operational risk 很少没有前兆。真正难的是，这些前兆平时看起来往往像“小问题”：交接越来越赶、维护窗口越来越短、例外审批越来越频繁、现场越来越依赖个人经验而不是正式流程。

        这些信号单独看都不一定像事故种子，但只要它们长期一起出现，就说明系统正在失去缓冲。也因此，运行风险管理最有价值的部分往往不是事故后追责，而是事故前识别这些慢性变脆的信号。
        """,
        body_en="""
        Operational risk is rarely without warning. The difficulty is that the warnings often look small in everyday work: rushed handoffs, shrinking maintenance windows, more frequent exception handling, and growing dependence on personal experience instead of the formal process.

        Any one of those signals may not look like an accident seed by itself. But when they appear together over time, the system is losing buffer. That is why one of the most valuable parts of operational-risk management is not post-event blame, but pre-event recognition of these slow fragility signals.
        """,
    )
)
CASES_ETHICS_CONTENT["operational_risk"]["sections"].append(
    section(
        "variation",
        "## 为什么 operational risk 还要看“表面相似、实际不同”的运行环境",
        "## Why Operational Risk Also Has to Examine Operating Environments That Look Similar but Behave Differently",
        body_zh="""
        运行风险分析不能只看流程名字一样，就默认风险结构也一样。哪怕两个机场都有相似跑道编号、相近业务类型或相近任务名称，实际的空间布局、交通密度和周边约束仍可能完全不同。

        这也是 operational risk 的一个关键提醒：风险不是挂在流程标题上的，它挂在真实运行条件上。只要真实条件不同，work as done 和缓冲结构就会一起变化。
        """,
        body_en="""
        Operational-risk analysis cannot assume that similar procedure names imply similar risk structure. Even if two airports share a runway label, business type, or task name, the real spatial layout, traffic density, and surrounding constraints may differ substantially.

        This is one of the key reminders of operational risk: risk does not attach itself to the procedure title. It attaches to real operating conditions. Once those conditions differ, work as done and the available buffer change with them.
        """,
    )
)
CASES_ETHICS_CONTENT["operational_risk"]["inline_visuals"].extend(
    [
        visual(
            "application",
            "Operational Risk 2-18-2026.pdf",
            "这张图要看懂的是：运行风险 mitigation 不是只盯一线个体，它同时分布在个人、组织、系统设计和具体运行条件四层。",
            "This figure should show that operational-risk mitigation is not focused only on the frontline individual. It is distributed across individual, organization, system design, and operating-condition layers.",
            asset_name_contains="page-02",
        ),
        visual(
            "variation",
            "Operational Risk 2-18-2026.pdf",
            "这张图要看懂的是：即便表面标签相似，不同运行场景的空间布局和环境约束也会让风险结构明显不同。",
            "This figure should show that even when surface labels look similar, different operating layouts and environmental constraints can produce very different risk structures.",
            asset_name_contains="page-16",
        ),
    ]
)

CASES_ETHICS_CONTENT["cardosi_case"]["sections"].extend(
    [
        section(
            "reconstruct",
            "## 这类通信案例最重要的是把链条重新搭出来",
            "## The Key to This Type of Communication Case Is Reconstructing the Chain",
            body_zh="""
            Cardosi 案例如果只看最后结果，会很容易落成“有人没听清”。真正有价值的读法，是把 communication chain 一层层重新搭出来：

            - 信息最初是怎样表达的
            - 在通道里怎样被削弱、遮挡或踩断
            - 哪些成员因此拿到了不完整 picture
            - 后面的程序和显示有没有机会把它补回来

            一旦这样重建，案例就会从“单句 communication mistake”重新变回多层系统问题。
            """,
            body_en="""
            If the Cardosi case is read only through the final outcome, it quickly collapses into “someone did not hear clearly.” The stronger reading rebuilds the communication chain layer by layer:

            - how the information was originally expressed
            - how it was weakened, blocked, or stepped on in the channel
            - which actors therefore received only a partial picture
            - whether later procedure or displays had any chance to repair that picture

            Once rebuilt that way, the case stops being a single communication mistake and returns to a multi-layer system problem.
            """,
        ),
        section(
            "redundancy",
            "## 为什么关键通信必须有冗余表达和确认机制",
            "## Why Critical Communication Needs Redundancy and Confirmation",
            body_zh="""
            航空通信环境本来就容易受噪声、重叠发话和时间压力影响，所以如果关键内容只以一种脆弱表达形式出现，它就太容易在链条里丢失。Cardosi 材料的价值之一，就是提醒你把 communication 当成 barrier，而不是当成中性背景。

            只要通信承担 barrier 角色，它就应该有冗余、回读、确认和补救设计。
            """,
            body_en="""
            Aviation communication environments are already vulnerable to noise, overlapping speech, and time pressure. If critical content appears in only one fragile expression format, it becomes too easy for the message to vanish somewhere in the chain. One important lesson of the Cardosi material is that communication should be treated as a barrier, not as neutral background.

            Once communication is treated as a barrier, redundancy, read-back, confirmation, and recovery design become necessary.
            """,
        ),
    ]
)
CASES_ETHICS_CONTENT["cardosi_case"]["examples"].append(
    callout(
        "example",
        "redundancy",
        "案例：为什么一条信息“说过了”并不等于风险已经被管住",
        "Example: Why “It Was Said Once” Does Not Mean the Risk Was Controlled",
        body_zh="在高负荷通信环境里，一条关键消息即使已经被说出口，也可能因为通道遮挡、接收不完整或共享局面缺失而没有真正成为团队防线。Cardosi 案例的一个核心提醒就是：信息存在过，不等于信息真的被系统吸收了。",
        body_en="In a high-load communication environment, a critical message may be spoken and still fail to become a real team defense because the channel is blocked, reception is partial, or shared understanding never forms. One of the core lessons in the Cardosi case is that information having existed is not the same as information having been absorbed by the system.",
    )
)
CASES_ETHICS_CONTENT["cardosi_case"]["sections"].append(
    section(
        "flow",
        "## 为什么 Cardosi 材料先花时间讲 ATC 分工和流转",
        "## Why the Cardosi Material Spends Time on ATC Roles and Flow First",
        body_zh="""
        Cardosi 材料并不是一上来就讲事故，因为如果不先理解 terminal controller、en route controller 和 arrival / departure 的分工，后面的通信问题就会失去工作背景。

        这也说明案例分析的一个常见原则：在判断 communication failure 前，先看这条通信本来嵌在什么工作流里。只有先看清工作流，才知道一段话为什么会在那个位置变得关键。
        """,
        body_en="""
        The Cardosi material does not begin directly with the incident because the later communication problem loses context unless the reader first understands the roles of terminal controller, en route controller, and arrival / departure flow.

        That illustrates a common case-analysis principle: before judging a communication failure, first examine the workflow inside which the communication lives. Only then does it become clear why a given transmission becomes critical at that point in the chain.
        """,
    )
)
CASES_ETHICS_CONTENT["cardosi_case"]["inline_visuals"].append(
    visual(
        "flow",
        "Cardosi 2-2-2026.pdf",
        "这张图要看懂的是：ATC 沟通不是孤立对话，而是嵌在不同控制角色和流转节点之间的连续工作链上。",
        "This figure should show that ATC communication is not an isolated conversation. It sits inside a continuous workflow spanning different controller roles and transfer points.",
        asset_name_contains="page-03",
    )
)

CASES_ETHICS_CONTENT["f16_analysis_prompts"]["sections"].extend(
    [
        section(
            "order",
            "## prompts 真正提供的是分析顺序，而不只是问题清单",
            "## Prompts Provide an Order of Analysis, Not Just a List of Questions",
            body_zh="""
            这页最容易被低估的地方，是 prompts 看起来像很多问题，但其实它们更像一条顺序。先看事件和任务，再看信息和界面，再看团队与组织，最后才回到改进建议。这个顺序能防止讨论一开始就跳去结论或责任归因。

            所以 prompt 的价值不在数量，而在它能不能稳住案例分析的展开节奏。
            """,
            body_en="""
            The most underestimated part of the prompts is that they look like many separate questions, but they really provide an order. Start with the event and task, then move to information and interface, then to team and organization, and only afterward to recommendations. That order prevents the discussion from jumping too early to conclusion or blame.

            The value of prompts therefore is not their count, but whether they stabilize the rhythm of case analysis.
            """,
        ),
        section(
            "output",
            "## 用 prompts 做完分析后，应该产出什么",
            "## What a Prompted Analysis Should Produce",
            body_zh="""
            一套 prompts 用得好，最后不应只留下“讨论过很多问题”，而应留下一个更清楚的输出：

            - 哪些证据支持哪条因果链
            - 哪些层级的问题最值得优先改
            - 哪些结论还只是推测，需要继续补证据

            这也是为什么 prompts 适合课堂讨论和案例复盘，它能把发散观察压回结构化输出。
            """,
            body_en="""
            When prompts are used well, the result should not be merely “we discussed many questions.” The analysis should produce something clearer:

            - which evidence supports which causal chain
            - which layers are the highest-priority targets for change
            - which conclusions remain tentative and still need more evidence

            That is why prompts fit both classroom discussion and case review. They compress scattered observation back into structured output.
            """,
        ),
    ]
)
CASES_ETHICS_CONTENT["f16_analysis_prompts"]["examples"].append(
    callout(
        "example",
        "output",
        "案例：为什么 prompts 能把“各说各话”压回同一张分析图上",
        "Example: Why Prompts Pull a Discussion Back from Fragmentation",
        body_zh="没有 prompts 时，团队可能一会儿讲界面、一会儿讲程序、一会儿讲培训，最后谁也不知道这些观察之间是什么关系。用了 prompts 之后，大家会被迫把每条观察放回同一分析顺序里，这样案例才会从散点意见变成可执行复盘。",
        body_en="Without prompts, a team may jump from interface to procedure to training and end with no clear relationship among those observations. With prompts, each observation is forced back into one analysis order, and the case becomes an actionable review instead of a cloud of disconnected opinions.",
    )
)
CASES_ETHICS_CONTENT["f16_analysis_prompts"]["sections"].append(
    section(
        "evidence_limits",
        "## 为什么 prompts 还在提醒你区分“看见了什么”和“推断了什么”",
        "## Why the Prompts Keep Reminding You to Separate Observation from Inference",
        body_zh="""
        prompts 的一个隐藏作用，是防止案例讨论在中途悄悄把推断当成事实。因为只要团队已经有了强烈直觉，后面的所有问题都可能被用来支持这个直觉，而不是检验它。

        所以 prompts 真正成熟的用法，不是快速把答案说出来，而是逼自己反复区分：哪些是明确证据，哪些只是当前最合理的解释。这个区分一旦守住，后面的责任判断和改进建议才更稳。
        """,
        body_en="""
        One hidden function of the prompts is preventing the discussion from quietly treating inference as fact. Once a team forms a strong intuition early, later questions can be used to support that intuition rather than test it.

        The more mature use of prompts therefore is not producing a fast answer, but repeatedly separating what is directly evidenced from what is only the best current interpretation. Once that line is protected, later responsibility judgments and recommendations become much more stable.
        """,
    )
)
CASES_ETHICS_CONTENT["f16_analysis_prompts"]["sections"].append(
    section(
        "task_demands",
        "## 为什么这个案例必须把任务需求写清楚，不能只写“飞行员失误”",
        "## Why This Case Has to State the Task Demands Explicitly Instead of Stopping at “Pilot Error”",
        body_zh="""
        F16 材料一开始就把夜间训练、空中加油、返航和两次着陆尝试摆出来，目的就是提醒你：这是一个任务负荷不断叠加的案例，不是单次离散动作。

        如果不先把这些任务需求写清楚，后面的判断就很容易被压缩成“某个操作者做错了”。但一旦任务链条被摊开，你就会看到 workload、时间压力、程序和显示支持其实都在影响最后结果。
        """,
        body_en="""
        The F16 material begins by laying out the night training mission, air-to-air refueling, return flight, and two landing attempts to emphasize that this is a case of accumulating task demand rather than one isolated maneuver.

        Without stating those task demands first, the analysis collapses too easily into “an operator made a mistake.” Once the task chain is laid out, it becomes clear that workload, time pressure, procedure, and display support all shape the eventual outcome.
        """,
    )
)
CASES_ETHICS_CONTENT["f16_analysis_prompts"]["inline_visuals"] = [
    visual(
        "task_demands",
        "Sp26_F16-AnalysisPrompts_20260219.pdf",
        "这张图要看懂的是：空中加油不是背景细节，而是这个案例里显著提高任务负荷和精细操纵要求的关键节点。",
        "This figure should show that air-to-air refueling is not background detail. It is a key task node that sharply increases workload and precision-control demand in the case.",
        asset_name_contains="page-03",
    ),
    visual(
        "background",
        "Sp26_F16-AnalysisPrompts_20260219.pdf",
        "这张图要看懂的是：第一次落地尝试本身就包含复杂的视觉和几何判断，所以后续分析必须把任务环境和操作条件一起纳入。",
        "This figure should show that the first landing attempt already contained demanding visual and geometric judgment, so later analysis has to include task environment and operating conditions together.",
        asset_name_contains="page-04",
    ),
]

CASES_ETHICS_CONTENT["boeing_737max_and_ethics"]["sections"].extend(
    [
        section(
            "mismatch",
            "## 这页真正要你看到的是“假设失配”",
            "## What This Page Really Wants You to See Is Assumption Mismatch",
            body_zh="""
            737 Max 之所以是系统案例，是因为多个层级都在同时依赖一些彼此并不稳的假设：

            - 设计假设飞行员会怎样理解系统状态
            - 培训假设飞行员已经具备哪些知识与反应路径
            - 运行假设异常会以怎样的速度出现
            - 认证假设这些条件已经被充分验证

            一旦这些假设互相错位，问题就不再只是单个元件，而是整套系统在把风险往下游转移。
            """,
            body_en="""
            The 737 Max becomes a system case because several layers depend simultaneously on assumptions that do not hold together securely:

            - design assumptions about how the crew will understand system state
            - training assumptions about what knowledge and response paths the crew already possesses
            - operational assumptions about how quickly the anomaly will emerge
            - certification assumptions that these conditions have been adequately demonstrated

            Once those assumptions become misaligned, the issue is no longer only one component. The entire system begins transferring risk downstream.
            """,
        ),
        section(
            "governance",
            "## 为什么这页最后一定会落到治理和责任分配",
            "## Why This Page Ultimately Has to Land on Governance and Responsibility Allocation",
            body_zh="""
            737 Max 的伦理讨论之所以不能和工程分开，是因为这里的很多风险并不是自然发生，而是被某些决策允许、放大或未被及时纠正。换句话说，风险链里不仅有 technical failure，也有 decision failure。

            这就是为什么课程把 regulator、manufacturer、operator 和 training assumptions 都拉进来讨论。责任不是抽象标签，而是系统里谁有能力改变条件、谁却没有及时改变。
            """,
            body_en="""
            The ethics discussion in the 737 Max case cannot be separated from engineering because many of the risks did not emerge spontaneously. They were permitted, amplified, or left uncorrected by decisions. In other words, the chain contains not only technical failure, but decision failure.

            That is why the course brings regulator, manufacturer, operator, and training assumptions into the same discussion. Responsibility is not an abstract label; it is about who had the power to change the conditions and failed to do so in time.
            """,
        ),
    ]
)
CASES_ETHICS_CONTENT["boeing_737max_and_ethics"]["examples"].append(
    callout(
        "example",
        "governance",
        "案例：为什么“前一航班已经出过问题”仍然没能变成可靠防线",
        "Example: Why “The Previous Flight Already Had Trouble” Still Failed to Become a Reliable Defense",
        body_zh="前一班次信息存在过，却没有稳定变成后一班次的保护，这件事本身就是系统失配证据。它说明系统里“信息出现”“信息被理解”“信息被转化成行动防线”这三步并没有真正接上。也正因为如此，这页才不能只讲硬件故障，而必须讲治理和传递机制。",
        body_en="The fact that prior-flight information existed but did not reliably become a defense for the later crew is itself evidence of system mismatch. It shows that the steps from “information appeared” to “information was understood” to “information became an operational defense” were never fully connected. That is why this page cannot stop at hardware failure alone and must also discuss governance and transmission mechanisms.",
    )
)
CASES_ETHICS_CONTENT["boeing_737max_and_ethics"]["sections"].append(
    section(
        "response_data",
        "## 为什么 737 Max 这页还要补进 pilot response 数据",
        "## Why the 737 Max Page Also Needs Pilot-Response Evidence",
        body_zh="""
        737 Max 讨论如果只停在设计缺陷，很容易忽视一个关键点：真正进入运行系统后，飞行员到底怎样理解并处理这些异常状态。也正因为如此，课程才会补进 Volpe 报告这类材料，把案例从“设计评议”继续推进到“真实运行响应”。

        这一步很重要，因为很多风险并不是在系统设计图纸上完全显现，而是在 crew response、checklist 使用和异常诊断里真正暴露出来。
        """,
        body_en="""
        If the 737 Max discussion stops only at design defect, it misses a critical point: once the issue enters the operating system, how do flight crews actually interpret and manage the abnormal state. That is why the course adds sources such as the Volpe report, pushing the case from design critique into real operational response.

        This step matters because many risks are not fully visible on the design diagram itself. They become exposed in crew response, checklist use, and abnormal-state diagnosis.
        """,
    )
)
CASES_ETHICS_CONTENT["boeing_737max_and_ethics"]["inline_visuals"].append(
    visual(
        "response_data",
        "Boeing 737Max and Ethics 2-23-26.pdf",
        "这张图要看懂的是：737 Max 的问题不能只停在硬件层，课程还要求你去看飞行员在真实系统失效场景中的响应模式与限制。",
        "This figure should show that the 737 Max case cannot stop at hardware. The course also asks you to examine how flight crews respond under real aircraft-system failures and limitations.",
        asset_name_contains="page-06",
    )
)

CASES_ETHICS_CONTENT["boeing_737max_and_ethics"]["sections"].extend(
    [
        section(
            "chain_detail",
            "## 把 737 Max 写成一条完整失配链，至少要过哪几步",
            "## If You Write 737 Max as One Complete Mismatch Chain, Which Steps Must Be Included",
            body_zh="""
            这页真正成熟的读法，不是只停在 “MCAS 出了问题”，而是至少要把下面几步接起来：

            1. 前一航班和其他运行信息已经暴露出异常线索，但没有稳定变成后续防线。
            2. 系统状态可见性和告警解释空间不足，机组很难迅速形成完整局面理解。
            3. 异常发生时，飞行员要在高时间压力下同时做诊断、控制和程序调用。
            4. 设计与培训假设把过多恢复责任放到了机组即时反应上。
            5. 认证与治理层没有足够早地把这些相互依赖的假设识别成系统性脆弱点。

            只有把这几步接起来，你看到的才不是一个“坏元件故事”，而是一条真正的系统失配链。
            """,
            body_en="""
            The mature reading of this page cannot stop at “MCAS malfunctioned.” At minimum it has to connect the following steps:

            1. prior-flight and other operational information had already exposed anomaly signals, but those signals did not become reliable later defenses
            2. system-state visibility and alert interpretation space were limited, making it hard for the crew to form a complete picture quickly
            3. when the anomaly emerged, the crew had to diagnose, control, and invoke procedures under intense time pressure
            4. design and training assumptions transferred too much recovery responsibility onto immediate crew response
            5. certification and governance did not identify those interacting assumptions early enough as a systemic fragility

            Only when those steps are connected do you stop seeing a “bad component story” and begin to see a genuine system mismatch chain.
            """,
        ),
        section(
            "mitigation_layers",
            "## 为什么缓解不能只落在一个层级",
            "## Why Mitigation Cannot Be Concentrated at Only One Layer",
            body_zh="""
            课件里那张 mitigation 图很重要，因为它把个人、组织、系统设计和 operational risk 放在同一页上。这个排列本身就在表达一个判断：像 737 Max 这样的案例，不可能靠单一层改动真正补上。

            如果只补培训，而系统状态仍然难以理解，风险会留下来；如果只改界面，却不处理 operator、manufacturer 和 regulator 之间的信息与责任链，风险也会换一种方式回来。真正稳的改法，是让 training、checklists、alerts、system design、operator practice 和 governance 一起构成多层缓解。
            """,
            body_en="""
            The mitigation slide matters because it places individual, organization, system design, and operational risk on the same page. That layout itself expresses a judgment: a case like 737 Max cannot be repaired by changing only one layer.

            If training alone is improved while system state remains difficult to understand, the risk stays alive. If interface changes are made but the information and responsibility chain across operator, manufacturer, and regulator remains weak, the risk returns in another form. The stronger strategy is multi-layer mitigation across training, checklists, alerts, system design, operator practice, and governance.
            """,
        ),
    ]
)
CASES_ETHICS_CONTENT["boeing_737max_and_ethics"]["examples"].append(
    callout(
        "example",
        "mitigation_layers",
        "案例：为什么“多给飞行员一点培训”不能算完整答案",
        "Example: Why “Give Pilots More Training” Is Not a Complete Answer",
        body_zh="培训当然重要，但如果系统状态仍然不够可见、单点信息权重仍然过高、异常时的 checklist 与警示逻辑仍然不足，那么培训只是把更多恢复负担继续压给机组。737 Max 这页真正要强调的是：当风险本来就是多层生成的，缓解也必须是多层的。",
        body_en="Training obviously matters, but if system state still lacks visibility, if too much weight still rests on single-point information, and if checklist and alert logic remain weak under abnormal conditions, then training merely transfers more recovery burden onto the crew. The deeper lesson of the 737 Max page is that when risk is generated across layers, mitigation also has to operate across layers.",
    )
)
