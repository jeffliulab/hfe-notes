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

