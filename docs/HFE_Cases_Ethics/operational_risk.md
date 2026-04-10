# Operational Risk

Operational risk 这页要你看到的，是风险不只存在于某一次错误动作里，而是长期藏在运行条件、组织约束和 work as done 里。

!!! note "本页主问题"
    为什么真正的运行风险往往不是一次事件才突然出现，而是系统在日常运行中慢慢积累出来的？

## 本章重点

- operational risk 关注的是日常运行系统，而不只是单次失误。
- work as imagined 和 work as done 往往存在结构性差距。
- 组织约束、时间压力、环境变化和一线补丁行为会持续重塑风险水平。
- 这页把 Swiss Cheese、fatigue、stress、procedure 等页面重新拉回同一运行视角。

## 先记住一句话

!!! tip "复习时先记住这句话"
    先记住一句话：运行风险不是事故发生后才有的东西，它通常在事故前很久就已经存在于工作条件里。

## operational risk 到底在看什么

这页关心的不是单个动作的对错，而是系统在持续运行时有没有逐步变脆。换句话说，它问的是：班次、资源、流程、组织目标和现场补救行为，是否正在侵蚀原本设计好的安全边界。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/operational-risk-2-18-2026/page-01.png" alt="这张图要看懂的是：运行风险不是单点问题，而是随着运行条件持续变化的一组系统约束。" loading="lazy">
  <figcaption>这张图要看懂的是：运行风险不是单点问题，而是随着运行条件持续变化的一组系统约束。</figcaption>
</figure>

!!! warning "最容易误解的地方"
    不要把 operational risk 理解成“又一个风险清单”。它更像是一种持续追问运行条件是否在侵蚀防线的视角。

## 为什么 work as imagined 和 work as done 的差距会变成风险

管理和设计往往先写出一个理想流程，但一线工作会受到时间压力、设备状态、环境变化和资源限制影响。如果系统长期只检查“有没有按理想流程做”，却不看实际工作如何被挤压和变形，风险就会被低估。

!!! example "案例：为什么长期 workaround 会变成运行风险信号"
    如果一线人员长期用临时补丁绕过某条程序，那通常不是“员工不守规矩”这么简单，而是一个更深的运行信号：程序可能已经不再适配真实任务节奏，系统正在靠脆弱补丁维持表面正常。

## 这页为什么会成为很多案例页的底板

很多案例页最后都会回到 operational risk，因为一线错误很少是孤立的。背后常常已经累积了长期的组织张力、任务负荷和现实约束，而这些因素平时就已经在慢慢改变风险结构。

!!! note "一句话结论"
    operational risk 的价值，是提醒你把事故看成运行系统的产物，而不是看成单次偶发偏差。

## 这套概念怎么真正拿来判断问题

把概念页真正用起来时，不要停在定义。更实用的读法是固定沿着三步走：

1. 先定位当前任务和场景是什么。
2. 再问这页讲的限制、机制或风险，在这个场景里会怎样出现。
3. 最后把判断落回设计、流程、训练或组织改进。

这样概念才不会停在“知道术语”，而会变成“会分析问题”。

## 本章总结

!!! tip "复习时重点记这几条"
    - operational risk 关注的是持续运行中的风险生成。
    - 理想流程和真实工作之间的差距会不断改变风险水平。
    - 组织约束和 workaround 是重要风险信号。
    - 这页为后面的案例分析提供系统运行视角。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `案例与伦理`
- 关联源文件数: 1
- 文本单元数: 251
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Operational Risk 2-18-2026.pdf` | `pdf` | 251 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Operational Risk 2-18-2026.pdf) |

## 相关主题

- [Swiss Cheese 模型](../HFE_Foundations/swiss_cheese.md)
- [错误分析与调查流程](../HFE_Risk_Methods/error_analysis_methods.md)
- [检查单与程序](../HFE_Aviation_Automation/checklists_and_procedures.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "Operational Risk 2-18-2026.pdf | 251 text units"
    下载原件: [Operational Risk 2-18-2026.pdf](../assets/source_files/Lectures_Spring_2026/Operational Risk 2-18-2026.pdf)
    映射页面: `operational_risk`
    
    ```text
    [operational-risk-2-18-2026-0001] page:1:line:1 | OPERATIONAL RISK
    [operational-risk-2-18-2026-0002] page:1:line:2 | ENP-0112
    [operational-risk-2-18-2026-0003] page:1:line:3 | 2/18/2026
    [operational-risk-2-18-2026-0004] page:1:line:4 | Dr. Divya C. Chandra
    [operational-risk-2-18-2026-0005] page:1:line:5 | Hurricane Helene
    [operational-risk-2-18-2026-0006] page:1:line:6 | September 2024
    [operational-risk-2-18-2026-0007] page:2:line:1 | MITIGATIONS
    [operational-risk-2-18-2026-0008] page:2:line:2 | 2/18/26
    [operational-risk-2-18-2026-0009] page:2:line:3 | ENP-0112
    [operational-risk-2-18-2026-0010] page:2:line:4 | 2
    [operational-risk-2-18-2026-0011] page:2:line:5 | Individual
    [operational-risk-2-18-2026-0012] page:2:line:6 | • Selection and training (Knowledge, Skills, and Abilities)
    [operational-risk-2-18-2026-0013] page:2:line:7 | • Motivation, arousal (optimize attention)
    [operational-risk-2-18-2026-0014] page:2:line:8 | Organization
    [operational-risk-2-18-2026-0015] page:2:line:9 | • Policies and procedures (e.g., checklists)
    [operational-risk-2-18-2026-0016] page:2:line:10 | • Safety culture
    [operational-risk-2-18-2026-0017] page:2:line:11 | System Design
    [operational-risk-2-18-2026-0018] page:2:line:12 | • Controls (soft or hard), “Usability” (e.g., visibility of system state, interaction
    [operational-risk-2-18-2026-0019] page:2:line:13 | with data)
    [operational-risk-2-18-2026-0020] page:2:line:14 | • Automated systems? (take the operator out of the system)
    [operational-risk-2-18-2026-0021] page:2:line:15 | Operational Risk
    [operational-risk-2-18-2026-0022] page:2:line:16 | • Variation across each operation (e.g., across flights)
    [operational-risk-2-18-2026-0023] page:2:line:17 | • Work as imagined (theory) vs. work as done (reality)
    [operational-risk-2-18-2026-0024] page:2:line:18 | CRM
    [operational-risk-2-18-2026-0025] page:2:line:19 | Monitoring
    [operational-risk-2-18-2026-0026] page:2:line:20 | Fatigue
    [operational-risk-2-18-2026-0027] page:2:line:21 | Displays and Alerts
    [operational-risk-2-18-2026-0028] page:3:line:1 | TOPICS
    [operational-risk-2-18-2026-0029] page:3:line:2 | • Operations
    [operational-risk-2-18-2026-0030] page:3:line:3 | • Threat and error framework, sources of risk
    [operational-risk-2-18-2026-0031] page:3:line:4 | • Safety 1 and Safety 2
    [operational-risk-2-18-2026-0032] page:3:line:5 | • Human error vs. human contribution to safety
    [operational-risk-2-18-2026-0033] page:3:line:6 | • Analysis of a sample ASRS event
    [operational-risk-2-18-2026-0034] page:3:line:7 | • Limitations
    [operational-risk-2-18-2026-0035] page:3:line:8 | • What was the pilot’s contribution to safety?
    [operational-risk-2-18-2026-0036] page:3:line:9 | 2/18/26
    [operational-risk-2-18-2026-0037] page:3:line:10 | ENP-0112
    [operational-risk-2-18-2026-0038] page:3:line:11 | 3
    [operational-risk-2-18-2026-0039] page:4:line:1 | OPERATIONS
    [operational-risk-2-18-2026-0040] page:4:line:2 | 2/18/26
    [operational-risk-2-18-2026-0041] page:4:line:3 | ENP-0112
    [operational-risk-2-18-2026-0042] page:4:line:4 | 4
    [operational-risk-2-18-2026-0043] page:5:line:1 | THREAT AND ERROR MANAGEMENT (TEM)
    [operational-risk-2-18-2026-0044] page:5:line:2 | FRAMEWORK
    [operational-risk-2-18-2026-0045] page:5:line:3 | • Threats and errors are part of everyday aviation operations that must be managed by aviation
    [operational-risk-2-18-2026-0046] page:5:line:4 | professionals.
    [operational-risk-2-18-2026-0047] page:5:line:5 | • Undesired states carry the potential for unsafe outcomes.
    [operational-risk-2-18-2026-0048] page:5:line:6 | • Undesired state management largely represents the last opportunity to avoid an unsafe outcome and
    [operational-risk-2-18-2026-0049] page:5:line:7 | thus maintain safety margins in aviation operations.
    [operational-risk-2-18-2026-0050] page:5:line:8 | • TEM is analogous to “defensive driving.” It emphasizes techniques that minimize risks related to
    [operational-risk-2-18-2026-0051] page:5:line:9 | safety.
    [operational-risk-2-18-2026-0052] page:5:line:10 | 2/18/26
    [operational-risk-2-18-2026-0053] page:5:line:11 | ENP-0112
    [operational-risk-2-18-2026-0054] page:5:line:12 | 5
    [operational-risk-2-18-2026-0055] page:5:line:13 | https://skybrary.aero/articles/threat-and-error-management-tem
    [operational-risk-2-18-2026-0056] page:5:line:14 | Merritt & Klinect (2006). Defensive Flying for Pilots: An Introduction to Threat and
    [operational-risk-2-18-2026-0057] page:5:line:15 | Error Management. https://skybrary.aero/sites/default/files/bookshelf/1982.pdf
    [operational-risk-2-18-2026-0058] page:6:line:1 | ORIGINS OF TEM
    [operational-risk-2-18-2026-0059] page:6:line:2 | Do the concepts taught in training transfer to normal everyday flight operations?
    [operational-risk-2-18-2026-0060] page:6:line:3 | • Assess through Line Operations Safety Audits (LOSA), now the LOSA Collaborative. (Originally a
    [operational-risk-2-18-2026-0061] page:6:line:4 | partnership between University of Texas researchers and airlines.)
    [operational-risk-2-18-2026-0062] page:6:line:5 | • Designed to assess the effectiveness of CRM training, expanded to address error and its
    [operational-risk-2-18-2026-0063] page:6:line:6 | management.
    [operational-risk-2-18-2026-0064] page:6:line:7 | • FAA endorses LOSA as a voluntary safety program (FAA AC 120-90)
    [operational-risk-2-18-2026-0065] page:6:line:8 | 2/18/26
    [operational-risk-2-18-2026-0066] page:6:line:9 | ENP-0112
    [operational-risk-2-18-2026-0067] page:6:line:10 | 6
    [operational-risk-2-18-2026-0068] page:7:line:1 | THREAT DEFINITION
    [operational-risk-2-18-2026-0069] page:7:line:2 | • Threats are events or errors that
    [operational-risk-2-18-2026-0070] page:7:line:3 | • Occur outside the influence of the flight crew (i.e., not caused by the crew)
    [operational-risk-2-18-2026-0071] page:7:line:4 | • Increase the operational complexity of a flight, and
    [operational-risk-2-18-2026-0072] page:7:line:5 | • Require crew attention and management if safety margins are to be maintained
    [operational-risk-2-18-2026-0073] page:7:line:6 | • Examples
    [operational-risk-2-18-2026-0074] page:7:line:7 | • High terrain, icing conditions, aircraft malfunction, other people’s errors (e.g., dispatcher error)
    [operational-risk-2-18-2026-0075] page:7:line:8 | • Two categories
    [operational-risk-2-18-2026-0076] page:7:line:9 | • Environmental threats are outside the control of the airline
    [operational-risk-2-18-2026-0077] page:7:line:10 | • Airline threats originate from the flight operations (e.g., aircraft malfunctions)
    [operational-risk-2-18-2026-0078] page:7:line:11 | • All are independent of flight crew, but must be managed by the crew
    [operational-risk-2-18-2026-0079] page:7:line:12 | 2/18/26
    [operational-risk-2-18-2026-0080] page:7:line:13 | ENP-0112
    [operational-risk-2-18-2026-0081] page:7:line:14 | 7
    [operational-risk-2-18-2026-0082] page:8:line:1 | ERROR DEFINITION
    [operational-risk-2-18-2026-0083] page:8:line:2 | • Errors are defined as flight crew actions or inactions that
    [operational-risk-2-18-2026-0084] page:8:line:3 | • Lead to a deviation from crew or organizational intentions or expectations
    [operational-risk-2-18-2026-0085] page:8:line:4 | • Reduce safety margins; and
    [operational-risk-2-18-2026-0086] page:8:line:5 | • Increase the probability of adverse operational events on the ground or during flight
    [operational-risk-2-18-2026-0087] page:8:line:6 | • Examples – Three Categories
    [operational-risk-2-18-2026-0088] page:8:line:7 | • Aircraft handling, e.g., errors related to manual flying, or managing automated systems
    [operational-risk-2-18-2026-0089] page:8:line:8 | • Communication errors, e.g., related to ATC communications, or pilot-to-pilot comms
    [operational-risk-2-18-2026-0090] page:8:line:9 | • Procedural errors, e.g., deviations from regulations or  standard operating procedures)
    [operational-risk-2-18-2026-0091] page:8:line:10 | 2/18/26
    [operational-risk-2-18-2026-0092] page:8:line:11 | ENP-0112
    [operational-risk-2-18-2026-0093] page:8:line:12 | 8
    [operational-risk-2-18-2026-0094] page:9:line:1 | MANAGING RISK: OPERATIONAL COMPLEXITY IN
    [operational-risk-2-18-2026-0095] page:9:line:2 | FLIGHT OPERATIONS
    [operational-risk-2-18-2026-0096] page:9:line:3 | 2/18/26
    [operational-risk-2-18-2026-0097] page:9:line:4 | ENP-0112
    [operational-risk-2-18-2026-0098] page:9:line:5 | 9
    [operational-risk-2-18-2026-0099] page:9:line:6 | Sources of Operational Complexity
    [operational-risk-2-18-2026-0100] page:9:line:7 | • ATC interventions
    [operational-risk-2-18-2026-0101] page:9:line:8 | • Aircraft equipment or performance
    [operational-risk-2-18-2026-0102] page:9:line:9 | • Crew factors
    [operational-risk-2-18-2026-0103] page:9:line:10 | • Operator factors
    [operational-risk-2-18-2026-0104] page:9:line:11 | • Environment factors
    [operational-risk-2-18-2026-0105] page:9:line:12 | Aircraft Factors
    [operational-risk-2-18-2026-0106] page:9:line:13 | •
    [operational-risk-2-18-2026-0107] page:9:line:14 | Lack or unreliability of automated
    [operational-risk-2-18-2026-0108] page:9:line:15 | systems
    [operational-risk-2-18-2026-0109] page:9:line:16 | •
    [operational-risk-2-18-2026-0110] page:9:line:17 | Performance characteristics
    [operational-risk-2-18-2026-0111] page:9:line:18 | ATC Intervention (such as)
    [operational-risk-2-18-2026-0112] page:9:line:19 | •
    [operational-risk-2-18-2026-0113] page:9:line:20 | (Late) route amendments
    [operational-risk-2-18-2026-0114] page:9:line:21 | •
    [operational-risk-2-18-2026-0115] page:9:line:22 | Unpublished restrictions
    [operational-risk-2-18-2026-0116] page:9:line:23 | •
    [operational-risk-2-18-2026-0117] page:9:line:24 | Vectors
    [operational-risk-2-18-2026-0118] page:9:line:25 | Environment Factors
    [operational-risk-2-18-2026-0119] page:9:line:26 | •
    [operational-risk-2-18-2026-0120] page:9:line:27 | Terrain
    [operational-risk-2-18-2026-0121] page:9:line:28 | •
    [operational-risk-2-18-2026-0122] page:9:line:29 | Traffic
    [operational-risk-2-18-2026-0123] page:9:line:30 | •
    [operational-risk-2-18-2026-0124] page:9:line:31 | Weather
    [operational-risk-2-18-2026-0125] page:9:line:32 | •
    [operational-risk-2-18-2026-0126] page:9:line:33 | Prohibited airspace
    [operational-risk-2-18-2026-0127] page:9:line:34 | Operator Factors
    [operational-risk-2-18-2026-0128] page:9:line:35 | •
    [operational-risk-2-18-2026-0129] page:9:line:36 | Independence vs. dependence on
    [operational-risk-2-18-2026-0130] page:9:line:37 | Dispatch
    [operational-risk-2-18-2026-0131] page:9:line:38 | •
    [operational-risk-2-18-2026-0132] page:9:line:39 | Clarity and consistency of pilot roles
    [operational-risk-2-18-2026-0133] page:9:line:40 | in reviewing route
    [operational-risk-2-18-2026-0134] page:9:line:41 | Crew Factors
    [operational-risk-2-18-2026-0135] page:9:line:42 | •
    [operational-risk-2-18-2026-0136] page:9:line:43 | Expectations (confirmation bias)
    [operational-risk-2-18-2026-0137] page:9:line:44 | •
    [operational-risk-2-18-2026-0138] page:9:line:45 | Fatigue
    [operational-risk-2-18-2026-0139] page:9:line:46 | •
    [operational-risk-2-18-2026-0140] page:9:line:47 | Communication style
    [operational-risk-2-18-2026-0141] page:9:line:48 | •
    [operational-risk-2-18-2026-0142] page:9:line:49 | Distractions
    [operational-risk-2-18-2026-0143] page:9:line:50 | •
    [operational-risk-2-18-2026-0144] page:9:line:51 | Local area familiarity
    [operational-risk-2-18-2026-0145] page:9:line:52 | •
    [operational-risk-2-18-2026-0146] page:9:line:53 | Familiarity with different types of routes
    [operational-risk-2-18-2026-0147] page:9:line:54 | Chandra, D.C., & Markunas, R. (2017). “Line Pilot Perspectives on Complexity of Terminal Instrument Flight
    [operational-risk-2-18-2026-0148] page:9:line:55 | Procedures,” DOT-VNTSC-FAA-17-06. U.S. DOT Volpe National Transportation Systems Center.
    [operational-risk-2-18-2026-0149] page:10:line:1 | SAFETY 1 AND SAFETY 2
    [operational-risk-2-18-2026-0150] page:10:line:2 | 2/18/26
    [operational-risk-2-18-2026-0151] page:10:line:3 | ENP-0112
    [operational-risk-2-18-2026-0152] page:10:line:4 | 10
    [operational-risk-2-18-2026-0153] page:11:line:1 | SAFETY 1 AND SAFETY 2
    [operational-risk-2-18-2026-0154] page:11:line:2 | • Safety 1 examines what went wrong
    [operational-risk-2-18-2026-0155] page:11:line:3 | • Safety = absence of accidents or an acceptable level of risk
    [operational-risk-2-18-2026-0156] page:11:line:4 | • Analyze accident/incident investigations, look for remedies
    [operational-risk-2-18-2026-0157] page:11:line:5 | • Humans, organizations, and technology are a source of error, failure, and malfunctions
    [operational-risk-2-18-2026-0158] page:11:line:6 | • Accidents/incidents are relatively rare
    [operational-risk-2-18-2026-0159] page:11:line:7 | • In contrast, Safety 2 examines everything that what went right
    [operational-risk-2-18-2026-0160] page:11:line:8 | • Risks are always being managed, human variability is necessary and helpful in many situations.
    [operational-risk-2-18-2026-0161] page:11:line:9 | • The vast majority of flight operations are safe. Study these.
    [operational-risk-2-18-2026-0162] page:11:line:10 | 2/18/26
    [operational-risk-2-18-2026-0163] page:11:line:11 | ENP-0112
    [operational-risk-2-18-2026-0164] page:11:line:12 | 11
    [operational-risk-2-18-2026-0165] page:12:line:1 | MORE ON SAFETY 1 AND SAFETY 2
    [operational-risk-2-18-2026-0166] page:12:line:2 | • Safety 1 and Safety 2 are complementary views. Need to consider both.
    [operational-risk-2-18-2026-0167] page:12:line:3 | • In Safety 1, when things go right, it’s because the work went as designed/imagined.
    [operational-risk-2-18-2026-0168] page:12:line:4 | Reinforce compliance and eliminate variability. Systems are decomposable into
    [operational-risk-2-18-2026-0169] page:12:line:5 | components. Root cause can be identified.
    [operational-risk-2-18-2026-0170] page:12:line:6 | • In reality systems are complex and inter-dependent. Trying to constrain performance can
    [operational-risk-2-18-2026-0171] page:12:line:7 | make it more difficult to achieve the desired outcomes and be counterproductive. Human
    [operational-risk-2-18-2026-0172] page:12:line:8 | flexibility and adaptive behavior is necessary and can be a source of success (“work as
    [operational-risk-2-18-2026-0173] page:12:line:9 | done”).
    [operational-risk-2-18-2026-0174] page:12:line:10 | 2/18/26
    [operational-risk-2-18-2026-0175] page:12:line:11 | ENP-0112
    [operational-risk-2-18-2026-0176] page:12:line:12 | 12
    [operational-risk-2-18-2026-0177] page:13:line:1 | SAMPLE ASRS EVENT 1347601
    [operational-risk-2-18-2026-0178] page:13:line:2 | ASRS = Aviation Safety Reporting System
    [operational-risk-2-18-2026-0179] page:13:line:3 | 2/18/26
    [operational-risk-2-18-2026-0180] page:13:line:4 | ENP-0112
    [operational-risk-2-18-2026-0181] page:13:line:5 | 13
    [operational-risk-2-18-2026-0182] page:14:line:1 | LIMITATIONS OF ASRS RECORDS
    [operational-risk-2-18-2026-0183] page:14:line:2 | • Self-reported, subjective, and written from memory
    [operational-risk-2-18-2026-0184] page:14:line:3 | • May be incomplete or biased, based on a single perspective of the event
    [operational-risk-2-18-2026-0185] page:14:line:4 | • Generally filed because an undesirable outcome occurred or almost occurred. Not filed
    [operational-risk-2-18-2026-0186] page:14:line:5 | when all goes well.
    [operational-risk-2-18-2026-0187] page:14:line:6 | • Harder to evaluate Safety 2 in ASRS events.
    [operational-risk-2-18-2026-0188] page:14:line:7 | • Cannot make any statements about rates of events in general
    [operational-risk-2-18-2026-0189] page:14:line:8 | • Timing issues
    [operational-risk-2-18-2026-0190] page:14:line:9 | • May refer to out-of-date arrivals, departures, or approaches.
    [operational-risk-2-18-2026-0191] page:14:line:10 | • Old charts may not be available.
    [operational-risk-2-18-2026-0192] page:14:line:11 | • Delayed entry of events due to processing time (a few months).
    [operational-risk-2-18-2026-0193] page:14:line:12 | 2/18/26
    [operational-risk-2-18-2026-0194] page:14:line:13 | ENP-0112
    [operational-risk-2-18-2026-0195] page:14:line:14 | 14
    [operational-risk-2-18-2026-0196] page:15:line:1 | ACCESSION NUMBER (ACN) 1347601
    [operational-risk-2-18-2026-0197] page:15:line:2 | • Obtained from NASA public database, Aviation Safety Reporting System (ASRS)
    [operational-risk-2-18-2026-0198] page:15:line:3 | https://asrs.arc.nasa.gov/search/database.html
    [operational-risk-2-18-2026-0199] page:15:line:4 | • Coded fields include time/day (201604 = April 2016) and other facts about the submitted report.
    [operational-risk-2-18-2026-0200] page:15:line:5 | • Narrative has been de-identified.
    [operational-risk-2-18-2026-0201] page:15:line:6 | • Some acronyms
    [operational-risk-2-18-2026-0202] page:15:line:7 | FO = first officer
    [operational-risk-2-18-2026-0203] page:15:line:8 | DFW = Dallas-Fort Worth airport in Texas (TX)
    [operational-risk-2-18-2026-0204] page:15:line:9 | DAL = Dallas Love Field, TX
    [operational-risk-2-18-2026-0205] page:15:line:10 | FL### = Flight Level (altitude in thousands of feet), e.g., FL340 = 34,000 ft altitude
    [operational-risk-2-18-2026-0206] page:15:line:11 | ACARS = text messaging system for airline company communications
    [operational-risk-2-18-2026-0207] page:15:line:12 | ASAP = airlines’ internal safety reporting system for pilots
    [operational-risk-2-18-2026-0208] page:15:line:13 | MFD = multi-function display in the flight deck
    [operational-risk-2-18-2026-0209] page:15:line:14 | PA = public announcement
    [operational-risk-2-18-2026-0210] page:15:line:15 | 2/18/26
    [operational-risk-2-18-2026-0211] page:15:line:16 | ENP-0112
    [operational-risk-2-18-2026-0212] page:15:line:17 | 15
    [operational-risk-2-18-2026-0213] page:16:line:1 | DALLAS-FORT WORTH (DFW) AND DALLAS (DAL)
    [operational-risk-2-18-2026-0214] page:16:line:2 | 2/18/26
    [operational-risk-2-18-2026-0215] page:16:line:3 | ENP-0112
    [operational-risk-2-18-2026-0216] page:16:line:4 | 16
    [operational-risk-2-18-2026-0217] page:16:line:5 | DAL
    [operational-risk-2-18-2026-0218] page:16:line:6 | DFW
    [operational-risk-2-18-2026-0219] page:16:line:7 | Note that both airports have a “13L” runway, of similar lengths.
    [operational-risk-2-18-2026-0220] page:16:line:8 | The distance between these airports is about 10 miles.
    [operational-risk-2-18-2026-0221] page:16:line:9 | Chart images from airnav.com
    [operational-risk-2-18-2026-0222] page:17:line:1 | EXAMPLE ASRS EVENT
    [operational-risk-2-18-2026-0223] page:17:line:2 | • What happened? Summarize in your own words.
    [operational-risk-2-18-2026-0224] page:17:line:3 | • What was the sequence of events? (facts)
    [operational-risk-2-18-2026-0225] page:17:line:4 | • What were the “threats” in this situation?
    [operational-risk-2-18-2026-0226] page:17:line:5 | (See list on earlier slide, Operational Complexity, for ideas)
    [operational-risk-2-18-2026-0227] page:17:line:6 | • What information could you find online that would help you understand this event?
    [operational-risk-2-18-2026-0228] page:17:line:7 | • How did the flight crew contribute to safety?
    [operational-risk-2-18-2026-0229] page:17:line:8 | • What might have happened with a different crew?
    [operational-risk-2-18-2026-0230] page:17:line:9 | • What might have happened if there were no crew, but an autonomous system instead?
    [operational-risk-2-18-2026-0231] page:17:line:10 | 2/18/26
    [operational-risk-2-18-2026-0232] page:17:line:11 | ENP-0112
    [operational-risk-2-18-2026-0233] page:17:line:12 | 17
    [operational-risk-2-18-2026-0234] page:18:line:1 | EXTRA
    [operational-risk-2-18-2026-0235] page:18:line:2 | Connection to earlier reading
    [operational-risk-2-18-2026-0236] page:18:line:3 | 2/18/26
    [operational-risk-2-18-2026-0237] page:18:line:4 | ENP-0112
    [operational-risk-2-18-2026-0238] page:18:line:5 | 18
    [operational-risk-2-18-2026-0239] page:19:line:1 | LIMITS OF EXPERTISE
    [operational-risk-2-18-2026-0240] page:19:line:2 | • Why do highly skilled pilots make errors?
    [operational-risk-2-18-2026-0241] page:19:line:3 | • Important to avoid hindsight bias
    [operational-risk-2-18-2026-0242] page:19:line:4 | • Examine the situation as the pilots understood it at the time to understand their responses
    [operational-risk-2-18-2026-0243] page:19:line:5 | • Need to understand skilled performance and factors that affect the probability of
    [operational-risk-2-18-2026-0244] page:19:line:6 | errors
    [operational-risk-2-18-2026-0245] page:19:line:7 | • Human cognitive and perceptual limitations
    [operational-risk-2-18-2026-0246] page:19:line:8 | • Task demands
    [operational-risk-2-18-2026-0247] page:19:line:9 | • Events in the environment
    [operational-risk-2-18-2026-0248] page:19:line:10 | • Social and organizational factors
    [operational-risk-2-18-2026-0249] page:19:line:11 | 2/18/26
    [operational-risk-2-18-2026-0250] page:19:line:12 | ENP-0112
    [operational-risk-2-18-2026-0251] page:19:line:13 | 19
    ```
