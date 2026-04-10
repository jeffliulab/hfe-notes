from __future__ import annotations

from note_blueprints import callout, page_blueprint, section, visual


HUMAN_PERFORMANCE_CONTENT: dict[str, dict] = {
    "attention_and_monitoring": page_blueprint(
        template_type="concept",
        page_intro_zh="注意与监控这一页最重要的结论是：持续监控并不是轻松任务，它恰恰是最容易衰退的任务类型之一。",
        page_intro_en="The most important conclusion of this page is that sustained monitoring is not an easy task; it is one of the task types most vulnerable to performance decay.",
        core_question_zh="为什么系统越要求人“盯着看、等着问题出现”，反而越容易在真正出事时失去监控效果？",
        core_question_en="Why do systems that ask people to “watch and wait for trouble” often lose monitoring effectiveness precisely when the trouble arrives?",
        must_learn_points_zh=[
            "注意是有限资源，会被优先级、疲劳、时间和告警策略不断重分配。",
            "监控任务因为刺激稀少、反馈少、事件低频，特别容易出现 vigilance decrement。",
            "自动化越强，人越容易退成被动监视者，从而提高 complacency 风险。",
            "监控失败经常是任务设计问题，不是单纯态度问题。",
        ],
        must_learn_points_en=[
            "Attention is a limited resource and is continuously reallocated by priority, fatigue, time, and alert strategy.",
            "Monitoring tasks are especially vulnerable to vigilance decrement because stimuli are rare and feedback is sparse.",
            "The stronger the automation, the easier it becomes for humans to drift into passive supervision and complacency.",
            "Monitoring failure is often a task-design problem rather than a pure attitude problem.",
        ],
        memory_anchor_zh="先记住一句话：如果一个系统把人的工作设计成“长时间盯着看，偶尔突然接管”，那就已经在和人的注意机制对着干了。",
        memory_anchor_en="Keep one sentence in mind: if a system designs the human role as long periods of watching followed by sudden intervention, it is already working against the structure of human attention.",
        sections=[
            section(
                "limits",
                "## 为什么注意本来就是有限资源",
                "## Why Attention Is Limited by Default",
                body_zh="注意不是可以无限拉长的稳定灯光，而是会随着优先级、负荷、时间和疲劳不断重新分配的资源。课程在这里不是让你背心理学术语，而是要你承认：系统设计必须把这种资源限制当成前提。",
                body_en="Attention is not a perfectly stable beam that can be extended indefinitely. It is a resource that gets redistributed by priority, workload, time, and fatigue. The point of the page is not memorizing cognitive terminology; it is recognizing that system design must treat this limitation as a starting assumption.",
            ),
            section(
                "monitoring",
                "## 为什么监控任务特别容易衰退",
                "## Why Monitoring Tasks Decay So Easily",
                body_zh="监控任务看起来轻松，其实很难，因为刺激稀少、事件低频、反馈弱，人的大脑很难长期维持同样高的警觉水平。等到真正异常出现时，操作者反而可能正处在最低参与状态。",
                body_en="Monitoring tasks look easy, but they are difficult because stimuli are sparse, critical events are infrequent, and feedback is weak. The brain struggles to maintain the same alertness level for long periods, which means the operator may be at the lowest engagement point when the real anomaly appears.",
            ),
            section(
                "design",
                "## 这页对系统设计的真正要求是什么",
                "## What This Implies for System Design",
                body_zh="如果任务本身容易监控衰退，设计就不能把责任全压给“人要更专心”。更合理的做法是：让状态变化更可见、关键事件更可区分、交叉检查更容易启动、恢复路径更清楚。",
                body_en="If the task itself is vulnerable to monitoring decay, design cannot leave the burden at “the person should pay more attention.” A stronger response is to make state changes more visible, critical events more distinguishable, cross-checking easier to trigger, and recovery paths clearer.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="监控失败经常是任务设计和信号设计的失败，而不是“人不够认真”的简单道德判断。",
                note_body_en="Monitoring failure is often a failure of task and signal design rather than a simple moral judgment that the operator was not serious enough.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "design",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="“要求人保持警觉”本身不是设计方案。如果系统没有主动帮助保持状态把握，提醒人专心通常不会长期有效。",
                body_en="“Ask the operator to stay vigilant” is not a design solution. If the system does not actively support state awareness, telling people to stay focused rarely works over time.",
            )
        ],
        examples=[
            callout(
                "example",
                "monitoring",
                "案例：为什么低事件率监控最容易掉链子",
                "Example: Why Low-Event-Rate Monitoring Fails So Easily",
                body_zh="当系统长时间稳定，操作者主要在“等问题出现”时，注意会自然下滑。等到真正关键的异常终于出现，信号反而可能被延迟识别，这就是 vigilance decrement 最典型的系统表现。",
                body_en="When the system stays stable for a long time and the operator mainly waits for trouble to appear, attention naturally declines. When the truly critical anomaly finally arrives, its signal may be recognized late. That is one of the most typical system expressions of vigilance decrement.",
            )
        ],
        summary_points_zh=[
            "注意是有限资源，不会无限稳定。",
            "监控任务尤其容易出现 vigilance decrement。",
            "自动化会把人推向更脆弱的被动监视角色。",
            "设计必须主动支持监控，而不是只要求更专心。",
        ],
        summary_points_en=[
            "Attention is limited and cannot stay perfectly stable forever.",
            "Monitoring tasks are especially vulnerable to vigilance decrement.",
            "Automation often pushes people into a more fragile passive-supervision role.",
            "Design must actively support monitoring instead of only demanding more attention.",
        ],
    ),
    "fatigue_and_sleep": page_blueprint(
        template_type="concept",
        page_intro_zh="疲劳与睡眠这一页要你看到：疲劳不是“有点累”的主观抱怨，而是会系统性改变反应、判断、记忆和监控能力的生理约束。",
        page_intro_en="This page asks you to see fatigue not as a vague feeling of tiredness, but as a physiological constraint that systematically alters reaction, judgment, memory, and monitoring.",
        core_question_zh="为什么疲劳管理不能只靠个人自律，而必须被看成排班、任务长度、时段和组织要求共同制造的系统问题？",
        core_question_en="Why can fatigue management not rely on personal discipline alone, but must be treated as a system problem created by scheduling, task length, timing, and organizational demands?",
        must_learn_points_zh=[
            "睡眠不足会让很多关键认知能力下降，即使人主观上觉得“还能工作”。",
            "生理节律会改变不同时段的风险窗口。",
            "疲劳问题经常由班次、夜班、任务长度和组织要求共同制造。",
            "疲劳管理应当进入排班、交接和高风险任务设计，而不只是健康建议。",
        ],
        must_learn_points_en=[
            "Sleep loss degrades critical cognitive functions even when the person still feels capable of working.",
            "Circadian rhythm changes the risk window across different times of day.",
            "Fatigue is often jointly produced by shifts, night work, task duration, and organizational demand.",
            "Fatigue management belongs in scheduling, handoff design, and high-risk task planning rather than only in wellness advice.",
        ],
        memory_anchor_zh="先记住一句话：再好的界面、程序和培训，最后也要经过一个可能正在疲劳中的人来执行。",
        memory_anchor_en="Keep one sentence in mind: even the best interface, procedure, and training must still pass through a human who may already be fatigued.",
        sections=[
            section(
                "effects",
                "## 疲劳到底会影响什么",
                "## What Fatigue Actually Alters",
                body_zh="疲劳会影响反应速度、工作记忆、判断质量、监控耐力和恢复能力。危险之处在于，人未必会立刻意识到自己下降了多少，所以主观感受和实际表现可能并不同步。",
                body_en="Fatigue alters reaction time, working memory, judgment quality, monitoring endurance, and recovery ability. The danger is that people do not always recognize how much they have declined, so subjective feeling and actual performance may diverge sharply.",
            ),
            section(
                "rhythm",
                "## 为什么同一任务在不同时段风险不同",
                "## Why the Same Task Carries Different Risk at Different Times",
                body_zh="课程强调生理节律，是因为风险并不是均匀分布的。夜班、清晨低谷、长时持续任务和睡眠债累积，都会让同一任务在不同时间表现出不同脆弱性。",
                body_en="Circadian rhythm matters because risk is not uniformly distributed across the day. Night work, early-morning lows, long-duration tasks, and accumulated sleep debt all change how vulnerable the same task becomes over time.",
            ),
            section(
                "design",
                "## 为什么疲劳管理是系统设计问题",
                "## Why Fatigue Management Is a Design Problem",
                body_zh="如果组织长期把排班、任务长度、夜班负担和高风险任务时段安排得不合理，那么“提醒大家多休息”很难真正解决问题。更成熟的管理方式，是把疲劳当成需要被设计和缓冲的风险源。",
                body_en="If scheduling, task duration, night-work burden, and high-risk task timing are poorly designed, telling people to rest more will not solve the problem. A stronger approach treats fatigue as a risk source that must be designed around and buffered against.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="疲劳不是个人软弱，而是系统必须正视的生理约束。",
                note_body_en="Fatigue is not personal weakness; it is a physiological constraint the system must take seriously.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "design",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="把 fatigue management 缩成“提醒大家多睡觉”是远远不够的。真正危险的变量，往往在排班和任务设计里。",
                body_en="Reducing fatigue management to “tell people to sleep more” is not enough. The more dangerous variables usually sit inside scheduling and task design.",
            )
        ],
        examples=[
            callout(
                "example",
                "rhythm",
                "案例：为什么夜班同样的任务会更危险",
                "Example: Why the Same Task Becomes More Dangerous on a Night Shift",
                body_zh="同样的监控或操作任务，放在夜班和白班并不等价。夜间低谷会让警觉、判断和恢复速度下降，使原本还能接受的任务负荷变成更高风险窗口。",
                body_en="The same monitoring or operational task is not equivalent on day shift and night shift. Circadian low points degrade alertness, judgment, and recovery speed, turning what seemed like an acceptable workload into a higher-risk window.",
            )
        ],
        summary_points_zh=[
            "疲劳会系统性影响反应、记忆、判断和监控。",
            "生理节律会改变风险窗口。",
            "疲劳常由排班和组织条件共同制造。",
            "疲劳管理必须进入系统设计层。",
        ],
        summary_points_en=[
            "Fatigue systematically alters reaction, memory, judgment, and monitoring.",
            "Circadian rhythm changes the risk window.",
            "Fatigue is often co-produced by scheduling and organizational conditions.",
            "Fatigue management has to move into system design.",
        ],
    ),
    "stress_and_decision_making": page_blueprint(
        template_type="concept",
        page_intro_zh="压力、决策与分心这一页讲的不是“人一紧张就变差”这么简单，而是压力怎样缩窄注意和策略空间，让人更容易走向次优判断。",
        page_intro_en="This page is not simply about people becoming worse under pressure. It examines how stress narrows attention and strategy space, making suboptimal judgment more likely.",
        core_question_zh="为什么高压力、高时间压力和多任务分心会让人更容易看漏、想偏、过快下结论，或者反而迟迟下不了决策？",
        core_question_en="Why do high pressure, time pressure, and distraction make omission, bias, premature closure, or delayed decision more likely?",
        must_learn_points_zh=[
            "压力会占用认知资源，缩窄搜索和比较范围。",
            "分心会打断计划执行，让人更容易漏步、失去时间线或忘掉中间状态。",
            "时间压力会推动启发式判断和 satisficing。",
            "关键不是要求人“更冷静”，而是看系统有没有减轻还是继续加码认知负担。",
        ],
        must_learn_points_en=[
            "Stress consumes cognitive resources and narrows search and comparison space.",
            "Distraction interrupts plan execution and increases omission, timeline loss, and state forgetting.",
            "Time pressure pushes people toward heuristics and satisficing.",
            "The key question is not only whether the person stayed calm, but whether the system reduced or intensified cognitive burden.",
        ],
        memory_anchor_zh="先记住一句话：压力最危险的地方，不是让人“感觉不好”，而是让人只剩下更少的线索和更少的策略可用。",
        memory_anchor_en="Keep one sentence in mind: the most dangerous thing about stress is not how it feels, but how it leaves the person with fewer usable cues and fewer workable strategies.",
        sections=[
            section(
                "chain",
                "## 压力、分心和决策为什么会连在一起",
                "## Why Stress, Distraction, and Decision Making Belong Together",
                body_zh="压力占用认知资源，分心打断执行链条，时间压力缩短比较窗口。三者叠加时，操作者更容易依赖最熟悉的路径，而不是继续搜索和修正。",
                body_en="Stress consumes cognitive resources, distraction interrupts the execution chain, and time pressure shortens the comparison window. When all three combine, operators are more likely to rely on familiar paths rather than continue searching and correcting.",
            ),
            section(
                "signals",
                "## 为什么很多人明明看见了信息却没用上",
                "## Why People Often See the Signal but Still Fail to Use It",
                body_zh="高压力场景里，问题常常不是完全没看见，而是新信息没有进入当前判断框架。换句话说，压力和预设会让人更倾向于抓住已有解释，而不是重新组织局面。",
                body_en="In high-pressure settings, the problem is often not that the signal was completely unseen, but that it never entered the active judgment frame. Stress and expectation bias the person toward the current explanation instead of re-organizing the situation around new evidence.",
            ),
            section(
                "design",
                "## 这页对系统设计提出什么要求",
                "## What This Page Demands from System Design",
                body_zh="面对高负荷场景，系统不应该继续堆更多模糊信息和额外任务，而应帮助保留关键线索、减少无意义切换、明确优先级，并让团队协作真正减负。",
                body_en="In high-load settings, systems should not add more ambiguous information and extra tasks. They should preserve critical cues, reduce needless switching, clarify priority, and let teamwork genuinely remove burden.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="压力下的差决策，很多时候不是“人太差”，而是系统没有帮人保住足够好的判断条件。",
                note_body_en="Poor decisions under stress often reflect not that the person is weak, but that the system failed to preserve adequate judgment conditions.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "signals",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="压力不总会让表现立刻下降；更危险的是持续高压加不完整信息，会让人越来越依赖熟悉路径而忽略新线索。",
                body_en="Stress does not always degrade performance immediately. The more dangerous pattern is sustained pressure plus incomplete information, which drives increasing reliance on familiar paths while underweighting new cues.",
            )
        ],
        examples=[
            callout(
                "example",
                "design",
                "案例：为什么“更快做决定”有时反而更危险",
                "Example: Why “Decide Faster” Can Become More Dangerous",
                body_zh="在时间压力极高时，操作者可能很快给出一个看似果断的答案，但这个答案建立在过窄的信息搜索上。系统如果没有帮助保留关键线索和第二视角，快速决策就可能只是快速收错。",
                body_en="Under extreme time pressure, an operator may reach a quick and seemingly decisive answer, but that answer may rest on a very narrow information search. If the system does not preserve critical cues and a second perspective, fast decision making may simply become fast wrong closure.",
            )
        ],
        summary_points_zh=[
            "压力会缩窄注意和策略空间。",
            "分心会打断计划执行和时间线维护。",
            "时间压力会推动启发式和 satisficing。",
            "系统设计的任务是帮人保住判断条件。",
        ],
        summary_points_en=[
            "Stress narrows attention and strategy space.",
            "Distraction interrupts execution and timeline maintenance.",
            "Time pressure pushes heuristics and satisficing.",
            "System design should preserve the conditions for good judgment.",
        ],
    ),
    "situation_awareness": page_blueprint(
        template_type="concept",
        page_intro_zh="情境意识这一页把“看见信息”拆成三层：先感知，再理解，再预测。重点是让你看到信息可见和局面可理解之间还有很长一段距离。",
        page_intro_en="This page breaks “seeing information” into three layers: perception, comprehension, and projection. The goal is to show that visible information and understandable situation are not the same thing.",
        core_question_zh="为什么系统明明把很多信息都显示出来了，操作者却仍然可能既不理解当前局面，也无法预测接下来会怎样？",
        core_question_en="Why can a system display large amounts of information and still leave the operator unable to understand the current situation or predict what happens next?",
        must_learn_points_zh=[
            "情境意识至少包括 perception、comprehension、projection 三层。",
            "信息可见不等于意义清楚，更不等于未来状态可预测。",
            "很多显示、CRM、监控和自动化问题最后都会回到 SA 断裂上。",
            "SA 的本质不是信息量，而是信息有没有被组织成可行动的 mental model。",
        ],
        must_learn_points_en=[
            "Situation awareness includes at least perception, comprehension, and projection.",
            "Visible information does not guarantee meaning, and meaning does not guarantee prediction.",
            "Many display, CRM, monitoring, and automation problems ultimately return to breaks in SA.",
            "The essence of SA is not information quantity but whether information is organized into an actionable mental model.",
        ],
        memory_anchor_zh="先记住一句话：情境意识不是“多看一点”，而是把看到的线索真正拼成当前局面，并能往前预判一步。",
        memory_anchor_en="Keep one sentence in mind: situation awareness is not merely about looking harder; it is about turning seen cues into an accurate current picture and one step of forward projection.",
        sections=[
            section(
                "layers",
                "## 三层结构到底分别在说什么",
                "## What the Three Layers Actually Mean",
                body_zh="""
课程里的三层结构是：

1. `perception`：有没有注意到关键线索。
2. `comprehension`：这些线索有没有被拼成正确的当前局面。
3. `projection`：如果不干预，系统接下来会往哪里走。
""",
                body_en="""
The three layers in the course are:

1. `perception`: whether the critical cues were noticed
2. `comprehension`: whether the cues were integrated into the correct current picture
3. `projection`: where the system is likely to go next if nobody intervenes
""",
            ),
            section(
                "difficulty",
                "## 为什么第二层和第三层最容易断",
                "## Why the Second and Third Layers Break So Easily",
                body_zh="操作者可能已经看到了读数、告警和状态变化，但仍然不知道哪个信号优先、多个信号之间有什么关系、以及未来几十秒会怎么演化。也就是说，SA 的难点往往不在“看见”，而在“组织和推演”。",
                body_en="Operators may see the readings, alerts, and state changes yet still not know which cue has priority, how several signals relate, or how the situation will evolve over the next seconds. In other words, the hard part of SA is often not noticing but organizing and projecting.",
            ),
            section(
                "relation",
                "## 为什么课程很多页最后都会回到 SA",
                "## Why So Many Course Topics Return to SA",
                body_zh="display 页在问信息怎么被看见，CRM 页在问信息怎么被团队共享，monitoring 页在问状态怎么被持续保持，spatial disorientation 页在问感官和仪表冲突时还能不能建立正确局面。它们本质上都在问：系统有没有帮人形成足够好的情境意识。",
                body_en="The display page asks how information becomes visible, the CRM page asks how information becomes shared across the team, the monitoring page asks how state awareness is sustained, and the spatial-disorientation page asks whether the operator can still build the correct picture when sensory intuition conflicts with instruments. At root they all ask whether the system helps people form sufficient SA.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="情境意识的核心不是“信息多”，而是“信息有没有被组织成可行动的理解和预测”。",
                note_body_en="The core of situation awareness is not “more information,” but whether information has been organized into understanding and prediction that support action.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "difficulty",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="看到数据并不等于形成 SA。很多事故正是发生在“数据都在眼前，但局面没真正被拼出来”的状态下。",
                body_en="Seeing the data does not mean SA has been achieved. Many accidents unfold in the state where the data is present but the situation has not actually been assembled in the operator’s mind.",
            )
        ],
        examples=[
            callout(
                "example",
                "difficulty",
                "案例：为什么“信息可见”还不够",
                "Example: Why “Visible Information” Is Still Not Enough",
                body_zh="一个机组可能看到了高度、速度和告警，却仍然没有意识到这些线索共同指向正在偏离的飞行状态。问题不在数据是否存在，而在这些数据有没有被整合成正确局面并转化成提前干预。",
                body_en="A flight crew may see altitude, speed, and alerts and still fail to realize that the signals collectively point to a diverging flight state. The issue is not whether the data exists, but whether it has been integrated into the right picture and converted into early intervention.",
            )
        ],
        summary_points_zh=[
            "SA 包括感知、理解和预测三层。",
            "信息可见不等于真正理解。",
            "很多 HFE 主题最后都会回到 SA 是否断裂。",
            "SA 的关键是形成可行动的 mental model。",
        ],
        summary_points_en=[
            "SA includes perception, comprehension, and projection.",
            "Visible information does not equal true understanding.",
            "Many HFE topics ultimately return to whether SA breaks down.",
            "The key is forming an actionable mental model.",
        ],
    ),
    "spatial_disorientation": page_blueprint(
        template_type="concept",
        page_intro_zh="空间定向错觉这一页最关键的提醒是：人的感觉系统在飞行环境里并不总可靠，直觉姿态和真实姿态可以完全相反。",
        page_intro_en="The central reminder of this page is that human sensory systems are not always reliable in flight; felt orientation and actual orientation can diverge completely.",
        core_question_zh="为什么人在飞行中会对自己的姿态产生强烈但错误的感觉，而系统又该怎样帮助操作者在这种错觉里仍然做出正确判断？",
        core_question_en="Why do people in flight develop strong but wrong bodily sensations about aircraft attitude, and how should the system help them still make correct judgments inside that illusion?",
        must_learn_points_zh=[
            "内耳和身体感觉在某些加速度、转弯和低可见度条件下会误导操作者。",
            "仪表通常比直觉更可靠，但压力和惊讶会降低人转向仪表的能力。",
            "空间定向问题是典型的“人的感觉系统和系统信息冲突”案例。",
            "有效控制要依赖训练、显示和程序，而不是临场意志力。",
        ],
        must_learn_points_en=[
            "Vestibular and bodily cues can mislead operators under certain acceleration, turning, and low-visibility conditions.",
            "Instruments are usually more reliable than bodily intuition, but stress and surprise can reduce the operator’s ability to shift to them.",
            "Spatial disorientation is a classic case of conflict between human sensing and system information.",
            "Effective control depends on training, displays, and procedure rather than on willpower in the moment.",
        ],
        memory_anchor_zh="先记住一句话：在空间定向错觉里，最危险的不是“没感觉”，而是“感觉非常真实，但其实错了”。",
        memory_anchor_en="Keep one sentence in mind: in spatial disorientation, the danger is not the absence of feeling, but the presence of a very convincing feeling that is nevertheless wrong.",
        sections=[
            section(
                "conflict",
                "## 感觉系统和仪表为什么会冲突",
                "## Why Sensory Systems and Instruments Conflict",
                body_zh="在某些飞行条件下，内耳和身体感觉会给出与真实姿态不一致的线索。此时仪表显示的是更可靠的状态信息，但人的直觉体验可能更强烈、更有说服力。",
                body_en="Under some flight conditions, vestibular and bodily cues provide signals that do not match the actual attitude. Instruments provide the more reliable state information, but the bodily experience may feel stronger and more convincing.",
            ),
            section(
                "danger",
                "## 为什么这种错觉会特别危险",
                "## Why This Illusion Becomes Especially Dangerous",
                body_zh="空间定向错觉危险，不只是因为它会让人看错，而是因为当事人往往非常相信自己的感觉。一旦操作者用错觉去解释仪表，就会快速进入错误控制循环。",
                body_en="Spatial disorientation is dangerous not only because it misleads perception, but because the person often trusts the sensation strongly. Once the operator uses that sensation to reinterpret the instruments, the control loop can deteriorate quickly.",
            ),
            section(
                "control",
                "## 系统怎样帮助人对抗这种错觉",
                "## How the System Helps Counter the Illusion",
                body_zh="有效控制不可能只靠当场“冷静一点”。更现实的防线包括：训练对错觉的预期、仪表扫描习惯、显示支持、程序化交叉检查和在高风险阶段对感官直觉保持怀疑。",
                body_en="Effective control cannot depend only on “stay calm in the moment.” More realistic defenses include training for anticipated illusions, disciplined instrument scan, display support, procedural cross-checking, and explicit suspicion toward bodily intuition in high-risk phases.",
                note_title_zh="一句话结论",
                note_title_en="One-Sentence Conclusion",
                note_body_zh="空间定向错觉的本质，是当感觉系统不可靠时，系统有没有提供足够强的替代路径让人回到正确判断。",
                note_body_en="The essence of spatial disorientation is whether the system offers a strong enough alternative path back to correct judgment when sensory intuition becomes unreliable.",
            ),
        ],
        warnings=[
            callout(
                "warning",
                "danger",
                "最容易误解的地方",
                "The Most Common Misunderstanding",
                body_zh="不要把空间定向问题理解成“飞行员再仔细一点就好”。错觉之所以危险，正是因为它对当事人来说极其真实。",
                body_en="Do not interpret spatial disorientation as something a pilot could solve merely by trying harder. The illusion is dangerous precisely because it feels deeply real to the person experiencing it.",
            )
        ],
        examples=[
            callout(
                "example",
                "control",
                "案例：为什么仪表扫描是对抗错觉的关键防线",
                "Example: Why Instrument Scan Is a Critical Defense Against Illusion",
                body_zh="当身体感觉告诉操作者飞机正在某个方向倾斜时，仪表扫描能提供一条结构化替代路径，把判断从主观感觉拉回系统信息。如果这条扫描习惯没建立，错觉就更容易主导动作。",
                body_en="When the body tells the operator that the aircraft is banking in a certain direction, instrument scan offers a structured alternative path that pulls judgment back to system information. If that scan habit is weak, the illusion more easily drives the action.",
            )
        ],
        summary_points_zh=[
            "空间定向错觉来自感觉系统与真实姿态的冲突。",
            "危险在于错觉往往非常真实。",
            "仪表、训练和程序是主要防线。",
            "这页是典型的人类感知与系统信息冲突案例。",
        ],
        summary_points_en=[
            "Spatial disorientation arises from conflict between sensory intuition and actual state.",
            "Its danger lies in how convincing the illusion feels.",
            "Instruments, training, and procedure are the primary defenses.",
            "This page is a classic case of conflict between human perception and system information.",
        ],
    ),
}

HUMAN_PERFORMANCE_CONTENT["attention_and_monitoring"]["sections"].extend(
    [
        section(
            "decrement",
            "## vigilance decrement 为什么不是主观懒散，而是任务规律",
            "## Why Vigilance Decrement Is a Task Pattern Rather Than Mere Laziness",
            body_zh="""
            vigilance decrement 最值得记住的一点，是它并不需要操作者态度很差才会出现。只要任务满足几个条件，它就会自然变脆：

            - 关键事件出现频率低
            - 大部分时间没有即时反馈
            - 操作者只能被动等待异常出现

            这说明监控衰退并不是道德问题，而是任务规律。设计如果假装不存在这条规律，就会把本来就难做的任务继续交给人硬扛。
            """,
            body_en="""
            The most important thing about vigilance decrement is that it does not require a poor attitude to appear. Once several task conditions exist, performance naturally becomes fragile:

            - critical events are rare
            - immediate feedback is weak most of the time
            - the operator mainly waits for abnormality to appear

            That means monitoring decay is not a moral problem; it is a task pattern. If design pretends this pattern does not exist, it hands an already fragile role back to the operator without support.
            """,
        ),
        section(
            "mitigation",
            "## 真正有效的监控支持通常长什么样",
            "## What Effective Monitoring Support Usually Looks Like",
            body_zh="""
            如果系统知道监控任务本身容易衰退，那么 mitigation 不应只停在“提醒更专心”。更成熟的支持通常包括：

            - 让状态变化更容易被 detect
            - 用更有意义的反馈告诉操作者系统是否正在偏离
            - 让团队内的交叉监控更容易启动
            - 在关键阶段减少无关负担，让注意资源不被噪声吞掉

            这也是为什么 monitoring 这页和 display、alert、automation 几页会反复互相连接。
            """,
            body_en="""
            If the system already knows that monitoring tasks decay, mitigation cannot stop at “pay closer attention.” More mature support usually includes:

            - making state changes easier to detect
            - using feedback that tells the operator whether the system is drifting
            - making cross-monitoring easier to trigger inside the team
            - reducing irrelevant burden during critical phases so attention is not consumed by noise

            That is also why the monitoring page keeps reconnecting to the display, alert, and automation pages.
            """,
        ),
    ]
)
HUMAN_PERFORMANCE_CONTENT["attention_and_monitoring"]["examples"].append(
    callout(
        "example",
        "mitigation",
        "案例：为什么“多看着点”不是一个完整 mitigation",
        "Example: Why “Watch More Carefully” Is Not a Complete Mitigation",
        body_zh="如果一个监控任务本身是低事件率、低反馈、长时持续的，那么要求操作者“更警觉”只能短期起作用。真正有用的改进通常是改变信号、反馈和协作结构，让问题更容易在正确时间被看见。",
        body_en="If a monitoring task is inherently low-event-rate, low-feedback, and long-duration, telling the operator to “stay more alert” can only help briefly. Stronger improvement usually changes the signals, feedback, and coordination structure so the problem becomes easier to detect at the right time.",
    )
)

HUMAN_PERFORMANCE_CONTENT["fatigue_and_sleep"]["sections"].extend(
    [
        section(
            "sleep_debt",
            "## 为什么 sleep debt 会让人比自己感觉中更差",
            "## Why Sleep Debt Can Make Performance Worse Than the Person Feels",
            body_zh="""
            疲劳最麻烦的地方之一，是主观体验和客观下降并不总同步。人可能觉得“还撑得住”，但反应速度、记忆稳定性和监控耐力已经明显下降。

            这也是为什么疲劳风险不能只靠自评。只要班次、夜班和睡眠债长期叠加，系统就不该假设操作者会准确知道自己还能否稳定完成高风险任务。
            """,
            body_en="""
            One of the hardest parts of fatigue is that subjective experience and objective decline do not always move together. People may feel that they are still functioning adequately while reaction speed, memory stability, and monitoring endurance have already degraded.

            That is why fatigue risk cannot rely only on self-report. Once shifts, night work, and sleep debt accumulate, the system should not assume the operator can accurately judge whether high-risk performance is still stable.
            """,
        ),
        section(
            "countermeasure",
            "## 疲劳管理真正应该落到哪些系统动作上",
            "## Which System Actions Real Fatigue Management Should Reach",
            body_zh="""
            课程讲 fatigue，不是为了给出健康建议，而是为了推动设计动作。真正有效的管理通常会落到：

            - 排班长度和轮转节奏
            - 夜班和清晨高风险任务的分配
            - 交接设计和关键任务前的状态确认
            - 必要时的二人确认、休息窗口或任务重分配

            一旦这些动作没有进入系统层，疲劳管理就很容易停留在“大家自己注意休息”的空话上。
            """,
            body_en="""
            The point of teaching fatigue is not to offer general wellness advice; it is to drive system action. Stronger management usually reaches:

            - shift length and rotation rhythm
            - allocation of high-risk tasks during night and early-morning windows
            - handoff design and state confirmation before critical work
            - where needed, two-person confirmation, rest windows, or task redistribution

            If those actions never move into the system layer, fatigue management easily stalls at the empty phrase “everyone should rest more.”
            """,
        ),
    ]
)
HUMAN_PERFORMANCE_CONTENT["fatigue_and_sleep"]["examples"].append(
    callout(
        "example",
        "countermeasure",
        "案例：为什么真正的 fatigue management 往往先改班次，不是先改态度",
        "Example: Why Real Fatigue Management Often Starts with Scheduling Rather Than Attitude",
        body_zh="如果夜班长度、交替节奏和关键任务安排本身就持续把人放在生理低谷窗口，那么再多个人层面的“注意保持状态”都只能补一小部分漏洞。真正强的控制，通常要先改排班和任务配置。",
        body_en="If shift length, rotation rhythm, and critical-task timing continually place people into physiological low points, then personal advice about maintaining alertness can only patch a small portion of the risk. Stronger control usually starts by changing scheduling and task allocation.",
    )
)
HUMAN_PERFORMANCE_CONTENT["fatigue_and_sleep"]["sections"].append(
    section(
        "microsleep",
        "## 为什么 microsleep 对高风险任务特别致命",
        "## Why Microsleep Is Especially Dangerous in High-Risk Tasks",
        body_zh="""
        fatigue 讨论里一个很关键但常被低估的点，是 microsleep。对当事人来说，它可能只是几秒的意识断裂；对系统来说，这几秒已经足够让监控、驾驶、核对或流程保持完全失守。

        这也是为什么疲劳风险不能只按“还能不能继续工作”去看，而要按任务类型去看。只要任务依赖持续监控、快速响应或精准时机，短暂掉线就已经可能构成高风险。
        """,
        body_en="""
        One critical but often underestimated part of fatigue is microsleep. To the individual it may feel like only a few seconds of broken awareness. To the system those seconds can be enough for monitoring, driving, verification, or procedural holding to fail completely.

        That is why fatigue cannot be judged only by whether the person can still continue working. It also has to be judged by task type. If the task depends on continuous monitoring, rapid response, or precise timing, even a brief lapse can already create high risk.
        """,
    )
)
HUMAN_PERFORMANCE_CONTENT["fatigue_and_sleep"]["sections"].append(
    section(
        "evidence",
        "## 为什么 fatigue 讨论要反复拿驾驶和医疗错误做证据",
        "## Why the Page Keeps Returning to Driving and Medical Error Evidence",
        body_zh="""
        课程反复拿疲劳驾驶和医疗错误做例子，不是为了堆统计数字，而是为了说明 fatigue 风险跨场景存在。只要任务依赖持续监控、及时判断和稳定执行，睡眠不足就会在非常不同的行业里表现出相似的脆弱性。

        这也是为什么 fatigue 不能被理解成某个行业的特殊难题。它更像一个底层限制，会穿透驾驶、医疗、航空和工业任务，把原本还能控制的任务窗口推向更高风险。
        """,
        body_en="""
        The course keeps returning to drowsy driving and medical error not to pile up statistics, but to show that fatigue risk generalizes across domains. Whenever a task depends on sustained monitoring, timely judgment, and stable execution, sleep loss creates similar vulnerability even in very different industries.

        That is why fatigue should not be understood as a niche problem for one sector. It behaves more like an underlying constraint that cuts across driving, medicine, aviation, and industrial work, pushing otherwise manageable task windows toward higher risk.
        """,
    )
)
HUMAN_PERFORMANCE_CONTENT["fatigue_and_sleep"]["inline_visuals"].extend(
    [
        visual(
            "evidence",
            "Sp26_Fatigue+Sleep_20260211.pdf",
            "这张图要看懂的是：疲劳驾驶不是抽象警告，而是已经在事故、伤亡和时间窗口上表现出稳定模式的现实风险。",
            "This figure should make one point concrete: drowsy driving is not an abstract warning. It is a real risk that already shows a stable pattern in crashes, injuries, and time-of-day windows.",
            asset_name_contains="page-04",
        ),
        visual(
            "countermeasure",
            "Sp26_Fatigue+Sleep_20260211.pdf",
            "这张图要看懂的是：疲劳管理真正有效时，会先改班次结构和连续工作时长，而不是只要求个人更努力扛住疲劳。",
            "This figure should show that strong fatigue management changes schedule structure and continuous-duty duration first, rather than only asking individuals to cope harder.",
            asset_name_contains="page-05",
        ),
    ]
)

HUMAN_PERFORMANCE_CONTENT["stress_and_decision_making"]["sections"].extend(
    [
        section(
            "closure",
            "## 为什么压力下最危险的是过早收束",
            "## Why Premature Closure Is One of the Biggest Dangers Under Stress",
            body_zh="""
            在高压力和高时间压力下，人不一定会立刻停工，相反常常会更快做出一个“足够可用”的解释。问题在于，这个解释很可能建立在过窄的信息搜索和过少的替代方案比较上。

            这就是 premature closure 的危险：人不是没有在想，而是太快停止继续想。
            """,
            body_en="""
            Under high stress and time pressure, people do not always freeze. Many instead form a “good enough” explanation very quickly. The danger is that the explanation may rest on a narrow search of information and too little comparison with alternatives.

            That is the risk of premature closure: the person is still thinking, but stops thinking further too early.
            """,
        ),
        section(
            "curve",
            "## 为什么压力和表现不是线性关系",
            "## Why the Relationship Between Stress and Performance Is Not Linear",
            body_zh="""
            这页一个很容易被忽略的点是：压力和表现不是简单的“压力越大越差”或“越忙越好”。在一定范围内，唤醒水平上升确实可能让人更专注；但一旦超过可承受区间，注意会缩窄、信息处理变慢、工作记忆和灵活调整一起下降。

            这也解释了为什么很多高压事故不是从“完全不会做”开始，而是从一开始还能撑住，随后迅速跨过临界点开始连锁失真。
            """,
            body_en="""
            One easy-to-miss point on this page is that stress and performance do not move in a simple straight line. Within a certain range, higher arousal can indeed sharpen focus. But once the level crosses a manageable band, attention narrows, information processing slows, and working memory plus flexibility degrade together.

            That also explains why many high-pressure failures do not begin with total incapacity. They begin with performance that initially looks acceptable and then quickly crosses a threshold into cascading distortion.
            """,
        ),
        section(
            "recovery",
            "## 为什么分心真正可怕的是让人丢掉中间状态",
            "## Why Distraction Is Dangerous Because It Destroys Intermediate State",
            body_zh="""
            分心不只是把注意力挪走几秒，更麻烦的是它会切断任务连续性。人一旦被打断，再回来时往往要重新找：我做到哪了、哪些步骤已经完成、哪些判断还没做。

            如果系统没有帮助保存这些中间状态，分心就很容易变成漏步、重复动作、错误顺序和错误确认。
            """,
            body_en="""
            Distraction is not only a temporary redirection of attention. The bigger problem is that it breaks task continuity. When people return, they often have to reconstruct where they were, which steps were completed, and which judgments remain unfinished.

            If the system does not preserve that intermediate state, distraction easily turns into omission, repeated action, sequence error, or wrong confirmation.
            """,
        ),
    ]
)
HUMAN_PERFORMANCE_CONTENT["stress_and_decision_making"]["examples"].append(
    callout(
        "example",
        "closure",
        "案例：为什么“很果断”有时只是很快收错",
        "Example: Why a Decision That Looks Decisive May Simply Be Fast Wrong Closure",
        body_zh="在压力场景里，一个快速明确的决定看起来像高水平表现，但如果它建立在很少的线索、没有第二视角和没有再核对，就可能只是更快地把错误解释固定下来。系统如果不能保留复核空间，果断本身就会变成风险放大器。",
        body_en="In a pressure-filled situation, a fast and explicit decision may look like strong performance. But if it rests on very few cues, no second perspective, and no cross-check, it may simply be a faster way to lock in the wrong explanation. If the system does not preserve review space, decisiveness itself can amplify risk.",
    )
)
HUMAN_PERFORMANCE_CONTENT["stress_and_decision_making"]["sections"].append(
    section(
        "team_buffer",
        "## 为什么团队缓冲能显著降低压力下的判断失真",
        "## Why Team Buffer Can Reduce Judgment Distortion Under Stress",
        body_zh="""
        压力下的错误不一定只能靠个人硬撑。很多时候，更有效的防线来自团队缓冲，例如第二视角、口头复述、短暂停顿、任务重分配和明确的 cross-check。

        这些做法的价值在于，它们能在高压时刻给人重新看一眼问题的机会。也就是说，系统不是假设个人一定不会收错，而是主动给决策留出被纠正的空间。
        """,
        body_en="""
        Errors under stress do not have to be managed only by asking the individual to cope harder. Many stronger defenses come from team buffer, such as a second perspective, verbal restatement, a brief pause, task redistribution, or an explicit cross-check.

        Their value is that they create another chance to look again at the problem under pressure. The system is therefore not assuming that the individual will never close too early. It is creating room for the decision to be corrected before it hardens.
        """,
    )
)
HUMAN_PERFORMANCE_CONTENT["stress_and_decision_making"]["inline_visuals"].extend(
    [
        visual(
            "chain",
            "Sp26_StressDecisionMaking_20260225.pdf",
            "这张图要看懂的是：高任务需求会同时带来注意收缩、分心、工作记忆下降和 SA 受损，所以压力问题从来不是单点能力下降。",
            "This figure should show that high task demand simultaneously drives attentional narrowing, distraction, working-memory loss, and degraded SA, which is why stress is never a single-capacity problem.",
            asset_name_contains="page-03",
        ),
        visual(
            "curve",
            "Sp26_StressDecisionMaking_20260225.pdf",
            "这张图要看懂的是：压力和表现之间更像一条带拐点的曲线，超过阈值后，继续加压不会带来更好表现，只会更快失真。",
            "This figure should show that stress and performance follow a curve with a turning point. Once the threshold is crossed, adding more pressure no longer improves performance and instead accelerates distortion.",
            asset_name_contains="page-04",
        ),
    ]
)

HUMAN_PERFORMANCE_CONTENT["situation_awareness"]["sections"].extend(
    [
        section(
            "model",
            "## 为什么 Endsley 模型把 SA 放在“决策之前、动作之后”这条链上",
            "## Why the Endsley Model Places SA on the Chain Between Environment, Decision, and Action",
            body_zh="""
            Endsley 模型的价值，不只是把 SA 分成三层，而是把它明确放到“环境输入 -> SA -> 决策 -> 动作 -> 反馈”这条链上。这样一来，SA 就不再是抽象心理状态，而是直接决定后续判断和动作质量的中间机制。

            这也解释了为什么课程里会把 workload、stress、automation 和 interface design 都接到 SA 上。它们不是在旁边“影响一下心情”，而是在改变人能否形成足够好的局面理解。
            """,
            body_en="""
            The value of the Endsley model is not only that it divides SA into three levels, but that it places SA explicitly on the chain of environment input, SA, decision, action, and feedback. That turns SA from an abstract mental state into an intermediate mechanism that directly shapes judgment and action quality.

            That also explains why the course connects workload, stress, automation, and interface design to SA. These factors are not merely influencing mood from the side. They are changing whether the person can form an adequate picture of the situation at all.
            """,
        ),
        section(
            "breakdowns",
            "## 三层 SA 断裂在实际分析里怎样分别出现",
            "## How the Three SA Breakdowns Appear in Real Analysis",
            body_zh="""
            这页最值得带走的，不只是三层定义，而是复盘时如何用它们定位断裂点：

            - 如果关键线索根本没被 notice，通常是 Level 1 问题
            - 如果线索被看见却被解释错，通常是 Level 2 问题
            - 如果当前状态理解得差不多，但未来走势判断错了，通常是 Level 3 问题

            一旦断裂层级被找准，后面的 mitigation 才不会乱：是改 detectability、改 mental model 支持，还是改 projection 支持。
            """,
            body_en="""
            The most useful takeaway is not only the three-layer definition, but how to use the layers during review:

            - if the critical cue was never noticed, the breakdown is often Level 1
            - if the cue was seen but interpreted wrongly, the breakdown is often Level 2
            - if current state was understood reasonably well but the future path was predicted badly, the breakdown is often Level 3

            Once the break layer is identified, mitigation becomes far more targeted: improve detectability, improve mental-model support, or improve projection support.
            """,
        ),
        section(
            "team_sa",
            "## 为什么 SA 不只是个人状态，也可能是团队状态",
            "## Why SA Is Not Only an Individual State but Also a Team State",
            body_zh="""
            课程后半段会反复出现一个提醒：即使每个人都各自看见了一部分信息，团队仍然可能没有形成共享局面。也就是说，个人 SA 和 team SA 之间并不自动相等。

            这时问题就不再只在显示，而也在沟通、briefing、cross-check 和权限结构上。团队有没有把分散线索重新拼成同一个 picture，这往往决定了后续动作是否一致。
            """,
            body_en="""
            Later in the course a recurring reminder appears: even if individuals each notice part of the information, the team may still fail to form one shared picture. Individual SA and team SA are therefore not automatically the same thing.

            At that point the problem is no longer only in the display. It also belongs to communication, briefing, cross-check, and authority structure. Whether the team rebuilds one common picture from distributed cues often determines whether later action becomes coordinated.
            """,
        ),
    ]
)
HUMAN_PERFORMANCE_CONTENT["situation_awareness"]["examples"].append(
    callout(
        "example",
        "team_sa",
        "案例：为什么团队里每个人都看见一点，不等于团队真的知道发生了什么",
        "Example: Why “Everyone Saw a Piece of It” Does Not Mean the Team Understood the Situation",
        body_zh="一个人可能看到速度异常，另一个人注意到告警，第三个人知道程序状态变化，但如果这些线索没有被及时拼成共享局面，团队仍然可能继续沿着错误判断走下去。SA 的关键不是线索分散存在，而是线索有没有被组织成同一 picture。",
        body_en="One person may notice the speed anomaly, another the alert, and a third the procedure-state change, yet the team can still continue along the wrong path if those cues are never assembled into one shared picture. The key to SA is not whether cues exist in distributed form, but whether they are organized into one coherent picture.",
    )
)
HUMAN_PERFORMANCE_CONTENT["situation_awareness"]["sections"].append(
    section(
        "update",
        "## 为什么 SA 还要看 picture 更新得够不够快",
        "## Why SA Also Depends on How Fast the Picture Gets Updated",
        body_zh="""
        SA 不是静态拥有一张 picture，而是要不断更新 picture。高风险系统里，状态经常在变，如果团队还停留在几分钟前的理解，就算当时理解过也可能已经落后于系统现实。

        所以 SA 分析不能只问“有没有建立 picture”，还要问“picture 更新速度够不够快”。很多事故不是从完全不知道开始，而是从来不及把旧 picture 替换成新 picture 开始。
        """,
        body_en="""
        SA is not the static possession of one picture. It is the continuous updating of that picture. In high-risk systems the state keeps changing, and if the team is still operating from the understanding of a few minutes earlier, the picture may already be stale even if it was once correct.

        SA analysis therefore cannot ask only whether a picture existed. It also has to ask whether the picture was updated quickly enough. Many events do not begin with total ignorance, but with failure to replace the old picture in time.
        """,
    )
)
HUMAN_PERFORMANCE_CONTENT["situation_awareness"]["inline_visuals"].extend(
    [
        visual(
            "model",
            "Sp26_SituationAwareness_20260325.pdf",
            "这张图要看懂的是：SA 不是孤立状态，它夹在环境输入、决策和动作之间，前面受显示与负荷影响，后面直接影响行为结果。",
            "This figure should show that SA is not an isolated state. It sits between environmental input, decision, and action, shaped upstream by displays and workload and shaping downstream behavior directly.",
            asset_name_contains="page-03",
        ),
        visual(
            "layers",
            "Sp26_SituationAwareness_20260325.pdf",
            "这张图要看懂的是：Level 1、2、3 不是三个平行标签，而是从看见线索、理解局面到预测走势的一条递进链。",
            "This figure should show that Levels 1, 2, and 3 are not parallel labels. They are a progression from noticing cues, to understanding the situation, to projecting where it is going.",
            asset_name_contains="page-04",
        ),
    ]
)

HUMAN_PERFORMANCE_CONTENT["spatial_disorientation"]["sections"].extend(
    [
        section(
            "mechanism",
            "## 为什么空间定向错觉首先是一个生理机制问题",
            "## Why Spatial Disorientation Starts as a Physiological Mechanism Problem",
            body_zh="""
            空间定向错觉不是单纯“心理感觉不准”，它首先是一个生理机制问题。内耳和前庭系统在加速度、转弯和低外部参照条件下，本来就可能给出和真实姿态不一致的信号。

            这意味着错觉不是个别人偶尔主观想错，而是人的感觉系统在特定环境下确实存在系统性失真。理解这一层之后，才会知道为什么仪表和程序必须成为主参考系。
            """,
            body_en="""
            Spatial disorientation is not merely a vague psychological feeling. It starts as a physiological mechanism problem. Under acceleration, turning, and low external-reference conditions, the inner ear and vestibular system can legitimately produce signals that do not match the actual aircraft attitude.

            That means the illusion is not a random personal mistake. It is a systematic distortion that can emerge from the sensing system itself under specific conditions. Once that is understood, the need for instruments and procedure as the main reference becomes much clearer.
            """,
        ),
        section(
            "illusion_strength",
            "## 为什么这类错觉特别难靠主观意志克服",
            "## Why This Type of Illusion Is So Hard to Overcome by Willpower Alone",
            body_zh="""
            空间定向错觉的难点不在于“理论上知道会发生”，而在于当它真的发生时，身体感觉会非常强，甚至比仪表信息更像“真相”。人在这种状态下不是故意忽视仪表，而是主观体验本身在和系统信息竞争。

            所以这页不断强调程序、仪表扫描和训练，是因为这些外部结构必须足够强，才能压过错觉带来的主观确定感。
            """,
            body_en="""
            The difficulty of spatial disorientation is not merely knowing in theory that it can happen. When it actually happens, the bodily sensation can feel so compelling that it appears more truthful than the instrument indications. The person is not deliberately ignoring the instruments; subjective experience is actively competing with system information.

            That is why the page keeps returning to procedure, instrument scan, and training. Those external structures must be strong enough to override the false certainty created by the illusion.
            """,
        ),
        section(
            "design_link",
            "## 为什么这页最终还是会回到显示和程序设计",
            "## Why This Page Ultimately Returns to Display and Procedure Design",
            body_zh="""
            只要人的感官在某些情境下会失真，系统就必须准备替代路径。这条替代路径通常不是一句“相信仪表”，而是更具体的支持：

            - 仪表状态是否足够容易扫读
            - 关键阶段是否有固定 cross-check 程序
            - 培训是否让人提前预期错觉类型
            - 团队成员是否能在异常时帮助彼此回到仪表

            这也说明空间定向错觉并不是孤立专题，而是把 perception、display、procedure 和 CRM 连在一起的综合页。
            """,
            body_en="""
            Once it is accepted that human sensation can distort under certain conditions, the system has to provide an alternate path. That alternate path is more concrete than the phrase “trust the instruments.” It includes support such as:

            - whether the instrument state is easy enough to scan quickly
            - whether fixed cross-check procedure exists for critical phases
            - whether training has already normalized the expected illusion types
            - whether team members can help one another return to instrument-based control

            That is why spatial disorientation is not an isolated topic. It connects perception, display, procedure, and CRM into one integrated page.
            """,
        ),
    ]
)
HUMAN_PERFORMANCE_CONTENT["spatial_disorientation"]["examples"].append(
    callout(
        "example",
        "illusion_strength",
        "案例：为什么“我明明感觉飞机在转”本身就可能是风险信号",
        "Example: Why “I Clearly Feel the Aircraft Turning” Can Itself Be a Risk Signal",
        body_zh="在空间定向错觉里，最危险的不是完全没感觉，而是感觉异常确定。当操作者非常确信自己的身体感受时，反而更可能去怀疑仪表。这正是为什么课程反复强调：越强烈的主观确定感，有时越需要更强的仪表纪律和程序约束。",
        body_en="In spatial disorientation, the dangerous state is not feeling nothing. It is feeling something with great certainty. When the operator becomes highly convinced by bodily sensation, the instruments are more likely to be doubted. That is why the course repeatedly emphasizes that the stronger the subjective certainty, the stronger the need for instrument discipline and procedural support.",
    )
)
HUMAN_PERFORMANCE_CONTENT["spatial_disorientation"]["sections"].append(
    section(
        "transition",
        "## 为什么从主观感觉重新切回仪表读取这么难",
        "## Why the Transition Back from Bodily Sensation to Instrument Reading Is So Hard",
        body_zh="""
        空间定向错觉里最难的瞬间，往往不是第一次出现异常感觉，而是已经产生强烈感觉之后，要把控制重新交回仪表。这个切换之所以难，是因为人需要在几乎不相信自己身体的前提下继续行动。

        也因此，训练和程序设计的重点不能只停在“知道有错觉”，还要让操作者提前练习这类切换动作。真正关键的是在高压和高确定感下，仍然能回到外部参考系。
        """,
        body_en="""
        In spatial disorientation, the hardest moment is often not the first appearance of an abnormal sensation, but the later moment when control has to be handed back to the instruments despite the sensation feeling convincing. The transition is hard because the person has to continue acting while no longer trusting the body as the main reference.

        That is why training and procedure cannot stop at merely teaching that illusions exist. Operators need practice in making this transition itself. The real challenge is returning to the external reference system under both pressure and false certainty.
        """,
    )
)
HUMAN_PERFORMANCE_CONTENT["spatial_disorientation"]["inline_visuals"].extend(
    [
        visual(
            "mechanism",
            "Sp26_SpDisorientation_20260330.pdf",
            "这张图要看懂的是：空间定向错觉不是抽象概念，它和内耳结构、半规管等具体生理通道直接相关。",
            "This figure should show that spatial disorientation is not an abstract idea. It connects directly to concrete physiology such as the inner ear and semicircular canals.",
            asset_name_contains="page-02",
        ),
        visual(
            "mechanism",
            "Sp26_SpDisorientation_20260330.pdf",
            "这张图要看懂的是：前庭系统本来就是姿态与运动感的重要来源，所以一旦它被误导，主观感觉会非常有说服力。",
            "This figure should show that the vestibular system is a primary source of motion and attitude sensation, which is why its distortion can feel so convincing to the operator.",
            asset_name_contains="page-03",
        ),
    ]
)

HUMAN_PERFORMANCE_CONTENT["attention_and_monitoring"]["sections"].append(
    section(
        "supervisory",
        "## 为什么监控任务常常出现在“监督式控制”而不是手动控制里",
        "## Why Monitoring Problems Often Appear in Supervisory Rather Than Manual Control",
        body_zh="""
        课程里会把 attention 和 automation 放到一起讲，是因为人最容易在监督式控制里滑向被动监视者。系统越稳定、越自动，人越容易从持续操作者变成偶尔插手的监督者。

        这类角色迁移本身就会提高 vigilance decrement 和 complacency 风险。也就是说，注意问题并不是单纯心理学问题，它经常是角色设计问题。
        """,
        body_en="""
        The course keeps attention and automation together because people are especially likely to drift into passive supervision under supervisory control. The more stable and automatic the system feels, the easier it is for the operator to move from active controller to occasional overseer.

        That role migration itself increases vigilance-decrement and complacency risk. In other words, attention is not only a psychology problem. It is often a role-design problem.
        """,
    )
)
HUMAN_PERFORMANCE_CONTENT["attention_and_monitoring"]["inline_visuals"].extend(
    [
        visual(
            "supervisory",
            "Attention and Monitoring 2-9- 2026.pdf",
            "这张图要看懂的是：从手动控制到全自动控制，人的位置不是简单消失，而是逐步被推向监督式角色，而这正是监控脆弱性最常出现的地方。",
            "This figure should show that as control shifts from manual toward full automation, the human does not simply disappear. The role is pushed toward supervision, which is exactly where monitoring vulnerability often grows.",
            asset_name_contains="page-03",
        ),
        visual(
            "limits",
            "Attention and Monitoring 2-9- 2026.pdf",
            "这张图要看懂的是：注意并不是单独一块能力，它嵌在从感知、认知到动作的整个信息处理链里，所以任何一环的负担都会回头影响监控表现。",
            "This figure should show that attention is not one isolated faculty. It sits inside the full chain from perception to cognition to action, so burden at any stage feeds back into monitoring performance.",
            asset_name_contains="page-04",
        ),
    ]
)
