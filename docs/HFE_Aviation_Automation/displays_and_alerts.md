# 显示与告警

显示与告警这一页讲的核心矛盾是：你必须让关键信息足够显眼，但又不能把操作者淹没在噪声里。

!!! note "本页主问题"
    怎样让操作者在关键时刻既能注意到重要信号，
    又能立刻理解系统状态和下一步动作？

## 本章重点

- display 负责让系统状态可见，
  alert 负责在关键时刻重新分配注意力。
- 好的告警不是“更响更亮”，
  而是“更可信、
  更可判断、
  更能引导动作”。
- false alarm 会侵蚀信任，
  最后导致真正重要的告警也被忽略。
- 显示层级和告警设计，
  本质上都在做注意资源管理。

## 先记住一句话

!!! tip "复习时先记住这句话"
    先记住一句话：
    告警设计的目标不是制造刺激，
    而是让人及时把注意力转到真正需要看的地方，
    并且知道接下来该做什么。

## 显示和告警分别承担什么角色

display 的任务是让状态可见、
可比较、
可推断；
alert 的任务是把注意力在关键时刻拉过去。
如果两者脱节，
就会出现“看见了但看不懂”或“听见了但不知道怎么做”的问题。

## 读这页时要固定问哪三个问题

看到一个告警系统时，
先固定问：

1. 这个告警真的代表高优先级风险吗？
2. 告警出现时，操作者能快速看懂系统处于什么状态吗？
3. 告警之后，下一步动作清楚吗？

## 为什么 false alarm 最后会变成信任问题

如果系统经常发出低价值告警，
操作者就会学会延迟响应、
选择性忽略，
甚至对告警系统整体失去信任。
这样一来，
真正关键的告警也会被拖慢处理。

!!! note "一句话结论"
    显示与告警设计的本质，
    不是“做得更热闹”，
    而是让注意力、
    理解和行动重新对齐。

!!! warning "最容易误解的地方"
    “更多告警更安全”通常是错的。
    低价值告警过多时，
    系统是在消耗注意力，
    而不是保护注意力。

!!! example "案例：为什么 alarm fatigue 最后会拖慢真正关键的反应"
    如果病房监护系统不断发出噪声很大的低优先级告警，
    护理人员会逐渐降低对告警的整体响应敏感度。
    等到真正危及生命的信号出现时，
    系统早已失去“被立即认真对待”的资格。

## 告警真正难的不是被听见，而是被正确排序

很多系统以为只要把告警做得更醒目，
问题就解决了。
但操作者真正面对的不是单一告警，
而是一堆同时竞争注意力的信号。
告警设计真正要解决的是：
哪个最先处理、
哪个只是背景噪声、
哪个必须立即转动作。

也就是说，
alerting 本质上不是感官刺激设计，
而是优先级设计。

## 为什么显示和告警必须一起看

一条告警如果只会响，
却不能把人带到正确状态信息上，
它就只是打断，
不是真正帮助。
好的系统会让告警和显示之间形成清楚 mapping：
听到或看到提醒后，
操作者能立刻找到最关键的状态解释和后续动作线索。

所以课程把 display 和 alert 放在一起讲，
不是巧合，
而是因为二者共同决定了“注意到之后能不能理解并行动”。

!!! example "案例：为什么“听见警报”不等于“知道现在该做什么”"
    如果告警只有声音强度差别，
    却没有把人快速引向故障位置、
    状态趋势和推荐动作，
    操作者就可能先被打断，
    再花额外时间重新找状态。
    这样一来，
    告警反而会制造二次负担。
    好的设计会让告警和显示解释一起出现。

## 为什么 false alarm 和 nuisance alarm 会慢慢掏空整个告警系统

告警系统真正的长期风险，
不只是漏报，
也包括太多不值得响应的报文。
只要操作者持续接触 false alarm 或 nuisance alarm，
系统就会一点点消耗他们对提醒的信任和处理速度。

这就是为什么告警设计既要考虑“有没有报出来”，
也要考虑“报出来的东西是否值得打断人”。
如果系统频繁让人白白切换注意力，
真正的关键警报到来时就更容易被延迟处理。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/displays-and-alerts-2-4-26/page-09.png" alt="这张图要看懂的是：alarm fatigue 不是抽象概念，临床环境里过多 nuisance alarm 会直接侵蚀信任、干扰工作并拖慢真正关键的响应。" loading="lazy">
  <figcaption>这张图要看懂的是：alarm fatigue 不是抽象概念，临床环境里过多 nuisance alarm 会直接侵蚀信任、干扰工作并拖慢真正关键的响应。</figcaption>
</figure>

## 为什么高质量 display 设计会把“看到状态”和“采取动作”直接连起来

display 设计真正成熟时，
不会让操作者先看到一堆分散数据，
再自己艰难拼出局面。
更强的做法，
是让最关键的状态关系和行动线索在界面里被组织出来，
让人一眼知道哪里正在变差、
风险相对方向是什么、
下一步该优先处理什么。

这也是为什么很多航空显示会把交通、
速度带、
告警区和状态趋势整合在一起。
显示一旦能把“注意到”直接接到“理解并行动”，
告警系统整体的负担就会下降。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/displays-and-alerts-2-4-26/page-21.png" alt="这张图要看懂的是：像 TCAS 这样的集成显示，不只是把更多信息放进一个屏，而是把交通冲突、垂直速度和回避指令组织成能直接支持动作的界面。" loading="lazy">
  <figcaption>这张图要看懂的是：像 TCAS 这样的集成显示，不只是把更多信息放进一个屏，而是把交通冲突、垂直速度和回避指令组织成能直接支持动作的界面。</figcaption>
</figure>

## 本章总结

!!! tip "复习时重点记这几条"
    - display 让状态可见，
      alert 让注意力转向关键处。
    - 好的告警必须同时支持理解和行动。
    - false alarm 会侵蚀长期信任。
    - 这页本质上在讲注意资源管理。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `航空与自动化`
- 关联源文件数: 1
- 文本单元数: 619
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Displays and Alerts 2-4-26.pdf` | `pdf` | 619 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Displays and Alerts 2-4-26.pdf) |

## 相关主题

- [注意与监控](../HFE_Human_Performance/attention_and_monitoring.md)
- [检查单与程序](checklists_and_procedures.md)
- [航空与自动化导论](aviation_automation_intro.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "Displays and Alerts 2-4-26.pdf | 619 text units"
    下载原件: [Displays and Alerts 2-4-26.pdf](../assets/source_files/Lectures_Spring_2026/Displays and Alerts 2-4-26.pdf)
    映射页面: `displays_and_alerts`
    
    ```text
    [displays-and-alerts-2-4-26-0001] page:1:line:1 | DISPLAYS AND ALERTS
    [displays-and-alerts-2-4-26-0002] page:1:line:2 | ENP-0112
    [displays-and-alerts-2-4-26-0003] page:1:line:3 | 2/4/2026
    [displays-and-alerts-2-4-26-0004] page:1:line:4 | Dr. Divya C. Chandra
    [displays-and-alerts-2-4-26-0005] page:1:line:5 | 2/4/26
    [displays-and-alerts-2-4-26-0006] page:1:line:6 | ENP-0112
    [displays-and-alerts-2-4-26-0007] page:1:line:7 | 1
    [displays-and-alerts-2-4-26-0008] page:2:line:1 | TOPICS
    [displays-and-alerts-2-4-26-0009] page:2:line:2 | • Visual displays
    [displays-and-alerts-2-4-26-0010] page:2:line:3 | • Auditory displays
    [displays-and-alerts-2-4-26-0011] page:2:line:4 | • Alerts in aviation
    [displays-and-alerts-2-4-26-0012] page:2:line:5 | • Collision avoidance
    [displays-and-alerts-2-4-26-0013] page:2:line:6 | • Implementation and testing
    [displays-and-alerts-2-4-26-0014] page:2:line:7 | 2/4/26
    [displays-and-alerts-2-4-26-0015] page:2:line:8 | ENP-0112
    [displays-and-alerts-2-4-26-0016] page:2:line:9 | 2
    [displays-and-alerts-2-4-26-0017] page:3:line:1 | VISUAL DISPLAYS
    [displays-and-alerts-2-4-26-0018] page:3:line:2 | 3
    [displays-and-alerts-2-4-26-0019] page:3:line:3 | 2/4/26
    [displays-and-alerts-2-4-26-0020] page:3:line:4 | ENP-0112
    [displays-and-alerts-2-4-26-0021] page:4:line:1 | VISUAL DISPLAY DESIGN CONSIDERATIONS
    [displays-and-alerts-2-4-26-0022] page:4:line:2 | • Display size
    [displays-and-alerts-2-4-26-0023] page:4:line:3 | • Screen resolution
    [displays-and-alerts-2-4-26-0024] page:4:line:4 | • Off-axis viewing
    [displays-and-alerts-2-4-26-0025] page:4:line:5 | • Luminance
    [displays-and-alerts-2-4-26-0026] page:4:line:6 | • Brightness
    [displays-and-alerts-2-4-26-0027] page:4:line:7 | • Font
    [displays-and-alerts-2-4-26-0028] page:4:line:8 | •
    [displays-and-alerts-2-4-26-0029] page:4:line:9 | Size (in visual angle)
    [displays-and-alerts-2-4-26-0030] page:4:line:10 | •
    [displays-and-alerts-2-4-26-0031] page:4:line:11 | Readability (e.g., serifs and spacing)
    [displays-and-alerts-2-4-26-0032] page:4:line:12 | • Field of view
    [displays-and-alerts-2-4-26-0033] page:4:line:13 | • Vibrations
    [displays-and-alerts-2-4-26-0034] page:4:line:14 | • Dark adaptation
    [displays-and-alerts-2-4-26-0035] page:4:line:15 | • Density
    [displays-and-alerts-2-4-26-0036] page:4:line:16 | • Clutter
    [displays-and-alerts-2-4-26-0037] page:4:line:17 | • Color and contrast
    [displays-and-alerts-2-4-26-0038] page:4:line:18 | • Highlighting
    [displays-and-alerts-2-4-26-0039] page:4:line:19 | • Grouping
    [displays-and-alerts-2-4-26-0040] page:4:line:20 | • Graphical vs. text representation of data
    [displays-and-alerts-2-4-26-0041] page:4:line:21 | • Analog vs. Digital
    [displays-and-alerts-2-4-26-0042] page:4:line:22 | • Redundant coding
    [displays-and-alerts-2-4-26-0043] page:4:line:23 | 4
    [displays-and-alerts-2-4-26-0044] page:4:line:24 | See also, Proctor & Van Zandt (Reading List)
    [displays-and-alerts-2-4-26-0045] page:4:line:25 | 2/4/26
    [displays-and-alerts-2-4-26-0046] page:4:line:26 | ENP-0112
    [displays-and-alerts-2-4-26-0047] page:5:line:1 | VISUAL DISPLAY DESIGN PRINCIPLES
    [displays-and-alerts-2-4-26-0048] page:5:line:2 | • Principle of Information Need
    [displays-and-alerts-2-4-26-0049] page:5:line:3 | • Proximity Compatibility
    [displays-and-alerts-2-4-26-0050] page:5:line:4 | • Redundancy
    [displays-and-alerts-2-4-26-0051] page:5:line:5 | • Principle of Pictorial Realism
    [displays-and-alerts-2-4-26-0052] page:5:line:6 | • Principle of the Moving Part
    [displays-and-alerts-2-4-26-0053] page:5:line:7 | • Predictive Aiding
    [displays-and-alerts-2-4-26-0054] page:5:line:8 | 5
    [displays-and-alerts-2-4-26-0055] page:5:line:9 | Wickens et al., 2004
    [displays-and-alerts-2-4-26-0056] page:5:line:10 | 2/4/26
    [displays-and-alerts-2-4-26-0057] page:5:line:11 | ENP-0112
    [displays-and-alerts-2-4-26-0058] page:6:line:1 | AUDITORY DISPLAYS
    [displays-and-alerts-2-4-26-0059] page:6:line:2 | 6
    [displays-and-alerts-2-4-26-0060] page:6:line:3 | 2/4/26
    [displays-and-alerts-2-4-26-0061] page:6:line:4 | ENP-0112
    [displays-and-alerts-2-4-26-0062] page:7:line:1 | TYPES OF AUDITORY DISPLAYS
    [displays-and-alerts-2-4-26-0063] page:7:line:2 | • Symbolic
    [displays-and-alerts-2-4-26-0064] page:7:line:3 | • Map sounds to meanings
    [displays-and-alerts-2-4-26-0065] page:7:line:4 | • e.g., emergency preparedness signal, mail
    [displays-and-alerts-2-4-26-0066] page:7:line:5 | • Non-speech
    [displays-and-alerts-2-4-26-0067] page:7:line:6 | • Tones, combinations of frequencies, patterns
    [displays-and-alerts-2-4-26-0068] page:7:line:7 | • Can vary in time
    [displays-and-alerts-2-4-26-0069] page:7:line:8 | • Speech
    [displays-and-alerts-2-4-26-0070] page:7:line:9 | • Can be used in combination with non-speech
    [displays-and-alerts-2-4-26-0071] page:7:line:10 | • Can convey more complex information, if the person is alert
    [displays-and-alerts-2-4-26-0072] page:7:line:11 | Aural warnings test
    [displays-and-alerts-2-4-26-0073] page:7:line:12 | 2/4/26
    [displays-and-alerts-2-4-26-0074] page:7:line:13 | ENP-0112
    [displays-and-alerts-2-4-26-0075] page:7:line:14 | 7
    [displays-and-alerts-2-4-26-0076] page:8:line:1 | AUDITORY ALARMS
    [displays-and-alerts-2-4-26-0077] page:8:line:2 | • Primarily used for emergency alarms and warning signals
    [displays-and-alerts-2-4-26-0078] page:8:line:3 | • True alarms: alarms sounded when intended
    [displays-and-alerts-2-4-26-0079] page:8:line:4 | • False alarm: sounds, but does not need to
    [displays-and-alerts-2-4-26-0080] page:8:line:5 | • Missed alarm: should have sounded, but did not
    [displays-and-alerts-2-4-26-0081] page:8:line:6 | • Nuisance alarm: sounds as intended, but when the alert is not really needed for operations
    [displays-and-alerts-2-4-26-0082] page:8:line:7 | 8
    [displays-and-alerts-2-4-26-0083] page:8:line:8 | 2/4/26
    [displays-and-alerts-2-4-26-0084] page:8:line:9 | ENP-0112
    [displays-and-alerts-2-4-26-0085] page:9:line:1 | ALARM INCIDENTS IN CLINICAL CARE
    [displays-and-alerts-2-4-26-0086] page:9:line:2 | • False alarms problematic (81%
    [displays-and-alerts-2-4-26-0087] page:9:line:3 | respondents)
    [displays-and-alerts-2-4-26-0088] page:9:line:4 | • Nuisance alarms disruptive to
    [displays-and-alerts-2-4-26-0089] page:9:line:5 | patient care (77% respondents)
    [displays-and-alerts-2-4-26-0090] page:9:line:6 | • Distrust alarms and disable devices
    [displays-and-alerts-2-4-26-0091] page:9:line:7 | (78% respondents)
    [displays-and-alerts-2-4-26-0092] page:9:line:8 | 9
    [displays-and-alerts-2-4-26-0093] page:9:line:9 | nursing.advanceweb.com
    [displays-and-alerts-2-4-26-0094] page:9:line:10 | Korniewicz D, Clark T, David Y. A National Online Survey on the Effectiveness of Clinical
    [displays-and-alerts-2-4-26-0095] page:9:line:11 | Alarms. American Journal of Critical Care Management 17(1): 36-41, 2008.
    [displays-and-alerts-2-4-26-0096] page:9:line:12 | 2/4/26
    [displays-and-alerts-2-4-26-0097] page:9:line:13 | ENP-0112
    [displays-and-alerts-2-4-26-0098] page:10:line:1 | From Ahlstrom, 2003 DOT/FAA/CT-TN03/10
    [displays-and-alerts-2-4-26-0099] page:10:line:2 | AUDITORY ALARM ISSUES IN AIR TRAFFIC CONTROL
    [displays-and-alerts-2-4-26-0100] page:10:line:3 | Table 2.  Mean Ratings of Items by Terminal AT Participants
    [displays-and-alerts-2-4-26-0101] page:10:line:4 | Problem
    [displays-and-alerts-2-4-26-0102] page:10:line:5 | Mean
    [displays-and-alerts-2-4-26-0103] page:10:line:6 | St Dev
    [displays-and-alerts-2-4-26-0104] page:10:line:7 | Alarms are easily confused (because they sound alike)
    [displays-and-alerts-2-4-26-0105] page:10:line:8 | 6.7
    [displays-and-alerts-2-4-26-0106] page:10:line:9 | 3.18
    [displays-and-alerts-2-4-26-0107] page:10:line:10 | Alarms go off too frequently, especially false alarms
    [displays-and-alerts-2-4-26-0108] page:10:line:11 | 6.4
    [displays-and-alerts-2-4-26-0109] page:10:line:12 | 3.57
    [displays-and-alerts-2-4-26-0110] page:10:line:13 | Alarms are annoying
    [displays-and-alerts-2-4-26-0111] page:10:line:14 | 6.3
    [displays-and-alerts-2-4-26-0112] page:10:line:15 | 2.53
    [displays-and-alerts-2-4-26-0113] page:10:line:16 | It is difficult to locate the source of the alarms
    [displays-and-alerts-2-4-26-0114] page:10:line:17 | 5.3
    [displays-and-alerts-2-4-26-0115] page:10:line:18 | 3.26
    [displays-and-alerts-2-4-26-0116] page:10:line:19 | Too many alarms go off at the same time
    [displays-and-alerts-2-4-26-0117] page:10:line:20 | 5.2
    [displays-and-alerts-2-4-26-0118] page:10:line:21 | 3.33
    [displays-and-alerts-2-4-26-0119] page:10:line:22 | There are too many alarms for a person to learn the meaning of each alarm
    [displays-and-alerts-2-4-26-0120] page:10:line:23 | 4.9
    [displays-and-alerts-2-4-26-0121] page:10:line:24 | 3.41
    [displays-and-alerts-2-4-26-0122] page:10:line:25 | Alarms sound more urgent than they should or sound less urgent than they should
    [displays-and-alerts-2-4-26-0123] page:10:line:26 | 4.8
    [displays-and-alerts-2-4-26-0124] page:10:line:27 | 3.16
    [displays-and-alerts-2-4-26-0125] page:10:line:28 | Alarms are too loud
    [displays-and-alerts-2-4-26-0126] page:10:line:29 | 4.5
    [displays-and-alerts-2-4-26-0127] page:10:line:30 | 2.91
    [displays-and-alerts-2-4-26-0128] page:10:line:31 | Alarms disrupt thought
    [displays-and-alerts-2-4-26-0129] page:10:line:32 | 4.4
    [displays-and-alerts-2-4-26-0130] page:10:line:33 | 3.66
    [displays-and-alerts-2-4-26-0131] page:10:line:34 | Alarms can be masked (difficult to hear over background noise)
    [displays-and-alerts-2-4-26-0132] page:10:line:35 | 4.1
    [displays-and-alerts-2-4-26-0133] page:10:line:36 | 3.43
    [displays-and-alerts-2-4-26-0134] page:10:line:37 | Alarms interfere with voice communications
    [displays-and-alerts-2-4-26-0135] page:10:line:38 | 4.0
    [displays-and-alerts-2-4-26-0136] page:10:line:39 | 2.87
    [displays-and-alerts-2-4-26-0137] page:10:line:40 | Alarms startle the user
    [displays-and-alerts-2-4-26-0138] page:10:line:41 | 3.8
    [displays-and-alerts-2-4-26-0139] page:10:line:42 | 2.77
    [displays-and-alerts-2-4-26-0140] page:10:line:43 | Some alarms which are visual would be better auditory and vice versa
    [displays-and-alerts-2-4-26-0141] page:10:line:44 | 3.1
    [displays-and-alerts-2-4-26-0142] page:10:line:45 | 2.84
    [displays-and-alerts-2-4-26-0143] page:10:line:46 | There are not audio alarms in some situations where there should be audio alarms
    [displays-and-alerts-2-4-26-0144] page:10:line:47 | 2.1
    [displays-and-alerts-2-4-26-0145] page:10:line:48 | 2.29
    [displays-and-alerts-2-4-26-0146] page:10:line:49 | Alarms go off so infrequently, that when they do go off, those hearing the alarms don't
    [displays-and-alerts-2-4-26-0147] page:10:line:50 | know their meaning
    [displays-and-alerts-2-4-26-0148] page:10:line:51 | 1.9
    [displays-and-alerts-2-4-26-0149] page:10:line:52 | 2.39
    [displays-and-alerts-2-4-26-0150] page:10:line:53 | 0 (not a problem) to
    [displays-and-alerts-2-4-26-0151] page:10:line:54 | 10 (severe problem)
    [displays-and-alerts-2-4-26-0152] page:10:line:55 | 2/4/26
    [displays-and-alerts-2-4-26-0153] page:10:line:56 | ENP-0112
    [displays-and-alerts-2-4-26-0154] page:10:line:57 | 10
    [displays-and-alerts-2-4-26-0155] page:11:line:1 | URGENCY
    [displays-and-alerts-2-4-26-0156] page:11:line:2 | • Too loud is ineffective; most effective way to increase urgency is to increase speed of warning
    [displays-and-alerts-2-4-26-0157] page:11:line:3 | • Urgency categories and central warning design
    [displays-and-alerts-2-4-26-0158] page:11:line:4 | • See Title 14 Code of Federal Regulations Section 25.1322 Flightcrew alerting
    [displays-and-alerts-2-4-26-0159] page:11:line:5 | Level of Urgency
    [displays-and-alerts-2-4-26-0160] page:11:line:6 | Meaning
    [displays-and-alerts-2-4-26-0161] page:11:line:7 | Visual Cue
    [displays-and-alerts-2-4-26-0162] page:11:line:8 | Auditory Cue
    [displays-and-alerts-2-4-26-0163] page:11:line:9 | Warning
    [displays-and-alerts-2-4-26-0164] page:11:line:10 | Immediate action required
    [displays-and-alerts-2-4-26-0165] page:11:line:11 | Red
    [displays-and-alerts-2-4-26-0166] page:11:line:12 | Nonverbal to get attention, backup verbal
    [displays-and-alerts-2-4-26-0167] page:11:line:13 | message for more information
    [displays-and-alerts-2-4-26-0168] page:11:line:14 | Caution
    [displays-and-alerts-2-4-26-0169] page:11:line:15 | Immediate awareness and
    [displays-and-alerts-2-4-26-0170] page:11:line:16 | subsequent response
    [displays-and-alerts-2-4-26-0171] page:11:line:17 | Amber or Yellow
    [displays-and-alerts-2-4-26-0172] page:11:line:18 | Non verbal (optional verbal)
    [displays-and-alerts-2-4-26-0173] page:11:line:19 | Advisory
    [displays-and-alerts-2-4-26-0174] page:11:line:20 | Awareness and may require
    [displays-and-alerts-2-4-26-0175] page:11:line:21 | subsequent response
    [displays-and-alerts-2-4-26-0176] page:11:line:22 | Any color other
    [displays-and-alerts-2-4-26-0177] page:11:line:23 | than red or green
    [displays-and-alerts-2-4-26-0178] page:11:line:24 | n/a
    [displays-and-alerts-2-4-26-0179] page:11:line:25 | Non-alert
    [displays-and-alerts-2-4-26-0180] page:11:line:26 | Information only
    [displays-and-alerts-2-4-26-0181] page:11:line:27 | Green, white, cyan,
    [displays-and-alerts-2-4-26-0182] page:11:line:28 | etc.
    [displays-and-alerts-2-4-26-0183] page:11:line:29 | None (Quiet/Dark)
    [displays-and-alerts-2-4-26-0184] page:11:line:30 | Edworthy, J. Loxley, S., and Dennis, I. (1991). Improving Auditory Warning Design: Relationship between Warning Sound Parameters and
    [displays-and-alerts-2-4-26-0185] page:11:line:31 | Perceived Urgency. Human Factors 33(2) pp. 205-231. https://doi.org/10.1177/001872089103300206
    [displays-and-alerts-2-4-26-0186] page:11:line:32 | 2/4/26
    [displays-and-alerts-2-4-26-0187] page:11:line:33 | ENP-0112
    [displays-and-alerts-2-4-26-0188] page:11:line:34 | 11
    [displays-and-alerts-2-4-26-0189] page:12:line:1 | AUDITORY VS. VISUAL DISPLAYS
    [displays-and-alerts-2-4-26-0190] page:12:line:2 | Auditory
    [displays-and-alerts-2-4-26-0191] page:12:line:3 | Visual
    [displays-and-alerts-2-4-26-0192] page:12:line:4 | Reception
    [displays-and-alerts-2-4-26-0193] page:12:line:5 | Omnidirectional
    [displays-and-alerts-2-4-26-0194] page:12:line:6 | Must be in field of view
    [displays-and-alerts-2-4-26-0195] page:12:line:7 | (Attention & selection)
    [displays-and-alerts-2-4-26-0196] page:12:line:8 | Speed
    [displays-and-alerts-2-4-26-0197] page:12:line:9 | Fastest
    [displays-and-alerts-2-4-26-0198] page:12:line:10 | Slowest
    [displays-and-alerts-2-4-26-0199] page:12:line:11 | Order
    [displays-and-alerts-2-4-26-0200] page:12:line:12 | Difficult
    [displays-and-alerts-2-4-26-0201] page:12:line:13 | Easy
    [displays-and-alerts-2-4-26-0202] page:12:line:14 | Urgency
    [displays-and-alerts-2-4-26-0203] page:12:line:15 | Easy
    [displays-and-alerts-2-4-26-0204] page:12:line:16 | Difficult
    [displays-and-alerts-2-4-26-0205] page:12:line:17 | Noise
    [displays-and-alerts-2-4-26-0206] page:12:line:18 | Not affected by visual
    [displays-and-alerts-2-4-26-0207] page:12:line:19 | Not affected by audio
    [displays-and-alerts-2-4-26-0208] page:12:line:20 | Symbolism
    [displays-and-alerts-2-4-26-0209] page:12:line:21 | Melodious, linguistic
    [displays-and-alerts-2-4-26-0210] page:12:line:22 | Pictorial, linguistic
    [displays-and-alerts-2-4-26-0211] page:12:line:23 | Mobility
    [displays-and-alerts-2-4-26-0212] page:12:line:24 | Most flexible
    [displays-and-alerts-2-4-26-0213] page:12:line:25 | Some flexibility
    [displays-and-alerts-2-4-26-0214] page:12:line:26 | Suitability
    [displays-and-alerts-2-4-26-0215] page:12:line:27 | Time-dependent info
    [displays-and-alerts-2-4-26-0216] page:12:line:28 | Space-dependent info
    [displays-and-alerts-2-4-26-0217] page:12:line:29 | 2/4/26
    [displays-and-alerts-2-4-26-0218] page:12:line:30 | ENP-0112
    [displays-and-alerts-2-4-26-0219] page:12:line:31 | 12
    [displays-and-alerts-2-4-26-0220] page:13:line:1 | WHEN TO USE AUDIO OR VISUAL DISPLAYS
    [displays-and-alerts-2-4-26-0221] page:13:line:2 | • Not an either/or situation, could use both
    [displays-and-alerts-2-4-26-0222] page:13:line:3 | Auditory
    [displays-and-alerts-2-4-26-0223] page:13:line:4 | Visual
    [displays-and-alerts-2-4-26-0224] page:13:line:5 | Message is simple/short
    [displays-and-alerts-2-4-26-0225] page:13:line:6 | Message is complex/long
    [displays-and-alerts-2-4-26-0226] page:13:line:7 | Message won’t be referred to later
    [displays-and-alerts-2-4-26-0227] page:13:line:8 | Message will be referred to later
    [displays-and-alerts-2-4-26-0228] page:13:line:9 | Message deals with time
    [displays-and-alerts-2-4-26-0229] page:13:line:10 | Message deals with space
    [displays-and-alerts-2-4-26-0230] page:13:line:11 | Immediate action required
    [displays-and-alerts-2-4-26-0231] page:13:line:12 | Immediate action not required
    [displays-and-alerts-2-4-26-0232] page:13:line:13 | Visual channel overburdened
    [displays-and-alerts-2-4-26-0233] page:13:line:14 | Auditory systems overburdened
    [displays-and-alerts-2-4-26-0234] page:13:line:15 | Brightness/Darkness problems
    [displays-and-alerts-2-4-26-0235] page:13:line:16 | Noisy environment
    [displays-and-alerts-2-4-26-0236] page:13:line:17 | Person is moving
    [displays-and-alerts-2-4-26-0237] page:13:line:18 | Person is static
    [displays-and-alerts-2-4-26-0238] page:13:line:19 | Communications with many people at the
    [displays-and-alerts-2-4-26-0239] page:13:line:20 | same time
    [displays-and-alerts-2-4-26-0240] page:13:line:21 | Communication with one (or few) individuals, or
    [displays-and-alerts-2-4-26-0241] page:13:line:22 | when info has to be distributed at different times
    [displays-and-alerts-2-4-26-0242] page:13:line:23 | When multiple complex data sources are
    [displays-and-alerts-2-4-26-0243] page:13:line:24 | monitored compared
    [displays-and-alerts-2-4-26-0244] page:13:line:25 | When high resolution of variables is required or
    [displays-and-alerts-2-4-26-0245] page:13:line:26 | when absolute (instead of relative) values are
    [displays-and-alerts-2-4-26-0246] page:13:line:27 | required
    [displays-and-alerts-2-4-26-0247] page:13:line:28 | When 3D aspect can be represented
    [displays-and-alerts-2-4-26-0248] page:13:line:29 | (spatialized sound)
    [displays-and-alerts-2-4-26-0249] page:13:line:30 | When sound would interfere with the task (e.g.,
    [displays-and-alerts-2-4-26-0250] page:13:line:31 | speech) or be masked by the environment
    [displays-and-alerts-2-4-26-0251] page:13:line:32 | 2/4/26
    [displays-and-alerts-2-4-26-0252] page:13:line:33 | ENP-0112
    [displays-and-alerts-2-4-26-0253] page:13:line:34 | 13
    [displays-and-alerts-2-4-26-0254] page:14:line:1 | ALERTS IN AVIATION
    [displays-and-alerts-2-4-26-0255] page:14:line:2 | 14
    [displays-and-alerts-2-4-26-0256] page:14:line:3 | 2/4/26
    [displays-and-alerts-2-4-26-0257] page:14:line:4 | ENP-0112
    [displays-and-alerts-2-4-26-0258] page:15:line:1 | CONSIDERATIONS FOR DESIGN OF AURAL WARNINGS
    [displays-and-alerts-2-4-26-0259] page:15:line:2 | • Goal: Accomplish intended function without disrupting user’s ongoing tasks and
    [displays-and-alerts-2-4-26-0260] page:15:line:3 | information processing
    [displays-and-alerts-2-4-26-0261] page:15:line:4 | • What’s the intended function?
    [displays-and-alerts-2-4-26-0262] page:15:line:5 | • Attract attention (alert), convey information, or both?
    [displays-and-alerts-2-4-26-0263] page:15:line:6 | • Cue to perform an action or indication that a defined threshold has been reached
    [displays-and-alerts-2-4-26-0264] page:15:line:7 | • Additional context/explanation (urgency, nature of the problem)
    [displays-and-alerts-2-4-26-0265] page:15:line:8 | • Voice messages both alert and inform
    [displays-and-alerts-2-4-26-0266] page:15:line:9 | • Avoid startle response (onset rate)
    [displays-and-alerts-2-4-26-0267] page:15:line:10 | • Convey urgency
    [displays-and-alerts-2-4-26-0268] page:15:line:11 | • Warning, caution, advisory
    [displays-and-alerts-2-4-26-0269] page:15:line:12 | 2/4/26
    [displays-and-alerts-2-4-26-0270] page:15:line:13 | ENP-0112
    [displays-and-alerts-2-4-26-0271] page:15:line:14 | 15
    [displays-and-alerts-2-4-26-0272] page:16:line:1 | MORE DESIGN CONSIDERATIONS FOR AURAL
    [displays-and-alerts-2-4-26-0273] page:16:line:2 | WARNINGS
    [displays-and-alerts-2-4-26-0274] page:16:line:3 | • Compliance
    [displays-and-alerts-2-4-26-0275] page:16:line:4 | • Intervention immediacy vs. intervention importance
    [displays-and-alerts-2-4-26-0276] page:16:line:5 | • Effectiveness
    [displays-and-alerts-2-4-26-0277] page:16:line:6 | • Understandability +
    [displays-and-alerts-2-4-26-0278] page:16:line:7 | • Learning time and retention
    [displays-and-alerts-2-4-26-0279] page:16:line:8 | • Number of different warnings
    [displays-and-alerts-2-4-26-0280] page:16:line:9 | • More is less (potential for confusion)
    [displays-and-alerts-2-4-26-0281] page:16:line:10 | • Similar temporal patterns are confusable, as are single tones
    [displays-and-alerts-2-4-26-0282] page:16:line:11 | • How many is too many?
    [displays-and-alerts-2-4-26-0283] page:16:line:12 | 2/4/26
    [displays-and-alerts-2-4-26-0284] page:16:line:13 | ENP-0112
    [displays-and-alerts-2-4-26-0285] page:16:line:14 | 16
    [displays-and-alerts-2-4-26-0286] page:17:line:1 | STILL MORE DESIGN CONSIDERATIONS FOR AURAL
    [displays-and-alerts-2-4-26-0287] page:17:line:2 | WARNINGS
    [displays-and-alerts-2-4-26-0288] page:17:line:3 | • Background noise & prominence
    [displays-and-alerts-2-4-26-0289] page:17:line:4 | • Match warning frequencies and amplitudes to environment
    [displays-and-alerts-2-4-26-0290] page:17:line:5 | • Auditory masking
    [displays-and-alerts-2-4-26-0291] page:17:line:6 | • Ensure audibility without disrupting subsequent speech
    [displays-and-alerts-2-4-26-0292] page:17:line:7 | • Cascading alarms & cacophony
    [displays-and-alerts-2-4-26-0293] page:17:line:8 | • Standardization
    [displays-and-alerts-2-4-26-0294] page:17:line:9 | • User expectations and prior learning
    [displays-and-alerts-2-4-26-0295] page:17:line:10 | • Testing for comprehension and usability
    [displays-and-alerts-2-4-26-0296] page:17:line:11 | 2/4/26
    [displays-and-alerts-2-4-26-0297] page:17:line:12 | ENP-0112
    [displays-and-alerts-2-4-26-0298] page:17:line:13 | 17
    [displays-and-alerts-2-4-26-0299] page:18:line:1 | COLLISION AVOIDANCE
    [displays-and-alerts-2-4-26-0300] page:18:line:2 | 2/4/26
    [displays-and-alerts-2-4-26-0301] page:18:line:3 | ENP-0112
    [displays-and-alerts-2-4-26-0302] page:18:line:4 | 18
    [displays-and-alerts-2-4-26-0303] page:19:line:1 | PILOT TRAINING — “SEE AND AVOID”
    [displays-and-alerts-2-4-26-0304] page:19:line:2 | • “Rules of the air” (right of way) in uncontrolled airspace (without ATC)
    [displays-and-alerts-2-4-26-0305] page:19:line:3 | •
    [displays-and-alerts-2-4-26-0306] page:19:line:4 | Title 14 Code of Federal Regulations (CFR) § 91.113 Right-of-way rules: Except water operations.
    [displays-and-alerts-2-4-26-0307] page:19:line:5 | •
    [displays-and-alerts-2-4-26-0308] page:19:line:6 | Title 14 CFR § 107.37 Operation near aircraft; right-of-way rules [For Unmanned aircraft]
    [displays-and-alerts-2-4-26-0309] page:19:line:7 | • For example, from § 91.113
    [displays-and-alerts-2-4-26-0310] page:19:line:8 | (d) Converging. When aircraft of the same category are converging at approximately the same altitude (except head-on,
    [displays-and-alerts-2-4-26-0311] page:19:line:9 | or nearly so), the aircraft to the other's right has the right-of-way. If the aircraft are of different categories—
    [displays-and-alerts-2-4-26-0312] page:19:line:10 | (1) A balloon has the right-of-way over any other category of aircraft;
    [displays-and-alerts-2-4-26-0313] page:19:line:11 | (2) A glider has the right-of-way over powered aircraft.
    [displays-and-alerts-2-4-26-0314] page:19:line:12 | (3) An airship has the right-of-way over all other powered aircraft, except for an aircraft towing or refueling other aircraft.
    [displays-and-alerts-2-4-26-0315] page:19:line:13 | (4) An aircraft towing or refueling other aircraft has the right-of-way over all other powered aircraft.
    [displays-and-alerts-2-4-26-0316] page:19:line:14 | (e) Approaching head-on. When aircraft are approaching each other head-on, or nearly so, each pilot of each aircraft
    [displays-and-alerts-2-4-26-0317] page:19:line:15 | shall alter course to the right.
    [displays-and-alerts-2-4-26-0318] page:19:line:16 | • Self-announce position when landing and departing uncontrolled airports (without ATC)
    [displays-and-alerts-2-4-26-0319] page:19:line:17 | 2/4/26
    [displays-and-alerts-2-4-26-0320] page:19:line:18 | ENP-0112
    [displays-and-alerts-2-4-26-0321] page:19:line:19 | 19
    [displays-and-alerts-2-4-26-0322] page:20:line:1 | SURVEILLANCE TECHNOLOGIES
    [displays-and-alerts-2-4-26-0323] page:20:line:2 | • Primary and Secondary Surveillance Radar
    [displays-and-alerts-2-4-26-0324] page:20:line:3 | •
    [displays-and-alerts-2-4-26-0325] page:20:line:4 | Center (12 sec) vs. Terminal (5-sec) rotation rates
    [displays-and-alerts-2-4-26-0326] page:20:line:5 | •
    [displays-and-alerts-2-4-26-0327] page:20:line:6 | Position uncertainty if aircraft is turning or climbing/descending
    [displays-and-alerts-2-4-26-0328] page:20:line:7 | • Automatic-Dependent Surveillance – Broadcast (ADS-B)
    [displays-and-alerts-2-4-26-0329] page:20:line:8 | •
    [displays-and-alerts-2-4-26-0330] page:20:line:9 | Out: own aircraft transmits position
    [displays-and-alerts-2-4-26-0331] page:20:line:10 | •
    [displays-and-alerts-2-4-26-0332] page:20:line:11 | In: own aircraft receives positions from other aircraft
    [displays-and-alerts-2-4-26-0333] page:20:line:12 | •
    [displays-and-alerts-2-4-26-0334] page:20:line:13 | 1-second refresh rate, position plus other data
    [displays-and-alerts-2-4-26-0335] page:20:line:14 | • Airborne surveillance (TCAS)
    [displays-and-alerts-2-4-26-0336] page:20:line:15 | •
    [displays-and-alerts-2-4-26-0337] page:20:line:16 | Some version of TCAS is mandatory on most commercial aircraft
    [displays-and-alerts-2-4-26-0338] page:20:line:17 | •
    [displays-and-alerts-2-4-26-0339] page:20:line:18 | See for example, 14 CFR § 121.356 Collision avoidance system
    [displays-and-alerts-2-4-26-0340] page:20:line:19 | •
    [displays-and-alerts-2-4-26-0341] page:20:line:20 | Traffic display and vertical resolution advisories
    [displays-and-alerts-2-4-26-0342] page:20:line:21 | •
    [displays-and-alerts-2-4-26-0343] page:20:line:22 | Assumes 5-sec response time for pilot
    [displays-and-alerts-2-4-26-0344] page:20:line:23 | • Airborne Collision Avoidance System – X (ACAS X family)
    [displays-and-alerts-2-4-26-0345] page:20:line:24 | •
    [displays-and-alerts-2-4-26-0346] page:20:line:25 | Incorporates neural networks
    [displays-and-alerts-2-4-26-0347] page:20:line:26 | •
    [displays-and-alerts-2-4-26-0348] page:20:line:27 | Xu version is for unmanned aerial vehicles, sXu for small unmanned aerial vehicles
    [displays-and-alerts-2-4-26-0349] page:20:line:28 | Limitations of  the technology
    [displays-and-alerts-2-4-26-0350] page:20:line:29 | affect alert design and logic.
    [displays-and-alerts-2-4-26-0351] page:20:line:30 | 2/4/26
    [displays-and-alerts-2-4-26-0352] page:20:line:31 | ENP-0112
    [displays-and-alerts-2-4-26-0353] page:20:line:32 | 20
    [displays-and-alerts-2-4-26-0354] page:21:line:1 | INTEGRATED TRAFFIC DISPLAYS
    [displays-and-alerts-2-4-26-0355] page:21:line:2 | Traffic alert and collision avoidance system (TCAS) displays may be
    [displays-and-alerts-2-4-26-0356] page:21:line:3 | integrated with a vertical speed indicator or primary flight display
    [displays-and-alerts-2-4-26-0357] page:21:line:4 | 2/4/26
    [displays-and-alerts-2-4-26-0358] page:21:line:5 | ENP-0112
    [displays-and-alerts-2-4-26-0359] page:21:line:6 | 21
    [displays-and-alerts-2-4-26-0360] page:21:line:7 | TCAS display, photo by Paul Nelson
    [displays-and-alerts-2-4-26-0361] page:21:line:8 | Figures 2-1 and 2.2 from AC 90-120 (November 2024)
    [displays-and-alerts-2-4-26-0362] page:22:line:1 | •
    [displays-and-alerts-2-4-26-0363] page:22:line:2 | New symbols can present more
    [displays-and-alerts-2-4-26-0364] page:22:line:3 | information
    [displays-and-alerts-2-4-26-0365] page:22:line:4 | e.g., data quality, directionality
    [displays-and-alerts-2-4-26-0366] page:22:line:5 | •
    [displays-and-alerts-2-4-26-0367] page:22:line:6 | How much information can be
    [displays-and-alerts-2-4-26-0368] page:22:line:7 | encoded visually in a traffic symbol
    [displays-and-alerts-2-4-26-0369] page:22:line:8 | without confusing the pilot?
    [displays-and-alerts-2-4-26-0370] page:22:line:9 | Garmin G-1000 Cockpit Display of Traffic Information (CDTI) (RTCA SC-186, 2008)
    [displays-and-alerts-2-4-26-0371] page:22:line:10 | ADS-B TRAFFIC DISPLAY
    [displays-and-alerts-2-4-26-0372] page:22:line:11 | Automatic-Dependent Surveillance-Broadcast (ADS-B) technology
    [displays-and-alerts-2-4-26-0373] page:22:line:12 | 2/4/26
    [displays-and-alerts-2-4-26-0374] page:22:line:13 | ENP-0112
    [displays-and-alerts-2-4-26-0375] page:22:line:14 | 22
    [displays-and-alerts-2-4-26-0376] page:23:line:1 | TRAFFIC DISPLAY SYMBOLOGY EXAMPLES (AC 90-120)
    [displays-and-alerts-2-4-26-0377] page:23:line:2 | 2/4/26
    [displays-and-alerts-2-4-26-0378] page:23:line:3 | ENP-0112
    [displays-and-alerts-2-4-26-0379] page:23:line:4 | 23
    [displays-and-alerts-2-4-26-0380] page:23:line:5 | TCAS traffic display (left column) shows symbols:
    [displays-and-alerts-2-4-26-0381] page:23:line:6 | – Traffic Alerts (TAs) [yellow circle]
    [displays-and-alerts-2-4-26-0382] page:23:line:7 | – Resolution Advisories (RAs) [red square]
    [displays-and-alerts-2-4-26-0383] page:23:line:8 | – Proximate traffic as either hollow or filled diamond
    [displays-and-alerts-2-4-26-0384] page:23:line:9 | – Relative altitude and climb/descent information
    [displays-and-alerts-2-4-26-0385] page:23:line:10 | And generates aural messages, such as:
    [displays-and-alerts-2-4-26-0386] page:23:line:11 | – “Traffic, Traffic” (TA)
    [displays-and-alerts-2-4-26-0387] page:23:line:12 | – “Climb, Climb” (RA)
    [displays-and-alerts-2-4-26-0388] page:23:line:13 | ACAS II or ADS-B symbols in right column
    [displays-and-alerts-2-4-26-0389] page:24:line:1 | TCAS AURAL WARNINGS
    [displays-and-alerts-2-4-26-0390] page:24:line:2 | • TCAS test
    [displays-and-alerts-2-4-26-0391] page:24:line:3 | • Without and with audio
    [displays-and-alerts-2-4-26-0392] page:24:line:4 | • Altitude tape version of TCAS
    [displays-and-alerts-2-4-26-0393] page:24:line:5 | command
    [displays-and-alerts-2-4-26-0394] page:24:line:6 | TCAS
    [displays-and-alerts-2-4-26-0395] page:24:line:7 | TVSI/RVSI
    [displays-and-alerts-2-4-26-0396] page:24:line:8 | What would you do if
    [displays-and-alerts-2-4-26-0397] page:24:line:9 | you only saw this display
    [displays-and-alerts-2-4-26-0398] page:24:line:10 | of vertical speed?
    [displays-and-alerts-2-4-26-0399] page:24:line:11 | 2/4/26
    [displays-and-alerts-2-4-26-0400] page:24:line:12 | ENP-0112
    [displays-and-alerts-2-4-26-0401] page:24:line:13 | 24
    [displays-and-alerts-2-4-26-0402] page:25:line:1 | IMPLEMENTATION AND
    [displays-and-alerts-2-4-26-0403] page:25:line:2 | TESTING
    [displays-and-alerts-2-4-26-0404] page:25:line:3 | 2/4/26
    [displays-and-alerts-2-4-26-0405] page:25:line:4 | ENP-0112
    [displays-and-alerts-2-4-26-0406] page:25:line:5 | 25
    [displays-and-alerts-2-4-26-0407] page:26:line:1 | GENERIC IMPLEMENTATION ISSUES
    [displays-and-alerts-2-4-26-0408] page:26:line:2 | • Design
    [displays-and-alerts-2-4-26-0409] page:26:line:3 | • Display size
    [displays-and-alerts-2-4-26-0410] page:26:line:4 | • Presentation of information
    [displays-and-alerts-2-4-26-0411] page:26:line:5 | • Interaction (controls)
    [displays-and-alerts-2-4-26-0412] page:26:line:6 | • Location relative to operator
    [displays-and-alerts-2-4-26-0413] page:26:line:7 | • Evaluation
    [displays-and-alerts-2-4-26-0414] page:26:line:8 | • By regulators, end users, purchasers…
    [displays-and-alerts-2-4-26-0415] page:26:line:9 | • Standardization
    [displays-and-alerts-2-4-26-0416] page:26:line:10 | 2/4/26
    [displays-and-alerts-2-4-26-0417] page:26:line:11 | ENP-0112
    [displays-and-alerts-2-4-26-0418] page:26:line:12 | 26
    [displays-and-alerts-2-4-26-0419] page:27:line:1 | DISPLAY EVALUATION TOPICS AND GUIDANCE
    [displays-and-alerts-2-4-26-0420] page:27:line:2 | • General issues
    [displays-and-alerts-2-4-26-0421] page:27:line:3 | • Legibility of fonts and labels, training, ease of
    [displays-and-alerts-2-4-26-0422] page:27:line:4 | use, “intuitiveness”
    [displays-and-alerts-2-4-26-0423] page:27:line:5 | • Hardware
    [displays-and-alerts-2-4-26-0424] page:27:line:6 | • Screen size
    [displays-and-alerts-2-4-26-0425] page:27:line:7 | • Physical controls and interaction
    [displays-and-alerts-2-4-26-0426] page:27:line:8 | • Screen technology (e.g., CRT, LCD, HUD)
    [displays-and-alerts-2-4-26-0427] page:27:line:9 | • Resolution, refresh rate, viewing angle,
    [displays-and-alerts-2-4-26-0428] page:27:line:10 | brightness (daylight readability)
    [displays-and-alerts-2-4-26-0429] page:27:line:11 | • Input devices, e.g., touch screen, cursor
    [displays-and-alerts-2-4-26-0430] page:27:line:12 | control device
    [displays-and-alerts-2-4-26-0431] page:27:line:13 | • Software
    [displays-and-alerts-2-4-26-0432] page:27:line:14 | • Software controls (e.g., buttons, icons)
    [displays-and-alerts-2-4-26-0433] page:27:line:15 | • Color
    [displays-and-alerts-2-4-26-0434] page:27:line:16 | • Multi-tasking and interaction
    [displays-and-alerts-2-4-26-0435] page:27:line:17 | • Data entry, configuration
    [displays-and-alerts-2-4-26-0436] page:27:line:18 | • Information time lag (e.g., traffic)
    [displays-and-alerts-2-4-26-0437] page:27:line:19 | • Design standards and guidance
    [displays-and-alerts-2-4-26-0438] page:27:line:20 | • RTCA DO-160 Environmental Testing
    [displays-and-alerts-2-4-26-0439] page:27:line:21 | • RTCA DO 178 Software assurance
    [displays-and-alerts-2-4-26-0440] page:27:line:22 | • Many others
    [displays-and-alerts-2-4-26-0441] page:27:line:23 | 2/4/26
    [displays-and-alerts-2-4-26-0442] page:27:line:24 | ENP-0112
    [displays-and-alerts-2-4-26-0443] page:27:line:25 | 27
    [displays-and-alerts-2-4-26-0444] page:28:line:1 | TECHNIQUES FOR EVALUATING DISPLAYS
    [displays-and-alerts-2-4-26-0445] page:28:line:2 | • Type of evaluation varies by stage of development, purpose, time/resource limitations
    [displays-and-alerts-2-4-26-0446] page:28:line:3 | • Bench test
    [displays-and-alerts-2-4-26-0447] page:28:line:4 | •
    [displays-and-alerts-2-4-26-0448] page:28:line:5 | Symbols, interaction, intuitiveness
    [displays-and-alerts-2-4-26-0449] page:28:line:6 | •
    [displays-and-alerts-2-4-26-0450] page:28:line:7 | User-interface Assessment checklist
    [displays-and-alerts-2-4-26-0451] page:28:line:8 | •
    [displays-and-alerts-2-4-26-0452] page:28:line:9 | Operational evaluation
    [displays-and-alerts-2-4-26-0453] page:28:line:10 | •
    [displays-and-alerts-2-4-26-0454] page:28:line:11 | Simulators
    [displays-and-alerts-2-4-26-0455] page:28:line:12 | •
    [displays-and-alerts-2-4-26-0456] page:28:line:13 | In-Flight evaluations
    [displays-and-alerts-2-4-26-0457] page:28:line:14 | • Inspection
    [displays-and-alerts-2-4-26-0458] page:28:line:15 | •
    [displays-and-alerts-2-4-26-0459] page:28:line:16 | Checklist, observation…
    [displays-and-alerts-2-4-26-0460] page:28:line:17 | • Who is doing the evaluation?
    [displays-and-alerts-2-4-26-0461] page:28:line:18 | • Engineer
    [displays-and-alerts-2-4-26-0462] page:28:line:19 | • Non-expert
    [displays-and-alerts-2-4-26-0463] page:28:line:20 | • (Representative) End user
    [displays-and-alerts-2-4-26-0464] page:28:line:21 | • Regulator
    [displays-and-alerts-2-4-26-0465] page:28:line:22 | 2/4/26
    [displays-and-alerts-2-4-26-0466] page:28:line:23 | ENP-0112
    [displays-and-alerts-2-4-26-0467] page:28:line:24 | 28
    [displays-and-alerts-2-4-26-0468] page:29:line:1 | A MENTAL MODEL OF RESEARCH ON FLIGHT DECK
    [displays-and-alerts-2-4-26-0469] page:29:line:2 | SYSTEMS
    [displays-and-alerts-2-4-26-0470] page:29:line:3 | 29
    [displays-and-alerts-2-4-26-0471] page:29:line:4 | Researcher
    [displays-and-alerts-2-4-26-0472] page:29:line:5 | Pilo
    [displays-and-alerts-2-4-26-0473] page:29:line:6 | t
    [displays-and-alerts-2-4-26-0474] page:29:line:7 | ?
    [displays-and-alerts-2-4-26-0475] page:29:line:8 | Research
    [displays-and-alerts-2-4-26-0476] page:29:line:9 | 2/4/26
    [displays-and-alerts-2-4-26-0477] page:29:line:10 | ENP-0112
    [displays-and-alerts-2-4-26-0478] page:29:line:11 | Chandra, D.C. (2023). Creating usable research for the design and evaluation of flight deck systems and human interfaces. In
    [displays-and-alerts-2-4-26-0479] page:29:line:12 | Proceedings of the 23rd International Symposium on Aviation Psychology, May 31 to June 3, Rochester, New York.
    [displays-and-alerts-2-4-26-0480] page:29:line:13 | https://rosap.ntl.bts.gov/view/dot/84141
    [displays-and-alerts-2-4-26-0481] page:30:line:1 | A MENTAL MODEL OF RESEARCH ON FLIGHT DECK
    [displays-and-alerts-2-4-26-0482] page:30:line:2 | SYSTEMS
    [displays-and-alerts-2-4-26-0483] page:30:line:3 | 30
    [displays-and-alerts-2-4-26-0484] page:30:line:4 | Researcher
    [displays-and-alerts-2-4-26-0485] page:30:line:5 | Design
    [displays-and-alerts-2-4-26-0486] page:30:line:6 | Build
    [displays-and-alerts-2-4-26-0487] page:30:line:7 | Test
    [displays-and-alerts-2-4-26-0488] page:30:line:8 | Evaluate
    [displays-and-alerts-2-4-26-0489] page:30:line:9 | Market (Sell/Buy)
    [displays-and-alerts-2-4-26-0490] page:30:line:10 | Install
    [displays-and-alerts-2-4-26-0491] page:30:line:11 | Train
    [displays-and-alerts-2-4-26-0492] page:30:line:12 | Operate
    [displays-and-alerts-2-4-26-0493] page:30:line:13 | Maintain
    [displays-and-alerts-2-4-26-0494] page:30:line:14 | Pilo
    [displays-and-alerts-2-4-26-0495] page:30:line:15 | t
    [displays-and-alerts-2-4-26-0496] page:30:line:16 | Research
    [displays-and-alerts-2-4-26-0497] page:30:line:17 | 2/4/26
    [displays-and-alerts-2-4-26-0498] page:30:line:18 | ENP-0112
    [displays-and-alerts-2-4-26-0499] page:30:line:19 | Chandra, D.C. (2023). Creating usable research for the design and evaluation of flight deck systems and human interfaces. In
    [displays-and-alerts-2-4-26-0500] page:30:line:20 | Proceedings of the 23rd International Symposium on Aviation Psychology, May 31 to June 3, Rochester, New York.
    [displays-and-alerts-2-4-26-0501] page:30:line:21 | https://rosap.ntl.bts.gov/view/dot/84141
    [displays-and-alerts-2-4-26-0502] page:31:line:1 | A MENTAL MODEL OF RESEARCH ON FLIGHT DECK
    [displays-and-alerts-2-4-26-0503] page:31:line:2 | SYSTEMS
    [displays-and-alerts-2-4-26-0504] page:31:line:3 | 31
    [displays-and-alerts-2-4-26-0505] page:31:line:4 | Guidance Documents &
    [displays-and-alerts-2-4-26-0506] page:31:line:5 | Evaluation Procedures
    [displays-and-alerts-2-4-26-0507] page:31:line:6 | Practitioners in
    [displays-and-alerts-2-4-26-0508] page:31:line:7 | Government and Industry
    [displays-and-alerts-2-4-26-0509] page:31:line:8 | Researcher
    [displays-and-alerts-2-4-26-0510] page:31:line:9 | Design
    [displays-and-alerts-2-4-26-0511] page:31:line:10 | Build
    [displays-and-alerts-2-4-26-0512] page:31:line:11 | Test
    [displays-and-alerts-2-4-26-0513] page:31:line:12 | Evaluate
    [displays-and-alerts-2-4-26-0514] page:31:line:13 | Market (Sell/Buy)
    [displays-and-alerts-2-4-26-0515] page:31:line:14 | Install
    [displays-and-alerts-2-4-26-0516] page:31:line:15 | Train
    [displays-and-alerts-2-4-26-0517] page:31:line:16 | Operate
    [displays-and-alerts-2-4-26-0518] page:31:line:17 | Maintain
    [displays-and-alerts-2-4-26-0519] page:31:line:18 | Pilo
    [displays-and-alerts-2-4-26-0520] page:31:line:19 | t
    [displays-and-alerts-2-4-26-0521] page:31:line:20 | Research
    [displays-and-alerts-2-4-26-0522] page:31:line:21 | 2/4/26
    [displays-and-alerts-2-4-26-0523] page:31:line:22 | ENP-0112
    [displays-and-alerts-2-4-26-0524] page:31:line:23 | Chandra, D.C. (2023). Creating usable research for the design and evaluation of flight deck systems and human interfaces. In
    [displays-and-alerts-2-4-26-0525] page:31:line:24 | Proceedings of the 23rd International Symposium on Aviation Psychology, May 31 to June 3, Rochester, New York.
    [displays-and-alerts-2-4-26-0526] page:31:line:25 | https://rosap.ntl.bts.gov/view/dot/84141
    [displays-and-alerts-2-4-26-0527] page:32:line:1 | A MENTAL MODEL OF RESEARCH ON FLIGHT DECK
    [displays-and-alerts-2-4-26-0528] page:32:line:2 | SYSTEMS
    [displays-and-alerts-2-4-26-0529] page:32:line:3 | 32
    [displays-and-alerts-2-4-26-0530] page:32:line:4 | Guidance Documents &
    [displays-and-alerts-2-4-26-0531] page:32:line:5 | Evaluation Procedures
    [displays-and-alerts-2-4-26-0532] page:32:line:6 | Practitioners in
    [displays-and-alerts-2-4-26-0533] page:32:line:7 | Government and Industry
    [displays-and-alerts-2-4-26-0534] page:32:line:8 | Researcher
    [displays-and-alerts-2-4-26-0535] page:32:line:9 | Design
    [displays-and-alerts-2-4-26-0536] page:32:line:10 | Build
    [displays-and-alerts-2-4-26-0537] page:32:line:11 | Test
    [displays-and-alerts-2-4-26-0538] page:32:line:12 | Evaluate
    [displays-and-alerts-2-4-26-0539] page:32:line:13 | Market (Sell/Buy)
    [displays-and-alerts-2-4-26-0540] page:32:line:14 | Install
    [displays-and-alerts-2-4-26-0541] page:32:line:15 | Train
    [displays-and-alerts-2-4-26-0542] page:32:line:16 | Operate
    [displays-and-alerts-2-4-26-0543] page:32:line:17 | Maintain
    [displays-and-alerts-2-4-26-0544] page:32:line:18 | Pilo
    [displays-and-alerts-2-4-26-0545] page:32:line:19 | t
    [displays-and-alerts-2-4-26-0546] page:32:line:20 | Research
    [displays-and-alerts-2-4-26-0547] page:32:line:21 | 2/4/26
    [displays-and-alerts-2-4-26-0548] page:32:line:22 | ENP-0112
    [displays-and-alerts-2-4-26-0549] page:32:line:23 | Chandra, D.C. (2023). Creating usable research for the design and evaluation of flight deck systems and human interfaces. In
    [displays-and-alerts-2-4-26-0550] page:32:line:24 | Proceedings of the 23rd International Symposium on Aviation Psychology, May 31 to June 3, Rochester, New York.
    [displays-and-alerts-2-4-26-0551] page:32:line:25 | https://rosap.ntl.bts.gov/view/dot/84141
    [displays-and-alerts-2-4-26-0552] page:33:line:1 | REFERENCES
    [displays-and-alerts-2-4-26-0553] page:33:line:2 | https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs400/afs410/airborne-
    [displays-and-alerts-2-4-26-0554] page:33:line:3 | collision-avoidance-system-acas
    [displays-and-alerts-2-4-26-0555] page:33:line:4 | Federal Aviation Administration. (2011). Introduction to TCAS II Version 7.1 (Report No. HQ-111358). tcas ii v7.1 intro
    [displays-and-alerts-2-4-26-0556] page:33:line:5 | booklet.pdf (faa.gov)
    [displays-and-alerts-2-4-26-0557] page:33:line:6 | Chandra, D.C. (2023). Creating usable research for the design and evaluation of flight deck systems and human
    [displays-and-alerts-2-4-26-0558] page:33:line:7 | interfaces. In Proceedings of the 23rd International Symposium on Aviation Psychology, May 31 to June 3, Rochester,
    [displays-and-alerts-2-4-26-0559] page:33:line:8 | New York. https://rosap.ntl.bts.gov/view/dot/84141
    [displays-and-alerts-2-4-26-0560] page:33:line:9 | Proctor, R. W., Van Zandt, T., (2018). Human factors in simple and complex system. Third edition, Boca Raton, FL, CRC
    [displays-and-alerts-2-4-26-0561] page:33:line:10 | Press.
    [displays-and-alerts-2-4-26-0562] page:33:line:11 | https://en.wikipedia.org/wiki/Traffic_collision_avoidance_system
    [displays-and-alerts-2-4-26-0563] page:33:line:12 | Yeh, M., Swider, C., Donovan, C., Hiltunen, D., Chase, S. & Jo, Y. (2024) Human Factors Considerations in the Design and
    [displays-and-alerts-2-4-26-0564] page:33:line:13 | Evaluation of Flight Deck Displays and Controls, Version 3.0. DOT/FAA/AM-24/23.
    [displays-and-alerts-2-4-26-0565] page:33:line:14 | https://rosap.ntl.bts.gov/view/dot/87936
    [displays-and-alerts-2-4-26-0566] page:33:line:15 | 2/4/26
    [displays-and-alerts-2-4-26-0567] page:33:line:16 | ENP-0112
    [displays-and-alerts-2-4-26-0568] page:33:line:17 | 33
    [displays-and-alerts-2-4-26-0569] page:34:line:1 | EXTRAS
    [displays-and-alerts-2-4-26-0570] page:34:line:2 | 2/4/26
    [displays-and-alerts-2-4-26-0571] page:34:line:3 | ENP-0112
    [displays-and-alerts-2-4-26-0572] page:34:line:4 | 34
    [displays-and-alerts-2-4-26-0573] page:35:line:1 | MORE ABOUT VISUAL DISPLAY
    [displays-and-alerts-2-4-26-0574] page:35:line:2 | DESIGN
    [displays-and-alerts-2-4-26-0575] page:35:line:3 | 2/4/26
    [displays-and-alerts-2-4-26-0576] page:35:line:4 | ENP-0112
    [displays-and-alerts-2-4-26-0577] page:35:line:5 | 35
    [displays-and-alerts-2-4-26-0578] page:36:line:1 | PRINCIPLE OF INFORMATION NEED
    [displays-and-alerts-2-4-26-0579] page:36:line:2 | 36
    [displays-and-alerts-2-4-26-0580] page:36:line:3 | Present only the information necessary to carry out the required
    [displays-and-alerts-2-4-26-0581] page:36:line:4 | tasks.
    [displays-and-alerts-2-4-26-0582] page:36:line:5 | (Need to know what are the required tasks)
    [displays-and-alerts-2-4-26-0583] page:36:line:6 | 767-424 flight deck
    [displays-and-alerts-2-4-26-0584] page:36:line:7 | 2/4/26
    [displays-and-alerts-2-4-26-0585] page:36:line:8 | ENP-0112
    [displays-and-alerts-2-4-26-0586] page:37:line:1 | PROXIMITY COMPATIBILITY
    [displays-and-alerts-2-4-26-0587] page:37:line:2 | 37
    [displays-and-alerts-2-4-26-0588] page:37:line:3 | Effort required for task is decreased when displays that are related, compared,
    [displays-and-alerts-2-4-26-0589] page:37:line:4 | or integrated to perform a task are closer together
    [displays-and-alerts-2-4-26-0590] page:37:line:5 | Lateral control
    [displays-and-alerts-2-4-26-0591] page:37:line:6 | Vertical control
    [displays-and-alerts-2-4-26-0592] page:37:line:7 | 2/4/26
    [displays-and-alerts-2-4-26-0593] page:37:line:8 | ENP-0112
    [displays-and-alerts-2-4-26-0594] page:38:line:1 | REDUNDANCY
    [displays-and-alerts-2-4-26-0595] page:38:line:2 | 38
    [displays-and-alerts-2-4-26-0596] page:38:line:3 | Repeat the message in alternate forms
    [displays-and-alerts-2-4-26-0597] page:38:line:4 | commons.wikimeida.org
    [displays-and-alerts-2-4-26-0598] page:38:line:5 | 2/4/26
    [displays-and-alerts-2-4-26-0599] page:38:line:6 | ENP-0112
    [displays-and-alerts-2-4-26-0600] page:39:line:1 | PRINCIPLE OF PICTORIAL REALISM
    [displays-and-alerts-2-4-26-0601] page:39:line:2 | 39
    [displays-and-alerts-2-4-26-0602] page:39:line:3 | A display should match the human’s internal model of the variable
    [displays-and-alerts-2-4-26-0603] page:39:line:4 | that it represents
    [displays-and-alerts-2-4-26-0604] page:39:line:5 | 2/4/26
    [displays-and-alerts-2-4-26-0605] page:39:line:6 | ENP-0112
    [displays-and-alerts-2-4-26-0606] page:40:line:1 | PRINCIPLE OF THE MOVING PART
    [displays-and-alerts-2-4-26-0607] page:40:line:2 | 40
    [displays-and-alerts-2-4-26-0608] page:40:line:3 | The moving element on a
    [displays-and-alerts-2-4-26-0609] page:40:line:4 | display should correspond
    [displays-and-alerts-2-4-26-0610] page:40:line:5 | with the element that moves
    [displays-and-alerts-2-4-26-0611] page:40:line:6 | in the user’s mental model
    [displays-and-alerts-2-4-26-0612] page:40:line:7 | 2/4/26
    [displays-and-alerts-2-4-26-0613] page:40:line:8 | ENP-0112
    [displays-and-alerts-2-4-26-0614] page:41:line:1 | PREDICTIVE AIDS
    [displays-and-alerts-2-4-26-0615] page:41:line:2 | 41
    [displays-and-alerts-2-4-26-0616] page:41:line:3 | Helps operators to see the future state of
    [displays-and-alerts-2-4-26-0617] page:41:line:4 | the system
    [displays-and-alerts-2-4-26-0618] page:41:line:5 | 2/4/26
    [displays-and-alerts-2-4-26-0619] page:41:line:6 | ENP-0112
    ```
