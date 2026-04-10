# 自动化车辆

自动化车辆这一页不是在重复航空自动化，而是在看一个迁移问题：当接管、信任校准和责任分配进入驾驶场景后，风险会怎样重组。

!!! note "本页主问题"
    自动化车辆最危险的地方，
    为什么往往不是系统在正常巡航时做得好不好，
    而是人和系统在接管边界上怎样交接责任？

## 这个案例最重要的结论

- 自动化车辆的核心难题是 handoff，
  而不是稳定巡航。
- trust calibration 比“让用户更相信系统”更重要，
  它要求用户既不盲信也不过度弃用。
- 航空自动化里的 mode confusion、
  monitoring decay 和 automation surprise 在这里高度可迁移。
- 责任边界如果写不清，
  接管失败就会变成设计与使用共同制造的灰区。

## 先记住这个案例的一句话判断

!!! tip "先记住这个案例的一句话判断"
    先记住这个案例的一句话判断：
    自动化车辆最危险的时刻，
    往往是系统要求“你现在马上接管”，
    而人却已经不在同一个情境里。

## 背景与 stakes

驾驶自动化和航空自动化的共同点，
是都把人推向“平时低参与、
关键时刻高责任”的角色。
不同点在于，
道路环境变化更快、
用户更杂、
边界更容易被误解，
所以接管窗口通常更脆弱。

## 事件链真正容易断在哪里

自动化车辆的问题通常不是“系统能不能自己开一会儿”，
而是：
用户长时间不需要主动控制后，
是否还保持了足够的 situation awareness、
模式理解和动作准备，
一旦 ODD 边界到来能否及时接回控制。

!!! example "案例：handoff 为什么会变成高风险窗口"
    用户在自动驾驶模式下长时间处于被动监控状态，
    系统突然发出接管请求时，
    用户需要在很短时间里重新建立环境理解、
    识别系统边界并做出动作。
    这条链只要其中一环晚了半拍，
    风险就会迅速放大。

## 这个案例教会我们的系统层问题

如果系统默认人会始终保持适度警觉，
但设计本身又长期让人退出主任务，
那么设计假设就自相矛盾了。
自动化车辆因此成为一个非常典型的 HFE 问题：
界面、
告警、
模式说明、
handoff 时机和责任分配必须一起设计。

!!! note "一句话结论"
    自动化车辆最难的不是让系统多做一点，
    而是让人和系统在接管边界上真正对得上。

!!! warning "最容易误解的地方"
    不要把问题简化成“驾驶员没专心”。
    如果系统长期设计成让人不需要专心，
    最后又要求瞬时高质量接管，
    那本身就是设计假设的问题。

## 为什么 automated vehicle 讨论离不开 ODD 边界

自动化车辆最关键的前提之一是 ODD，
也就是系统到底在哪些条件下被假定可以工作。
一旦这个边界不清楚，
用户就很容易在系统其实已经接近能力边缘时，
仍然误以为它处在“正常自动化”状态。

所以 ODD 不是法规术语点缀，
而是 handoff 风险的起点：
越不清楚边界，
越容易把接管做成措手不及。

## 为什么驾驶员监控问题和系统设计问题其实分不开

automated vehicle 场景里，
团队很容易把问题写成“driver was inattentive”。
但更深一层的问题通常是：
系统究竟把驾驶员放在什么角色上？
是持续参与者、
后备接管者，
还是名义上负责但实际上长期脱离任务的人？

只要这个角色定义不清，
driver monitoring 再强，
也很难真正补上 handoff 逻辑里的结构漏洞。

!!! example "案例：为什么“请随时准备接管”这句话本身可能就是弱设计"
    如果系统让人长时间低参与，
    却又要求在边界逼近时立即高质量接管，
    那么“请准备接管”就不只是提示语，
    而可能是在把一个结构上难以完成的任务压给驾驶员。
    问题不只在注意力，
    而在角色设计本身。

## 为什么 automated vehicle 设计还要解决 trust calibration

自动化车辆里还有一个特别典型的问题：
人到底该信系统多少。
信得太少，
会导致频繁打断、
低效和不必要的人工接管；
信得太多，
又会让人跨过 ODD 边界，
或者在真正需要接管时反应太慢。

所以 automated vehicle 设计不仅要让系统能工作，
还要让人形成合适的 trust calibration。
换句话说，
系统必须把自己的边界、
能力和不确定性表达得足够清楚，
让人既不过度依赖，
也不过度怀疑。

## 这个案例最后要带走什么

!!! tip "复习时重点记这几条"
    - 自动化车辆的核心难点是 handoff。
    - trust calibration 比单纯提升信任更重要。
    - 航空自动化教训会大量迁移到这里。
    - 接管边界的责任分配必须被设计清楚。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `航空与自动化`
- 关联源文件数: 1
- 文本单元数: 374
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Automated Vehicles 3-11-26-2.pdf` | `pdf` | 374 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Automated Vehicles 3-11-26-2.pdf) |

## 相关主题

- [航空与自动化导论](aviation_automation_intro.md)
- [显示与告警](displays_and_alerts.md)
- [Boeing 737 Max 与伦理](../HFE_Cases_Ethics/boeing_737max_and_ethics.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "Automated Vehicles 3-11-26-2.pdf | 374 text units"
    下载原件: [Automated Vehicles 3-11-26-2.pdf](../assets/source_files/Lectures_Spring_2026/Automated Vehicles 3-11-26-2.pdf)
    映射页面: `automated_vehicles`
    
    ```text
    [automated-vehicles-3-11-26-2-0001] page:1:line:1 | AUTOMATED VEHICLES
    [automated-vehicles-3-11-26-2-0002] page:1:line:2 | ENP-0112
    [automated-vehicles-3-11-26-2-0003] page:1:line:3 | 3/11/2026
    [automated-vehicles-3-11-26-2-0004] page:1:line:4 | Dr. Divya C. Chandra
    [automated-vehicles-3-11-26-2-0005] page:1:line:5 | 3/11/26
    [automated-vehicles-3-11-26-2-0006] page:1:line:6 | ENP-0112
    [automated-vehicles-3-11-26-2-0007] page:1:line:7 | 1
    [automated-vehicles-3-11-26-2-0008] page:1:line:8 | Yellowstone National Park Visitor Buses (Sumer 2021)
    [automated-vehicles-3-11-26-2-0009] page:2:line:1 | PLAN
    [automated-vehicles-3-11-26-2-0010] page:2:line:2 | • Driving tasks and vocabulary
    [automated-vehicles-3-11-26-2-0011] page:2:line:3 | • Automation related to driving
    [automated-vehicles-3-11-26-2-0012] page:2:line:4 | • Flying vs. Driving comparison
    [automated-vehicles-3-11-26-2-0013] page:2:line:5 | – class discussion
    [automated-vehicles-3-11-26-2-0014] page:2:line:6 | 3/11/26
    [automated-vehicles-3-11-26-2-0015] page:2:line:7 | ENP-0112
    [automated-vehicles-3-11-26-2-0016] page:2:line:8 | 2
    [automated-vehicles-3-11-26-2-0017] page:3:line:1 | DRIVING
    [automated-vehicles-3-11-26-2-0018] page:3:line:2 | Tasks and Vocabulary
    [automated-vehicles-3-11-26-2-0019] page:3:line:3 | 3/11/26
    [automated-vehicles-3-11-26-2-0020] page:3:line:4 | ENP-0112
    [automated-vehicles-3-11-26-2-0021] page:3:line:5 | 3
    [automated-vehicles-3-11-26-2-0022] page:4:line:1 | WHAT DOES IT MEAN TO “DRIVE”?
    [automated-vehicles-3-11-26-2-0023] page:4:line:2 | • DDT – Dynamic Driving Task
    [automated-vehicles-3-11-26-2-0024] page:4:line:3 | • Lateral and longitudinal control
    [automated-vehicles-3-11-26-2-0025] page:4:line:4 | • OEDR – Object and Event Detection and Recognition
    [automated-vehicles-3-11-26-2-0026] page:4:line:5 | • Active safety assistance, such as Automatic Emergency Braking Technology, AEBT
    [automated-vehicles-3-11-26-2-0027] page:4:line:6 | • ODD – Operating Design Domain
    [automated-vehicles-3-11-26-2-0028] page:4:line:7 | • Getting into and out of the ODD
    [automated-vehicles-3-11-26-2-0029] page:4:line:8 | 3/11/26
    [automated-vehicles-3-11-26-2-0030] page:4:line:9 | ENP-0112
    [automated-vehicles-3-11-26-2-0031] page:4:line:10 | 4
    [automated-vehicles-3-11-26-2-0032] page:4:line:11 | Most people think of themselves as either the driver or a rider.
    [automated-vehicles-3-11-26-2-0033] page:4:line:12 | What other role(s) are there?
    [automated-vehicles-3-11-26-2-0034] page:5:line:1 | AUTOMATED-SYSTEMS FOR DRIVING
    [automated-vehicles-3-11-26-2-0035] page:5:line:2 | Earlier Systems
    [automated-vehicles-3-11-26-2-0036] page:5:line:3 | • Automatic transmission
    [automated-vehicles-3-11-26-2-0037] page:5:line:4 | • Power steering
    [automated-vehicles-3-11-26-2-0038] page:5:line:5 | • Electronic vehicle stability (EVS)
    [automated-vehicles-3-11-26-2-0039] page:5:line:6 | • Antilock brakes (ABS)
    [automated-vehicles-3-11-26-2-0040] page:5:line:7 | Newer Driver Assistance Technologies (Level 1)
    [automated-vehicles-3-11-26-2-0041] page:5:line:8 | • Momentary Driver Assistance
    [automated-vehicles-3-11-26-2-0042] page:5:line:9 | • Automatic emergency braking technology (AEBT)
    [automated-vehicles-3-11-26-2-0043] page:5:line:10 | • Forward collision warning (FCW)
    [automated-vehicles-3-11-26-2-0044] page:5:line:11 | • Lane departure warning
    [automated-vehicles-3-11-26-2-0045] page:5:line:12 | • (Continuous) Driver Assistance
    [automated-vehicles-3-11-26-2-0046] page:5:line:13 | • Adaptive cruise control (ACC)
    [automated-vehicles-3-11-26-2-0047] page:5:line:14 | • Lane keeping assistance
    [automated-vehicles-3-11-26-2-0048] page:5:line:15 | • Blind spot monitoring
    [automated-vehicles-3-11-26-2-0049] page:5:line:16 | • Adaptable features (headlights)
    [automated-vehicles-3-11-26-2-0050] page:5:line:17 | 3/11/26
    [automated-vehicles-3-11-26-2-0051] page:5:line:18 | ENP-0112
    [automated-vehicles-3-11-26-2-0052] page:5:line:19 | 5
    [automated-vehicles-3-11-26-2-0053] page:6:line:1 | CONFUSING TERMS (A FEW EXAMPLES)
    [automated-vehicles-3-11-26-2-0054] page:6:line:2 | • Similar names but different concepts
    [automated-vehicles-3-11-26-2-0055] page:6:line:3 | • Remote assistance, remote driving, remote supervision, remote monitoring
    [automated-vehicles-3-11-26-2-0056] page:6:line:4 | (“Driverless” does not mean there is no human in the system…)
    [automated-vehicles-3-11-26-2-0057] page:6:line:5 | • Different acronym but same idea
    [automated-vehicles-3-11-26-2-0058] page:6:line:6 | • ADAS [Advanced Driver-Assistance System] **
    [automated-vehicles-3-11-26-2-0059] page:6:line:7 | • ADS [Automated Driving System]**
    [automated-vehicles-3-11-26-2-0060] page:6:line:8 | • Marketing-speak
    [automated-vehicles-3-11-26-2-0061] page:6:line:9 | • Fully self-driving, or even self-driving*
    [automated-vehicles-3-11-26-2-0062] page:6:line:10 | *A 2018 automation survey from the MIT Age Lab found that 22.7% of respondents said that self-
    [automated-vehicles-3-11-26-2-0063] page:6:line:11 | driving vehicles were available for purchase and 8.2% said yes to “Have you, or has someone you
    [automated-vehicles-3-11-26-2-0064] page:6:line:12 | know, ever driven or taken a ride in a vehicle you would describe as self-driving?”
    [automated-vehicles-3-11-26-2-0065] page:6:line:13 | **Not to be confused with DADDS (Driver
    [automated-vehicles-3-11-26-2-0066] page:6:line:14 | Alcohol Detection System for Safety)
    [automated-vehicles-3-11-26-2-0067] page:6:line:15 | 3/11/26
    [automated-vehicles-3-11-26-2-0068] page:6:line:16 | ENP-0112
    [automated-vehicles-3-11-26-2-0069] page:6:line:17 | 6
    [automated-vehicles-3-11-26-2-0070] page:7:line:1 | SAE LEVELS OF AUTOMATION
    [automated-vehicles-3-11-26-2-0071] page:7:line:2 | • SAE International
    [automated-vehicles-3-11-26-2-0072] page:7:line:3 | • Standards for aviation and automotive companies
    [automated-vehicles-3-11-26-2-0073] page:7:line:4 | • Industry-Recommended practices
    [automated-vehicles-3-11-26-2-0074] page:7:line:5 | • https://www.sae.org
    [automated-vehicles-3-11-26-2-0075] page:7:line:6 | • How is the document (J3016) used?
    [automated-vehicles-3-11-26-2-0076] page:7:line:7 | • Voluntary compliance
    [automated-vehicles-3-11-26-2-0077] page:7:line:8 | • Many factors are not addressed, e.g.,
    [automated-vehicles-3-11-26-2-0078] page:7:line:9 | • Standardization of vehicle behavior across vehicles/manufacturers
    [automated-vehicles-3-11-26-2-0079] page:7:line:10 | • Consumer education
    [automated-vehicles-3-11-26-2-0080] page:7:line:11 | • Maintenance of vehicle safety features
    [automated-vehicles-3-11-26-2-0081] page:7:line:12 | • Cost of the vehicle features
    [automated-vehicles-3-11-26-2-0082] page:7:line:13 | • Cost of insurance
    [automated-vehicles-3-11-26-2-0083] page:7:line:14 | • Risk of driver distraction with more automation?
    [automated-vehicles-3-11-26-2-0084] page:7:line:15 | 3/11/26
    [automated-vehicles-3-11-26-2-0085] page:7:line:16 | ENP-0112
    [automated-vehicles-3-11-26-2-0086] page:7:line:17 | 7
    [automated-vehicles-3-11-26-2-0087] page:8:line:1 | 3/11/26
    [automated-vehicles-3-11-26-2-0088] page:8:line:2 | ENP-0112
    [automated-vehicles-3-11-26-2-0089] page:8:line:3 | 8
    [automated-vehicles-3-11-26-2-0090] page:9:line:1 | TRANSLATION
    [automated-vehicles-3-11-26-2-0091] page:9:line:2 | 0. No automation. Driver is totally involved.
    [automated-vehicles-3-11-26-2-0092] page:9:line:3 | 1. Driver assistance – system handles steering or acceleration. Driver monitors.
    [automated-vehicles-3-11-26-2-0093] page:9:line:4 | 2. Partial driving automation – system handles steering and acceleration. Driver monitors.
    [automated-vehicles-3-11-26-2-0094] page:9:line:5 | 3. Conditional driving automation – human must monitor and respond. Driver is “fallback
    [automated-vehicles-3-11-26-2-0095] page:9:line:6 | ready.”
    [automated-vehicles-3-11-26-2-0096] page:9:line:7 | 4. High driving automation – full automation in limited contexts (ODDs). Driver has no role
    [automated-vehicles-3-11-26-2-0097] page:9:line:8 | when vehicle is in its ODD.
    [automated-vehicles-3-11-26-2-0098] page:9:line:9 | 5. Full driving automation – full automation in all contexts. Driver has no role unless
    [automated-vehicles-3-11-26-2-0099] page:9:line:10 | desired.
    [automated-vehicles-3-11-26-2-0100] page:9:line:11 | Driver handles OEDR
    [automated-vehicles-3-11-26-2-0101] page:9:line:12 | Driver is the fallback
    [automated-vehicles-3-11-26-2-0102] page:9:line:13 | System handles OEDR
    [automated-vehicles-3-11-26-2-0103] page:9:line:14 | System is the fallback.
    [automated-vehicles-3-11-26-2-0104] page:9:line:15 | 3/11/26
    [automated-vehicles-3-11-26-2-0105] page:9:line:16 | ENP-0112
    [automated-vehicles-3-11-26-2-0106] page:9:line:17 | 9
    [automated-vehicles-3-11-26-2-0107] page:10:line:1 | OVERSIGHT
    [automated-vehicles-3-11-26-2-0108] page:10:line:2 | • Approval of test sites is by State Department of Transportation (DOT)
    [automated-vehicles-3-11-26-2-0109] page:10:line:3 | • Federal Agencies involved
    [automated-vehicles-3-11-26-2-0110] page:10:line:4 | •
    [automated-vehicles-3-11-26-2-0111] page:10:line:5 | US DOT
    [automated-vehicles-3-11-26-2-0112] page:10:line:6 | •
    [automated-vehicles-3-11-26-2-0113] page:10:line:7 | https://www.transportation.gov/AV
    [automated-vehicles-3-11-26-2-0114] page:10:line:8 | •
    [automated-vehicles-3-11-26-2-0115] page:10:line:9 | National Highway Traffic Safety Administration (NHTSA)
    [automated-vehicles-3-11-26-2-0116] page:10:line:10 | •
    [automated-vehicles-3-11-26-2-0117] page:10:line:11 | https://www.nhtsa.gov/vehicle-safety/automated-vehicles-safety
    [automated-vehicles-3-11-26-2-0118] page:10:line:12 | •
    [automated-vehicles-3-11-26-2-0119] page:10:line:13 | Federal Transit Administration for public transit (e.g., buses, trains)
    [automated-vehicles-3-11-26-2-0120] page:10:line:14 | •
    [automated-vehicles-3-11-26-2-0121] page:10:line:15 | https://www.transit.dot.gov/research-innovation/strategic-transit-automation-research-plan-report-0116
    [automated-vehicles-3-11-26-2-0122] page:10:line:16 | •
    [automated-vehicles-3-11-26-2-0123] page:10:line:17 | Federal Motor Carrier Safety Administration (trucks)
    [automated-vehicles-3-11-26-2-0124] page:10:line:18 | •
    [automated-vehicles-3-11-26-2-0125] page:10:line:19 | https://www.fmcsa.dot.gov/research-and-analysis/technology/automated-cmv-evaluation-ace-program
    [automated-vehicles-3-11-26-2-0126] page:10:line:20 | • Some Federal laws that apply
    [automated-vehicles-3-11-26-2-0127] page:10:line:21 | •
    [automated-vehicles-3-11-26-2-0128] page:10:line:22 | Federal Motor Vehicle Safety Standards
    [automated-vehicles-3-11-26-2-0129] page:10:line:23 | •
    [automated-vehicles-3-11-26-2-0130] page:10:line:24 | American’s with Disabilities Act (ADA)
    [automated-vehicles-3-11-26-2-0131] page:10:line:25 | •
    [automated-vehicles-3-11-26-2-0132] page:10:line:26 | Buy America Act
    [automated-vehicles-3-11-26-2-0133] page:10:line:27 | 3/11/26
    [automated-vehicles-3-11-26-2-0134] page:10:line:28 | ENP-0112
    [automated-vehicles-3-11-26-2-0135] page:10:line:29 | 10
    [automated-vehicles-3-11-26-2-0136] page:11:line:1 | MITIGATIONS RELATED TO AUTOMATED
    [automated-vehicles-3-11-26-2-0137] page:11:line:2 | VEHICLES
    [automated-vehicles-3-11-26-2-0138] page:11:line:3 | 2/23/26
    [automated-vehicles-3-11-26-2-0139] page:11:line:4 | ENP-0112
    [automated-vehicles-3-11-26-2-0140] page:11:line:5 | 11
    [automated-vehicles-3-11-26-2-0141] page:11:line:6 | Individual
    [automated-vehicles-3-11-26-2-0142] page:11:line:7 | • Selection and training (Knowledge, Skills, and Abilities)
    [automated-vehicles-3-11-26-2-0143] page:11:line:8 | • Motivation, arousal (optimize attention)
    [automated-vehicles-3-11-26-2-0144] page:11:line:9 | Organization
    [automated-vehicles-3-11-26-2-0145] page:11:line:10 | • Policies and procedures (e.g., checklists)
    [automated-vehicles-3-11-26-2-0146] page:11:line:11 | • Safety culture
    [automated-vehicles-3-11-26-2-0147] page:11:line:12 | System Design
    [automated-vehicles-3-11-26-2-0148] page:11:line:13 | • Controls (soft or hard), “Usability” (e.g., visibility of system state, interaction
    [automated-vehicles-3-11-26-2-0149] page:11:line:14 | with data)
    [automated-vehicles-3-11-26-2-0150] page:11:line:15 | • Automated systems? (take the operator out of the system)
    [automated-vehicles-3-11-26-2-0151] page:11:line:16 | Operational Risk
    [automated-vehicles-3-11-26-2-0152] page:11:line:17 | • Variation across each operation (e.g., across flights)
    [automated-vehicles-3-11-26-2-0153] page:11:line:18 | • Work as imagined (theory) vs. work as done (reality)
    [automated-vehicles-3-11-26-2-0154] page:11:line:19 | Wide user population, relatively
    [automated-vehicles-3-11-26-2-0155] page:11:line:20 | little training and oversight
    [automated-vehicles-3-11-26-2-0156] page:11:line:21 | What is the “culture” of a driver?
    [automated-vehicles-3-11-26-2-0157] page:11:line:22 | How can it be influenced?
    [automated-vehicles-3-11-26-2-0158] page:11:line:23 | AV designers can
    [automated-vehicles-3-11-26-2-0159] page:11:line:24 | address these
    [automated-vehicles-3-11-26-2-0160] page:12:line:1 | AUTOMATION AND DRIVING
    [automated-vehicles-3-11-26-2-0161] page:12:line:2 | More on April 8 with Guest Lecturer Prof. Shannon Roberts (UMass)
    [automated-vehicles-3-11-26-2-0162] page:12:line:3 | 3/11/26
    [automated-vehicles-3-11-26-2-0163] page:12:line:4 | ENP-0112
    [automated-vehicles-3-11-26-2-0164] page:12:line:5 | 12
    [automated-vehicles-3-11-26-2-0165] page:13:line:1 | WHY AUTOMATE?
    [automated-vehicles-3-11-26-2-0166] page:13:line:2 | • Reduce workload
    [automated-vehicles-3-11-26-2-0167] page:13:line:3 | • Car cruise control, wing-leveler, heading hold
    [automated-vehicles-3-11-26-2-0168] page:13:line:4 | • Offload “boring” tasks
    [automated-vehicles-3-11-26-2-0169] page:13:line:5 | • Make task easier, more comfortable
    [automated-vehicles-3-11-26-2-0170] page:13:line:6 | • Improve safety
    [automated-vehicles-3-11-26-2-0171] page:13:line:7 | • Perform tasks that are more ‘difficult’ or dangerous for humans
    [automated-vehicles-3-11-26-2-0172] page:13:line:8 | • Extend human capabilities
    [automated-vehicles-3-11-26-2-0173] page:13:line:9 | • More efficiency, precision, flexibility
    [automated-vehicles-3-11-26-2-0174] page:13:line:10 | • Reduce costs
    [automated-vehicles-3-11-26-2-0175] page:13:line:11 | • Reduce staff...e.g., flight engineer  or longer duty hours allowable for AVs?
    [automated-vehicles-3-11-26-2-0176] page:13:line:12 | • Because we can…?
    [automated-vehicles-3-11-26-2-0177] page:13:line:13 | From 1/26/26  lecture on automation in aviation
    [automated-vehicles-3-11-26-2-0178] page:13:line:14 | 3/11/26
    [automated-vehicles-3-11-26-2-0179] page:13:line:15 | ENP-0112
    [automated-vehicles-3-11-26-2-0180] page:13:line:16 | 13
    [automated-vehicles-3-11-26-2-0181] page:14:line:1 | “USE” OF AUTOMATION
    [automated-vehicles-3-11-26-2-0182] page:14:line:2 | • Use: Voluntary activation or disengagement of automation by human operators
    [automated-vehicles-3-11-26-2-0183] page:14:line:3 | • Misuse: Overreliance on automation, which can result in failures of monitoring or
    [automated-vehicles-3-11-26-2-0184] page:14:line:4 | decision biases
    [automated-vehicles-3-11-26-2-0185] page:14:line:5 | • Disuse: Neglect or underutilization of automation
    [automated-vehicles-3-11-26-2-0186] page:14:line:6 | • Abuse: Automation of functions without due regard for the consequences for human
    [automated-vehicles-3-11-26-2-0187] page:14:line:7 | performance
    [automated-vehicles-3-11-26-2-0188] page:14:line:8 | Parasuraman, R., & Riley, V. (1997). Humans and automation: Use,
    [automated-vehicles-3-11-26-2-0189] page:14:line:9 | misuse, disuse, abuse. Human Factors, 39, 230-253.
    [automated-vehicles-3-11-26-2-0190] page:14:line:10 | 3/11/26
    [automated-vehicles-3-11-26-2-0191] page:14:line:11 | ENP-0112
    [automated-vehicles-3-11-26-2-0192] page:14:line:12 | 14
    [automated-vehicles-3-11-26-2-0193] page:15:line:1 | CALIBRATED TRUST IN AUTOMATION
    [automated-vehicles-3-11-26-2-0194] page:15:line:2 | Lee J, See K. Trust in automation: Designing for appropriate reliance. Human Factors 46(1):50-80, 2004.
    [automated-vehicles-3-11-26-2-0195] page:15:line:3 | 3/11/26
    [automated-vehicles-3-11-26-2-0196] page:15:line:4 | ENP-0112
    [automated-vehicles-3-11-26-2-0197] page:15:line:5 | 15
    [automated-vehicles-3-11-26-2-0198] page:16:line:1 | SOME POTENTIAL CONSEQUENCES OF
    [automated-vehicles-3-11-26-2-0199] page:16:line:2 | FLIGHT DECK CAR AUTOMATION
    [automated-vehicles-3-11-26-2-0200] page:16:line:3 | • Boredom, complacency, lack of appropriate response in an emergency
    [automated-vehicles-3-11-26-2-0201] page:16:line:4 | • Misunderstanding or lack of knowledge of what automation is doing/considering
    [automated-vehicles-3-11-26-2-0202] page:16:line:5 | • Error in data entry/interaction
    [automated-vehicles-3-11-26-2-0203] page:16:line:6 | • Overconfidence in automation
    [automated-vehicles-3-11-26-2-0204] page:16:line:7 | • False alarms
    [automated-vehicles-3-11-26-2-0205] page:16:line:8 | • Mode confusion
    [automated-vehicles-3-11-26-2-0206] page:16:line:9 | (1/26/26 lecture)
    [automated-vehicles-3-11-26-2-0207] page:16:line:10 | 3/11/26
    [automated-vehicles-3-11-26-2-0208] page:16:line:11 | ENP-0112
    [automated-vehicles-3-11-26-2-0209] page:16:line:12 | 16
    [automated-vehicles-3-11-26-2-0210] page:17:line:1 | FROM 2011…
    [automated-vehicles-3-11-26-2-0211] page:17:line:2 | How do these look
    [automated-vehicles-3-11-26-2-0212] page:17:line:3 | today?
    [automated-vehicles-3-11-26-2-0213] page:17:line:4 | There are still legal
    [automated-vehicles-3-11-26-2-0214] page:17:line:5 | and other unknowns.
    [automated-vehicles-3-11-26-2-0215] page:17:line:6 | What else?
    [automated-vehicles-3-11-26-2-0216] page:17:line:7 | (1/26/26 lecture)
    [automated-vehicles-3-11-26-2-0217] page:17:line:8 | 3/11/26
    [automated-vehicles-3-11-26-2-0218] page:17:line:9 | ENP-0112
    [automated-vehicles-3-11-26-2-0219] page:17:line:10 | 17
    [automated-vehicles-3-11-26-2-0220] page:18:line:1 | EVOLVING AUTOMATION PHILOSOPHIES
    [automated-vehicles-3-11-26-2-0221] page:18:line:2 | • The automated system has final authority.
    [automated-vehicles-3-11-26-2-0222] page:18:line:3 | • Keep the pilot/driver from doing something foolish.
    [automated-vehicles-3-11-26-2-0223] page:18:line:4 | • The pilot driver has final authority.
    [automated-vehicles-3-11-26-2-0224] page:18:line:5 | • Keep the automation from doing something foolish.
    [automated-vehicles-3-11-26-2-0225] page:18:line:6 | • Something in between?
    [automated-vehicles-3-11-26-2-0226] page:18:line:7 | • Adaptive or adaptable automation?
    [automated-vehicles-3-11-26-2-0227] page:18:line:8 | • Sharing authority?
    [automated-vehicles-3-11-26-2-0228] page:18:line:9 | • Team work?
    [automated-vehicles-3-11-26-2-0229] page:18:line:10 | (1/26/26 lecture)
    [automated-vehicles-3-11-26-2-0230] page:18:line:11 | 3/11/26
    [automated-vehicles-3-11-26-2-0231] page:18:line:12 | ENP-0112
    [automated-vehicles-3-11-26-2-0232] page:18:line:13 | 18
    [automated-vehicles-3-11-26-2-0233] page:19:line:1 | THOUGHTS ABOUT AUTOMATION
    [automated-vehicles-3-11-26-2-0234] page:19:line:2 | • Capabilities will continue to improve
    [automated-vehicles-3-11-26-2-0235] page:19:line:3 | • Use of automation/autonomy is intended to reduce cost and staffing and improve safety, but the
    [automated-vehicles-3-11-26-2-0236] page:19:line:4 | opposite can occur
    [automated-vehicles-3-11-26-2-0237] page:19:line:5 | • Moving from demonstration to real world is challenging
    [automated-vehicles-3-11-26-2-0238] page:19:line:6 | • Creeping complexity
    [automated-vehicles-3-11-26-2-0239] page:19:line:7 | • Exhaustive testing of complex systems is not possible
    [automated-vehicles-3-11-26-2-0240] page:19:line:8 | • Bainbridge, Ironies of Automation, 1983
    [automated-vehicles-3-11-26-2-0241] page:19:line:9 | “…the more advanced a control system is… the more crucial may be the contribution of the human operator.”
    [automated-vehicles-3-11-26-2-0242] page:19:line:10 | • Reimer, 2023 Webinar
    [automated-vehicles-3-11-26-2-0243] page:19:line:11 | • “Robots make mistakes too.”
    [automated-vehicles-3-11-26-2-0244] page:19:line:12 | • “Electrification of vehicles provides performance characteristics and incredible acceleration.”
    [automated-vehicles-3-11-26-2-0245] page:19:line:13 | • “Automation and electrification offer opportunities for a better system, but they need to be combined together
    [automated-vehicles-3-11-26-2-0246] page:19:line:14 | with human understanding and human expertise.”
    [automated-vehicles-3-11-26-2-0247] page:19:line:15 | 3/11/26
    [automated-vehicles-3-11-26-2-0248] page:19:line:16 | ENP-0112
    [automated-vehicles-3-11-26-2-0249] page:19:line:17 | 19
    [automated-vehicles-3-11-26-2-0250] page:20:line:1 | DRIVING VS. FLYING
    [automated-vehicles-3-11-26-2-0251] page:20:line:2 | 3/11/26
    [automated-vehicles-3-11-26-2-0252] page:20:line:3 | ENP-0112
    [automated-vehicles-3-11-26-2-0253] page:20:line:4 | 20
    [automated-vehicles-3-11-26-2-0254] page:21:line:1 | DIMENSIONS FOR COMPARING FLYING VS. DRIVING
    [automated-vehicles-3-11-26-2-0255] page:21:line:2 | Driving
    [automated-vehicles-3-11-26-2-0256] page:21:line:3 | Flying
    [automated-vehicles-3-11-26-2-0257] page:21:line:4 | 3/11/26
    [automated-vehicles-3-11-26-2-0258] page:21:line:5 | ENP-0112
    [automated-vehicles-3-11-26-2-0259] page:21:line:6 | 21
    [automated-vehicles-3-11-26-2-0260] page:22:line:1 | MANAGING RISK: OPERATIONAL COMPLEXITY IN
    [automated-vehicles-3-11-26-2-0261] page:22:line:2 | FLIGHT OPERATIONS – DRIVING: THE “ODD”
    [automated-vehicles-3-11-26-2-0262] page:22:line:3 | Operational Complexity
    [automated-vehicles-3-11-26-2-0263] page:22:line:4 | • ATC interventions
    [automated-vehicles-3-11-26-2-0264] page:22:line:5 | • Aircraft Vehicle equipment or
    [automated-vehicles-3-11-26-2-0265] page:22:line:6 | performance
    [automated-vehicles-3-11-26-2-0266] page:22:line:7 | • Crew Driver factors
    [automated-vehicles-3-11-26-2-0267] page:22:line:8 | • Operator factors
    [automated-vehicles-3-11-26-2-0268] page:22:line:9 | • Environment factors
    [automated-vehicles-3-11-26-2-0269] page:22:line:10 | Aircraft Vehicle Factors
    [automated-vehicles-3-11-26-2-0270] page:22:line:11 | •
    [automated-vehicles-3-11-26-2-0271] page:22:line:12 | Lack or unreliability of
    [automated-vehicles-3-11-26-2-0272] page:22:line:13 | automated systems
    [automated-vehicles-3-11-26-2-0273] page:22:line:14 | •
    [automated-vehicles-3-11-26-2-0274] page:22:line:15 | Performance characteristics
    [automated-vehicles-3-11-26-2-0275] page:22:line:16 | ATC Intervention (such as)
    [automated-vehicles-3-11-26-2-0276] page:22:line:17 | •
    [automated-vehicles-3-11-26-2-0277] page:22:line:18 | (Late) route amendments
    [automated-vehicles-3-11-26-2-0278] page:22:line:19 | •
    [automated-vehicles-3-11-26-2-0279] page:22:line:20 | Unpublished restrictions
    [automated-vehicles-3-11-26-2-0280] page:22:line:21 | •
    [automated-vehicles-3-11-26-2-0281] page:22:line:22 | Vectors
    [automated-vehicles-3-11-26-2-0282] page:22:line:23 | Environment Factors
    [automated-vehicles-3-11-26-2-0283] page:22:line:24 | •
    [automated-vehicles-3-11-26-2-0284] page:22:line:25 | Terrain
    [automated-vehicles-3-11-26-2-0285] page:22:line:26 | •
    [automated-vehicles-3-11-26-2-0286] page:22:line:27 | Traffic
    [automated-vehicles-3-11-26-2-0287] page:22:line:28 | •
    [automated-vehicles-3-11-26-2-0288] page:22:line:29 | Weather
    [automated-vehicles-3-11-26-2-0289] page:22:line:30 | •
    [automated-vehicles-3-11-26-2-0290] page:22:line:31 | Prohibited  airspace roads
    [automated-vehicles-3-11-26-2-0291] page:22:line:32 | Operator Factors
    [automated-vehicles-3-11-26-2-0292] page:22:line:33 | •
    [automated-vehicles-3-11-26-2-0293] page:22:line:34 | Independence vs. dependence
    [automated-vehicles-3-11-26-2-0294] page:22:line:35 | on Dispatch
    [automated-vehicles-3-11-26-2-0295] page:22:line:36 | •
    [automated-vehicles-3-11-26-2-0296] page:22:line:37 | Clarity and consistency of
    [automated-vehicles-3-11-26-2-0297] page:22:line:38 | pilot roles in reviewing route
    [automated-vehicles-3-11-26-2-0298] page:22:line:39 | Crew Driver Factors
    [automated-vehicles-3-11-26-2-0299] page:22:line:40 | •
    [automated-vehicles-3-11-26-2-0300] page:22:line:41 | Expectations (confirmation bias)
    [automated-vehicles-3-11-26-2-0301] page:22:line:42 | •
    [automated-vehicles-3-11-26-2-0302] page:22:line:43 | Fatigue
    [automated-vehicles-3-11-26-2-0303] page:22:line:44 | •
    [automated-vehicles-3-11-26-2-0304] page:22:line:45 | Communication style
    [automated-vehicles-3-11-26-2-0305] page:22:line:46 | •
    [automated-vehicles-3-11-26-2-0306] page:22:line:47 | Distractions
    [automated-vehicles-3-11-26-2-0307] page:22:line:48 | •
    [automated-vehicles-3-11-26-2-0308] page:22:line:49 | Local area familiarity
    [automated-vehicles-3-11-26-2-0309] page:22:line:50 | •
    [automated-vehicles-3-11-26-2-0310] page:22:line:51 | Familiarity with different types of
    [automated-vehicles-3-11-26-2-0311] page:22:line:52 | routes
    [automated-vehicles-3-11-26-2-0312] page:22:line:53 | (2/18/26 lecture)
    [automated-vehicles-3-11-26-2-0313] page:22:line:54 | 3/11/26
    [automated-vehicles-3-11-26-2-0314] page:22:line:55 | ENP-0112
    [automated-vehicles-3-11-26-2-0315] page:22:line:56 | 22
    [automated-vehicles-3-11-26-2-0316] page:23:line:1 | MORE DRIVING VS. FLYING
    [automated-vehicles-3-11-26-2-0317] page:23:line:2 | Driving
    [automated-vehicles-3-11-26-2-0318] page:23:line:3 | • Relatively little training or currency
    [automated-vehicles-3-11-26-2-0319] page:23:line:4 | checks
    [automated-vehicles-3-11-26-2-0320] page:23:line:5 | • Wider population of operators
    [automated-vehicles-3-11-26-2-0321] page:23:line:6 | • Could stop and reset/review
    [automated-vehicles-3-11-26-2-0322] page:23:line:7 | • “Operational design domain” (ODD)
    [automated-vehicles-3-11-26-2-0323] page:23:line:8 | • Safety? (Private vs. Public risk)
    [automated-vehicles-3-11-26-2-0324] page:23:line:9 | Flying
    [automated-vehicles-3-11-26-2-0325] page:23:line:10 | • Intensive training and currency reviews
    [automated-vehicles-3-11-26-2-0326] page:23:line:11 | • Relatively limited set of operators
    [automated-vehicles-3-11-26-2-0327] page:23:line:12 | • Certifications and approval of both pilots
    [automated-vehicles-3-11-26-2-0328] page:23:line:13 | and aircraft
    [automated-vehicles-3-11-26-2-0329] page:23:line:14 | • ATC monitors flights and can aid in
    [automated-vehicles-3-11-26-2-0330] page:23:line:15 | emergencies
    [automated-vehicles-3-11-26-2-0331] page:23:line:16 | • Always in motion
    [automated-vehicles-3-11-26-2-0332] page:23:line:17 | • Public expects high safety levels for
    [automated-vehicles-3-11-26-2-0333] page:23:line:18 | commercial operations
    [automated-vehicles-3-11-26-2-0334] page:23:line:19 | 3/11/26
    [automated-vehicles-3-11-26-2-0335] page:23:line:20 | ENP-0112
    [automated-vehicles-3-11-26-2-0336] page:23:line:21 | 23
    [automated-vehicles-3-11-26-2-0337] page:24:line:1 | LINKS AND RESOURCES
    [automated-vehicles-3-11-26-2-0338] page:24:line:2 | •
    [automated-vehicles-3-11-26-2-0339] page:24:line:3 | SAE
    [automated-vehicles-3-11-26-2-0340] page:24:line:4 | •
    [automated-vehicles-3-11-26-2-0341] page:24:line:5 | https://www.sae.org
    [automated-vehicles-3-11-26-2-0342] page:24:line:6 | •
    [automated-vehicles-3-11-26-2-0343] page:24:line:7 | https://www.sae.org/news/2021/06/sae-revises-levels-of-driving-automation
    [automated-vehicles-3-11-26-2-0344] page:24:line:8 | •
    [automated-vehicles-3-11-26-2-0345] page:24:line:9 | Driving
    [automated-vehicles-3-11-26-2-0346] page:24:line:10 | •
    [automated-vehicles-3-11-26-2-0347] page:24:line:11 | The Simpsons - Robotic truck driving video
    [automated-vehicles-3-11-26-2-0348] page:24:line:12 | •
    [automated-vehicles-3-11-26-2-0349] page:24:line:13 | Tesla marketing:
    [automated-vehicles-3-11-26-2-0350] page:24:line:14 | •
    [automated-vehicles-3-11-26-2-0351] page:24:line:15 | Autopilot and Full Self-Driving Capability.
    [automated-vehicles-3-11-26-2-0352] page:24:line:16 | •
    [automated-vehicles-3-11-26-2-0353] page:24:line:17 | https://www.tesla.com/support/autopilot
    [automated-vehicles-3-11-26-2-0354] page:24:line:18 | •
    [automated-vehicles-3-11-26-2-0355] page:24:line:19 | National Highway Traffic Safety Administration (NHTSA)
    [automated-vehicles-3-11-26-2-0356] page:24:line:20 | •
    [automated-vehicles-3-11-26-2-0357] page:24:line:21 | https://www.nhtsa.gov/technology-innovation/automated-vehicles-safety
    [automated-vehicles-3-11-26-2-0358] page:24:line:22 | •
    [automated-vehicles-3-11-26-2-0359] page:24:line:23 | https://www.nhtsa.gov/vehicle-manufacturers/automated-driving-systems
    [automated-vehicles-3-11-26-2-0360] page:24:line:24 | •
    [automated-vehicles-3-11-26-2-0361] page:24:line:25 | https://www.transportation.gov/briefing-room/trump-administration-releases-“ensuring-american-leadership-automated-vehicle
    [automated-vehicles-3-11-26-2-0362] page:24:line:26 | •
    [automated-vehicles-3-11-26-2-0363] page:24:line:27 | https://www.transportation.gov/AV
    [automated-vehicles-3-11-26-2-0364] page:24:line:28 | •
    [automated-vehicles-3-11-26-2-0365] page:24:line:29 | MIT Age Lab, Transportation
    [automated-vehicles-3-11-26-2-0366] page:24:line:30 | •
    [automated-vehicles-3-11-26-2-0367] page:24:line:31 | https://agelab.mit.edu/transportation-and-livable-communities/overview/
    [automated-vehicles-3-11-26-2-0368] page:24:line:32 | •
    [automated-vehicles-3-11-26-2-0369] page:24:line:33 | Video from Sept 20, 2023 ”ADAS in the Wild”
    [automated-vehicles-3-11-26-2-0370] page:24:line:34 | •
    [automated-vehicles-3-11-26-2-0371] page:24:line:35 | https://youtu.be/DUaYzxZsAig?feature=shared
    [automated-vehicles-3-11-26-2-0372] page:24:line:36 | 3/11/26
    [automated-vehicles-3-11-26-2-0373] page:24:line:37 | ENP-0112
    [automated-vehicles-3-11-26-2-0374] page:24:line:38 | 24
    ```
