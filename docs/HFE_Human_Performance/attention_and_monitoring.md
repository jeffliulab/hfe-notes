# 注意与监控

本页整理注意资源、监控任务、automation complacency 与 vigilance decrement 等核心问题。

## 课件里的讲解顺序

这一部分不是我主观概括，而是根据 PPT / PDF 的标题行和页首内容还原老师大致的课堂展开顺序。

### Attention and Monitoring 2-9- 2026.pdf

1. INTRODUCTION TO ATTENTION &
2. TOPICS Supervisory control of automation
3. SHERIDAN’S SPECTRUM OF AUTOMATION
4. Proctor and VanZandt, 2017 HUMAN INFORMATION PROCESSING MODEL
5. WHAT IS ATTENTION? Attention is associated with “consciousness” and “awareness”
6. OVERVIEW: MODELS OF ATTENTION Attention Models
7. YERKES-DODSON LAW Kahneman D. Attention and Effort. Prentice Hall, Inc., 1973.
8. VIGILANCE Vigilance is sustained attention, the ability to


## 这页的逻辑顺序

建议按下面的顺序读这页，这样会更像老师在课堂上带着你展开概念。

1. 注意为什么是有限资源
2. 监控任务为何特别容易衰退
3. 自动化如何改变人的注意分配

## 核心概念

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

## 课件图示与页面预览

下面展示从原始 PPT/PDF 中自动提取出的配图或页面预览。它们不是装饰图，而是正文讲解时应该对照着看的课堂材料。

<div class="note-visual-grid">
  <figure class="note-visual">
    <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/attention-and-monitoring-2-9-2026/page-01.png" alt="Attention and Monitoring 2-9- 2026.pdf · 第 1 页预览" loading="lazy">
    <figcaption>Attention and Monitoring 2-9- 2026.pdf · 第 1 页预览</figcaption>
  </figure>
  <figure class="note-visual">
    <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/attention-and-monitoring-2-9-2026/page-03.png" alt="Attention and Monitoring 2-9- 2026.pdf · 第 3 页预览" loading="lazy">
    <figcaption>Attention and Monitoring 2-9- 2026.pdf · 第 3 页预览</figcaption>
  </figure>
  <figure class="note-visual">
    <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/attention-and-monitoring-2-9-2026/page-04.png" alt="Attention and Monitoring 2-9- 2026.pdf · 第 4 页预览" loading="lazy">
    <figcaption>Attention and Monitoring 2-9- 2026.pdf · 第 4 页预览</figcaption>
  </figure>
</div>

## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `人的表现`
- 关联源文件数: 1
- 文本单元数: 227
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Attention and Monitoring 2-9- 2026.pdf` | `pdf` | 227 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Attention and Monitoring 2-9- 2026.pdf) |

## 相关主题

- [显示与告警](../HFE_Aviation_Automation/displays_and_alerts.md)
- [疲劳与睡眠](fatigue_and_sleep.md)
- [情境意识](situation_awareness.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "Attention and Monitoring 2-9- 2026.pdf | 227 text units"
    下载原件: [Attention and Monitoring 2-9- 2026.pdf](../assets/source_files/Lectures_Spring_2026/Attention and Monitoring 2-9- 2026.pdf)
    映射页面: `attention_and_monitoring`
    
    ```text
    [attention-and-monitoring-2-9-2026-0001] page:1:line:1 | INTRODUCTION TO
    [attention-and-monitoring-2-9-2026-0002] page:1:line:2 | ATTENTION &
    [attention-and-monitoring-2-9-2026-0003] page:1:line:3 | MONITORING
    [attention-and-monitoring-2-9-2026-0004] page:1:line:4 | ENP-0112
    [attention-and-monitoring-2-9-2026-0005] page:1:line:5 | 2/9/2026
    [attention-and-monitoring-2-9-2026-0006] page:1:line:6 | Dr. Divya C. Chandra
    [attention-and-monitoring-2-9-2026-0007] page:1:line:7 | 2/9/26
    [attention-and-monitoring-2-9-2026-0008] page:1:line:8 | ENP-0112
    [attention-and-monitoring-2-9-2026-0009] page:1:line:9 | 1
    [attention-and-monitoring-2-9-2026-0010] page:2:line:1 | TOPICS
    [attention-and-monitoring-2-9-2026-0011] page:2:line:2 | • Supervisory control of automation
    [attention-and-monitoring-2-9-2026-0012] page:2:line:3 | • Attention and vigilance
    [attention-and-monitoring-2-9-2026-0013] page:2:line:4 | • Monitoring techniques
    [attention-and-monitoring-2-9-2026-0014] page:2:line:5 | • Discussion of flight path monitoring reading
    [attention-and-monitoring-2-9-2026-0015] page:2:line:6 | • Extras
    [attention-and-monitoring-2-9-2026-0016] page:2:line:7 | • PAPI video
    [attention-and-monitoring-2-9-2026-0017] page:2:line:8 | • Models of attention
    [attention-and-monitoring-2-9-2026-0018] page:2:line:9 | 2/9/26
    [attention-and-monitoring-2-9-2026-0019] page:2:line:10 | ENP-0112
    [attention-and-monitoring-2-9-2026-0020] page:2:line:11 | 2
    [attention-and-monitoring-2-9-2026-0021] page:3:line:1 | SHERIDAN’S SPECTRUM OF AUTOMATION
    [attention-and-monitoring-2-9-2026-0022] page:3:line:2 | 2/9/26
    [attention-and-monitoring-2-9-2026-0023] page:3:line:3 | ENP-0112
    [attention-and-monitoring-2-9-2026-0024] page:3:line:4 | 3
    [attention-and-monitoring-2-9-2026-0025] page:4:line:1 | Proctor and VanZandt, 2017
    [attention-and-monitoring-2-9-2026-0026] page:4:line:2 | HUMAN INFORMATION PROCESSING MODEL
    [attention-and-monitoring-2-9-2026-0027] page:4:line:3 | 2/9/26
    [attention-and-monitoring-2-9-2026-0028] page:4:line:4 | ENP-0112
    [attention-and-monitoring-2-9-2026-0029] page:4:line:5 | 4
    [attention-and-monitoring-2-9-2026-0030] page:5:line:1 | WHAT IS ATTENTION?
    [attention-and-monitoring-2-9-2026-0031] page:5:line:2 | • Attention is associated with “consciousness” and “awareness”
    [attention-and-monitoring-2-9-2026-0032] page:5:line:3 | • Attention “connects” perception and cognition
    [attention-and-monitoring-2-9-2026-0033] page:5:line:4 | • It is an “executive” function
    [attention-and-monitoring-2-9-2026-0034] page:5:line:5 | • We use metaphors to model attention
    [attention-and-monitoring-2-9-2026-0035] page:5:line:6 | • Spotlight, filter, bottleneck, (limited) resource
    [attention-and-monitoring-2-9-2026-0036] page:5:line:7 | • Some words to describe attention
    [attention-and-monitoring-2-9-2026-0037] page:5:line:8 | • Focused, selective, divided, distributed
    [attention-and-monitoring-2-9-2026-0038] page:5:line:9 | 2/9/26
    [attention-and-monitoring-2-9-2026-0039] page:5:line:10 | ENP-0112
    [attention-and-monitoring-2-9-2026-0040] page:5:line:11 | 5
    [attention-and-monitoring-2-9-2026-0041] page:6:line:1 | OVERVIEW: MODELS OF ATTENTION
    [attention-and-monitoring-2-9-2026-0042] page:6:line:2 | 6
    [attention-and-monitoring-2-9-2026-0043] page:6:line:3 | Attention Models
    [attention-and-monitoring-2-9-2026-0044] page:6:line:4 | Bottleneck
    [attention-and-monitoring-2-9-2026-0045] page:6:line:5 | Models
    [attention-and-monitoring-2-9-2026-0046] page:6:line:6 | Resource
    [attention-and-monitoring-2-9-2026-0047] page:6:line:7 | Models
    [attention-and-monitoring-2-9-2026-0048] page:6:line:8 | Early
    [attention-and-monitoring-2-9-2026-0049] page:6:line:9 | Selection
    [attention-and-monitoring-2-9-2026-0050] page:6:line:10 | (1958, 1964)
    [attention-and-monitoring-2-9-2026-0051] page:6:line:11 | Late
    [attention-and-monitoring-2-9-2026-0052] page:6:line:12 | Selection
    [attention-and-monitoring-2-9-2026-0053] page:6:line:13 | (1970)
    [attention-and-monitoring-2-9-2026-0054] page:6:line:14 | Single
    [attention-and-monitoring-2-9-2026-0055] page:6:line:15 | Resources
    [attention-and-monitoring-2-9-2026-0056] page:6:line:16 | (1973)
    [attention-and-monitoring-2-9-2026-0057] page:6:line:17 | Multiple
    [attention-and-monitoring-2-9-2026-0058] page:6:line:18 | Resources
    [attention-and-monitoring-2-9-2026-0059] page:6:line:19 | (1979)
    [attention-and-monitoring-2-9-2026-0060] page:6:line:20 | Biased Competition
    [attention-and-monitoring-2-9-2026-0061] page:6:line:21 | Theory (1995);
    [attention-and-monitoring-2-9-2026-0062] page:6:line:22 | Executive
    [attention-and-monitoring-2-9-2026-0063] page:6:line:23 | Process Model
    [attention-and-monitoring-2-9-2026-0064] page:6:line:24 | (1997)
    [attention-and-monitoring-2-9-2026-0065] page:6:line:25 | See Proctor & Van Zandt, 2017
    [attention-and-monitoring-2-9-2026-0066] page:7:line:1 | YERKES-DODSON LAW
    [attention-and-monitoring-2-9-2026-0067] page:7:line:2 | Kahneman D. Attention and Effort. Prentice Hall, Inc., 1973.
    [attention-and-monitoring-2-9-2026-0068] page:7:line:3 | An observed relationship between
    [attention-and-monitoring-2-9-2026-0069] page:7:line:4 | arousal and performance
    [attention-and-monitoring-2-9-2026-0070] page:7:line:5 | 2/9/26
    [attention-and-monitoring-2-9-2026-0071] page:7:line:6 | ENP-0112
    [attention-and-monitoring-2-9-2026-0072] page:7:line:7 | 7
    [attention-and-monitoring-2-9-2026-0073] page:8:line:1 | VIGILANCE
    [attention-and-monitoring-2-9-2026-0074] page:8:line:2 | Vigilance is sustained attention, the ability to
    [attention-and-monitoring-2-9-2026-0075] page:8:line:3 | maintain attention/arousal. (Vigilance is hard.)
    [attention-and-monitoring-2-9-2026-0076] page:8:line:4 | • Factors
    [attention-and-monitoring-2-9-2026-0077] page:8:line:5 | • Time
    [attention-and-monitoring-2-9-2026-0078] page:8:line:6 | • Salience
    [attention-and-monitoring-2-9-2026-0079] page:8:line:7 | • Signal rate
    [attention-and-monitoring-2-9-2026-0080] page:8:line:8 | • Arousal level
    [attention-and-monitoring-2-9-2026-0081] page:8:line:9 | Monitoring is a vigilance task.
    [attention-and-monitoring-2-9-2026-0082] page:8:line:10 | 2/9/26
    [attention-and-monitoring-2-9-2026-0083] page:8:line:11 | ENP-0112
    [attention-and-monitoring-2-9-2026-0084] page:8:line:12 | 8
    [attention-and-monitoring-2-9-2026-0085] page:9:line:1 | PERCEPTUAL NARROWING
    [attention-and-monitoring-2-9-2026-0086] page:9:line:2 | • Increased tendency to focus on a few cues
    [attention-and-monitoring-2-9-2026-0087] page:9:line:3 | • Selection of relevant cues often involves a
    [attention-and-monitoring-2-9-2026-0088] page:9:line:4 | discrimination
    [attention-and-monitoring-2-9-2026-0089] page:9:line:5 | • High workload impairs discrimination
    [attention-and-monitoring-2-9-2026-0090] page:9:line:6 | between relevant and non-relevant cues
    [attention-and-monitoring-2-9-2026-0091] page:9:line:7 | • Reduced ability to focus on relevant cues
    [attention-and-monitoring-2-9-2026-0092] page:9:line:8 | 2/9/26
    [attention-and-monitoring-2-9-2026-0093] page:9:line:9 | ENP-0112
    [attention-and-monitoring-2-9-2026-0094] page:9:line:10 | 9
    [attention-and-monitoring-2-9-2026-0095] page:9:line:11 | Restricted attention due to high demands
    [attention-and-monitoring-2-9-2026-0096] page:10:line:1 | SOME MONITORING TECHNIQUES
    [attention-and-monitoring-2-9-2026-0097] page:10:line:2 | • Scanning
    [attention-and-monitoring-2-9-2026-0098] page:10:line:3 | • Visual scan for traffic
    [attention-and-monitoring-2-9-2026-0099] page:10:line:4 | • Instrument scan
    [attention-and-monitoring-2-9-2026-0100] page:10:line:5 | • Cross checking (independent sources)
    [attention-and-monitoring-2-9-2026-0101] page:10:line:6 | • Flows/checklists
    [attention-and-monitoring-2-9-2026-0102] page:10:line:7 | • Point and Call (double-pointing)
    [attention-and-monitoring-2-9-2026-0103] page:10:line:8 | 2/9/26
    [attention-and-monitoring-2-9-2026-0104] page:10:line:9 | ENP-0112
    [attention-and-monitoring-2-9-2026-0105] page:10:line:10 | 10
    [attention-and-monitoring-2-9-2026-0106] page:11:line:1 | INSTRUMENT SCAN
    [attention-and-monitoring-2-9-2026-0107] page:11:line:2 | FAA Pilot's Handbook of Aeronautical Knowledge, FAA-H-8083-25B
    [attention-and-monitoring-2-9-2026-0108] page:11:line:3 | https://commons.wikimedia.org/wiki/File:Six_flight_instruments.JPG
    [attention-and-monitoring-2-9-2026-0109] page:11:line:4 | Contributions/Meggar at the English-language Wikipedia, CC BY-SA 3.0
    [attention-and-monitoring-2-9-2026-0110] page:11:line:5 | <http://creativecommons.org/licenses/by-sa/3.0/>, via Wikimedia
    [attention-and-monitoring-2-9-2026-0111] page:11:line:6 | Commons
    [attention-and-monitoring-2-9-2026-0112] page:11:line:7 | Basic T
    [attention-and-monitoring-2-9-2026-0113] page:11:line:8 | Requires practice and proficiency!
    [attention-and-monitoring-2-9-2026-0114] page:11:line:9 | ?
    [attention-and-monitoring-2-9-2026-0115] page:11:line:10 | 2/9/26
    [attention-and-monitoring-2-9-2026-0116] page:11:line:11 | ENP-0112
    [attention-and-monitoring-2-9-2026-0117] page:11:line:12 | 11
    [attention-and-monitoring-2-9-2026-0118] page:12:line:1 | HEAD-UP DISPLAY
    [attention-and-monitoring-2-9-2026-0119] page:12:line:2 | • Collimated display (at infinity)
    [attention-and-monitoring-2-9-2026-0120] page:12:line:3 | • Integrated data
    [attention-and-monitoring-2-9-2026-0121] page:12:line:4 | • Attention is a different issue…
    [attention-and-monitoring-2-9-2026-0122] page:12:line:5 | http://aviationknowledge.wikidot.com/aviation:human-factors-issue-
    [attention-and-monitoring-2-9-2026-0123] page:12:line:6 | associated-with-heads-up-displa
    [attention-and-monitoring-2-9-2026-0124] page:12:line:7 | 2/9/26
    [attention-and-monitoring-2-9-2026-0125] page:12:line:8 | ENP-0112
    [attention-and-monitoring-2-9-2026-0126] page:12:line:9 | 12
    [attention-and-monitoring-2-9-2026-0127] page:13:line:1 | MONITORING AND SENSE-MAKING
    [attention-and-monitoring-2-9-2026-0128] page:13:line:2 | • Mental Models and Situation Awareness, covered later in class
    [attention-and-monitoring-2-9-2026-0129] page:13:line:3 | 2/4/26
    [attention-and-monitoring-2-9-2026-0130] page:13:line:4 | ENP-0112
    [attention-and-monitoring-2-9-2026-0131] page:13:line:5 | 13
    [attention-and-monitoring-2-9-2026-0132] page:13:line:6 | Monitoring, essentially, is “sense making” (Section 3.1). It is systematic observation and
    [attention-and-monitoring-2-9-2026-0133] page:13:line:7 | interpretation of the current state of the airplane and its operational environment; it requires
    [attention-and-monitoring-2-9-2026-0134] page:13:line:8 | integration of current inputs with operational knowledge, which includes mental models, and
    [attention-and-monitoring-2-9-2026-0135] page:13:line:9 | the generation of expected values of flight path targets.
    [attention-and-monitoring-2-9-2026-0136] page:13:line:10 | Monitoring is tied to expectations (Section 3.1). Monitoring—looking and listening to gather
    [attention-and-monitoring-2-9-2026-0137] page:13:line:11 | information about the operational environment—is not simply moving one’s eyes to each
    [attention-and-monitoring-2-9-2026-0138] page:13:line:12 | indication and reading it. Typically, but not always, there is an expectation about what that
    [attention-and-monitoring-2-9-2026-0139] page:13:line:13 | indication will be, perhaps based on a projection from the last glance.
    [attention-and-monitoring-2-9-2026-0140] page:13:line:14 | Mumaw, Billman, & Feary (2020) Analysis of pilot monitoring skills and a review of training
    [attention-and-monitoring-2-9-2026-0141] page:13:line:15 | effectiveness. (NASA/TM-20210000047) (in Canvas, under Supplementary readings)
    [attention-and-monitoring-2-9-2026-0142] page:14:line:1 | HAND SIGNALS FOR MONITORING
    [attention-and-monitoring-2-9-2026-0143] page:14:line:2 | • Japanese hand rail signals (4:16)
    [attention-and-monitoring-2-9-2026-0144] page:14:line:3 | 2/9/26
    [attention-and-monitoring-2-9-2026-0145] page:14:line:4 | ENP-0112
    [attention-and-monitoring-2-9-2026-0146] page:14:line:5 | 14
    [attention-and-monitoring-2-9-2026-0147] page:15:line:1 | DISCUSSION:
    [attention-and-monitoring-2-9-2026-0148] page:15:line:2 | PRACTICAL GUIDE TO FLIGHT PATH MONITORING
    [attention-and-monitoring-2-9-2026-0149] page:15:line:3 | • Do you have personal experience in monitoring?
    [attention-and-monitoring-2-9-2026-0150] page:15:line:4 | • For what purpose?
    [attention-and-monitoring-2-9-2026-0151] page:15:line:5 | • What are your reflections about the monitoring task?
    [attention-and-monitoring-2-9-2026-0152] page:15:line:6 | • How might (or might not) this apply to other modes of transportation?
    [attention-and-monitoring-2-9-2026-0153] page:15:line:7 | Flight Safety Foundation (November, 2014). A practical guide
    [attention-and-monitoring-2-9-2026-0154] page:15:line:8 | for improving flight path monitoring.
    [attention-and-monitoring-2-9-2026-0155] page:15:line:9 | 2/9/26
    [attention-and-monitoring-2-9-2026-0156] page:15:line:10 | ENP-0112
    [attention-and-monitoring-2-9-2026-0157] page:15:line:11 | 15
    [attention-and-monitoring-2-9-2026-0158] page:16:line:1 | SOME REFERENCES
    [attention-and-monitoring-2-9-2026-0159] page:16:line:2 | Proctor and Van Zandt textbook (in Canvas under Reading List)
    [attention-and-monitoring-2-9-2026-0160] page:16:line:3 | Flight Safety Foundation (2014). A practical guide for improving flight path monitoring.
    [attention-and-monitoring-2-9-2026-0161] page:16:line:4 | Mumaw, Billman, & Feary (2020) Analysis of pilot monitoring skills and a review of
    [attention-and-monitoring-2-9-2026-0162] page:16:line:5 | training effectiveness. (NASA/TM-20210000047) (in Canvas, under Supplementary
    [attention-and-monitoring-2-9-2026-0163] page:16:line:6 | readings)
    [attention-and-monitoring-2-9-2026-0164] page:16:line:7 | 2/4/26
    [attention-and-monitoring-2-9-2026-0165] page:16:line:8 | ENP-0112
    [attention-and-monitoring-2-9-2026-0166] page:16:line:9 | 16
    [attention-and-monitoring-2-9-2026-0167] page:17:line:1 | EXTRAS
    [attention-and-monitoring-2-9-2026-0168] page:17:line:2 | 2/9/26
    [attention-and-monitoring-2-9-2026-0169] page:17:line:3 | ENP-0112
    [attention-and-monitoring-2-9-2026-0170] page:17:line:4 | 17
    [attention-and-monitoring-2-9-2026-0171] page:18:line:1 | APPROACH VIDEOS
    [attention-and-monitoring-2-9-2026-0172] page:18:line:2 | LED VS. INCANDESCENT PAPI
    [attention-and-monitoring-2-9-2026-0173] page:18:line:3 | • PAPI/VASI video
    [attention-and-monitoring-2-9-2026-0174] page:18:line:4 | 2/9/26
    [attention-and-monitoring-2-9-2026-0175] page:18:line:5 | ENP-0112
    [attention-and-monitoring-2-9-2026-0176] page:18:line:6 | 18
    [attention-and-monitoring-2-9-2026-0177] page:19:line:1 | SPOTLIGHT METAPHOR
    [attention-and-monitoring-2-9-2026-0178] page:19:line:2 | • Attention can be aligned with direction of gaze, or directed to be independent of
    [attention-and-monitoring-2-9-2026-0179] page:19:line:3 | fixation
    [attention-and-monitoring-2-9-2026-0180] page:19:line:4 | • What you are “attending to” can be different from where your eyes are focused
    [attention-and-monitoring-2-9-2026-0181] page:19:line:5 | (e.g., team sports)
    [attention-and-monitoring-2-9-2026-0182] page:19:line:6 | 19
    [attention-and-monitoring-2-9-2026-0183] page:19:line:7 | Abstract Colored Circles Linked with Coloured Bands by Paul Klee 1914
    [attention-and-monitoring-2-9-2026-0184] page:20:line:1 | BOTTLENECK (FILTER) MODELS OF ATTENTION
    [attention-and-monitoring-2-9-2026-0185] page:20:line:2 | • Selective attention tasks (typically auditory)
    [attention-and-monitoring-2-9-2026-0186] page:20:line:3 | • Where exactly is the bottle neck (early or late) in information
    [attention-and-monitoring-2-9-2026-0187] page:20:line:4 | processing?
    [attention-and-monitoring-2-9-2026-0188] page:20:line:5 | • Early (Broadbent’s filter theory)
    [attention-and-monitoring-2-9-2026-0189] page:20:line:6 | • Late (Treisman’s filter attenuation theory, Deutsch & Deutsch)
    [attention-and-monitoring-2-9-2026-0190] page:20:line:7 | • Is the bottleneck a structural limitation (bug) or an optional strategy
    [attention-and-monitoring-2-9-2026-0191] page:20:line:8 | (feature)?
    [attention-and-monitoring-2-9-2026-0192] page:21:line:1 | MORE RECENT MODELS OF ATTENTION
    [attention-and-monitoring-2-9-2026-0193] page:21:line:2 | • Spatially-based Feature-Integration Theory (Treisman)
    [attention-and-monitoring-2-9-2026-0194] page:21:line:3 | • Attention as a unitary resource (e.g., Kahneman)
    [attention-and-monitoring-2-9-2026-0195] page:21:line:4 | • Attention as multiple resources (Wickens)
    [attention-and-monitoring-2-9-2026-0196] page:21:line:5 | • Executive Control Model (EPIC) (Meyer & Kieras)
    [attention-and-monitoring-2-9-2026-0197] page:22:line:1 | RESOURCE MODELS – SINGLE RESOURCES
    [attention-and-monitoring-2-9-2026-0198] page:22:line:2 | Attention is a resource that can be divided up among different tasks in different amounts
    [attention-and-monitoring-2-9-2026-0199] page:22:line:3 | 22
    [attention-and-monitoring-2-9-2026-0200] page:22:line:4 | Kahneman, 1973
    [attention-and-monitoring-2-9-2026-0201] page:23:line:1 | RESOURCE MODELS – SINGLE RESOURCES
    [attention-and-monitoring-2-9-2026-0202] page:23:line:2 | 23
    [attention-and-monitoring-2-9-2026-0203] page:23:line:3 | Kahneman, 1973
    [attention-and-monitoring-2-9-2026-0204] page:24:line:1 | RESOURCE MODELS – MULTIPLE RESOURCES
    [attention-and-monitoring-2-9-2026-0205] page:24:line:2 | Different attentional resources exist for different sensory-motor modalities and coding
    [attention-and-monitoring-2-9-2026-0206] page:24:line:3 | domains
    [attention-and-monitoring-2-9-2026-0207] page:24:line:4 | 24
    [attention-and-monitoring-2-9-2026-0208] page:24:line:5 | Proctor and Van Zandt, 2017
    [attention-and-monitoring-2-9-2026-0209] page:25:line:1 | THOUGHT EXERCISE
    [attention-and-monitoring-2-9-2026-0210] page:25:line:2 | Consider walking with a friend describing something to you…
    [attention-and-monitoring-2-9-2026-0211] page:25:line:3 | 25
    [attention-and-monitoring-2-9-2026-0212] page:26:line:1 | EXECUTIVE CONTROL MODELS
    [attention-and-monitoring-2-9-2026-0213] page:26:line:2 | • EPIC (Executive-Process/Interactive Control)
    [attention-and-monitoring-2-9-2026-0214] page:26:line:3 | 26
    [attention-and-monitoring-2-9-2026-0215] page:26:line:4 | Meyer and Kieras, 1997
    [attention-and-monitoring-2-9-2026-0216] page:27:line:1 | CHANGE BLINDNESS
    [attention-and-monitoring-2-9-2026-0217] page:27:line:2 | • The inability to detect changes in a visual scene
    [attention-and-monitoring-2-9-2026-0218] page:27:line:3 | • Focused attention is necessary to see change
    [attention-and-monitoring-2-9-2026-0219] page:27:line:4 | • We do not attend to all visual details in our visual buffer (iconic memory)
    [attention-and-monitoring-2-9-2026-0220] page:27:line:5 | • Change blindness occurs when attention is distracted or there is a break in visibility
    [attention-and-monitoring-2-9-2026-0221] page:27:line:6 | of information
    [attention-and-monitoring-2-9-2026-0222] page:27:line:7 | Asking for Directions
    [attention-and-monitoring-2-9-2026-0223] page:27:line:8 | 2/9/26
    [attention-and-monitoring-2-9-2026-0224] page:27:line:9 | ENP-0112
    [attention-and-monitoring-2-9-2026-0225] page:27:line:10 | 27
    [attention-and-monitoring-2-9-2026-0226] page:27:line:11 | What are some practical situations where this might occur, e.g.,
    [attention-and-monitoring-2-9-2026-0227] page:27:line:12 | in driving or flying?
    ```
