from __future__ import annotations

from textwrap import dedent


def pair(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": dedent(zh).strip(),
        "en": dedent(en).strip(),
    }


HUMAN_PERFORMANCE_CONTENT: dict[str, dict[str, str]] = {
    "attention_and_monitoring": pair(
        """
        ## 一眼看懂

        注意与监控这一页的核心不是“人要更专心”，而是承认注意本来就是有限资源，而持续监控又恰好是一种最容易衰退的任务。

        ## 核心逻辑

        - 注意不是无限的，它会被优先级、负荷、时间、疲劳和告警策略重新分配。
        - 监控任务看起来轻松，但因为刺激稀少、事件低频，反而容易出现 vigilance decrement。
        - 自动化越强，人越容易从主动操作者退成被动监视者，这时 complacency 风险会上升。

        ## 这页真正想建立的判断

        如果某个系统要求人长时间“盯着看、等着出问题”，就要立刻追问：

        - 这个监控任务是否现实可持续
        - 系统有没有主动帮助人保持对关键状态的把握
        - 一旦漏看，是否还留有恢复空间

        ## 难点讲解

        监控失败并不等于态度差。很多时候，失败来自任务本身的设计：太单调、太被动、反馈太少、关键变化出现得太突然。这也是为什么显示、告警和自动化设计必须和“人的注意机制”一起看。
        """,
        """
        ## At a Glance

        The point of this topic is not simply that people should pay more attention. Attention is limited, and sustained monitoring is one of the most fragile task types.

        ## Core Logic

        - attention is redistributed by priority, workload, time, fatigue, and alert strategy
        - monitoring tasks are vulnerable because low-event environments produce vigilance decrement
        - stronger automation often shifts humans toward passive supervision, increasing complacency risk

        ## What To Ask

        If a system expects long periods of watchful waiting, ask whether that monitoring task is realistically sustainable and whether the system helps preserve awareness and recovery.

        ## Common Difficulty

        Monitoring failure is often a design problem rather than a character flaw. Monotony, low feedback, and sudden state changes all work against sustained attention.
        """,
    ),
    "fatigue_and_sleep": pair(
        """
        ## 一眼看懂

        疲劳与睡眠这一页想说明：疲劳不是“有点累”的主观感受，而是会系统性影响反应速度、工作记忆、判断、监控和恢复能力的生理约束。

        ## 这页最重要的主线

        - 睡眠不足会让人表现得像“还能工作”，但很多关键认知功能已经下降。
        - 生理节律会改变不同时间段的风险水平，所以同样任务在不同班次上并不等价。
        - 疲劳管理不能只靠个体意志，因为排班、任务长度、夜班节律和组织要求本身就在制造疲劳。

        ## 为什么这页对 HFE 很关键

        人因工程如果只讲界面和流程，却不讲疲劳，就会默认人总能稳定发挥。课程其实是在提醒你：

        - 再好的程序也要经过疲劳中的人来执行
        - 再好的告警也要经过困倦中的人来察觉
        - 再好的培训也会被持续睡眠不足削弱

        ## 难点讲解

        很多人会把 fatigue management 理解成“提醒大家多休息”。这太弱了。更成熟的做法是把疲劳看作系统设计变量，例如：

        - 排班与轮班策略
        - 关键任务的时段安排
        - 交接设计
        - 高风险时段的辅助检查和双重确认
        """,
        """
        ## At a Glance

        Fatigue is not merely a feeling of tiredness. It is a physiological constraint that degrades reaction time, working memory, judgment, monitoring, and recovery.

        ## Core Message

        - sleep loss can leave people functional enough to continue working while quietly degrading important cognitive abilities
        - circadian rhythm changes the risk profile across time of day
        - fatigue management cannot rely only on personal willpower because schedules, task length, and night work generate fatigue systemically

        ## Why It Matters

        Interfaces, procedures, and training are all filtered through a fatigued human operator. That makes fatigue a system-design issue, not just a personal habit issue.

        ## Common Difficulty

        Telling people to rest more is not enough. Stronger approaches treat fatigue as a design variable in scheduling, task timing, handoff design, and high-risk cross-checking.
        """,
    ),
    "stress_and_decision_making": pair(
        """
        ## 一眼看懂

        压力、决策与分心这一页讲的是：人在高负荷下不是简单“变差”，而是会把注意和策略缩窄到更少的选项上，于是更容易看漏、想偏、决策过快或者过慢。

        ## 这页的核心链条

        - 压力会占用认知资源，缩窄搜索范围。
        - 分心会打断计划执行，让人更容易漏步、跳步或失去时间线。
        - 时间压力会推动启发式判断和 satisficing，而不是完整比较。

        ## 读这页时最重要的判断

        当一个环境又快、又乱、又有后果时，要问的不是“为什么操作者不更冷静”，而是：

        - 系统有没有帮他保留关键线索
        - 决策空间是不是被组织或界面压得太窄
        - 团队、程序和告警有没有减轻负担，而不是继续加码

        ## 难点讲解

        压力不总会导致错误，有时还会暂时提升警觉；真正危险的是过高压力、持续时间过长、信息又不完整时，操作者开始依赖最熟悉的路径，忽略不符合预期的新线索。这也是很多复杂事件里“明明看到了信息却没用上”的根源。
        """,
        """
        ## At a Glance

        Stress, decision making, and distraction are linked because high-load environments narrow attention and strategy space, making omission, bias, and poor timing more likely.

        ## Core Chain

        - stress consumes cognitive capacity and narrows search
        - distraction interrupts execution and weakens timeline tracking
        - time pressure pushes people toward heuristics and satisficing

        ## What To Ask

        In a fast, messy, high-consequence environment, the question is not only why the operator was not calmer. It is whether the system preserved the right cues, left enough decision space, and reduced rather than added burden.

        ## Common Difficulty

        Stress does not always cause failure, but high and sustained stress combined with incomplete information often drives people toward familiar responses while important new cues get underweighted.
        """,
    ),
    "situation_awareness": pair(
        """
        ## 一眼看懂

        情境意识不是“对周围有感觉”这么模糊的东西。课程里讲的 SA 更具体，它至少包含三层：先感知到信息，再理解它意味着什么，最后预测接下来会发生什么。

        ## 三层结构怎么理解

        1. `perception`：你有没有看到、听到、读到关键线索。
        2. `comprehension`：你有没有把这些线索拼成正确的当前局面。
        3. `projection`：你能不能预判如果不干预，系统接下来会走向哪里。

        ## 为什么很多人会卡在第二层和第三层

        因为系统里“信息可见”不代表“关系清楚”。操作者可能看到了读数和告警，但：

        - 不知道哪条信息优先级更高
        - 不知道多个信号如何组合解释
        - 不知道当前状态会在未来几十秒或几分钟里演化成什么

        所以 SA 的本质不是信息量，而是信息结构。

        ## 难点讲解

        课程里很多页面都在回到情境意识问题。显示设计、CRM、监控、自动化、空间定向，最后都在问：系统有没有帮助人形成足够准确、足够及时、足够可预测的 mental model。
        """,
        """
        ## At a Glance

        Situation awareness is not a vague sense of being aware. In the course it has a three-level structure: perceive the cues, comprehend what they mean, and project what will happen next.

        ## The Three Levels

        1. `perception`: noticing the relevant signals
        2. `comprehension`: combining them into an accurate understanding of the current state
        3. `projection`: anticipating how the state will evolve

        ## Why Higher Levels Are Hard

        Information can be visible without being interpretable. Operators may see numbers and alerts yet still lack priority, relationship, or future-state understanding.

        ## Common Difficulty

        Many course topics return to situation awareness because displays, CRM, monitoring, automation, and spatial disorientation all ask whether the system helps build a timely and accurate mental model.
        """,
    ),
    "spatial_disorientation": pair(
        """
        ## 一眼看懂

        空间定向错觉这页最关键的提醒是：人的感觉系统在飞行环境里并不总可靠。也就是说，“我感觉飞机是这样”的直觉，可能和真实姿态完全不一致。

        ## 这页的核心矛盾

        - 内耳和身体感觉在某些加速度、转弯和低可见度条件下会给出错误线索。
        - 仪表提供的是更可靠的状态信息，但人在压力、惊讶或训练不足时，未必能及时切回仪表。
        - 一旦操作者更相信身体感觉而不是仪表，风险会迅速放大。

        ## 这页真正想建立的认知

        空间定向问题不是单纯的“飞行技术失误”，而是一个典型的人因冲突：

        - 人的感觉系统在某些环境下天然会误导
        - 系统设计和训练必须提前承认这种误导
        - 仪表扫描、程序和训练就是为了在直觉不可靠时给出替代路径

        ## 难点讲解

        最难的地方在于，这类错觉对当事人来说往往极其真实。所以有效控制不能只依赖事发当下的“再冷静一点”，而要依赖更早期的训练、显示设计和程序化交叉检查。
        """,
        """
        ## At a Glance

        The key lesson in spatial disorientation is that human sensory intuition can be unreliable in flight. The felt motion of the aircraft may not match its actual state.

        ## Core Conflict

        - vestibular and bodily cues can become misleading under specific acceleration, turning, and visibility conditions
        - instruments provide more reliable state information, but people do not always shift to them quickly under surprise or stress
        - risk escalates when bodily sensation is trusted over instrument information

        ## Why It Matters

        Spatial disorientation is a classic human-factors conflict: human sensing can mislead, so design, training, and procedure must explicitly compensate for that weakness.

        ## Common Difficulty

        These illusions often feel compelling to the person experiencing them. That is why effective control depends on prior training, display support, and procedural cross-checking rather than willpower alone.
        """,
    ),
}
