from __future__ import annotations

from textwrap import dedent


def pair(zh: str, en: str) -> dict[str, str]:
    return {
        "zh": dedent(zh).strip(),
        "en": dedent(en).strip(),
    }


MEDICAL_DEVICES_CONTENT: dict[str, dict[str, str]] = {
    "iso_14971": pair(
        """
        ## 一眼看懂

        ISO 14971 不是一张表，而是一整套医疗器械风险管理语言。它要求团队持续识别 hazard、hazardous situation 和 harm，并把控制、验证与上市后反馈接成闭环。

        ## 先把几个容易混的词分开

        - `hazard`：潜在伤害源
        - `hazardous situation`：人或环境暴露在 hazard 下的具体情境
        - `harm`：真正发生的不良影响

        这三个词不分清，后面的风险文件几乎都会写乱。

        ## 标准的流程框架

        1. 建立风险管理计划
        2. 识别危害与可预见使用场景
        3. 估计并评价风险
        4. 实施风险控制
        5. 验证剩余风险与整体可接受性
        6. 用生产和上市后信息持续回看

        ## 难点讲解

        学 ISO 14971 最容易误解的地方，是把它看成“法规文书工作”。其实它真正的价值，是强迫团队用一致的语言把设计、临床、使用和伤害后果连起来。人因工作之所以重要，就是因为很多 hazardous situation 正是由使用路径触发的。
        """,
        """
        ## At a Glance

        ISO 14971 is not just a table format. It is the language and process framework for medical-device risk management.

        ## Three Terms To Separate

        - `hazard`: a potential source of harm
        - `hazardous situation`: the circumstance in which people or property are exposed to that hazard
        - `harm`: the actual injury or damage

        ## Process Logic

        1. plan risk management
        2. identify hazards and foreseeable use situations
        3. estimate and evaluate risk
        4. implement controls
        5. judge residual risk
        6. feed post-production information back into the system

        ## Why It Matters

        The standard is valuable because it forces consistent reasoning across design, use, and clinical consequence. Human-factors work matters here because many hazardous situations arise through use.
        """,
    ),
    "medical_device_urra": pair(
        """
        ## 一眼看懂

        医疗器械场景下的 URRA，比一般风险分析更强调“使用情境是否可预见”“任务是否 critical”“错误是否会通向病人伤害”，因为这里的后果往往直接落在患者安全上。

        ## 这页最重要的三个连接

        - 从任务分析连接到 critical task
        - 从 use error 连接到 hazardous situation 与 harm
        - 从 harm 再连接回界面、标签、IFU、培训与物理设计控制

        ## 为什么医疗器械里的 URRA 更严格

        - 使用者不一定是专家
        - 使用环境可能嘈杂、紧急、光线差或时间极紧
        - 病人状态会放大错误后果
        - 监管要求你证明风险识别和控制逻辑是完整、可追踪、可验证的

        ## 难点讲解

        很多团队会把 control 写成“培训用户”。这往往不够。课程里更想强调的是：如果界面、器械形态、信息呈现本身可以改，就不应该把主要风险压给培训和注意力。
        """,
        """
        ## At a Glance

        URRA in medical devices is stricter than a generic use-risk exercise because use conditions, critical tasks, and harm pathways directly affect patient safety.

        ## Three Key Connections

        - task analysis into critical task identification
        - use error into hazardous situation and harm
        - harm back into interface, labeling, IFU, training, and physical design controls

        ## Common Difficulty

        Teams often overuse “training” as the main control. The course pushes a stronger principle: if the interface or device can be redesigned, risk should not be left mainly to attention and training.
        """,
    ),
    "medical_device_use_errors": pair(
        """
        ## 一眼看懂

        医疗器械 use error 这一页想解决的问题是：当不良后果发生时，我们怎样区分“器械本身失效”“用户无意出错”“用户故意偏离”“环境把正确操作变得很难”。

        ## 这页要建立的判断习惯

        - 不要把所有不良使用都叫 use error
        - 要看错误是否在可预见使用范围内
        - 要看设计是否放大了误选、漏做、误判或顺序错误
        - 要看恢复机会是否存在

        ## 为什么这个区分重要

        因为一旦你把问题定义错了，后面的改进就会跑偏：

        - 如果明明是界面诱发错误，却只去补培训，风险还会回来
        - 如果本质是异常使用或故意违规，却按普通 use error 处理，控制措施也会失真

        ## 难点讲解

        这页真正难的地方不是下定义，而是承认“错误行为”常常是设计、时间压力、包装、标签和工作环境共同塑造出来的。也因此，人因分析必须回到具体任务和情境。
        """,
        """
        ## At a Glance

        This topic asks how to distinguish device failure, unintended use error, deliberate deviation, and environmental pressure when something goes wrong.

        ## Analytical Habit To Build

        - do not label every bad use episode as use error
        - judge whether the behavior was foreseeable
        - examine how design may have amplified selection, omission, judgment, or sequence errors
        - check whether recovery opportunities existed

        ## Why It Matters

        If the problem type is misclassified, the control strategy will also drift. Good human-factors analysis stays tied to specific tasks and contexts.
        """,
    ),
    "epipen_workbook": pair(
        """
        ## 一眼看懂

        EpiPen 工作簿这一页不是新的理论，而是把前面讲过的 task analysis、critical task、URRA 写法真正落到一个可操作的样例里。

        ## 读这种 workbook 时要看什么

        - 它如何把使用流程拆成一行行任务
        - 哪些步骤被标成 critical task
        - 每一行如何从 use step 走到 hazard、harm 与 control
        - 文档里哪些栏位只是描述，哪些栏位是在做风险判断

        ## 为什么样例很重要

        真正写风险文件时，最难的往往不是理解概念，而是把抽象概念翻译成表格中的具体语言。样例的价值就在这里：它让你看到“好的一行 URRA”到底长什么样。

        ## 难点讲解

        不要把 workbook 当成答案模板去硬套。更好的做法是学会它背后的写法顺序：任务先明确，错误再具体，伤害后果写完整，最后才回头判断控制是否足够。
        """,
        """
        ## At a Glance

        The EpiPen workbook is not a new theory page. It is a worked example that turns earlier concepts into something documentable.

        ## How To Read It

        - how the use flow is decomposed
        - which steps become critical tasks
        - how each row moves from use step to hazard, harm, and control
        - which fields are descriptive versus evaluative

        ## Why It Matters

        Examples are valuable because the hardest part of risk work is often translating concepts into disciplined document language.
        """,
    ),
}
