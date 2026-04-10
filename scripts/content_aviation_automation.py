from __future__ import annotations

from note_blueprints import callout, formalize_blueprint, page_blueprint, section


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

AVIATION_AUTOMATION_CONTENT = {
    slug: formalize_blueprint(blueprint) for slug, blueprint in AVIATION_AUTOMATION_CONTENT.items()
}
