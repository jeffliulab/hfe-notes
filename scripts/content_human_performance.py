from __future__ import annotations

from note_blueprints import callout, formalize_blueprint, page_blueprint, section


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

HUMAN_PERFORMANCE_CONTENT = {
    slug: formalize_blueprint(blueprint) for slug, blueprint in HUMAN_PERFORMANCE_CONTENT.items()
}
