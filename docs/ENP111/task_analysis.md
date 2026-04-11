# 任务分析

任务分析这一页的作用，是把一段连续使用过程拆成可观察、可讨论、可映射风险的步骤链。

!!! note "本页主问题"
    如果连任务本身都没拆清楚，
    我们又怎么知道错误会发生在哪一步、
    critical task 在哪里、
    控制措施该落到什么环节？

## 本章重点

- 任务分析的目标不是复述说明书，
  而是把真实任务需求拆成步骤、
  判断和信息需求。
- 它是后续 critical task、
  use error 和 URRA 的前提。
- 好的 task analysis 既看理想流程，
  也看真实工作中的偏差和替代路径。
- 任务拆得越具体，
  后续风险分析越能落地。

## 先记住方法定位

!!! tip "先记住这个方法的定位"
    先记住这个方法的定位：
    如果任务流没有被拆出来，
    后面的风险分析几乎都会漂在空中。

## 这个方法解决什么问题

task analysis 把“用户在用产品”这件看起来连续的事，
拆成一个个可分析的 use step、
subtask、
信息需求和操作要求。
这样做的目的，
是让后续所有讨论都能回到具体环节，
而不是停留在抽象判断上。

## 输入与输出是什么

输入通常包括：
目标任务、
用户特征、
使用环境、
设备说明、
现有流程和观察到的真实使用方式。

输出通常包括：

- 明确的任务步骤
- 每一步的信息、判断和动作要求
- 关键失败点
- 能进入 URRA 或 validation 的结构化任务表

## 操作步骤怎么走

可以按这条线做：

1. 先明确用户目标和起止条件。
2. 把任务拆成能被观察和讨论的 use step。
3. 为每一步补上需要看见什么、判断什么、操作什么。
4. 标出一旦失败就会影响安全或疗效的关键步骤。
5. 再把这些关键步骤带入 use error 和 risk analysis。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/08-task-analysis/slide-08-image8.png" alt="这张图要看懂的是：一张看似简单的操作说明，其实已经包含准备、姿态、方向、按压、保持和收尾等多个可拆分步骤。" loading="lazy">
  <figcaption>这张图要看懂的是：一张看似简单的操作说明，其实已经包含准备、姿态、方向、按压、保持和收尾等多个可拆分步骤。</figcaption>
</figure>

!!! warning "最容易做错的地方"
    最常见的问题，
    是把说明书顺序原样抄下来，
    却没有问用户在真实环境里会不会跳步、
    补救、
    回退或走替代路径。

!!! example "worked example：注射器任务为什么不能只写“给药”"
    如果表里只写“给药”，
    后面就看不见装配、
    剂量设定、
    确认、
    按压保持和废弃处理这些不同失败点。
    把任务拆开后，
    critical task 和风险控制才有地方落脚。

## 和前后方法是什么关系

前面 human error 页告诉你怎样读错误类型，
task analysis 则告诉你错误会落在哪个任务节点上。
后面的 URRA、
critical task 和 workbook 页面，
都会直接把这里拆出来的任务流拿去继续写。

!!! note "一句话结论"
    task analysis 的价值，
    不在于“列步骤”，
    而在于把风险分析绑到真实工作流上。

## 为什么 task analysis 的颗粒度会直接决定后面分析质量

task analysis 写得太粗时，
后面所有风险判断都会被迫写粗。
因为只要任务步骤仍然停在“准备设备”“完成给药”这种大块上，
团队就看不见真正高风险的感知、
确认、
对齐、
保持和恢复节点。

所以这页真正要练的，
不只是会拆步骤，
而是会把步骤拆到足以支撑后续 use error、
critical task 和 validation 的层级。
颗粒度不是写得越碎越好，
而是要碎到能支撑判断、
但又不碎到失去任务结构。

## 为什么 task analysis 最后一定会走到 critical task

任务分析不能停在“步骤列完了”。
真正有价值的地方，
是在步骤表里继续问：
哪一步一旦出错，
就会直接影响安全、
疗效、
剂量、
识别或恢复机会。

这就是 critical task 的来源。
它不是额外附加的一列，
而是 task analysis 真正的落点。
因为只有把关键步骤标出来，
团队才知道哪些节点值得投入更强的界面设计、
确认机制、
培训和验证资源。

!!! example "案例：为什么“确认针头已装好”这种步骤常常比“按压给药”更值得盯住"
    很多团队天然会把最显眼的动作当成主步骤，
    但任务分析常常会发现，
    真正高风险的点在更早环节。
    例如装配确认、
    剂量核对、
    解锁顺序和使用前准备，
    一旦漏掉，
    后面的执行再熟练也救不回来。
    这正是为什么 task analysis 必须把前置步骤写细。

## 为什么课堂里的 PB&J 例子其实很重要

课件里用 PB&J 不是为了讲一个轻松例子，
而是为了证明一件事：
只要任务开始被认真拆开，
很多原本“理所当然”的隐含步骤就会浮出来。

例如洗手、
检查原料状态、
准备顺序、
清理和收尾，
这些都不是装饰步骤。
它们说明 task analysis 的核心不是“把主要动作写出来”，
而是把真实完成任务所需要的全部支撑条件也写出来。
医疗器械、
航空程序和自动化系统里的任务分析，
逻辑上完全一样。

## 怎样判断一张 task analysis 表已经能拿去做后续工作

一张 task analysis 表真正可用时，
团队至少能用它稳定回答四个问题：

- 用户这一步到底要完成什么
- 这一步必须看到、判断和操作什么
- 一旦在这里出错，后果会往哪条风险链走
- 这一行能不能继续支撑 critical task、URRA 和 validation

如果表只能告诉你“步骤名称”，
却回答不了这些问题，
它通常还只是半成品。
task analysis 不是目录，
而是后续风险工作的骨架。

## 从 PB&J 到正式使用任务，课堂真正想让你学会什么

PB&J 例子最有用的地方，
在于它把“隐含步骤”硬生生拉到台面上。
很多人一开始只会写“拿面包、
抹花生酱、
抹果酱、
合上”，
但课程故意提醒你：
洗手、
检查是否过期、
准备位置、
开封方式、
清理收尾，
这些都可能决定任务是否安全、
干净、
有效完成。

这和正式产品任务没有本质区别。
到了注射器、
自动注射器或复杂设备场景，
只是支持条件更多、
后果更高而已。
PB&J 练的不是食物流程，
而是把“看起来理所当然”的任务支撑条件全部写出来的习惯。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/08-task-analysis/slide-04-image2.jpeg" alt="这张图要看懂的是：PB&amp;J 被放进课件里不是为了轻松一下，而是为了提醒你，看似简单的任务也隐藏着大量没有被说出口的步骤与前提。" loading="lazy">
  <figcaption>这张图要看懂的是：PB&amp;J 被放进课件里不是为了轻松一下，而是为了提醒你，看似简单的任务也隐藏着大量没有被说出口的步骤与前提。</figcaption>
</figure>

!!! example "案例：把 PB&J 改写成注射器任务表时，哪些隐藏步骤会突然变关键"
    一旦把 PB&J 的思路迁到注射器任务表里，
    隐藏步骤会迅速跳出来：
    确认药液与患者匹配、
    检查针头是否牢固、
    确认剂量窗口、
    保持注射时间、
    处理废弃物。
    这些都不是“附属细节”，
    而是决定 harm path 会不会被打开的关键节点。
    PB&J 之所以重要，
    就是因为它先用低风险例子把这种观察方式练熟。

## 本章总结

!!! tip "复习时重点记这几条"
    - task analysis 先把任务结构拆清楚，
      再谈风险。
    - 输入包括用户、
      环境、
      流程和真实使用方式。
    - 输出应该支持 critical task、
      URRA 和 validation。
    - 最怕把理想说明书当成真实工作流。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `ENP111 Use-related Risks`
- 关联源文件数: 1
- 文本单元数: 80
- 配图/预览数: 8

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `08 Task Analysis.pptx` | `pptx` | 80 | 8 | [open](../assets/source_files/ENP111/08 Task Analysis.pptx) |

## 相关主题

- [URRA 方法](urra_methods.md)
- [EpiPen URRA 工作簿](epipen_workbook.md)
- [医疗器械中的使用错误](medical_device_use_errors.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "08 Task Analysis.pptx | 80 text units"
    下载原件: [08 Task Analysis.pptx](../assets/source_files/ENP111/08 Task Analysis.pptx)
    映射页面: `task_analysis`
    
    ```text
    [08-task-analysis-0001] slide:1:p:1 | Sami Durrani PhD and Eric Bergman PhD
    [08-task-analysis-0002] slide:1:p:2 | Task Analysis
    [08-task-analysis-0003] slide:2:p:1 | 2
    [08-task-analysis-0004] slide:2:p:2 | There are many different forms of task analysis
    [08-task-analysis-0005] slide:2:p:3 | Hierarchical Task Analysis (HTA)
    [08-task-analysis-0006] slide:2:p:4 | Cognitive Task Analysis (CTA)
    [08-task-analysis-0007] slide:2:p:5 | And many more variations and modifications
    [08-task-analysis-0008] slide:2:p:6 | In medical device human factors, a “task analysis” is typically a modified HTA
    [08-task-analysis-0009] slide:2:p:7 | Types of task analysis
    [08-task-analysis-0010] slide:3:p:1 | 3
    [08-task-analysis-0011] slide:3:p:2 | Identify task
    [08-task-analysis-0012] slide:3:p:3 | Decompose task into sub-tasks (if needed)
    [08-task-analysis-0013] slide:3:p:4 | List use-steps (if known and if needed)
    [08-task-analysis-0014] slide:3:p:5 | Identify potential use-errors
    [08-task-analysis-0015] slide:3:p:6 | Use PCA to help identify potential causes and potential use errors
    [08-task-analysis-0016] slide:3:p:7 | Key steps in conducting a task analysis
    [08-task-analysis-0017] slide:4:p:1 | 4
    [08-task-analysis-0018] slide:4:p:2 | Simple Example: Peanut Butter & Jelly
    [08-task-analysis-0019] slide:5:p:1 | 5
    [08-task-analysis-0020] slide:5:p:2 | Task 1: Gather supplies
    [08-task-analysis-0021] slide:5:p:3 | PB&J
    [08-task-analysis-0022] slide:5:p:4 | Task 2: Prepare bread
    [08-task-analysis-0023] slide:5:p:5 | Use steps:
    [08-task-analysis-0024] slide:5:p:6 | Remove bag slip
    [08-task-analysis-0025] slide:5:p:7 | Open bag
    [08-task-analysis-0026] slide:5:p:8 | Grasp end piece
    [08-task-analysis-0027] slide:5:p:9 | Move it out of the way
    [08-task-analysis-0028] slide:5:p:10 | Grasp next two pieces
    [08-task-analysis-0029] slide:5:p:11 | Take them out of bag
    [08-task-analysis-0030] slide:5:p:12 | Place bread slices on plate, side-by-side
    [08-task-analysis-0031] slide:5:p:13 | BUT WAIT!
    [08-task-analysis-0032] slide:5:p:14 | We forgot to wash our hands!
    [08-task-analysis-0033] slide:5:p:15 | We also forgot to make sure the ingredients aren’t expired!
    [08-task-analysis-0034] slide:6:p:1 | 6
    [08-task-analysis-0035] slide:6:p:2 | Task 3: Spread peanut butter on slice 1
    [08-task-analysis-0036] slide:6:p:3 | Task 4: Spread jam on slice 2
    [08-task-analysis-0037] slide:6:p:4 | Task 5: Combine slices together
    [08-task-analysis-0038] slide:6:p:5 | Task 6: Cut sandwich diagonally (optional)
    [08-task-analysis-0039] slide:6:p:6 | Task 7: Eat
    [08-task-analysis-0040] slide:6:p:7 | Task 8: Clean up and store supplies
    [08-task-analysis-0041] slide:6:p:8 | PBJ
    [08-task-analysis-0042] slide:7:p:1 | 7
    [08-task-analysis-0043] slide:7:p:2 | Let’s do a quick task analysis: Autoinjector
    [08-task-analysis-0044] slide:8:p:1 | Autoinjector analysis continued…
    [08-task-analysis-0045] slide:8:p:2 | 8
    [08-task-analysis-0046] slide:9:p:1 | 9
    [08-task-analysis-0047] slide:9:p:2 | Define preliminary tasks and use steps
    [08-task-analysis-0048] slide:9:p:3 | OK to make assumptions early on
    [08-task-analysis-0049] slide:9:p:4 | Develop cognitive walkthrough and design sketches/mock-ups
    [08-task-analysis-0050] slide:9:p:5 | Do a preliminary hazard analysis (PHA)
    [08-task-analysis-0051] slide:9:p:6 | But what if you don’t have a design yet?
    [08-task-analysis-0052] slide:9:p:7 | Key concept:
    [08-task-analysis-0053] slide:9:p:8 | Don’t need a device design to start identifying potential use errors
    [08-task-analysis-0054] slide:10:p:1 | 10
    [08-task-analysis-0055] slide:10:p:2 | PHA Example:  Infusion Pump
    [08-task-analysis-0056] slide:10:p:3 | Hazard
    [08-task-analysis-0057] slide:10:p:4 | Potential Causes*
    [08-task-analysis-0058] slide:10:p:5 | *note: not UEs yet
    [08-task-analysis-0059] slide:10:p:6 | Potential Consequences
    [08-task-analysis-0060] slide:10:p:7 | Drug over-infusion
    [08-task-analysis-0061] slide:10:p:8 | User data entry error
    [08-task-analysis-0062] slide:10:p:9 | User does not understand amount programmed
    [08-task-analysis-0063] slide:10:p:10 | Overdose
    [08-task-analysis-0064] slide:10:p:11 | Battery dies mid-treatment
    [08-task-analysis-0065] slide:10:p:12 | User does not recharge battery
    [08-task-analysis-0066] slide:10:p:13 | User does not know battery state
    [08-task-analysis-0067] slide:10:p:14 | Underdose
    [08-task-analysis-0068] slide:10:p:15 | Contamination at infusion site
    [08-task-analysis-0069] slide:10:p:16 | User does not use sterile components
    [08-task-analysis-0070] slide:10:p:17 | Infection
    [08-task-analysis-0071] notes:1:p:1 | Quick introductions
    [08-task-analysis-0072] notes:2:p:1 | Hierarchical Task Analysis (HTA): HTA is one of the most widely used methods. It breaks down complex tasks into a hierarchical structure, showing the relationships between higher-level goals and lower-level sub-tasks. HTA is often used to design and evaluate user interfaces and to identify potential usability issues.
    [08-task-analysis-0073] notes:2:p:2 | Cognitive Task Analysis (CTA): CTA focuses on understanding the cognitive processes, strategies, and decision-making involved in completing a task. It is particularly useful in complex domains such as aviation, healthcare, and military operations. Techniques like think-aloud protocols, cognitive interviews, and knowledge elicitation are employed in CTA.
    [08-task-analysis-0074] notes:2:p:3 | Event-Based Task Analysis: Event-based analysis focuses on specific events or incidents within a task. It is useful for understanding how users respond to unexpected situations and how system design can support effective responses
    [08-task-analysis-0075] notes:3:p:1 | Key note, task analysis are hard, time consuming and require many iterations.
    [08-task-analysis-0076] notes:3:p:2 | OK, let’s assume that we went back and did the correction. Added in those key steps. Let’s keep on going.
    [08-task-analysis-0077] notes:4:p:1 | Oh man, I’m not even hungry even more. This simple example is isn’t as simple as I thought. To move us along, I am going to skip writing the use steps and talk about them.
    [08-task-analysis-0078] notes:4:p:2 | Two knives to avoid “contaminating” jar?
    [08-task-analysis-0079] notes:6:p:1 | Task analysis can be done even before a concrete design is available. At early stages, it's based on the intended use and functionality of the device or system rather than its specific design features.
    [08-task-analysis-0080] notes:6:p:2 | There’s several ways you can approach doing an early stage task analysis. And its important to know that the task analysis will grow as the team designs and develops the design.
    ```
