from __future__ import annotations

from note_blueprints import callout, page_blueprint, section, visual


AVIATION_AUTOMATION_CONTENT: dict[str, dict] = {
    "aviation_automation_intro": page_blueprint(
        template_type="concept",
        page_intro_zh="航空与自动化导论这页要先纠正一个直觉：自动化不是把人拿掉，而是把人的工作改成了更偏监控、模式理解、接管和异常管理的任务。",
        page_intro_en="The introduction to aviation and automation starts by correcting a common intuition: automation does not remove the human; it changes the human role toward monitoring, mode understanding, takeover, and exception management.",
        core_question_zh="当自动化承担更多功能后，人到底还剩下什么工作，而这些剩余工作是不是反而更难？",
        core_question_en="When automation takes over more functions, what work remains for the human, and do those residual tasks become harder rather than easier?",
        must_learn_points_zh=[
            "自动化既能减轻重复负担，也会制造监控、模式理解和接管风险。",
            "最关键的问题不是“系统做了多少”，而是“人剩下的工作是否仍然现实可做”。",
            "航空是自动化 HFE 的经典实验场，因为角色重分配、时间压力和高后果在这里都非常明显。",
            "自动化风险常常不是直接操作错误，而是 automation surprise、mode confusion 和 handoff failure。",
        ],
        must_learn_points_en=[
            "Automation can reduce repetitive burden while introducing monitoring, mode-understanding, and takeover risk.",
            "The key question is not how much the system does, but whether the human’s remaining work is still realistically doable.",
            "Aviation is a classic HFE laboratory for automation because role redistribution, time pressure, and consequence are all vivid here.",
            "Automation risk often appears not as direct manual error, but as automation surprise, mode confusion, and handoff failure.",
        ],
        memory_anchor_zh="先记住一句话：自动化不是把人从系统里删掉，而是把人的错误类型换了一种更隐蔽、也更难救回的形式。",
        memory_anchor_en="Keep one sentence in mind: automation does not delete the human from the system; it changes human failure modes into forms that are often less visible and harder to recover from.",
        sections=[
            section(
                "logic",
                "## 自动化为什么会同时增效也增险",
                "## Why Automation Can Improve and Increase Risk at the Same Time",
                body_zh="自动化的收益通常很直观：更稳定、更快、更少重复负担。但它的代价往往滞后出现，因为它会把人的工作改写成平时低参与、关键时刻高要求的任务。",
                body_en="The benefits of automation are usually obvious: more consistency, speed, and relief from repetitive load. The cost emerges later, because it rewrites the human role into low-engagement work that suddenly becomes high-demand when intervention is needed.",
            ),
            section(
                "questions",
                "## 读这页时要固定问哪三个问题",
                "## Which Three Questions Should Guide the Reading",
                body_zh="""
看到一个自动化系统时，先固定问三件事：

1. 自动化接管了什么？
2. 人保留了什么？
3. 剩下的人类任务是否在真实条件下仍然做得到？
""",
                body_en="""
When looking at an automated system, ask three fixed questions:

1. what has automation taken over?
2. what has the human retained?
3. are the remaining human tasks still doable under real conditions?
""",
            ),
            section(
                "implications",
                "## 为什么航空是这个问题的经典场景",
                "## Why Aviation Is the Classic Setting for This Problem",
                body_zh="在航空里，自动化状态多、模式切换快、信息量大、接管窗口短，所以“人保留的最后那点工作”往往最难。课程后面的 CRM、display、situation awareness 和 automated vehicles 页面，其实都在从不同角度继续追这一条线。",
                body_en="In aviation, there are many automation states, fast mode transitions, large information loads, and short takeover windows. That makes the “last remaining human role” especially difficult. Later pages on CRM, displays, situation awareness, and automated vehicles all continue this same line from different angles.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="自动化的真正难点，不在于系统会不会做事，而在于人会不会在关键时刻重新接得上这套系统。",
                note_body_en="The real difficulty in automation is not whether the system can perform, but whether the human can reconnect with it effectively at the critical moment.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "questions",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="“自动化越多越安全”并不是可靠判断。真正要看的是剩余人工任务有没有被设计得可见、可理解、可接管。",
                body_en="“More automation means more safety” is not a reliable conclusion. What matters is whether the remaining human tasks are visible, understandable, and take-overable.",
            )
        ],
        examples=[
            callout(
                "example",
                "implications",
                "案例：为什么自动化最危险的时刻往往不是正常巡航，而是突然接管",
                "Example: Why the Most Dangerous Automation Moment Is Often Takeover, Not Cruise",
                body_zh="在自动化系统长时间稳定运行时，人容易退成被动监控者；一旦系统要求立即接管，操作者却可能既缺少最新情境意识，也不确定当前模式和系统意图，这正是很多自动化事故的高风险窗口。",
                body_en="When an automated system runs stably for a long time, the human drifts toward passive monitoring. If the system then demands immediate takeover, the operator may lack current situation awareness and may not fully understand the active mode or system intent. That window is where many automation accidents become possible.",
            )
        ],
        summary_points_zh=[
            "自动化会重写人的任务，而不是消灭人的任务。",
            "关键问题是剩余人类任务是否现实可做。",
            "航空自动化问题会延伸到 CRM、display、SA 和 AV 页面。",
            "最危险的往往是监控和接管，而不是正常巡航。",
        ],
        summary_points_en=[
            "Automation rewrites the human role rather than eliminating it.",
            "The critical question is whether the remaining human tasks are realistically doable.",
            "Aviation-automation problems continue into CRM, displays, SA, and automated-vehicle pages.",
            "Monitoring and takeover are often more dangerous than normal cruise.",
        ],
    ),
    "crew_resource_management": page_blueprint(
        template_type="concept",
        page_intro_zh="CRM 这一页不是“团队关系更和谐”这么简单，而是研究团队怎样把沟通、授权、监控和交叉检查真正变成安全防线。",
        page_intro_en="This CRM page is not simply about better interpersonal harmony. It is about how teams turn communication, authority, monitoring, and cross-checking into real safety barriers.",
        core_question_zh="为什么技术上很强的机组或团队，仍然会因为沟通、授权结构和共享情境意识不足而失败？",
        core_question_en="Why can technically competent crews still fail because communication, authority structure, and shared situation awareness break down?",
        must_learn_points_zh=[
            "CRM 把安全从个人技术扩展到团队协作能力。",
            "authority gradient、assertiveness、briefing、debriefing、workload sharing 和 mutual monitoring 是同一套系统。",
            "很多重大事故不是没人看见问题，而是有人看见了却没能让团队吸收这个信号。",
            "CRM 不是应急时才出现，它在任务开始前的 brief 和任务后的 debrief 就已经开始了。",
        ],
        must_learn_points_en=[
            "CRM extends safety from individual skill to collective team performance.",
            "Authority gradient, assertiveness, briefing, debriefing, workload sharing, and mutual monitoring form one system.",
            "Many major accidents do not happen because nobody saw the problem, but because someone saw it and the team failed to absorb the signal.",
            "CRM does not begin only in the emergency; it begins in the brief and continues into the debrief.",
        ],
        memory_anchor_zh="先记住一句话：CRM 的作用，是把“团队里有人看见问题”变成“团队真的因此改变行动”。",
        memory_anchor_en="Keep one sentence in mind: CRM exists to convert “someone in the team noticed the problem” into “the team actually changed action because of that signal.”",
        sections=[
            section(
                "logic",
                "## CRM 真正解决的是什么问题",
                "## What CRM Actually Solves",
                body_zh="如果安全只靠最强的那个人，团队就很脆弱。CRM 的价值在于让沟通、挑战、确认和补位变成一套稳定做法，让多人系统能够抵消单个人的注意和判断局限。",
                body_en="If safety depends only on the strongest individual, the team is fragile. CRM matters because it turns communication, challenge, confirmation, and backup into a stable practice that lets a multi-person system compensate for individual limits.",
            ),
            section(
                "elements",
                "## 这页真正想让你抓住的几个元素",
                "## The Elements This Page Wants You to Hold Onto",
                body_zh="""
课程反复强调的元素包括：

- communication
- leadership 与 followership
- assertiveness
- briefing / debriefing
- workload management
- mutual monitoring
- shared mental model
""",
                body_en="""
The course keeps returning to a small set of elements:

- communication
- leadership and followership
- assertiveness
- briefing / debriefing
- workload management
- mutual monitoring
- shared mental model
""",
            ),
            section(
                "application",
                "## 为什么 authority gradient 会变成安全问题",
                "## Why Authority Gradient Becomes a Safety Problem",
                body_zh="如果权威差距太陡，下级成员即使看见问题也可能不敢有效挑战；如果权威差距太平，关键时刻又可能没人真正承担领导。CRM 要做的不是把权威抹掉，而是让团队在保持角色分工的同时，仍然能让风险信息向上流动。",
                body_en="If the authority gradient is too steep, junior members may fail to challenge even when they see the problem. If it is too flat, critical moments may lack real leadership. CRM is not about erasing authority; it is about preserving role structure while still letting risk information move upward effectively.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="好的 CRM，不是“大家都说很多话”，而是关键风险信息能在正确时间被正确的人听见并采纳。",
                note_body_en="Strong CRM is not “everyone talks more.” It is that the right risk information reaches the right person at the right time and is actually used.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "application",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把 CRM 当成“软技能附加项”。在高负荷团队系统里，它本身就是核心安全机制之一。",
                body_en="Do not treat CRM as a soft-skills add-on. In high-load team systems, it is itself one of the central safety mechanisms.",
            )
        ],
        examples=[
            callout(
                "example",
                "application",
                "案例：为什么 Tenerife 常被当作 CRM 的经典教材",
                "Example: Why Tenerife Is a Classic CRM Teaching Case",
                body_zh="Tenerife 一再被拿来讲 CRM，不是因为技术细节不重要，而是因为它清楚展示了 authority gradient、沟通 ambiguity 和共享情境意识失败怎样一起推高风险。",
                body_en="Tenerife remains a CRM teaching case not because the technical details are unimportant, but because it vividly shows how authority gradient, ambiguous communication, and failed shared situation awareness can combine into catastrophic risk.",
            )
        ],
        summary_points_zh=[
            "CRM 把安全从个人表现扩展到团队表现。",
            "它的关键是让风险信号能被团队吸收并转化成行动。",
            "authority gradient 是团队安全的结构变量。",
            "CRM 从 brief 开始，不是只在紧急时出现。",
        ],
        summary_points_en=[
            "CRM extends safety from individual performance to team performance.",
            "Its key function is turning risk signals into coordinated team action.",
            "Authority gradient is a structural team-safety variable.",
            "CRM starts in the brief, not only in the emergency.",
        ],
    ),
    "displays_and_alerts": page_blueprint(
        template_type="concept",
        page_intro_zh="显示与告警这一页讲的核心矛盾是：你必须让关键信息足够显眼，但又不能把操作者淹没在噪声里。",
        page_intro_en="The central tension in displays and alerts is that critical information must be salient without drowning the operator in noise.",
        core_question_zh="怎样让操作者在关键时刻既能注意到重要信号，又能立刻理解系统状态和下一步动作？",
        core_question_en="How do we make sure that, at the critical moment, the operator notices the important signal, understands system state, and knows the next action?",
        must_learn_points_zh=[
            "display 负责让系统状态可见，alert 负责在关键时刻重新分配注意力。",
            "好的告警不是“更响更亮”，而是“更可信、更可判断、更能引导动作”。",
            "false alarm 会侵蚀信任，最后导致真正重要的告警也被忽略。",
            "显示层级和告警设计，本质上都在做注意资源管理。",
        ],
        must_learn_points_en=[
            "Displays make system state visible, and alerts reallocate attention at critical moments.",
            "A good alert is not simply louder or brighter; it is more trustworthy, interpretable, and action-guiding.",
            "False alarms erode trust until even important alerts get ignored.",
            "Display hierarchy and alert design are both forms of attention-resource management.",
        ],
        memory_anchor_zh="先记住一句话：告警设计的目标不是制造刺激，而是让人及时把注意力转到真正需要看的地方，并且知道接下来该做什么。",
        memory_anchor_en="Keep one sentence in mind: the goal of alert design is not to create stimulation, but to move attention toward the right place at the right time while supporting the next action.",
        sections=[
            section(
                "logic",
                "## 显示和告警分别承担什么角色",
                "## What Displays and Alerts Each Need to Do",
                body_zh="display 的任务是让状态可见、可比较、可推断；alert 的任务是把注意力在关键时刻拉过去。如果两者脱节，就会出现“看见了但看不懂”或“听见了但不知道怎么做”的问题。",
                body_en="The job of a display is to make state visible, comparable, and inferable. The job of an alert is to pull attention at the critical moment. If the two are disconnected, the operator may notice the signal without understanding it or hear it without knowing what to do next.",
            ),
            section(
                "questions",
                "## 读这页时要固定问哪三个问题",
                "## Which Three Questions Should Guide the Reading",
                body_zh="""
看到一个告警系统时，先固定问：

1. 这个告警真的代表高优先级风险吗？
2. 告警出现时，操作者能快速看懂系统处于什么状态吗？
3. 告警之后，下一步动作清楚吗？
""",
                body_en="""
When reading an alert system, ask:

1. does this alert truly indicate a high-priority risk?
2. once it appears, can the operator quickly understand system state?
3. is the next action clear?
""",
            ),
            section(
                "fatigue",
                "## 为什么 false alarm 最后会变成信任问题",
                "## Why False Alarms Become a Trust Problem",
                body_zh="如果系统经常发出低价值告警，操作者就会学会延迟响应、选择性忽略，甚至对告警系统整体失去信任。这样一来，真正关键的告警也会被拖慢处理。",
                body_en="If the system produces frequent low-value alerts, operators learn to delay response, ignore selectively, or distrust the alerting system altogether. Once that happens, truly critical alerts are also handled more slowly.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="显示与告警设计的本质，不是“做得更热闹”，而是让注意力、理解和行动重新对齐。",
                note_body_en="The essence of display and alert design is not making the system more dramatic, but realigning attention, understanding, and action.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "fatigue",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="“更多告警更安全”通常是错的。低价值告警过多时，系统是在消耗注意力，而不是保护注意力。",
                body_en="“More alerts mean more safety” is usually false. Once low-value alerts become excessive, the system is consuming attention rather than protecting it.",
            )
        ],
        examples=[
            callout(
                "example",
                "fatigue",
                "案例：为什么 alarm fatigue 最后会拖慢真正关键的反应",
                "Example: Why Alarm Fatigue Slows Response to the Truly Critical Signal",
                body_zh="如果病房监护系统不断发出噪声很大的低优先级告警，护理人员会逐渐降低对告警的整体响应敏感度。等到真正危及生命的信号出现时，系统早已失去“被立即认真对待”的资格。",
                body_en="If a ward monitoring system constantly emits loud low-priority alerts, staff gradually lower their overall responsiveness to the alerting channel. By the time a life-critical signal appears, the system has already lost the privilege of immediate serious attention.",
            )
        ],
        summary_points_zh=[
            "display 让状态可见，alert 让注意力转向关键处。",
            "好的告警必须同时支持理解和行动。",
            "false alarm 会侵蚀长期信任。",
            "这页本质上在讲注意资源管理。",
        ],
        summary_points_en=[
            "Displays make state visible; alerts redirect attention to critical conditions.",
            "A good alert supports both understanding and action.",
            "False alarms erode long-term trust.",
            "At its core, this page is about managing limited attentional resources.",
        ],
    ),
    "checklists_and_procedures": page_blueprint(
        template_type="method",
        page_intro_zh="检查单与程序这一页讨论的，不是把人变成机械执行者，而是怎样把容易忘、容易跳、容易乱序的动作外化成可靠的协作结构。",
        page_intro_en="This page is not about turning people into mechanical followers. It is about externalizing vulnerable steps so they become reliable shared structures for work and coordination.",
        core_question_zh="检查单和程序怎样减少记忆负担、支持团队协同，同时又不和真实工作流脱节？",
        core_question_en="How do checklists and procedures reduce memory burden and support teamwork without drifting away from real work?",
        must_learn_points_zh=[
            "checklist 是认知支架，不只是备忘录。",
            "procedure 是组织对“正常工作该怎样完成”的稳定承诺。",
            "程序化的价值在于标准化、可核对和可共享，而不是僵硬。",
            "如果程序脱离 work as done，一线人员会开始绕开它。",
        ],
        must_learn_points_en=[
            "A checklist is a cognitive scaffold, not just a reminder.",
            "A procedure is an organizational commitment about how normal work should be performed.",
            "The value of proceduralization is standardization, checkability, and shared coordination rather than rigidity.",
            "If procedure drifts away from work as done, frontline operators begin routing around it.",
        ],
        memory_anchor_zh="先记住这个方法的定位：好的 checklist 不是替你思考，而是替你把最脆弱、最容易漏掉的部分稳住。",
        memory_anchor_en="Remember the role of the method this way: a good checklist does not think for you; it stabilizes the most fragile and omission-prone parts of the work.",
        sections=[
            section(
                "problem",
                "## 这个方法解决什么问题",
                "## What Problem This Method Solves",
                body_zh="当任务复杂、多人协作、时序关键、记忆负担重时，只靠个人稳定发挥往往不够。checklist 和 procedure 的作用，就是把这些脆弱点外化成可见、可读、可确认、可共享的结构。",
                body_en="When tasks are complex, collaborative, sequentially sensitive, and memory-intensive, individual consistency is not enough. Checklists and procedures externalize those fragile points into visible, readable, confirmable, and shareable structures.",
            ),
            section(
                "design",
                "## 好的程序设计具体在做什么",
                "## What Good Procedure Design Actually Does",
                body_zh="""
好的 checklist / procedure 会：

- 把关键步骤放在最可执行的顺序上
- 让确认点能被读出和回应
- 把异常情况的升级路径写清楚
- 让团队成员知道自己在何时该说、该听、该核对
""",
                body_en="""
Good checklist and procedure design:

- puts critical steps in the most usable order
- makes checkpoints readable and answerable
- defines escalation paths for abnormal situations
- clarifies when each team member should speak, listen, and cross-check
""",
            ),
            section(
                "fit",
                "## 为什么它不能脱离真实工作",
                "## Why It Cannot Drift Away from Real Work",
                body_zh="如果 procedure 只反映 work as imagined，而不反映 work as done，那么一线人员迟早会觉得它太慢、太僵、太不贴近任务节奏，最后开始绕开它。那时程序还在，但防线功能已经衰减。",
                body_en="If a procedure reflects only work as imagined rather than work as done, frontline staff will eventually experience it as too slow, too rigid, or too detached from task rhythm and begin routing around it. At that point the procedure still exists, but its barrier function has weakened.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="程序化真正的难点，不在于“有没有 checklist”，而在于 checklist 是否真的支持现实任务。",
                note_body_en="The real challenge of proceduralization is not whether a checklist exists, but whether it genuinely supports the real task.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "fit",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="程序化不等于越死板越好。过度僵化的程序，常常会把真实工作推向绕行和临时补丁。",
                body_en="Proceduralization does not mean the more rigid the better. Overly rigid procedures often push real work toward workaround behavior and temporary patching.",
            )
        ],
        examples=[
            callout(
                "example",
                "design",
                "worked example：为什么一张 checklist 能减轻认知负担",
                "Worked Example: Why a Checklist Can Reduce Cognitive Burden",
                body_zh="在起飞、给药或设备切换这类高时序任务里，团队不需要把每一步都死记在脑中。好的 checklist 让关键步骤外显化，让成员把有限注意力留给监控异常和交叉检查。",
                body_en="In high-sequence tasks such as takeoff, medication administration, or equipment switching, the team does not need to retain every step purely in memory. A good checklist externalizes the critical steps so limited attention can stay available for anomaly monitoring and cross-checking.",
            )
        ],
        summary_points_zh=[
            "checklist 是认知支架，procedure 是组织承诺。",
            "它们的价值在于标准化、可核对和协同支持。",
            "好程序必须匹配真实工作，而不只是理想流程。",
            "程序存在不等于防线仍有效。",
        ],
        summary_points_en=[
            "A checklist is a cognitive scaffold and a procedure is an organizational commitment.",
            "Their value lies in standardization, checkability, and coordination support.",
            "Strong procedures must fit real work rather than only ideal work.",
            "The existence of a procedure does not guarantee that the barrier is still effective.",
        ],
    ),
    "automated_vehicles": page_blueprint(
        template_type="case",
        page_intro_zh="自动化车辆这一页不是在重复航空自动化，而是在看一个迁移问题：当接管、信任校准和责任分配进入驾驶场景后，风险会怎样重组。",
        page_intro_en="The automated-vehicles page does not merely repeat aviation automation. It examines how risk is reorganized when takeover, trust calibration, and responsibility allocation enter the driving context.",
        core_question_zh="自动化车辆最危险的地方，为什么往往不是系统在正常巡航时做得好不好，而是人和系统在接管边界上怎样交接责任？",
        core_question_en="Why is the most dangerous point in automated vehicles often not normal automated performance, but the handoff boundary where responsibility shifts between the human and the system?",
        must_learn_points_zh=[
            "自动化车辆的核心难题是 handoff，而不是稳定巡航。",
            "trust calibration 比“让用户更相信系统”更重要，它要求用户既不盲信也不过度弃用。",
            "航空自动化里的 mode confusion、monitoring decay 和 automation surprise 在这里高度可迁移。",
            "责任边界如果写不清，接管失败就会变成设计与使用共同制造的灰区。",
        ],
        must_learn_points_en=[
            "The central problem in automated vehicles is handoff rather than stable cruise.",
            "Trust calibration matters more than simply making users trust the system; it requires avoiding both over-trust and under-use.",
            "Mode confusion, monitoring decay, and automation surprise from aviation transfer strongly into this domain.",
            "If responsibility boundaries stay unclear, takeover failure becomes a gray zone jointly produced by design and use.",
        ],
        memory_anchor_zh="先记住这个案例的一句话判断：自动化车辆最危险的时刻，往往是系统要求“你现在马上接管”，而人却已经不在同一个情境里。",
        memory_anchor_en="Keep this case judgment in mind: the most dangerous moment in automated vehicles often arrives when the system says “take over now” while the human is no longer cognitively in the same situation.",
        sections=[
            section(
                "background",
                "## 背景与 stakes",
                "## Background and Stakes",
                body_zh="驾驶自动化和航空自动化的共同点，是都把人推向“平时低参与、关键时刻高责任”的角色。不同点在于，道路环境变化更快、用户更杂、边界更容易被误解，所以接管窗口通常更脆弱。",
                body_en="Driving automation and aviation automation share the same basic shift: humans are moved into a low-engagement role that still carries high responsibility at critical moments. The difference is that the roadway environment changes faster, users are more heterogeneous, and the boundary is easier to misunderstand, making the takeover window especially fragile.",
            ),
            section(
                "chain",
                "## 事件链真正容易断在哪里",
                "## Where the Event Chain Most Easily Breaks",
                body_zh="自动化车辆的问题通常不是“系统能不能自己开一会儿”，而是：用户长时间不需要主动控制后，是否还保持了足够的 situation awareness、模式理解和动作准备，一旦 ODD 边界到来能否及时接回控制。",
                body_en="The real question in automated vehicles is not whether the system can drive itself for a while, but whether the user retains enough situation awareness, mode understanding, and action readiness to resume control once the ODD boundary arrives.",
            ),
            section(
                "system",
                "## 这个案例教会我们的系统层问题",
                "## The System-Level Lesson of the Case",
                body_zh="如果系统默认人会始终保持适度警觉，但设计本身又长期让人退出主任务，那么设计假设就自相矛盾了。自动化车辆因此成为一个非常典型的 HFE 问题：界面、告警、模式说明、handoff 时机和责任分配必须一起设计。",
                body_en="If the system assumes the human will remain suitably vigilant while the design itself pushes the human out of the primary task for long periods, the design assumption becomes self-contradictory. Automated vehicles therefore become a classic HFE problem: interface, alerts, mode explanation, handoff timing, and responsibility allocation must be designed together.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="自动化车辆最难的不是让系统多做一点，而是让人和系统在接管边界上真正对得上。",
                note_body_en="The hardest part of automated vehicles is not making the system do more, but making the human and system line up at the takeover boundary.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "system",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把问题简化成“驾驶员没专心”。如果系统长期设计成让人不需要专心，最后又要求瞬时高质量接管，那本身就是设计假设的问题。",
                body_en="Do not reduce the issue to “the driver was inattentive.” If the system is designed to make sustained attention unnecessary and then suddenly demands high-quality takeover, the design assumption itself is the problem.",
            )
        ],
        examples=[
            callout(
                "example",
                "chain",
                "案例：handoff 为什么会变成高风险窗口",
                "Example: Why Handoff Becomes a High-Risk Window",
                body_zh="用户在自动驾驶模式下长时间处于被动监控状态，系统突然发出接管请求时，用户需要在很短时间里重新建立环境理解、识别系统边界并做出动作。这条链只要其中一环晚了半拍，风险就会迅速放大。",
                body_en="A user spends a long period in passive supervision while the automated mode is active. When a takeover request arrives, the user must rapidly rebuild environmental understanding, identify the system boundary, and act. If any link in that chain is delayed, risk escalates quickly.",
            )
        ],
        summary_points_zh=[
            "自动化车辆的核心难点是 handoff。",
            "trust calibration 比单纯提升信任更重要。",
            "航空自动化教训会大量迁移到这里。",
            "接管边界的责任分配必须被设计清楚。",
        ],
        summary_points_en=[
            "The central problem in automated vehicles is handoff.",
            "Trust calibration matters more than simply increasing trust.",
            "Many aviation-automation lessons transfer directly into this domain.",
            "Responsibility at the takeover boundary must be designed explicitly.",
        ],
    ),
}

AVIATION_AUTOMATION_CONTENT["aviation_automation_intro"]["sections"].extend(
    [
        section(
            "monitoring",
            "## 自动化为什么会把“剩余的人类任务”变得更难",
            "## Why Automation Makes the Remaining Human Tasks Harder",
            body_zh="""
            自动化最反直觉的地方在这里：系统做得越多，人的工作不一定越轻松。很多时候，人的工作从“持续参与”变成了“长时间低参与 + 突然高责任”的组合。

            这会带来至少三种后果：

            - 平时更难维持足够的状态把握
            - 一旦模式切换，理解成本突然升高
            - 真正要接管时，动作窗口反而更短

            所以自动化的问题不是系统会不会工作，而是人还来不来得及重新进入工作。
            """,
            body_en="""
            The most counterintuitive part of automation is that the more the system does, the easier the human role does not necessarily become. In many cases the human role shifts from continuous engagement to a combination of long low-engagement periods and sudden high-responsibility moments.

            That produces at least three consequences:

            - it becomes harder to maintain strong state awareness during normal operation
            - when a mode change occurs, the understanding burden rises sharply
            - when takeover is required, the action window is often shorter

            The real automation problem is therefore not simply whether the system can perform, but whether the human can get back into the loop in time.
            """,
        ),
        section(
            "handoff",
            "## 这页真正要你固定检查的 handoff 问题",
            "## The Handoff Questions This Page Wants You to Keep Asking",
            body_zh="""
            以后看到任何自动化系统，都可以固定问四件事：

            - 系统什么时候会把控制权还给人
            - 到那个时刻，人已经丢掉了多少情境意识
            - 模式状态是不是足够清楚
            - 如果人接不住，系统是否还有缓冲空间

            只要这四个问题里有两个答不上来，自动化就很可能只是把风险从手工操作换成了 handoff failure。
            """,
            body_en="""
            For any automated system you see later, keep four questions in mind:

            - when does the system hand control back to the human
            - by that moment, how much situation awareness has the human already lost
            - is the active mode clear enough
            - if the human cannot take over cleanly, does the system still preserve any buffer

            If two or more of those questions cannot be answered clearly, the automation may simply be moving risk from manual control into handoff failure.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["aviation_automation_intro"]["examples"].append(
    callout(
        "example",
        "handoff",
        "案例：为什么“平时很稳”并不能证明自动化设计安全",
        "Example: Why “It Works Well Most of the Time” Does Not Prove the Automation Is Safe",
        body_zh="一个自动化系统如果在正常工况下长期稳定运行，很容易给团队一种“整体设计没问题”的感觉。但真正高风险的部分往往不在稳定阶段，而在模式异常、边界逼近和突然接管时刻。换句话说，正常表现不能自动证明异常交接也被设计好了。",
        body_en="If an automated system runs smoothly for long periods in nominal conditions, teams are easily lulled into thinking the overall design is strong. But the highest-risk portion often lives not in the stable phase, but at mode anomalies, edge-of-envelope moments, and sudden takeover demands. Normal performance therefore does not automatically prove that abnormal handoff has been designed well.",
    )
)

AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["sections"].extend(
    [
        section(
            "briefing",
            "## 为什么 brief 和 debrief 不是形式步骤",
            "## Why Briefs and Debriefs Are Not Formalities",
            body_zh="""
            CRM 很容易被误读成“出事时怎么沟通”，但课程其实把它放得更早、更后。brief 的价值，是在任务开始前就把角色、预期、异常标准和挑战权限对齐；debrief 的价值，是让团队在任务后把差点出错的地方重新变成共享经验。

            如果缺少这两个环节，团队就更容易在执行中临时猜测彼此理解是否一致，风险会沿着模糊分工不断放大。
            """,
            body_en="""
            CRM is often misread as “how to communicate during an emergency,” but the course places it both earlier and later. The brief aligns roles, expectations, abnormality thresholds, and challenge authority before the task begins. The debrief turns near misses and weak coordination moments into shared learning afterward.

            Without those two stages, teams are more likely to guess during execution whether their understanding is aligned, and risk grows along that ambiguity.
            """,
        ),
        section(
            "challenge",
            "## 为什么 challenge-response 会成为真正的安全机制",
            "## Why Challenge-Response Becomes a Real Safety Mechanism",
            body_zh="""
            CRM 不是鼓励“多说话”而已，它更强调说话必须能进入团队决策。challenge-response 之所以重要，是因为它把一句提醒从个人意见变成团队必须处理的输入。

            真正强的团队不是没人犯错，而是当有人看到偏差时，系统允许这条信息被提出来、被确认、被吸收，并最终改变行动。
            """,
            body_en="""
            CRM is not simply asking people to talk more. It is asking that speech actually enter team decision making. Challenge-response matters because it turns a concern from one person’s opinion into an input that the team must process.

            Strong teams are not teams where nobody ever errs. They are teams where observed deviation can be voiced, confirmed, absorbed, and turned into changed action.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["examples"].append(
    callout(
        "example",
        "challenge",
        "案例：为什么“有人看见了问题”还远远不够",
        "Example: Why “Someone Noticed the Problem” Is Still Not Enough",
        body_zh="很多团队失败并不是因为没人注意到异常，而是注意到的人没能让异常进入集体决策。可能是 authority gradient 太陡、语言太模糊、时间太紧，或者团队默认不会被真正听进去。CRM 的目标，就是切断这条从“看见”到“没被吸收”的断裂链。",
        body_en="Many teams fail not because nobody noticed the anomaly, but because the person who noticed it could not get that signal into collective decision making. Authority gradient may be too steep, language too weak, time too short, or the team may implicitly expect not to be heard. CRM exists to break that chain from “noticed” to “not absorbed.”",
    )
)
AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["sections"].append(
    section(
        "authority_gradient",
        "## 为什么 authority gradient 会直接决定 CRM 是否真正生效",
        "## Why Authority Gradient Directly Determines Whether CRM Actually Works",
        body_zh="""
        很多团队表面上允许成员发声，但一旦 authority gradient 太陡，提醒就会变成礼貌性意见，而不是必须处理的安全输入。此时 CRM 看起来存在，实际上最关键的 challenge function 仍然是弱的。

        所以 CRM 评估不能只看团队有没有交流，还要看低位成员提出担忧后，团队是不是会真的停下来重看局面、重新分配注意力，或者修正原计划。
        """,
        body_en="""
        Many teams appear to allow people to speak, but when the authority gradient is too steep, a concern becomes a polite opinion rather than a safety input that must be processed. In that condition CRM appears to exist while its most important challenge function remains weak.

        CRM evaluation therefore cannot stop at whether the team exchanged words. It also has to ask whether a lower-status concern actually causes the team to reassess the picture, redirect attention, or revise the plan.
        """,
    )
)

AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["sections"].extend(
    [
        section(
            "priority",
            "## 告警真正难的不是被听见，而是被正确排序",
            "## The Hardest Part of Alerting Is Not Being Heard but Being Prioritized Correctly",
            body_zh="""
            很多系统以为只要把告警做得更醒目，问题就解决了。但操作者真正面对的不是单一告警，而是一堆同时竞争注意力的信号。告警设计真正要解决的是：哪个最先处理、哪个只是背景噪声、哪个必须立即转动作。

            也就是说，alerting 本质上不是感官刺激设计，而是优先级设计。
            """,
            body_en="""
            Many systems assume that making an alert more salient is enough. But operators rarely face one signal at a time. They face multiple cues competing for limited attention. The real design question is which signal should be handled first, which one is background, and which one must convert immediately into action.

            In that sense, alerting is not primarily about sensory stimulation. It is about priority design.
            """,
        ),
        section(
            "mapping",
            "## 为什么显示和告警必须一起看",
            "## Why Displays and Alerts Have to Be Evaluated Together",
            body_zh="""
            一条告警如果只会响，却不能把人带到正确状态信息上，它就只是打断，不是真正帮助。好的系统会让告警和显示之间形成清楚 mapping：听到或看到提醒后，操作者能立刻找到最关键的状态解释和后续动作线索。

            所以课程把 display 和 alert 放在一起讲，不是巧合，而是因为二者共同决定了“注意到之后能不能理解并行动”。
            """,
            body_en="""
            An alert that only makes noise but does not guide the operator toward the right state information is merely interruption, not support. Strong systems create a clear mapping between alert and display so that once the alert is noticed, the operator can quickly locate the critical state explanation and the next action cue.

            That is why the course treats displays and alerts together. Together they determine whether attention turns into understanding and action.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["examples"].append(
    callout(
        "example",
        "mapping",
        "案例：为什么“听见警报”不等于“知道现在该做什么”",
        "Example: Why Hearing the Alert Does Not Mean Knowing What to Do Next",
        body_zh="如果告警只有声音强度差别，却没有把人快速引向故障位置、状态趋势和推荐动作，操作者就可能先被打断，再花额外时间重新找状态。这样一来，告警反而会制造二次负担。好的设计会让告警和显示解释一起出现。",
        body_en="If alerts differ only in loudness but do not guide the operator toward fault location, state trend, and the recommended action, the operator is first interrupted and then forced to spend extra time reconstructing the state. In that case the alert creates secondary burden. Strong design lets the alert and the explanatory display work together.",
    )
)
AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["sections"].append(
    section(
        "false_alarm",
        "## 为什么 false alarm 和 nuisance alarm 会慢慢掏空整个告警系统",
        "## Why False and Nuisance Alarms Gradually Hollow Out the Whole Alerting System",
        body_zh="""
        告警系统真正的长期风险，不只是漏报，也包括太多不值得响应的报文。只要操作者持续接触 false alarm 或 nuisance alarm，系统就会一点点消耗他们对提醒的信任和处理速度。

        这就是为什么告警设计既要考虑“有没有报出来”，也要考虑“报出来的东西是否值得打断人”。如果系统频繁让人白白切换注意力，真正的关键警报到来时就更容易被延迟处理。
        """,
        body_en="""
        The long-term danger in an alerting system is not only missed detection, but also too many signals that never deserved interruption in the first place. Once operators are repeatedly exposed to false or nuisance alerts, the system gradually erodes both trust and response speed.

        That is why alert design has to ask not only whether the signal appears, but whether it deserves to interrupt. If the system repeatedly forces unnecessary attention switching, the truly critical alert is more likely to be delayed when it finally arrives.
        """,
    )
)

AVIATION_AUTOMATION_CONTENT["checklists_and_procedures"]["sections"].extend(
    [
        section(
            "types",
            "## checklist 和 procedure 在团队里分别承担什么不同角色",
            "## What Different Roles Checklists and Procedures Play in a Team",
            body_zh="""
            这两个词经常被混用，但在实际工作里并不完全一样。procedure 更像系统对任务顺序和责任边界的稳定规定；checklist 更像把其中最容易漏掉、最需要协同确认的部分外显出来。

            所以 checklist 不是 procedure 的缩略版，而是程序在认知与协作层的一种执行支架。
            """,
            body_en="""
            These two terms are often used together, but they are not identical in practice. A procedure is the system’s stable specification of task order and responsibility boundaries. A checklist externalizes the portions most vulnerable to omission and most dependent on coordination.

            A checklist is therefore not just a shorter procedure. It is an execution scaffold for the cognitive and collaborative parts of the procedure.
            """,
        ),
        section(
            "drift",
            "## 为什么真正危险的是“程序还在，但大家已经不再靠它工作”",
            "## Why the Real Danger Is When the Procedure Still Exists but No One Truly Works Through It",
            body_zh="""
            系统里最难发现的一类风险，是 procedure 在文件里仍然完整存在，但现场已经形成绕行、压缩和默认跳步。表面上程序没有被删除，实际上它已经失去屏障作用。

            所以复盘程序问题时，不能只检查“有没有 procedure”，还要问一线到底有没有把它当成现实工具，而不是当成形式要求。
            """,
            body_en="""
            One of the hardest risks to notice is when the procedure still exists in documentation but real work has shifted toward workaround, compression, and default skipping. On paper the procedure is still present; in practice it has lost its barrier function.

            That is why procedure review cannot stop at asking whether a procedure exists. It must also ask whether frontline work still treats it as a usable tool rather than a formal requirement to be routed around.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["checklists_and_procedures"]["examples"].append(
    callout(
        "example",
        "drift",
        "案例：为什么一张 checklist 会从“防线”慢慢变成“背景纸面”",
        "Example: How a Checklist Slowly Stops Being a Defense and Turns into Background Paper",
        body_zh="如果 checklist 太长、节奏不匹配真实任务、关键步骤不突出，团队很容易先是压缩执行，后来变成默认跳读，最后只在形式上“有做过”。这时 checklist 还在，但它已经不再真正塑造行动。",
        body_en="If a checklist is too long, poorly aligned with task rhythm, or fails to highlight the critical steps, teams often begin by compressing it, then drift into default skipping, and finally keep only the appearance of compliance. The checklist still exists, but it no longer shapes action in a meaningful way.",
    )
)
AVIATION_AUTOMATION_CONTENT["checklists_and_procedures"]["sections"].append(
    section(
        "timing",
        "## 为什么 checklist 的时机和节奏跟内容本身一样重要",
        "## Why Checklist Timing and Rhythm Matter as Much as the Content",
        body_zh="""
        一张 checklist 就算内容正确，如果放在错误时机使用，也可能失去大部分价值。过早读会让关键项在真正执行时已经从工作记忆里掉出去，过晚读又可能因为任务已经推进太快而无法纠正。

        所以 checklist 设计不仅是“写什么”，也是“什么时候读、谁来读、怎么和动作节奏配合”。这也是程序页和团队页会彼此连起来的原因。
        """,
        body_en="""
        A checklist can contain correct content and still lose most of its value if it is used at the wrong time. Read too early, the critical items may fall out of working memory before execution. Read too late, the task may already have advanced too far for correction.

        Checklist design therefore is not only about what gets written. It is also about when it is read, who reads it, and how it aligns with action rhythm. That is one reason the procedure page connects so closely to the team page.
        """,
    )
)

AVIATION_AUTOMATION_CONTENT["automated_vehicles"]["sections"].extend(
    [
        section(
            "odd",
            "## 为什么 automated vehicle 讨论离不开 ODD 边界",
            "## Why Automated-Vehicle Analysis Cannot Be Separated from ODD Boundaries",
            body_zh="""
            自动化车辆最关键的前提之一是 ODD，也就是系统到底在哪些条件下被假定可以工作。一旦这个边界不清楚，用户就很容易在系统其实已经接近能力边缘时，仍然误以为它处在“正常自动化”状态。

            所以 ODD 不是法规术语点缀，而是 handoff 风险的起点：越不清楚边界，越容易把接管做成措手不及。
            """,
            body_en="""
            One of the most important premises in automated vehicles is the ODD, the conditions under which the system is assumed to function. Once that boundary is unclear, users can continue believing they are inside normal automation even as the system approaches its actual edge of capability.

            ODD is therefore not decorative regulatory language. It is the starting point of takeover risk: the less visible the boundary, the more abrupt and fragile the handoff becomes.
            """,
        ),
        section(
            "monitoring_driver",
            "## 为什么驾驶员监控问题和系统设计问题其实分不开",
            "## Why Driver Monitoring and System Design Cannot Really Be Separated",
            body_zh="""
            automated vehicle 场景里，团队很容易把问题写成“driver was inattentive”。但更深一层的问题通常是：系统究竟把驾驶员放在什么角色上？是持续参与者、后备接管者，还是名义上负责但实际上长期脱离任务的人？

            只要这个角色定义不清，driver monitoring 再强，也很难真正补上 handoff 逻辑里的结构漏洞。
            """,
            body_en="""
            In automated-vehicle analysis, teams often rush toward “the driver was inattentive.” The deeper question is what role the system actually assigns to the driver: continuously engaged participant, backup takeover agent, or nominally responsible person who is effectively detached from the task most of the time.

            If that role definition is unclear, even strong driver-monitoring logic cannot fully repair the structural weakness in the handoff model.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["automated_vehicles"]["examples"].append(
    callout(
        "example",
        "monitoring_driver",
        "案例：为什么“请随时准备接管”这句话本身可能就是弱设计",
        "Example: Why “Be Ready to Take Over at Any Time” Can Be a Weak Design Assumption",
        body_zh="如果系统让人长时间低参与，却又要求在边界逼近时立即高质量接管，那么“请准备接管”就不只是提示语，而可能是在把一个结构上难以完成的任务压给驾驶员。问题不只在注意力，而在角色设计本身。",
        body_en="If the system keeps the person in a low-engagement state for long periods while still expecting immediate high-quality takeover at the edge of capability, then “be ready to take over” is not just a warning phrase. It may be assigning a structurally unrealistic task to the driver. The problem is not attention alone, but role design itself.",
    )
)
AVIATION_AUTOMATION_CONTENT["automated_vehicles"]["sections"].append(
    section(
        "trust_calibration",
        "## 为什么 automated vehicle 设计还要解决 trust calibration",
        "## Why Automated-Vehicle Design Also Has to Solve Trust Calibration",
        body_zh="""
        自动化车辆里还有一个特别典型的问题：人到底该信系统多少。信得太少，会导致频繁打断、低效和不必要的人工接管；信得太多，又会让人跨过 ODD 边界，或者在真正需要接管时反应太慢。

        所以 automated vehicle 设计不仅要让系统能工作，还要让人形成合适的 trust calibration。换句话说，系统必须把自己的边界、能力和不确定性表达得足够清楚，让人既不过度依赖，也不过度怀疑。
        """,
        body_en="""
        Automated vehicles also face a characteristic problem: how much should the human trust the system. Too little trust creates frequent interruption, low efficiency, and unnecessary takeover. Too much trust pushes the person beyond the ODD boundary and slows response when takeover is actually required.

        Automated-vehicle design therefore is not only about whether the system performs, but also about whether the person can form the right trust calibration. The system has to communicate its boundary, capability, and uncertainty clearly enough that the user neither over-relies nor under-relies on it.
        """,
    )
)

AVIATION_AUTOMATION_CONTENT["aviation_automation_intro"]["sections"].append(
    section(
        "transfer",
        "## 为什么课程要先从航空谈自动化，再谈其他行业",
        "## Why the Course Starts with Aviation Before Moving to Other Automated Domains",
        body_zh="""
        课程先从航空谈自动化，不是因为只有航空重要，而是因为航空把许多自动化问题暴露得最清楚。角色重分配、模式切换、短接管窗口、信息密集和高后果，在这里都同时出现，所以很多后续行业问题都能先在航空里看到原型。

        这也是为什么航空页不是单独行业史，而更像一页方法学入口。只要这页读懂了，后面看到自动驾驶、临床报警或复杂设备接管时，你会更容易认出那些重复出现的人因模式。
        """,
        body_en="""
        The course begins with aviation not because aviation is the only important domain, but because aviation exposes many automation problems with unusual clarity. Role redistribution, mode shifts, short takeover windows, dense information, and high consequence all appear together there, which makes aviation a strong prototype for later domains.

        That is why this page is not merely industry history. It functions more like a methodological entry point. Once this page is understood, later issues in automated driving, clinical alarms, or complex-device takeover become easier to recognize as repetitions of the same human-factors patterns.
        """,
    )
)
AVIATION_AUTOMATION_CONTENT["aviation_automation_intro"]["inline_visuals"].extend(
    [
        visual(
            "transfer",
            "Intro to Aviation and Automation 1-26-26-2.pdf",
            "这张图要看懂的是：课程先从航空出发，是因为航空里的人因研究起步早、积累深，很多自动化问题会先在这里被看清，再迁移到其他交通和复杂系统。",
            "This figure should show why the course starts with aviation: human-factors work matured early there, so many automation problems become visible in aviation before being transferred to other transport and complex systems.",
            asset_name_contains="page-02",
        ),
    ]
)

AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["sections"].append(
    section(
        "behaviors",
        "## 为什么 CRM 最后要落实成“可观察行为”而不只是原则",
        "## Why CRM Ultimately Has to Be Defined in Observable Behaviors Rather Than Principles Alone",
        body_zh="""
        CRM 如果只停在“沟通很重要”“团队协作要更好”这种原则层，培训和评估都会变空。课程真正强调的是，团队行为必须能被看见、被描述、被反馈，例如是否有 closed-loop communication、是否做了 cross-check、是否在 brief 中提前对齐了异常标准。

        也就是说，CRM 不能只作为价值观存在，它还必须转成一组可训练、可观察、可复盘的行为指标。只有这样，团队协作才不会沦为抽象口号。
        """,
        body_en="""
        If CRM remains only at the level of principles like “communication matters” or “teamwork should improve,” both training and evaluation become vague. What the course really emphasizes is that team behavior has to be visible, describable, and feedback-ready, for example whether communication was closed loop, whether cross-checking happened, or whether abnormality thresholds were aligned in the brief.

        CRM therefore cannot exist only as a value statement. It also has to become a set of trainable, observable, and reviewable behavior markers. Without that translation, teamwork easily collapses into abstract slogans.
        """,
    )
)
AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["inline_visuals"].extend(
    [
        visual(
            "authority_gradient",
            "CRM 1-28-2026.pdf",
            "这张图要看懂的是：CRM 不是单一技巧，而是一组可以被观察和训练的团队行为，包括沟通、brief、监控、领导与共享情境意识。",
            "This figure should make one thing concrete: CRM is not a single trick but a trainable set of observable team behaviors including communication, briefing, monitoring, leadership, and shared situation awareness.",
            asset_name_contains="page-14",
        ),
        visual(
            "logic",
            "CRM 1-28-2026.pdf",
            "这张图要看懂的是：CRM 的问题从一开始就不是纯“人际技巧”，而是把 liveware、环境、规则和设备重新接到一起的系统协调问题。",
            "This figure should show that CRM is not merely an interpersonal topic. It is a coordination problem that reconnects people, environment, rules, and equipment as one operating system.",
            asset_name_contains="page-04",
        ),
    ]
)

AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["sections"].append(
    section(
        "integration",
        "## 为什么高质量 display 设计会把“看到状态”和“采取动作”直接连起来",
        "## Why High-Quality Display Design Connects State Perception Directly to Action",
        body_zh="""
        display 设计真正成熟时，不会让操作者先看到一堆分散数据，再自己艰难拼出局面。更强的做法，是让最关键的状态关系和行动线索在界面里被组织出来，让人一眼知道哪里正在变差、风险相对方向是什么、下一步该优先处理什么。

        这也是为什么很多航空显示会把交通、速度带、告警区和状态趋势整合在一起。显示一旦能把“注意到”直接接到“理解并行动”，告警系统整体的负担就会下降。
        """,
        body_en="""
        Mature display design does not force the operator to first notice scattered numbers and then reconstruct the situation from scratch. A stronger design organizes the critical relationships and action cues directly in the interface so the operator can see where the state is degrading, what the relative direction of risk is, and which action deserves priority.

        That is why many aviation displays integrate traffic, speed tapes, alert zones, and state trend in one place. Once the display can connect noticing directly to understanding and action, the burden on the alerting system decreases as well.
        """,
    )
)
AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["inline_visuals"].extend(
    [
        visual(
            "integration",
            "Displays and Alerts 2-4-26.pdf",
            "这张图要看懂的是：像 TCAS 这样的集成显示，不只是把更多信息放进一个屏，而是把交通冲突、垂直速度和回避指令组织成能直接支持动作的界面。",
            "This figure should show that an integrated display such as TCAS is not merely putting more data on one screen. It organizes traffic conflict, vertical-speed information, and resolution cues into an interface that supports direct action.",
            asset_name_contains="page-21",
        ),
        visual(
            "false_alarm",
            "Displays and Alerts 2-4-26.pdf",
            "这张图要看懂的是：alarm fatigue 不是抽象概念，临床环境里过多 nuisance alarm 会直接侵蚀信任、干扰工作并拖慢真正关键的响应。",
            "This figure should make alarm fatigue concrete: in clinical care, excessive nuisance alarms directly erode trust, disrupt work, and slow the response to truly critical signals.",
            asset_name_contains="page-09",
        ),
    ]
)

AVIATION_AUTOMATION_CONTENT["checklists_and_procedures"]["sections"].append(
    section(
        "comparison",
        "## 为什么真实 checklist 设计差异会直接改变执行质量",
        "## Why Real Differences in Checklist Design Directly Change Execution Quality",
        body_zh="""
        课程里拿不同 checklist 样式做对比，不是为了展示版式差异，而是为了提醒一件事：同样叫“before start checklist”，其长度、分组方式、可扫读性和节奏匹配程度都会直接影响执行效果。

        这意味着 checklist 不是只要“有”就行。版面结构、项目聚类、字量密度、读答节奏和任务阶段的对齐，都会决定它究竟是高质量支架，还是一张只会被快速跳过的纸。
        """,
        body_en="""
        The course compares different checklist formats not to make a typographic point, but to show something operationally important: even when two artifacts are both called “before start checklist,” their length, grouping, scanability, and rhythm fit can change execution quality substantially.

        That means a checklist does not become useful simply because it exists. Layout structure, item clustering, text density, read-response rhythm, and alignment with task phase all determine whether it functions as a strong scaffold or becomes paper that crews skim past.
        """,
    )
)
AVIATION_AUTOMATION_CONTENT["checklists_and_procedures"]["inline_visuals"].extend(
    [
        visual(
            "comparison",
            "Checklists and Procedures 3-23-26.pdf",
            "这张图要看懂的是：两张同样用于 B-757 的 before-start checklist，在长度、结构和可扫读性上的差异会直接改变机组执行时的认知负担。",
            "This figure should show that two before-start checklists for the same B-757 can create very different cognitive burdens because of differences in length, structure, and scanability.",
            asset_name_contains="page-15",
        ),
        visual(
            "problem",
            "Checklists and Procedures 3-23-26.pdf",
            "这张图要看懂的是：checklist 与 procedure 不只是个体记忆工具，它们属于组织层 mitigation，和培训、CRM、display 一样都是系统防线的一部分。",
            "This figure should make one point visible: checklists and procedures are not only personal memory aids. They are organizational mitigations and part of the same defense system as training, CRM, and displays.",
            asset_name_contains="page-02",
        ),
    ]
)

AVIATION_AUTOMATION_CONTENT["automated_vehicles"]["sections"].append(
    section(
        "levels",
        "## 为什么 SAE 自动化等级图很有用，但也容易被误读",
        "## Why the SAE Automation-Level Diagram Is Useful but Also Easy to Misread",
        body_zh="""
        SAE 等级图很有用，因为它能快速告诉人“什么时候还是人负责持续监控，什么时候系统才真正接管驾驶任务”。但它也容易被误读成一条简单的技术升级阶梯，好像等级越高就自然越安全、越省心。

        课程更想强调的是另一点：等级变化代表角色变化。只要人的角色、接管时机和责任边界没有被讲清楚，再漂亮的等级图也不能替系统解决 handoff 风险。
        """,
        body_en="""
        The SAE level diagram is useful because it quickly clarifies when the human is still responsible for continuous supervision and when the system is actually taking over the driving task. But it is also easy to misread as a simple ladder of technical progress, as if higher levels automatically mean greater safety and less human burden.

        The course wants to emphasize something else: level changes are role changes. If the human role, takeover timing, and responsibility boundary are not made explicit, even a clear level diagram cannot solve handoff risk.
        """,
    )
)
AVIATION_AUTOMATION_CONTENT["automated_vehicles"]["inline_visuals"].extend(
    [
        visual(
            "levels",
            "Automated Vehicles 3-11-26-2.pdf",
            "这张图要看懂的是：SAE 等级的真正意义不是营销标签，而是不同等级下谁在持续监控、谁在负责控制、谁在边界到来时必须接手。",
            "This figure should show that SAE levels are not just marketing labels. They define who is continuously monitoring, who is controlling, and who must take over when the boundary arrives.",
            asset_name_contains="page-08",
        ),
        visual(
            "background",
            "Automated Vehicles 3-11-26-2.pdf",
            "这张图要看懂的是：自动化越强，人越容易退成“旁观者”，而这正是接管时最脆弱的认知位置。",
            "This figure should make one point intuitive: the stronger the automation feels, the easier it is for the human to drift toward spectator status, which is exactly the fragile cognitive position at takeover.",
            asset_name_contains="page-02",
        ),
    ]
)

AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["sections"].extend(
    [
        section(
            "origins",
            "## 为什么 CRM 会在 1970s 事故之后变成正式主题",
            "## Why CRM Became a Formal Topic After the 1970s Accident Wave",
            body_zh="""
            CRM 不是凭空出现的。课件把 Eastern 401、Tenerife 和 United 173 放在一起，就是为了说明一个共同事实：很多高后果事故里，技术故障不是唯一线索，机组怎样分配注意、怎样挑战机长、怎样共享燃油和跑道状态，同样决定了事故会不会继续扩展。

            也正因为这些事故不断暴露“有人看见了问题，但团队没有把信号转成行动”，CRM 才从飞行文化话题变成正式训练主题。它不是锦上添花，而是事故教出来的结构性教训。
            """,
            body_en="""
            CRM did not appear out of nowhere. The course places Eastern 401, Tenerife, and United 173 together to show one common fact: in many high-consequence accidents, technical malfunction was not the only clue. How the crew allocated attention, challenged the captain, and shared awareness of fuel or runway state also determined whether the event would continue expanding.

            Because these accidents repeatedly exposed the pattern “someone saw the problem but the team did not convert the signal into action,” CRM moved from a cultural topic into a formal training topic. It is not decorative polish. It is a structural lesson taught by accidents.
            """,
        ),
        section(
            "shell",
            "## 为什么 ICAO SHELL 模型会让 CRM 不再像“软技能”",
            "## Why the ICAO SHELL Model Stops CRM from Looking Like a Pure Soft-Skills Topic",
            body_zh="""
            SHELL 模型的作用，是把 CRM 从“人和人沟通”重新拉回到系统接口。课件里 Software、Hardware、Environment 和 Liveware 被放在一起，意思很直接：团队协作质量并不是脱离设备、程序和环境单独存在的。

            所以 CRM 评估不能只看态度。它还要看 procedure 是否支持 cross-check，display 是否支持共享判断，环境是否让沟通被打断，角色分工是否让 challenge 有现实机会。SHELL 模型让 CRM 回到 HFE 的大框架里，而不是停在励志口号上。
            """,
            body_en="""
            The function of the SHELL model is to pull CRM back from “people talking to people” into the language of system interfaces. By placing Software, Hardware, Environment, and Liveware together, the lecture makes a direct point: team coordination quality does not exist independently of equipment, procedure, and operating context.

            CRM evaluation therefore cannot stop at attitude. It must also ask whether procedures support cross-checking, whether displays support shared interpretation, whether the environment blocks communication, and whether role structure gives challenge a real opportunity. SHELL puts CRM back inside the larger HFE frame instead of leaving it as motivational language.
            """,
        ),
        section(
            "audit",
            "## 如果要判断一支团队的 CRM 是否健康，最该看什么",
            "## If You Need to Judge Whether a Team’s CRM Is Healthy, What Should You Look For First",
            body_zh="""
            最有效的检查方法，不是问团队成员“你们重不重视沟通”，而是直接看行为链是否存在：

            - 关键状态有没有被提前 brief
            - 异常有没有被明确说出来，而不是含糊带过
            - challenge 提出后，团队有没有停下来重新分配注意力
            - cross-check 和 closed-loop communication 是不是真的发生
            - debrief 有没有把差点出事的节点重新沉淀成共享经验

            这也是为什么 CRM 最终会落到 behavioral markers。没有可观察行为，团队协作就很难被训练、评估和改进。
            """,
            body_en="""
            The most effective way to check CRM is not to ask whether the team “values communication.” It is to inspect whether the behavior chain actually exists:

            - were critical states briefed in advance
            - were anomalies spoken explicitly instead of vaguely
            - when a challenge was raised, did the team pause and redirect attention
            - did cross-checking and closed-loop communication actually occur
            - did the debrief convert near-failure moments into shared learning

            That is why CRM eventually lands on behavioral markers. Without observable behavior, teamwork is very hard to train, evaluate, or improve.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["crew_resource_management"]["examples"].append(
    callout(
        "example",
        "origins",
        "案例：为什么 United 173 不是“机长一个人判断错了”这么简单",
        "Example: Why United 173 Is Not Adequately Described as “The Captain Made the Wrong Judgment”",
        body_zh="United 173 常被提到，是因为它把 CRM 问题暴露得非常清楚：机长持续把注意力放在起落架问题上，而燃油状态这条更致命的信息没有被团队成功抬升成必须立刻改变计划的输入。这个案例的重点，不是单独批评谁，而是看团队为什么没能把已有信息转成集体行动。",
        body_en="United 173 is repeatedly cited because it exposes the CRM problem very clearly: the captain remained fixated on the landing-gear issue, while the more lethal signal about fuel state was not successfully elevated into an input that forced the team to change plan immediately. The point is not only to criticize one individual, but to ask why the team failed to turn available information into collective action.",
    )
)

AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["sections"].extend(
    [
        section(
            "principles",
            "## 为什么 display 设计原则会直接决定“能不能一眼读对”",
            "## Why Display Design Principles Directly Determine Whether a State Can Be Read Correctly at a Glance",
            body_zh="""
            课件里列的那些 display 设计原则不是视觉设计清单，而是在回答一个很实用的问题：当操作者没有太多时间时，界面还能不能把关键关系直接组织出来。信息密度、grouping、contrast、redundant coding、pictorial realism 和 predictive aiding，本质上都在帮助人更快抓住状态结构，而不是只看到更多数据。

            这也是为什么显示设计很少能靠“把更多东西放上去”解决。只要层级、邻近关系和表示方式不对，界面信息越多，操作者越可能看见一堆元素，却没能及时读出真正重要的状态关系。
            """,
            body_en="""
            The display principles listed in the lecture are not a decorative visual-design checklist. They answer a practical question: when the operator has little time, can the interface still organize the critical relationships directly. Information density, grouping, contrast, redundant coding, pictorial realism, and predictive aiding all exist to help people grasp state structure quickly rather than merely look at more data.

            That is also why display design rarely improves by simply adding more information. Once hierarchy, proximity, and representation are wrong, the operator may see many elements and still fail to read the important state relationship in time.
            """,
        ),
        section(
            "auditory",
            "## 为什么 auditory display 有时比 visual display 更适合先抢到注意力",
            "## Why an Auditory Display Can Sometimes Capture Attention Better Than a Visual One",
            body_zh="""
            课件把 auditory display 单独拿出来讲，是因为人在很多高负荷场景里，眼睛已经被占满了。此时声音的价值不是替代视觉理解，而是先把注意力从别处拉回来，告诉操作者“现在有一件事必须处理”。

            但声音也有明显边界。它很适合抢注意、区分优先级、表达紧急性，却不适合承载太复杂的状态结构。也正因为如此，好的系统往往会让 auditory alert 先把人拉过来，再由 visual display 接手更细的状态解释和动作引导。
            """,
            body_en="""
            The lecture separates auditory displays because in many high-load settings the eyes are already saturated. In that condition, sound is valuable not because it replaces visual understanding, but because it can pull attention back and say, “something now requires action.”

            But sound also has clear limits. It is good at capturing attention, distinguishing priority, and conveying urgency, but not at carrying complex state structure. That is why stronger systems often let the auditory alert pull the operator in first and then let the visual display carry the more detailed state explanation and action guidance.
            """,
        ),
        section(
            "testing",
            "## 为什么 display 和 alert 设计最后一定要回到 implementation 与 testing",
            "## Why Display and Alert Design Ultimately Has to Return to Implementation and Testing",
            body_zh="""
            这页最后讲 implementation 和 testing，是因为很多 display / alert 设计在概念上看起来都合理，真正上线后却会在噪声、工作负荷、设备差异或环境条件下表现出完全不同的效果。只有测试，团队才知道哪些提醒会被忽略、哪些显示会被误读、哪些优先级划分根本不稳。

            这也是为什么告警设计不能只在会议室里讨论。它必须进到 representative task、representative environment 和 representative workload 里去验证，否则系统很可能在纸面上“解释得通”，在现场却仍然让人看不清、听不准、反应不过来。
            """,
            body_en="""
            The lecture ends with implementation and testing because many display and alert designs look reasonable in principle yet behave very differently once noise, workload, device differences, or environment are introduced. Only testing tells the team which alerts get ignored, which displays are misread, and which priority distinctions are not stable in practice.

            That is also why alert design cannot remain a conference-room discussion. It has to be validated in representative tasks, representative environments, and representative workloads. Otherwise the system may look defensible on paper while still leaving people unable to see clearly, hear accurately, or respond in time.
            """,
        ),
    ]
)
AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["examples"].append(
    callout(
        "example",
        "auditory",
        "案例：为什么一个好的声音告警通常不会试图把全部状态都“说出来”",
        "Example: Why a Good Auditory Alert Usually Does Not Try to “Say Everything” About the State",
        body_zh="如果声音告警试图直接承载太多状态细节，操作者在高负荷下反而更难及时提取重点。更成熟的做法，是先用声音稳定表达优先级和紧急性，再把具体解释交给对应的 visual display。也就是说，声音的价值往往在于抢占注意，而不是单独完成诊断。",
        body_en="If an auditory alert tries to carry too much state detail directly, the operator under high load may struggle even more to extract the key point in time. A stronger approach is to let sound reliably express priority and urgency first, and then let the corresponding visual display carry the detailed explanation. In other words, the value of sound often lies in attention capture, not in performing diagnosis alone.",
    )
)
AVIATION_AUTOMATION_CONTENT["displays_and_alerts"]["inline_visuals"].append(
    visual(
        "principles",
        "Displays and Alerts 2-4-26.pdf",
        "这张图要看懂的是：好的显示不会把数据平铺出来，而是把航迹、冲突对象和模式信息组织成能被快速读出的状态结构。",
        "This figure should make one point concrete: a strong display does not simply lay out data. It organizes trajectory, conflict object, and mode information into a state structure that can be read quickly.",
        asset_name_contains="page-01",
    )
)
