from __future__ import annotations

from textwrap import dedent


def pair(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": dedent(zh).strip(),
        "en": dedent(en).strip(),
    }


FOUNDATIONS_CONTENT: dict[str, dict[str, str]] = {
    "course_overview": pair(
        """
        ## 一眼看懂

        这门课不是把“人会犯错”当成终点，而是把航空、医疗器械和自动化系统放在一起看：当任务、界面、组织、程序与环境互相作用时，系统为什么会变脆弱。

        ## 课程主线

        1. 先用人因工程和 human error 框架建立共同语言。
        2. 再用调查、任务分析、URRA 等方法把“问题”写成可分析对象。
        3. 然后进入航空、自动化与医疗器械场景，看方法怎样落到真实工作流。
        4. 最后通过案例与伦理讨论，回到“组织怎样制造或放大风险”。

        ## 学这页时最重要的事

        - 课程的基本单位不是“单个操作者”，而是“人在系统里的位置”。
        - 后面的所有方法页，本质上都在回答三个问题：任务是什么、哪里会失败、系统怎样把失败挡住或放大。
        - 如果你先抓住这条主线，后面读 Swiss Cheese、task analysis、URRA 时会更容易串起来。
        """,
        """
        ## At a Glance

        This course treats human factors as a systems problem rather than a collection of isolated operator mistakes. Aviation, medical devices, and automation are used as recurring application domains.

        ## Course Arc

        1. Build shared language through human factors and human error frameworks.
        2. Turn that language into methods such as investigation, task analysis, and URRA.
        3. Apply the methods in aviation, automation, and medical-device contexts.
        4. End with cases and ethics, where organizational choices shape risk.

        ## What To Keep In Mind

        - The recurring unit of analysis is the person-in-system relationship.
        - Later method pages answer three questions: what the task is, where failure can emerge, and how the system blocks or amplifies it.
        - If this logic is clear, the rest of the site becomes much easier to navigate.
        """,
    ),
    "human_factors_intro": pair(
        """
        ## 一眼看懂

        人因工程不是“研究人类弱点”的学科，而是把人的能力、限制、节律、记忆和注意特性带回设计中，让系统更容易被正确使用。

        ## 这个主题真正想说什么

        - 人因工程同时追求两个目标：人的福祉与系统绩效。
        - 重点不是把人从系统里拿掉，而是承认人永远在系统里，于是设计必须适配真实的人。
        - 所谓“设计得好”，不是让专家勉强能用，而是让普通用户在压力、疲劳、分心时依然不容易出错。

        ## 难点讲解

        很多人会把人因工程理解成“培训做得更好一点”。这其实太窄了。培训当然重要，但人因工程更关心的是：

        - 界面是否直观
        - 信息是否在正确时间出现
        - 任务步骤是否符合人的认知顺序
        - 系统是否允许人恢复、检查和纠正

        换句话说，人因工程优先改系统，而不是先责怪使用者。
        """,
        """
        ## At a Glance

        Human factors is not mainly about cataloging human weakness. It is about designing systems around real human capabilities, limits, rhythms, memory, and attention.

        ## The Core Message

        - Human factors has dual goals: human well-being and system performance.
        - The discipline assumes people remain part of the system, so design must fit real users rather than idealized users.
        - Good design is not merely expert-usable; it remains usable under stress, fatigue, and distraction.

        ## Why This Matters

        Training matters, but human factors is broader than training. It asks whether interfaces, timing, workflows, and recovery opportunities are designed to support correct action in the first place.
        """,
    ),
    "human_error_frameworks": pair(
        """
        ## 一眼看懂

        “人为失误框架”这页的重点，不是给错误贴标签本身，而是教你不要把所有问题都压缩成“某个人犯错了”。框架的作用，是把失误拆成不同层次，再决定应该改人、改任务，还是改系统。

        ## 先把几类错误分清楚

        - `slip`：计划是对的，但动作做错了。典型场景是按错、点错、操作顺序打滑。
        - `lapse`：计划是对的，但动作漏掉了，常和记忆或注意脱落有关。
        - `mistake`：执行并没有错，错的是前面的判断、理解或计划。
        - `violation`：明知规则却主动偏离，通常不能直接算作 error taxonomy 里的“无意失误”。

        ## 这套框架为什么重要

        课程里反复对比 old view 和 new view：

        - old view 把人看成“坏苹果”，认为系统本身是好的，问题在操作者
        - new view 认为错误是系统与情境共同产生的结果，重点是修系统、加防护、改善恢复能力

        所以同样是一个不良后果，框架不同，改进方向会完全不同。

        ## 难点讲解

        最容易混淆的地方，是把“内部因素”和“外部因素”看成二选一。其实课程想强调的是：

        - 人当然有认知、情绪和体力限制
        - 但系统设计、信息质量、培训、组织文化和外部压力，同样会塑造错误

        真正成熟的分析不会停在“这个人注意力不够”，而会继续追问：为什么这个系统要求人在这种条件下还必须靠纯注意力顶住？

        ## 读图时要抓住什么

        如果你在本页看到“感知-认知-动作”的图，不要把它当装饰。它在提醒你：错误不是一个点，而是信息进入、理解形成、动作输出整条链路中的失配。
        """,
        """
        ## At a Glance

        The point of a human error framework is not merely to label failure. It is to prevent every bad outcome from collapsing into “the operator made a mistake.”

        ## Core Categories

        - `slip`: the plan is correct, but the execution is wrong.
        - `lapse`: the plan is correct, but the action is omitted, often because memory or attention drops out.
        - `mistake`: execution is faithful, but the judgment or plan is wrong.
        - `violation`: a deliberate deviation from a rule, which is analytically different from unintended error.

        ## Why Frameworks Matter

        The course contrasts an old view and a new view:

        - the old view blames the individual as the faulty element
        - the new view asks how system design, context, and defenses shaped the failure

        The same event can therefore lead to very different interventions depending on the framework you use.

        ## Common Difficulty

        Internal and external explanations are not opposites. Human limits are real, but design, information quality, training, organizational culture, and time pressure also shape error production.
        """,
    ),
    "swiss_cheese": pair(
        """
        ## 一眼看懂

        Swiss Cheese 模型想表达的不是“系统有洞”这么简单，而是事故往往不是一次失败造成的，而是多层防线同时失效、漏洞在同一时刻对齐之后，风险才真正穿透到伤害。

        ## 这张模型图在说什么

        - 每一层 cheese 都代表一道防线，比如设计、程序、培训、监测、组织管理
        - 每一层上的 hole 代表局部弱点，它们可能长期存在却暂时没有造成后果
        - 当多层弱点刚好连成一条路径时，事故轨迹就会穿透整个系统

        ## 为什么它能改变分析思路

        这套模型最大的价值，是把关注点从“谁在最后一步犯错”转移到“为什么前面那么多层都没有拦住”。也就是说：

        - 事故调查不应只盯 front line
        - latent conditions 往往比最后一击更值得改
        - 系统越高风险，就越不能把安全押在单层防护上

        ## 难点讲解

        很多人会把 Swiss Cheese 理解成“只要多加几层流程就安全了”。这不够。层数本身不是关键，关键是：

        - 每层是否真的独立
        - 每层是否可检测、可恢复
        - 当某一层失效时，下一层是否还有足够时间接住
        """,
        """
        ## At a Glance

        The Swiss Cheese model says accidents usually emerge when multiple imperfect defenses fail together rather than from a single isolated mistake.

        ## How To Read The Model

        - each layer is a defense such as design, procedure, training, or supervision
        - each hole is a weakness that may exist long before harm occurs
        - harm appears when holes align across multiple layers

        ## Why It Matters

        The model shifts attention away from the final operator and toward upstream design, management, and organizational contributors. The key question becomes: why did every earlier barrier fail to intercept the problem?

        ## Common Difficulty

        Safety does not come from adding more layers by itself. It comes from having defenses that are meaningfully different, observable, and capable of catching one another's failures.
        """,
    ),
}
