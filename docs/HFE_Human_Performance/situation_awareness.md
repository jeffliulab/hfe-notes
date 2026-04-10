# 情境意识

情境意识这一页把“看见信息”拆成三层：先感知，再理解，再预测。重点是让你看到信息可见和局面可理解之间还有很长一段距离。

!!! note "本页主问题"
    为什么系统明明把很多信息都显示出来了，
    操作者却仍然可能既不理解当前局面，
    也无法预测接下来会怎样？

## 本章重点

- 情境意识至少包括 perception、
  comprehension、
  projection 三层。
- 信息可见不等于意义清楚，
  更不等于未来状态可预测。
- 很多显示、
  CRM、
  监控和自动化问题最后都会回到 SA 断裂上。
- SA 的本质不是信息量，
  而是信息有没有被组织成可行动的 mental model。

## 先记住一句话

!!! tip "复习时先记住这句话"
    先记住一句话：
    情境意识不是“多看一点”，
    而是把看到的线索真正拼成当前局面，
    并能往前预判一步。

## 三层结构到底分别在说什么

课程里的三层结构是：

1. `perception`：有没有注意到关键线索。
2. `comprehension`：这些线索有没有被拼成正确的当前局面。
3. `projection`：如果不干预，系统接下来会往哪里走。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/sp26-situationawareness-20260325/page-04.png" alt="这张图要看懂的是：Level 1、2、3 不是三个平行标签，而是从看见线索、理解局面到预测走势的一条递进链。" loading="lazy">
  <figcaption>这张图要看懂的是：Level 1、2、3 不是三个平行标签，而是从看见线索、理解局面到预测走势的一条递进链。</figcaption>
</figure>

## 为什么第二层和第三层最容易断

操作者可能已经看到了读数、
告警和状态变化，
但仍然不知道哪个信号优先、
多个信号之间有什么关系、
以及未来几十秒会怎么演化。
也就是说，
SA 的难点往往不在“看见”，
而在“组织和推演”。

!!! warning "最容易误解的地方"
    看到数据并不等于形成 SA。
    很多事故正是发生在“数据都在眼前，
    但局面没真正被拼出来”的状态下。

!!! example "案例：为什么“信息可见”还不够"
    一个机组可能看到了高度、
    速度和告警，
    却仍然没有意识到这些线索共同指向正在偏离的飞行状态。
    问题不在数据是否存在，
    而在这些数据有没有被整合成正确局面并转化成提前干预。

## 为什么课程很多页最后都会回到 SA

display 页在问信息怎么被看见，
CRM 页在问信息怎么被团队共享，
monitoring 页在问状态怎么被持续保持，
spatial disorientation 页在问感官和仪表冲突时还能不能建立正确局面。
它们本质上都在问：
系统有没有帮人形成足够好的情境意识。

!!! note "一句话结论"
    情境意识的核心不是“信息多”，
    而是“信息有没有被组织成可行动的理解和预测”。

## 为什么 Endsley 模型把 SA 放在“决策之前、动作之后”这条链上

Endsley 模型的价值，
不只是把 SA 分成三层，
而是把它明确放到“环境输入 -> SA -> 决策 -> 动作 -> 反馈”这条链上。
这样一来，
SA 就不再是抽象心理状态，
而是直接决定后续判断和动作质量的中间机制。

这也解释了为什么课程里会把 workload、
stress、
automation 和 interface design 都接到 SA 上。
它们不是在旁边“影响一下心情”，
而是在改变人能否形成足够好的局面理解。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/sp26-situationawareness-20260325/page-03.png" alt="这张图要看懂的是：SA 不是孤立状态，它夹在环境输入、决策和动作之间，前面受显示与负荷影响，后面直接影响行为结果。" loading="lazy">
  <figcaption>这张图要看懂的是：SA 不是孤立状态，它夹在环境输入、决策和动作之间，前面受显示与负荷影响，后面直接影响行为结果。</figcaption>
</figure>

## 三层 SA 断裂在实际分析里怎样分别出现

这页最值得带走的，
不只是三层定义，
而是复盘时如何用它们定位断裂点：

- 如果关键线索根本没被 notice，通常是 Level 1 问题
- 如果线索被看见却被解释错，通常是 Level 2 问题
- 如果当前状态理解得差不多，但未来走势判断错了，通常是 Level 3 问题

一旦断裂层级被找准，
后面的 mitigation 才不会乱：
是改 detectability、
改 mental model 支持，
还是改 projection 支持。

## 为什么 SA 不只是个人状态，也可能是团队状态

课程后半段会反复出现一个提醒：
即使每个人都各自看见了一部分信息，
团队仍然可能没有形成共享局面。
也就是说，
个人 SA 和 team SA 之间并不自动相等。

这时问题就不再只在显示，
而也在沟通、
briefing、
cross-check 和权限结构上。
团队有没有把分散线索重新拼成同一个 picture，
这往往决定了后续动作是否一致。

!!! example "案例：为什么团队里每个人都看见一点，不等于团队真的知道发生了什么"
    一个人可能看到速度异常，
    另一个人注意到告警，
    第三个人知道程序状态变化，
    但如果这些线索没有被及时拼成共享局面，
    团队仍然可能继续沿着错误判断走下去。
    SA 的关键不是线索分散存在，
    而是线索有没有被组织成同一 picture。

## 为什么 SA 还要看 picture 更新得够不够快

SA 不是静态拥有一张 picture，
而是要不断更新 picture。
高风险系统里，
状态经常在变，
如果团队还停留在几分钟前的理解，
就算当时理解过也可能已经落后于系统现实。

所以 SA 分析不能只问“有没有建立 picture”，
还要问“picture 更新速度够不够快”。
很多事故不是从完全不知道开始，
而是从来不及把旧 picture 替换成新 picture 开始。

## 本章总结

!!! tip "复习时重点记这几条"
    - SA 包括感知、
      理解和预测三层。
    - 信息可见不等于真正理解。
    - 很多 HFE 主题最后都会回到 SA 是否断裂。
    - SA 的关键是形成可行动的 mental model。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `人的表现`
- 关联源文件数: 1
- 文本单元数: 200
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Sp26_SituationAwareness_20260325.pdf` | `pdf` | 200 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Sp26_SituationAwareness_20260325.pdf) |

## 相关主题

- [注意与监控](attention_and_monitoring.md)
- [Crew Resource Management](../HFE_Aviation_Automation/crew_resource_management.md)
- [空间定向错觉](spatial_disorientation.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "Sp26_SituationAwareness_20260325.pdf | 200 text units"
    下载原件: [Sp26_SituationAwareness_20260325.pdf](../assets/source_files/Lectures_Spring_2026/Sp26_SituationAwareness_20260325.pdf)
    映射页面: `situation_awareness`
    
    ```text
    [sp26-situationawareness-20260325-0001] page:1:line:1 | SITUATION
    [sp26-situationawareness-20260325-0002] page:1:line:2 | AWARENESS
    [sp26-situationawareness-20260325-0003] page:1:line:3 | Dr. Andrew Liu
    [sp26-situationawareness-20260325-0004] page:1:line:4 | ENP-0112
    [sp26-situationawareness-20260325-0005] page:1:line:5 | Credit: Gary Larson, The Far Side
    [sp26-situationawareness-20260325-0006] page:2:line:1 | SITUATION AWARENESS
    [sp26-situationawareness-20260325-0007] page:2:line:2 | “Situation awareness is the perception of the elements in the environment within a
    [sp26-situationawareness-20260325-0008] page:2:line:3 | volume of time and space, the comprehension of their meaning, and the projection of
    [sp26-situationawareness-20260325-0009] page:2:line:4 | their status in the near future.”     -- Endsley (1995)
    [sp26-situationawareness-20260325-0010] page:2:line:5 | 3
    [sp26-situationawareness-20260325-0011] page:2:line:6 | • Perception (Level 1): Recognizing the status, attributes and dynamics of relevant
    [sp26-situationawareness-20260325-0012] page:2:line:7 | elements in the environment.
    [sp26-situationawareness-20260325-0013] page:2:line:8 | • Comprehension (Level 2): Understanding the significance of the relevant
    [sp26-situationawareness-20260325-0014] page:2:line:9 | elements in the context of operator goals.
    [sp26-situationawareness-20260325-0015] page:2:line:10 | • Projection (Level 3): Projecting the future actions of the elements in the
    [sp26-situationawareness-20260325-0016] page:2:line:11 | environment while accounting for their status and dynamics.
    [sp26-situationawareness-20260325-0017] page:2:line:12 | 3/25/26
    [sp26-situationawareness-20260325-0018] page:2:line:13 | ENP-0112
    [sp26-situationawareness-20260325-0019] page:3:line:1 | SITUATION AWARENESS IN DECISION MAKING
    [sp26-situationawareness-20260325-0020] page:3:line:2 | 4
    [sp26-situationawareness-20260325-0021] page:3:line:3 | 3/25/26
    [sp26-situationawareness-20260325-0022] page:3:line:4 | ENP-0112
    [sp26-situationawareness-20260325-0023] page:3:line:5 | Endsley, 1995
    [sp26-situationawareness-20260325-0024] page:4:line:1 | EXAMPLE OF SA ELEMENTS: DRIVING A CAR
    [sp26-situationawareness-20260325-0025] page:4:line:2 | Perception (Level 1)                  Comprehension (Level 2)                 Projection (Level 3)
    [sp26-situationawareness-20260325-0026] page:4:line:3 | 6
    [sp26-situationawareness-20260325-0027] page:4:line:4 | 3/25/26
    [sp26-situationawareness-20260325-0028] page:4:line:5 | ENP-0112
    [sp26-situationawareness-20260325-0029] page:5:line:1 | BREAKDOWNS IN SA
    [sp26-situationawareness-20260325-0030] page:5:line:2 | • Perception (Level 1):
    [sp26-situationawareness-20260325-0031] page:5:line:3 | •
    [sp26-situationawareness-20260325-0032] page:5:line:4 | Lack of detectability or distinguishability
    [sp26-situationawareness-20260325-0033] page:5:line:5 | •
    [sp26-situationawareness-20260325-0034] page:5:line:6 | Lack of attention
    [sp26-situationawareness-20260325-0035] page:5:line:7 | •
    [sp26-situationawareness-20260325-0036] page:5:line:8 | Visual obstructions, auditory masking
    [sp26-situationawareness-20260325-0037] page:5:line:9 | •
    [sp26-situationawareness-20260325-0038] page:5:line:10 | …
    [sp26-situationawareness-20260325-0039] page:5:line:11 | • Comprehension (Level 2):
    [sp26-situationawareness-20260325-0040] page:5:line:12 | •
    [sp26-situationawareness-20260325-0041] page:5:line:13 | No mental model for environment/observations
    [sp26-situationawareness-20260325-0042] page:5:line:14 | •
    [sp26-situationawareness-20260325-0043] page:5:line:15 | Incorrect mental model used to interpret perceived data
    [sp26-situationawareness-20260325-0044] page:5:line:16 | •
    [sp26-situationawareness-20260325-0045] page:5:line:17 | Data inappropriately used (e.g.,  auditory alarms that can have multiple meanings)
    [sp26-situationawareness-20260325-0046] page:5:line:18 | •
    [sp26-situationawareness-20260325-0047] page:5:line:19 | …
    [sp26-situationawareness-20260325-0048] page:5:line:20 | • Projection (Level 3):
    [sp26-situationawareness-20260325-0049] page:5:line:21 | •
    [sp26-situationawareness-20260325-0050] page:5:line:22 | Lack of a good enough mental model
    [sp26-situationawareness-20260325-0051] page:5:line:23 | •
    [sp26-situationawareness-20260325-0052] page:5:line:24 | Limited attentional or memory resources to perform projection
    [sp26-situationawareness-20260325-0053] page:5:line:25 | •
    [sp26-situationawareness-20260325-0054] page:5:line:26 | …
    [sp26-situationawareness-20260325-0055] page:5:line:27 | 3/25/26
    [sp26-situationawareness-20260325-0056] page:5:line:28 | ENP-0112
    [sp26-situationawareness-20260325-0057] page:5:line:29 | 7
    [sp26-situationawareness-20260325-0058] page:5:line:30 | A breakdown in a level is when you do not
    [sp26-situationawareness-20260325-0059] page:5:line:31 | have the relevant output from the SA level
    [sp26-situationawareness-20260325-0060] page:6:line:1 | AMTRAK ACCIDENT REVISITED
    [sp26-situationawareness-20260325-0061] page:6:line:2 | • Where did the breakdown in
    [sp26-situationawareness-20260325-0062] page:6:line:3 | situation awareness occur?
    [sp26-situationawareness-20260325-0063] page:6:line:4 | • Level 1 – Perception
    [sp26-situationawareness-20260325-0064] page:6:line:5 | • Level 2 – Comprehension
    [sp26-situationawareness-20260325-0065] page:6:line:6 | • Level 3 - Projection
    [sp26-situationawareness-20260325-0066] page:6:line:7 | 3/25/26
    [sp26-situationawareness-20260325-0067] page:6:line:8 | ENP-0112
    [sp26-situationawareness-20260325-0068] page:6:line:9 | 8
    [sp26-situationawareness-20260325-0069] page:7:line:1 | TEAM SITUATION AWARENESS
    [sp26-situationawareness-20260325-0070] page:7:line:2 | 9
    [sp26-situationawareness-20260325-0071] page:7:line:3 | Endsley, 1995
    [sp26-situationawareness-20260325-0072] page:7:line:4 | 3/25/26
    [sp26-situationawareness-20260325-0073] page:7:line:5 | ENP-0112
    [sp26-situationawareness-20260325-0074] page:8:line:1 | UBER ACCIDENT, MARCH 2018
    [sp26-situationawareness-20260325-0075] page:8:line:2 | • Operator took self-driving car out of garage to
    [sp26-situationawareness-20260325-0076] page:8:line:3 | begin evaluations at 9:14 pm
    [sp26-situationawareness-20260325-0077] page:8:line:4 | • Self-driving system in computer control mode
    [sp26-situationawareness-20260325-0078] page:8:line:5 | struck a pedestrian at 9:58 pm
    [sp26-situationawareness-20260325-0079] page:8:line:6 | • Human operator intervened <1 sec before impact
    [sp26-situationawareness-20260325-0080] page:8:line:7 | (engaged the steering wheel)
    [sp26-situationawareness-20260325-0081] page:8:line:8 | • The vehicle speed at impact was 39 mph.
    [sp26-situationawareness-20260325-0082] page:8:line:9 | • Operator began braking less than a second after
    [sp26-situationawareness-20260325-0083] page:8:line:10 | the impact.
    [sp26-situationawareness-20260325-0084] page:8:line:11 | • The data showed that all aspects of the self-driving
    [sp26-situationawareness-20260325-0085] page:8:line:12 | system were operating normally at the time of the
    [sp26-situationawareness-20260325-0086] page:8:line:13 | crash, and that there were no faults or diagnostic
    [sp26-situationawareness-20260325-0087] page:8:line:14 | messages.
    [sp26-situationawareness-20260325-0088] page:8:line:15 | 11
    [sp26-situationawareness-20260325-0089] page:8:line:16 | NTSB/HAR-19/03
    [sp26-situationawareness-20260325-0090] page:8:line:17 | 3/25/26
    [sp26-situationawareness-20260325-0091] page:8:line:18 | ENP-0112
    [sp26-situationawareness-20260325-0092] page:9:line:1 | UBER ACCIDENT, MARCH 2018
    [sp26-situationawareness-20260325-0093] page:9:line:2 | • Software classified the pedestrian as an unknown
    [sp26-situationawareness-20260325-0094] page:9:line:3 | object, vehicle, and bicycle with varying
    [sp26-situationawareness-20260325-0095] page:9:line:4 | probabilities and expectations of future travel
    [sp26-situationawareness-20260325-0096] page:9:line:5 | path (first registered 6 seconds prior to impact).
    [sp26-situationawareness-20260325-0097] page:9:line:6 | • 1.3 seconds before impact, the software
    [sp26-situationawareness-20260325-0098] page:9:line:7 | determined that an emergency braking maneuver
    [sp26-situationawareness-20260325-0099] page:9:line:8 | was needed to mitigate a collision
    [sp26-situationawareness-20260325-0100] page:9:line:9 | • Emergency braking maneuvers are not enabled
    [sp26-situationawareness-20260325-0101] page:9:line:10 | while the vehicle is under computer control, to
    [sp26-situationawareness-20260325-0102] page:9:line:11 | reduce the potential for erratic vehicle behavior.
    [sp26-situationawareness-20260325-0103] page:9:line:12 | • The vehicle relies on the operator to intervene
    [sp26-situationawareness-20260325-0104] page:9:line:13 | and take action.
    [sp26-situationawareness-20260325-0105] page:9:line:14 | 12
    [sp26-situationawareness-20260325-0106] page:9:line:15 | Video released by Uber
    [sp26-situationawareness-20260325-0107] page:9:line:16 | 3/25/26
    [sp26-situationawareness-20260325-0108] page:9:line:17 | ENP-0112
    [sp26-situationawareness-20260325-0109] page:10:line:1 | DESIGN AN INTERFACE FOR TRANSITIONS
    [sp26-situationawareness-20260325-0110] page:10:line:2 | SUV interior
    [sp26-situationawareness-20260325-0111] page:10:line:3 | • Locations that could mount a cell
    [sp26-situationawareness-20260325-0112] page:10:line:4 | phone (yellow region in center
    [sp26-situationawareness-20260325-0113] page:10:line:5 | console)
    [sp26-situationawareness-20260325-0114] page:10:line:6 | • ADS engagement/disengagement
    [sp26-situationawareness-20260325-0115] page:10:line:7 | knob (red)
    [sp26-situationawareness-20260325-0116] page:10:line:8 | • ADS engagement button (blue)
    [sp26-situationawareness-20260325-0117] page:10:line:9 | • HMI (green)
    [sp26-situationawareness-20260325-0118] page:10:line:10 | • inset illustrating image on tablet.
    [sp26-situationawareness-20260325-0119] page:10:line:11 | 3/25/26
    [sp26-situationawareness-20260325-0120] page:10:line:12 | ENP-0112
    [sp26-situationawareness-20260325-0121] page:10:line:13 | 14
    [sp26-situationawareness-20260325-0122] page:11:line:1 | EXPERIMENTAL MEASURES OF SA
    [sp26-situationawareness-20260325-0123] page:11:line:2 | • Explicit: Questions are defined that specifically ask operators about their SA
    [sp26-situationawareness-20260325-0124] page:11:line:3 | • Implicit: Responses are used to infer an operator’s SA
    [sp26-situationawareness-20260325-0125] page:11:line:4 | • Subjective: Measures that are provided by the operator self-assessments or an
    [sp26-situationawareness-20260325-0126] page:11:line:5 | observer
    [sp26-situationawareness-20260325-0127] page:11:line:6 | • Objective?  What objective measures could we use?  What are the pitfalls?
    [sp26-situationawareness-20260325-0128] page:11:line:7 | 3/25/26
    [sp26-situationawareness-20260325-0129] page:11:line:8 | ENP-0112
    [sp26-situationawareness-20260325-0130] page:11:line:9 | 15
    [sp26-situationawareness-20260325-0131] page:12:line:1 | EXPLICIT MEASURES OF SA
    [sp26-situationawareness-20260325-0132] page:12:line:2 | Asks operators questions about their perception of the state of the system/environment
    [sp26-situationawareness-20260325-0133] page:12:line:3 | • Retrospective
    [sp26-situationawareness-20260325-0134] page:12:line:4 | • Time dependent
    [sp26-situationawareness-20260325-0135] page:12:line:5 | • Are you testing memory or SA?
    [sp26-situationawareness-20260325-0136] page:12:line:6 | • Concurrent (Situation Presence Assessment Method, SPAM)
    [sp26-situationawareness-20260325-0137] page:12:line:7 | • Workload may be high
    [sp26-situationawareness-20260325-0138] page:12:line:8 | • Adding another task
    [sp26-situationawareness-20260325-0139] page:12:line:9 | • Freeze (SA Global Assessment Technology, SAGAT)
    [sp26-situationawareness-20260325-0140] page:12:line:10 | • Intrusive
    [sp26-situationawareness-20260325-0141] page:12:line:11 | 16
    [sp26-situationawareness-20260325-0142] page:12:line:12 | (Durso et al., 1995)
    [sp26-situationawareness-20260325-0143] page:12:line:13 | (Endsley et al., 1988)
    [sp26-situationawareness-20260325-0144] page:12:line:14 | 3/25/26
    [sp26-situationawareness-20260325-0145] page:12:line:15 | ENP-0112
    [sp26-situationawareness-20260325-0146] page:13:line:1 | IMPLICIT MEASURES OF SA
    [sp26-situationawareness-20260325-0147] page:13:line:2 | Experimenter infers SA from performance-based measures
    [sp26-situationawareness-20260325-0148] page:13:line:3 | • Advantages
    [sp26-situationawareness-20260325-0149] page:13:line:4 | • Objective and unobtrusive
    [sp26-situationawareness-20260325-0150] page:13:line:5 | • Can be through embedded task measures
    [sp26-situationawareness-20260325-0151] page:13:line:6 | • Disadvantages
    [sp26-situationawareness-20260325-0152] page:13:line:7 | • Poor performance isn’t necessarily a function of low SA
    [sp26-situationawareness-20260325-0153] page:13:line:8 | 17
    [sp26-situationawareness-20260325-0154] page:13:line:9 | 3/25/26
    [sp26-situationawareness-20260325-0155] page:13:line:10 | ENP-0112
    [sp26-situationawareness-20260325-0156] page:14:line:1 | SUBJECTIVE MEASURES OF SA
    [sp26-situationawareness-20260325-0157] page:14:line:2 | • Self-assessment or observer assessment
    [sp26-situationawareness-20260325-0158] page:14:line:3 | • Situation Awareness Rating Technique (SART)
    [sp26-situationawareness-20260325-0159] page:14:line:4 | • Instability - Likelihood of situation changing suddenly
    [sp26-situationawareness-20260325-0160] page:14:line:5 | • Observer with system knowledge rates user’s
    [sp26-situationawareness-20260325-0161] page:14:line:6 | performance
    [sp26-situationawareness-20260325-0162] page:14:line:7 | • Advantages
    [sp26-situationawareness-20260325-0163] page:14:line:8 | • Doesn’t rely on memory
    [sp26-situationawareness-20260325-0164] page:14:line:9 | • Non-intrusive
    [sp26-situationawareness-20260325-0165] page:14:line:10 | • Disadvantages
    [sp26-situationawareness-20260325-0166] page:14:line:11 | • Are you testing confidence or SA?
    [sp26-situationawareness-20260325-0167] page:14:line:12 | • Rating workload or SA?
    [sp26-situationawareness-20260325-0168] page:14:line:13 | • Observer only has limited idea of the subject’s internal knowledge states
    [sp26-situationawareness-20260325-0169] page:14:line:14 | 18
    [sp26-situationawareness-20260325-0170] page:14:line:15 | SA = Understanding − (Demand − Supply)
    [sp26-situationawareness-20260325-0171] page:14:line:16 | 3/25/26
    [sp26-situationawareness-20260325-0172] page:14:line:17 | ENP-0112
    [sp26-situationawareness-20260325-0173] page:15:line:1 | REFERENCES
    [sp26-situationawareness-20260325-0174] page:15:line:2 | •
    [sp26-situationawareness-20260325-0175] page:15:line:3 | Durso, F.T., Truitt, T.R., Hackworth, C.A., Crutchfield, J.M., Nikolic, D., Moertl, P.M., Ohrt, D. & Manning, C.A. (1995). Expertise and Chess: a Pilot
    [sp26-situationawareness-20260325-0176] page:15:line:4 | Study Comparing Situation Awareness Methodologies. In: D.J. Garland & M. Endsley (Eds), Experimental Analysis and Measurement of Situation
    [sp26-situationawareness-20260325-0177] page:15:line:5 | Awareness. Embry-Riddle Aeronautical University Press.
    [sp26-situationawareness-20260325-0178] page:15:line:6 | •
    [sp26-situationawareness-20260325-0179] page:15:line:7 | Durso, F. T., et al. (1999). Situation Awareness As a Predictor of Performance in En Route Air Traffic Controllers. Technical Report DOT/FAA/AM-
    [sp26-situationawareness-20260325-0180] page:15:line:8 | 99/3, US Dept. of Transportation/Federal Aviation Administration.
    [sp26-situationawareness-20260325-0181] page:15:line:9 | •
    [sp26-situationawareness-20260325-0182] page:15:line:10 | Endsley M.R., (1988) Situation awareness global assessment technique (SAGAT), Proc. of the IEEE 1988 National Aerospace and Electronics
    [sp26-situationawareness-20260325-0183] page:15:line:11 | Conf., 23-27 May, pp. 789-795 vol.3.
    [sp26-situationawareness-20260325-0184] page:15:line:12 | •
    [sp26-situationawareness-20260325-0185] page:15:line:13 | Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. Human Factors: The Journal of the Human Factors and
    [sp26-situationawareness-20260325-0186] page:15:line:14 | Ergonomics Society, 37(1), 32-64. https://doi.org/10.1518/001872095779049543
    [sp26-situationawareness-20260325-0187] page:15:line:15 | •
    [sp26-situationawareness-20260325-0188] page:15:line:16 | Ma R, Kaber D. (2005) Situation awareness and workload in driving while using adaptive cruise control and a cell phone. International Journal of
    [sp26-situationawareness-20260325-0189] page:15:line:17 | Industrial Ergonomics 35: 939-953.
    [sp26-situationawareness-20260325-0190] page:15:line:18 | •
    [sp26-situationawareness-20260325-0191] page:15:line:19 | National Transportation Safety Board. (2019). Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian
    [sp26-situationawareness-20260325-0192] page:15:line:20 | [Highway Accident Report]. https://www.ntsb.gov/investigations/accidentreports/reports/har1903.pdf
    [sp26-situationawareness-20260325-0193] page:15:line:21 | •
    [sp26-situationawareness-20260325-0194] page:15:line:22 | Proctor R, Van Zandt T. (2018) Human Factors in Simple and Complex Systems 3rd Edition. CRC Press.
    [sp26-situationawareness-20260325-0195] page:15:line:23 | •
    [sp26-situationawareness-20260325-0196] page:15:line:24 | Taylor R. (1990) Situational awareness rating technique (SART): The development of a tool for aircrew systems design. In Situational Awareness
    [sp26-situationawareness-20260325-0197] page:15:line:25 | in Aerospace Operations, AGARD-CP-478, pp. 311 - 3117. Neuilly Sur Seine, France: NATO – AGARD.
    [sp26-situationawareness-20260325-0198] page:15:line:26 | 3/25/26
    [sp26-situationawareness-20260325-0199] page:15:line:27 | 25
    [sp26-situationawareness-20260325-0200] page:15:line:28 | ENP-0112
    ```
