# 课程导论与学习地图

本章重点是先把整门课读成一张地图：这不是一门背术语的课，而是一门用系统视角解释事故、分析失效并提出改进的课。

!!! note "本页主问题"
    这门课到底在训练什么能力？
    为什么后面的方法页、
    应用页和案例页，
    其实都在回答同一组问题？

## 本章重点

- 这门课研究的不是“谁犯错了”，
  而是“人在系统里怎样和任务、
  工具、
  环境、
  组织一起作用”。
- 课程主线是：
  先建立共同语言，
  再学习分析方法，
  再进入行业场景，
  最后回到事故、
  责任和伦理。
- 后面的很多页虽然主题不同，
  但都在追问同一件事：
  失败是怎样产生的，
  为什么没被拦住，
  以及应该改哪里。
- 这门课训练的不只是解释事故，
  更包括提出可操作的 mitigation。
- 如果导论页没读明白，
  后面的名词会很多，
  但彼此很难连成线。

## 先记住一句话

!!! tip "复习时先记住这句话"
    把整门课先记成一句话：
    看到事故时，
    不要停在“谁错了”，
    而要继续追问系统怎样让错误出现、
    扩大，
    或者没被拦住。

## 这门课为什么带有 `forensic` 的味道

这里的 `forensic` 不是让课程变成法庭流程课，
而是强调一种分析姿态：
面对伤害、
险情或事故，
不能只停在表面结果，
而要把事件拆成一连串可追问的问题。

这套追问通常包括：

- 发生了什么
- 为什么会发生
- 原本哪几层防线应该拦住它
- 为什么这些防线没有起作用
- 后续 mitigation 应该改设计、改流程、改组织，还是一起改

所以这门课虽然会接触案例、
责任和事故调查，
但核心仍然是工程分析，
而不是法律术语本身。

## 课程主线是怎样串起来的

这门课最容易被误读成“每周换一个主题”。
其实课件已经把四个组件摆出来了：
`issues / theory`、
`analysis methods and frameworks`、
`mitigations`、
`cases`。

把这四块连起来，
课程结构就很清楚：

1. 基础页先告诉你该怎样看人和系统。
2. 方法页把这种视角变成可操作的分析步骤。
3. 应用页让你看到同一套逻辑在航空、自动化和医疗器械里怎样落地。
4. 案例页再把前面的框架拉回真实事故和伦理判断。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/course-intro-1-14-26/page-07.png" alt="这张图要看懂的是：课程的四个元素不是彼此分开的模块，而是理论、方法、改进和案例互相支撑的结构。" loading="lazy">
  <figcaption>这张图要看懂的是：课程的四个元素不是彼此分开的模块，而是理论、方法、改进和案例互相支撑的结构。</figcaption>
</figure>

!!! note "一句话结论"
    整门课不是按行业拆散来讲，
    而是把“理论 - 方法 - 改进 - 案例”反复套在不同场景上。

## 学到最后到底要会什么

从导论课件列出的 goals 看，
这门课最终训练的是四种能力：

- 能把 incident 的 causes 用标准 HFE 语言讲清楚
- 能把系统中的 hazard 和 use-related risk 解释得简洁、准确
- 能提出 corrective actions 和 countermeasures，而不是只会复述问题
- 能判断设计 tradeoff 对 safety 和 performance 的影响

换句话说，
这门课不是只训练“会看案例”，
而是训练你把案例讲清楚、
拆清楚，
并给出有逻辑的改进方向。

!!! example "案例：同一个药物错误，整门课会怎样把它拆开"
    一次给药错误，
    导论页先要求你别急着下结论。
    基础页会让你区分 human error 和 system conditions；
    方法页会要求你写任务步骤、
    失败点和 risk controls；
    应用页会让你看设备、
    标签、
    工作环境和流程；
    案例页再把责任、
    组织和伦理层面加回来。
    也就是说，
    整门课不是反复看“一个故事”，
    而是反复训练你用不同层级把同一个问题拆开。

## 这门课应该怎么学才不会散

比较有效的读法不是按周次被动跟着跑，
而是始终带着同一条问题链去看每一页：

- 这页讲的是哪一种失败或限制
- 这页提供了什么分析工具
- 这页最后落到哪些 mitigation
- 这和前面的基础概念怎么连起来

如果一直沿着这条线读，
`Swiss Cheese` 不会只是一个比喻，
`URRA` 不会只是一个模板，
案例页也不会只剩故事。

!!! warning "最容易走偏的读法"
    不要把课程读成“每页一个新名词”。
    如果只收集名词、
    不记主线，
    后面的事故分析就会变成概念拼盘。

## 本章总结

!!! tip "复习时重点记这几条"
    - 这门课带有 forensic 的味道，
      是因为它要求你对事故保持连续追问，
      而不是停在结论。
    - 课程骨架始终是：
      基础语言、
      分析方法、
      应用场景、
      案例与伦理。
    - 最终训练的能力包括解释 causes、
      提出 mitigation、
      评估 tradeoff。
    - 读整站时要始终带着同一条问题链：
      失败怎么出现、
      怎么扩散、
      怎么拦截、
      怎么改进。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `HFE基础`
- 关联源文件数: 1
- 文本单元数: 388
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Course intro 1-14-26.pdf` | `pdf` | 388 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Course intro 1-14-26.pdf) |

## 相关主题

- [人因工程导论](human_factors_intro.md)
- [错误分析与调查流程](../HFE_Risk_Methods/error_analysis_methods.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "Course intro 1-14-26.pdf | 388 text units"
    下载原件: [Course intro 1-14-26.pdf](../assets/source_files/Lectures_Spring_2026/Course intro 1-14-26.pdf)
    映射页面: `course_overview`
    
    ```text
    [course-intro-1-14-26-0001] page:1:line:1 | Engineering Forensics
    [course-intro-1-14-26-0002] page:1:line:2 | ENP-0112
    [course-intro-1-14-26-0003] page:1:line:3 | January 14, 2026
    [course-intro-1-14-26-0004] page:1:line:4 | Divya Chandra, Andy Liu, Parisa Arastu
    [course-intro-1-14-26-0005] page:1:line:5 | 1
    [course-intro-1-14-26-0006] page:2:line:1 | Agenda
    [course-intro-1-14-26-0007] page:2:line:2 | • Introductions
    [course-intro-1-14-26-0008] page:2:line:3 | • Course content
    [course-intro-1-14-26-0009] page:2:line:4 | • Syllabus
    [course-intro-1-14-26-0010] page:2:line:5 | • Generative AI discussion
    [course-intro-1-14-26-0011] page:2:line:6 | • Extras
    [course-intro-1-14-26-0012] page:2:line:7 | • Websites, context, mitigations
    [course-intro-1-14-26-0013] page:2:line:8 | 2
    [course-intro-1-14-26-0014] page:3:line:1 | Introductions
    [course-intro-1-14-26-0015] page:3:line:2 | Lecturers
    [course-intro-1-14-26-0016] page:3:line:3 | Divya Chandra, Ph.D. {d.chandra@tufts.edu}
    [course-intro-1-14-26-0017] page:3:line:4 | Andrew M. Liu, Ph.D. {aliu17@tufts.edu}
    [course-intro-1-14-26-0018] page:3:line:5 | Teaching Assistant
    [course-intro-1-14-26-0019] page:3:line:6 | Parisa Arastu, Arts & Sciences 26
    [course-intro-1-14-26-0020] page:3:line:7 | {Parisa.Arastu@tufts.edu}
    [course-intro-1-14-26-0021] page:3:line:8 | 3
    [course-intro-1-14-26-0022] page:4:line:1 | Class Members
    [course-intro-1-14-26-0023] page:4:line:2 | • Nate Brophy
    [course-intro-1-14-26-0024] page:4:line:3 | • En Chen (G; graduate student)
    [course-intro-1-14-26-0025] page:4:line:4 | • Jack Chung
    [course-intro-1-14-26-0026] page:4:line:5 | • Ainsley Cui (G)
    [course-intro-1-14-26-0027] page:4:line:6 | • Annica Grote
    [course-intro-1-14-26-0028] page:4:line:7 | • Amanda Hasenauer (G)
    [course-intro-1-14-26-0029] page:4:line:8 | • Austin Jobson
    [course-intro-1-14-26-0030] page:4:line:9 | • Quian Li (G)
    [course-intro-1-14-26-0031] page:4:line:10 | • Rianna Liu
    [course-intro-1-14-26-0032] page:4:line:11 | • Sachita Mane (G)
    [course-intro-1-14-26-0033] page:4:line:12 | • Joey Marmo
    [course-intro-1-14-26-0034] page:4:line:13 | • Varun Nair (G)
    [course-intro-1-14-26-0035] page:4:line:14 | • Lance Nielson-Konzen (G)
    [course-intro-1-14-26-0036] page:4:line:15 | • Elsa Ostenson
    [course-intro-1-14-26-0037] page:4:line:16 | • Matt Peryea (G)
    [course-intro-1-14-26-0038] page:4:line:17 | • Sahir Surani (G)
    [course-intro-1-14-26-0039] page:4:line:18 | • Deelia Wang (G)
    [course-intro-1-14-26-0040] page:4:line:19 | • Rachel Woo
    [course-intro-1-14-26-0041] page:4:line:20 | • Lucy Zimmerman
    [course-intro-1-14-26-0042] page:4:line:21 | • Adin Handler? (not in SIS)
    [course-intro-1-14-26-0043] page:4:line:22 | 4
    [course-intro-1-14-26-0044] page:5:line:1 | Engineering Forensics?
    [course-intro-1-14-26-0045] page:5:line:2 | • Common usage…..Forensic science applies scientific methods and processes to
    [course-intro-1-14-26-0046] page:5:line:3 | solve crimes or identify liability
    [course-intro-1-14-26-0047] page:5:line:4 | • Tort lawyers, expert witnesses and forensic science
    [course-intro-1-14-26-0048] page:5:line:5 | • Structural failures, engineering design deficiencies
    [course-intro-1-14-26-0049] page:5:line:6 | • Ex. CSI television crime drama
    [course-intro-1-14-26-0050] page:5:line:7 | • Forensic human factors
    [course-intro-1-14-26-0051] page:5:line:8 | • Analyses of injury cases
    [course-intro-1-14-26-0052] page:5:line:9 | • Expert witness in legal cases
    [course-intro-1-14-26-0053] page:5:line:10 | • Person-product or person-environment interaction –severe injury or death
    [course-intro-1-14-26-0054] page:5:line:11 | • This course uses “forensic” in an analytic manner
    [course-intro-1-14-26-0055] page:5:line:12 | • Learn from failures
    [course-intro-1-14-26-0056] page:5:line:13 | • Determine what went wrong and why
    [course-intro-1-14-26-0057] page:5:line:14 | • Identify mitigations
    [course-intro-1-14-26-0058] page:5:line:15 | 5
    [course-intro-1-14-26-0059] page:6:line:1 | Course Goals
    [course-intro-1-14-26-0060] page:6:line:2 | • Develop skills and knowledge needed to strategically investigate and analyze human-centered
    [course-intro-1-14-26-0061] page:6:line:3 | safety issues that can lead to unexpected adverse consequences in operational environments.
    [course-intro-1-14-26-0062] page:6:line:4 | • Practice explaining the causes of incidents concisely and clearly, in both oral and written formats,
    [course-intro-1-14-26-0063] page:6:line:5 | using accurate and standard human factors terms.
    [course-intro-1-14-26-0064] page:6:line:6 | • Practice explaining recommended counter measures and corrective actions, in both oral and
    [course-intro-1-14-26-0065] page:6:line:7 | written formats.
    [course-intro-1-14-26-0066] page:6:line:8 | • Evaluate tradeoffs in system design that can affect safety.
    [course-intro-1-14-26-0067] page:6:line:9 | • Participate in class discussions.
    [course-intro-1-14-26-0068] page:6:line:10 | • Give examples of human factors issues that affect safety.
    [course-intro-1-14-26-0069] page:6:line:11 | 6
    [course-intro-1-14-26-0070] page:7:line:1 | Issues/ sidebars
    [course-intro-1-14-26-0071] page:7:line:2 | Issues/theory ("Sidebars”)
    [course-intro-1-14-26-0072] page:7:line:3 | Analysis Methods and
    [course-intro-1-14-26-0073] page:7:line:4 | Frameworks
    [course-intro-1-14-26-0074] page:7:line:5 | Mitigations
    [course-intro-1-14-26-0075] page:7:line:6 | Cases
    [course-intro-1-14-26-0076] page:7:line:7 | Course Elements
    [course-intro-1-14-26-0077] page:7:line:8 | 7
    [course-intro-1-14-26-0078] page:8:line:1 | Example “Sidebars”
    [course-intro-1-14-26-0079] page:8:line:2 | After the talks, instructors will dive into issues and theories during the sidebar lectures. These will
    [course-intro-1-14-26-0080] page:8:line:3 | cover theory and context, or other related information.
    [course-intro-1-14-26-0081] page:8:line:4 | Example topics:
    [course-intro-1-14-26-0082] page:8:line:5 | • Attention and Monitoring
    [course-intro-1-14-26-0083] page:8:line:6 | • Automation, trust
    [course-intro-1-14-26-0084] page:8:line:7 | • Decision making, complacency
    [course-intro-1-14-26-0085] page:8:line:8 | • Distraction/inattention
    [course-intro-1-14-26-0086] page:8:line:9 | • Fatigue
    [course-intro-1-14-26-0087] page:8:line:10 | • Usability
    [course-intro-1-14-26-0088] page:8:line:11 | • Warnings/alarms
    [course-intro-1-14-26-0089] page:8:line:12 | • Organizational culture
    [course-intro-1-14-26-0090] page:8:line:13 | 8
    [course-intro-1-14-26-0091] page:9:line:1 | Course Structure
    [course-intro-1-14-26-0092] page:9:line:2 | • Typical class begins with the student presentations, then sidebar
    [course-intro-1-14-26-0093] page:9:line:3 | • There will guest lectures, without student talks.
    [course-intro-1-14-26-0094] page:9:line:4 | • Grading – emphasizes original work
    [course-intro-1-14-26-0095] page:9:line:5 | • Reading responses (15%)
    [course-intro-1-14-26-0096] page:9:line:6 | • Weekly, submitted through Rumi plug-in on Canvas
    [course-intro-1-14-26-0097] page:9:line:7 | • Presentations (45%)
    [course-intro-1-14-26-0098] page:9:line:8 | • Two individual oral presentations, focused on specific aspects of a real case
    [course-intro-1-14-26-0099] page:9:line:9 | • Rubric considers content, delivery, and handling questions
    [course-intro-1-14-26-0100] page:9:line:10 | • Exams (40%)
    [course-intro-1-14-26-0101] page:9:line:11 | • Written mid-term and final exams, in-class and on-line components
    [course-intro-1-14-26-0102] page:9:line:12 | • Ungraded but important to developing knowledge and skills
    [course-intro-1-14-26-0103] page:9:line:13 | • Attendance/Participation in discussions and Q&A for student presentations
    [course-intro-1-14-26-0104] page:9:line:14 | 9
    [course-intro-1-14-26-0105] page:10:line:1 | Submission Due Dates
    [course-intro-1-14-26-0106] page:10:line:2 | • Reading responses usually due Wed midnight (confirm in Canvas)
    [course-intro-1-14-26-0107] page:10:line:3 | • Readings will be available throughout the term, even if unread.
    [course-intro-1-14-26-0108] page:10:line:4 | • No late responses will be accepted for credit.
    [course-intro-1-14-26-0109] page:10:line:5 | • Presentation schedule will be developed by TA and posted to Canvas home page.
    [course-intro-1-14-26-0110] page:10:line:6 | • Topics for each talk will be finalized at least 2 weeks before the presentation date.
    [course-intro-1-14-26-0111] page:10:line:7 | • Midterm exam on March 9 during class
    [course-intro-1-14-26-0112] page:10:line:8 | • Final exam – May 1, 12-2p (based on Block Schedule E/E+)
    [course-intro-1-14-26-0113] page:10:line:9 | • Tell the TA and instructors as early as possible if you have any problems with the exam or
    [course-intro-1-14-26-0114] page:10:line:10 | presentation dates, or if you will be out on known dates.
    [course-intro-1-14-26-0115] page:10:line:11 | • We will also schedule a trip to the USDOT Volpe Center human factors laboratory.
    [course-intro-1-14-26-0116] page:10:line:12 | • Attendance is optional but recommended if possible.
    [course-intro-1-14-26-0117] page:10:line:13 | 10
    [course-intro-1-14-26-0118] page:11:line:1 | Reading Tips
    [course-intro-1-14-26-0119] page:11:line:2 | • GenAI summaries can be helpful, but can also be generic and
    [course-intro-1-14-26-0120] page:11:line:3 | uninteresting
    [course-intro-1-14-26-0121] page:11:line:4 | • Read the Abstracts and Executive Summaries in full
    [course-intro-1-14-26-0122] page:11:line:5 | • Skim the table of contents. What looks interesting to you?
    [course-intro-1-14-26-0123] page:11:line:6 | ➢Goal is to become familiar with the subject, not necessarily an expert
    [course-intro-1-14-26-0124] page:11:line:7 | on it.
    [course-intro-1-14-26-0125] page:11:line:8 | 11
    [course-intro-1-14-26-0126] page:12:line:1 | Reading Responses
    [course-intro-1-14-26-0127] page:12:line:2 | • Approximately 20 readings over the term
    [course-intro-1-14-26-0128] page:12:line:3 | • Responses should be short and in personal writing
    [course-intro-1-14-26-0129] page:12:line:4 | style, not formal.
    [course-intro-1-14-26-0130] page:12:line:5 | • Each reading response counts for 1% of grade up to
    [course-intro-1-14-26-0131] page:12:line:6 | 15%
    [course-intro-1-14-26-0132] page:12:line:7 | • Up to 5% extra credit for additional reading responses
    [course-intro-1-14-26-0133] page:12:line:8 | • Rumi plug-in
    [course-intro-1-14-26-0134] page:12:line:9 | • Simple word processor, configured to record all entries
    [course-intro-1-14-26-0135] page:12:line:10 | including use of copy/paste and AI tools to encourage
    [course-intro-1-14-26-0136] page:12:line:11 | original work.
    [course-intro-1-14-26-0137] page:12:line:12 | • Practice using Rumi for reading responses; we may use it
    [course-intro-1-14-26-0138] page:12:line:13 | for exams as well.
    [course-intro-1-14-26-0139] page:12:line:14 | • https://sites.tufts.edu/ets/tools/rumi/
    [course-intro-1-14-26-0140] page:12:line:15 | 12
    [course-intro-1-14-26-0141] page:12:line:16 | Rumi is a writing tool which makes the writing
    [course-intro-1-14-26-0142] page:12:line:17 | process visible. Integrated into Canvas, it deters AI
    [course-intro-1-14-26-0143] page:12:line:18 | misuse by encouraging students to write in their
    [course-intro-1-14-26-0144] page:12:line:19 | own voice and do their own thinking. It will try and
    [course-intro-1-14-26-0145] page:12:line:20 | detect when students are not creating their own
    [course-intro-1-14-26-0146] page:12:line:21 | writing, and collects evidence you can use to
    [course-intro-1-14-26-0147] page:12:line:22 | determine if the student is following your AI use
    [course-intro-1-14-26-0148] page:12:line:23 | policy.
    [course-intro-1-14-26-0149] page:12:line:24 | Rumi does this by:
    [course-intro-1-14-26-0150] page:12:line:25 | 1.Recording the students writing so that you can
    [course-intro-1-14-26-0151] page:12:line:26 | evaluate their process. When students create their
    [course-intro-1-14-26-0152] page:12:line:27 | own work, it looks very different from when they
    [course-intro-1-14-26-0153] page:12:line:28 | transcribe from AI or elsewhere.
    [course-intro-1-14-26-0154] page:12:line:29 | 2.Preventing students from copying and pasting
    [course-intro-1-14-26-0155] page:12:line:30 | from other sources without attribution. Whenever a
    [course-intro-1-14-26-0156] page:12:line:31 | student pastes text into the assignment, Rumi asks
    [course-intro-1-14-26-0157] page:12:line:32 | for a justification of where the text came from. You
    [course-intro-1-14-26-0158] page:12:line:33 | can evaluate if this is a quote, draft, or chunk of text
    [course-intro-1-14-26-0159] page:12:line:34 | taken from AI.
    [course-intro-1-14-26-0160] page:12:line:35 | 3.Evaluating the student’s writing behavior. Rumi
    [course-intro-1-14-26-0161] page:12:line:36 | has a number of metrics that help you see, at a high
    [course-intro-1-14-26-0162] page:12:line:37 | level, which submissions need to be evaluated for
    [course-intro-1-14-26-0163] page:12:line:38 | unethical AI use.
    [course-intro-1-14-26-0164] page:12:line:39 | 4.Allowing students to use AI tools that you have
    [course-intro-1-14-26-0165] page:12:line:40 | approved and to records those interactions for you
    [course-intro-1-14-26-0166] page:12:line:41 | to review.
    [course-intro-1-14-26-0167] page:12:line:42 | Rumi
    [course-intro-1-14-26-0168] page:13:line:1 | Analysis of a Case-High Level
    [course-intro-1-14-26-0169] page:13:line:2 | • Describe the facts  of the situation
    [course-intro-1-14-26-0170] page:13:line:3 | • What are the causes?
    [course-intro-1-14-26-0171] page:13:line:4 | • What should be done?
    [course-intro-1-14-26-0172] page:13:line:5 | 13
    [course-intro-1-14-26-0173] page:14:line:1 | Warning
    [course-intro-1-14-26-0174] page:14:line:2 | • Situations and videos can be alarming
    [course-intro-1-14-26-0175] page:14:line:3 | • Focus on series of missteps leading to the incident, not the human
    [course-intro-1-14-26-0176] page:14:line:4 | pain and suffering
    [course-intro-1-14-26-0177] page:14:line:5 | • Try to humanize, but not personalize
    [course-intro-1-14-26-0178] page:14:line:6 | 14
    [course-intro-1-14-26-0179] page:15:line:1 | How to begin…
    [course-intro-1-14-26-0180] page:15:line:2 | • The best sources are the original accident investigation reports.
    [course-intro-1-14-26-0181] page:15:line:3 | • US National Transportation Safety Board (NTSB) has well written, plain
    [course-intro-1-14-26-0182] page:15:line:4 | language reports.
    [course-intro-1-14-26-0183] page:15:line:5 | • Read the Executive summaries for an overview, then decide which sections to
    [course-intro-1-14-26-0184] page:15:line:6 | dive into further for your particular area of interest (“lens” that you are
    [course-intro-1-14-26-0185] page:15:line:7 | applying)
    [course-intro-1-14-26-0186] page:15:line:8 | • Higher level summaries are often available online, for example:
    [course-intro-1-14-26-0187] page:15:line:9 | • https://lessonslearned.faa.gov/general.cfm
    [course-intro-1-14-26-0188] page:15:line:10 | • Wikipedia
    [course-intro-1-14-26-0189] page:15:line:11 | Note: GenAI tools can be used to search and summarize references (if confirmed that they exist),
    [course-intro-1-14-26-0190] page:15:line:12 | but the presentation content should not be created with AI.
    [course-intro-1-14-26-0191] page:15:line:13 | 15
    [course-intro-1-14-26-0192] page:16:line:1 | Presenting the Case – General Example
    [course-intro-1-14-26-0193] page:16:line:2 | 1.
    [course-intro-1-14-26-0194] page:16:line:3 | What happened? (Video clips or simulations can help.)
    [course-intro-1-14-26-0195] page:16:line:4 | 2.
    [course-intro-1-14-26-0196] page:16:line:5 | Provide historical perspective on the operation in which the accident occurred
    [course-intro-1-14-26-0197] page:16:line:6 | 3.
    [course-intro-1-14-26-0198] page:16:line:7 | Timeline: Present a graphic timeline showing when various factors occurred.
    [course-intro-1-14-26-0199] page:16:line:8 | 4.
    [course-intro-1-14-26-0200] page:16:line:9 | Describe the human/operator behavior in the situation
    [course-intro-1-14-26-0201] page:16:line:10 | 5.
    [course-intro-1-14-26-0202] page:16:line:11 | What were the consequences (injuries, fatalities, economic damage)?
    [course-intro-1-14-26-0203] page:16:line:12 | 6.
    [course-intro-1-14-26-0204] page:16:line:13 | Characterize the culture of the organization
    [course-intro-1-14-26-0205] page:16:line:14 | 7.
    [course-intro-1-14-26-0206] page:16:line:15 | Explain the primary and contributing factors
    [course-intro-1-14-26-0207] page:16:line:16 | 8.
    [course-intro-1-14-26-0208] page:16:line:17 | Measures that should have been taken to avoid the accident or mitigate its
    [course-intro-1-14-26-0209] page:16:line:18 | consequences?
    [course-intro-1-14-26-0210] page:16:line:19 | 9.
    [course-intro-1-14-26-0211] page:16:line:20 | Policy recommendations: Develop and present recommendations for changes
    [course-intro-1-14-26-0212] page:16:line:21 | to reduce likelihood of recurrence
    [course-intro-1-14-26-0213] page:16:line:22 | 16
    [course-intro-1-14-26-0214] page:17:line:1 | Presentation Rubric
    [course-intro-1-14-26-0215] page:17:line:2 | • Overall Grade, Max 22.5 points for each (45 points total)
    [course-intro-1-14-26-0216] page:17:line:3 | • Content
    [course-intro-1-14-26-0217] page:17:line:4 | • Problem Statement (4 points)
    [course-intro-1-14-26-0218] page:17:line:5 | • Summary of case background and significance related to topic.
    [course-intro-1-14-26-0219] page:17:line:6 | • Demonstrated understanding of the context of the case.
    [course-intro-1-14-26-0220] page:17:line:7 | • Analysis and Discussion (4 points)
    [course-intro-1-14-26-0221] page:17:line:8 | • Analysis of situation, comparison to theory and/or previous cases, clear description and discussion
    [course-intro-1-14-26-0222] page:17:line:9 | of human-related issues.
    [course-intro-1-14-26-0223] page:17:line:10 | • Conclusions. (4 points)
    [course-intro-1-14-26-0224] page:17:line:11 | • Presentation of conclusions with important results highlighted.
    [course-intro-1-14-26-0225] page:17:line:12 | • Delivery
    [course-intro-1-14-26-0226] page:17:line:13 | • Interaction and Voice. Eye contact and engagement with audience. Appropriate voice
    [course-intro-1-14-26-0227] page:17:line:14 | volume, clarity, pace, and inflection. (4 points)
    [course-intro-1-14-26-0228] page:17:line:15 | • Questions/Answers (Q/A)
    [course-intro-1-14-26-0229] page:17:line:16 | • Ability to respond to questions. (6.5 points)
    [course-intro-1-14-26-0230] page:17:line:17 | 17
    [course-intro-1-14-26-0231] page:18:line:1 | Mid-term and Final Exam Formats
    [course-intro-1-14-26-0232] page:18:line:2 | • New format this year, trial.
    [course-intro-1-14-26-0233] page:18:line:3 | •
    [course-intro-1-14-26-0234] page:18:line:4 | In-person, during class for part of the exam. Also one online essay component for each exam.
    [course-intro-1-14-26-0235] page:18:line:5 | •
    [course-intro-1-14-26-0236] page:18:line:6 | May use Rumi plug-in to avoid hand-written responses.
    [course-intro-1-14-26-0237] page:18:line:7 | •
    [course-intro-1-14-26-0238] page:18:line:8 | May make adjustments for the final exam after the mid-term exam.
    [course-intro-1-14-26-0239] page:18:line:9 | • If you have a letter of accommodation (e.g., more time on exams), let us know ASAP so we can make
    [course-intro-1-14-26-0240] page:18:line:10 | arrangements
    [course-intro-1-14-26-0241] page:18:line:11 | • In-class exam components:
    [course-intro-1-14-26-0242] page:18:line:12 | 1.
    [course-intro-1-14-26-0243] page:18:line:13 | Prepare a reaction to new reading material.
    [course-intro-1-14-26-0244] page:18:line:14 | 2.
    [course-intro-1-14-26-0245] page:18:line:15 | Semi-prepared essay. We will give you a set of questions in advance. Will select one question from the set for the exam.
    [course-intro-1-14-26-0246] page:18:line:16 | •
    [course-intro-1-14-26-0247] page:18:line:17 | Can use GenAI to study and prepare
    [course-intro-1-14-26-0248] page:18:line:18 | •
    [course-intro-1-14-26-0249] page:18:line:19 | Suggested method is to outline a response for every question and then just write out the response during the exam
    [course-intro-1-14-26-0250] page:18:line:20 | time.
    [course-intro-1-14-26-0251] page:18:line:21 | •
    [course-intro-1-14-26-0252] page:18:line:22 | Length of response is less important than prioritization and analysis.
    [course-intro-1-14-26-0253] page:18:line:23 | •
    [course-intro-1-14-26-0254] page:18:line:24 | Add specific examples to support your points.
    [course-intro-1-14-26-0255] page:18:line:25 | • On-line component
    [course-intro-1-14-26-0256] page:18:line:26 | •
    [course-intro-1-14-26-0257] page:18:line:27 | Expect one short essay with a word-limit.
    [course-intro-1-14-26-0258] page:18:line:28 | •
    [course-intro-1-14-26-0259] page:18:line:29 | Should refer to reading materials.
    [course-intro-1-14-26-0260] page:18:line:30 | • Suggestions? Comments?
    [course-intro-1-14-26-0261] page:18:line:31 | 18
    [course-intro-1-14-26-0262] page:19:line:1 | Discussion of GenAI Responses
    [course-intro-1-14-26-0263] page:19:line:2 | • What is good?
    [course-intro-1-14-26-0264] page:19:line:3 | • What could be improved?
    [course-intro-1-14-26-0265] page:19:line:4 | • Is there anything false in the response?
    [course-intro-1-14-26-0266] page:19:line:5 | • Improving the prompts?
    [course-intro-1-14-26-0267] page:19:line:6 | • How can you “add value” to the AI response?
    [course-intro-1-14-26-0268] page:19:line:7 | ➢Questions/discussion about acceptable use of AI?
    [course-intro-1-14-26-0269] page:19:line:8 | 19
    [course-intro-1-14-26-0270] page:20:line:1 | Extras
    [course-intro-1-14-26-0271] page:20:line:2 | 20
    [course-intro-1-14-26-0272] page:21:line:1 | Transportation Sources on the Internet
    [course-intro-1-14-26-0273] page:21:line:2 | •
    [course-intro-1-14-26-0274] page:21:line:3 | https://www.standardsportal.org/usa_en/resources/sdo.aspx
    [course-intro-1-14-26-0275] page:21:line:4 | •
    [course-intro-1-14-26-0276] page:21:line:5 | https://www.nhtsa.gov/laws-regulations/fmvss
    [course-intro-1-14-26-0277] page:21:line:6 | •
    [course-intro-1-14-26-0278] page:21:line:7 | https://www.nhtsa.gov/technology-innovation/automated-vehicles-safety
    [course-intro-1-14-26-0279] page:21:line:8 | •
    [course-intro-1-14-26-0280] page:21:line:9 | https://www.faa.gov/regulations_policies/
    [course-intro-1-14-26-0281] page:21:line:10 | •
    [course-intro-1-14-26-0282] page:21:line:11 | https://www.fmcsa.dot.gov/regulations
    [course-intro-1-14-26-0283] page:21:line:12 | •
    [course-intro-1-14-26-0284] page:21:line:13 | https://www.fra.dot.gov/Page/P0020
    [course-intro-1-14-26-0285] page:21:line:14 | •
    [course-intro-1-14-26-0286] page:21:line:15 | https://www.fra.dot.gov/Page/P0010
    [course-intro-1-14-26-0287] page:21:line:16 | •
    [course-intro-1-14-26-0288] page:21:line:17 | https://www.fhwa.dot.gov/resources/
    [course-intro-1-14-26-0289] page:21:line:18 | •
    [course-intro-1-14-26-0290] page:21:line:19 | https://www.uscg.mil/Resources/Library/
    [course-intro-1-14-26-0291] page:21:line:20 | •
    [course-intro-1-14-26-0292] page:21:line:21 | https://apps.dtic.mil/dtic/tr/fulltext/u2/a281401.pdf (Mil Std 1472)
    [course-intro-1-14-26-0293] page:21:line:22 | •
    [course-intro-1-14-26-0294] page:21:line:23 | https://ntsb.gov/Pages/default.aspx
    [course-intro-1-14-26-0295] page:21:line:24 | •
    [course-intro-1-14-26-0296] page:21:line:25 | https://www.transportation.gov/
    [course-intro-1-14-26-0297] page:21:line:26 | •
    [course-intro-1-14-26-0298] page:21:line:27 | https://www.transit.dot.gov/
    [course-intro-1-14-26-0299] page:21:line:28 | •
    [course-intro-1-14-26-0300] page:21:line:29 | http://www.trb.org/Publications/Publications.aspx
    [course-intro-1-14-26-0301] page:21:line:30 | •
    [course-intro-1-14-26-0302] page:21:line:31 | https://trid.trb.org/
    [course-intro-1-14-26-0303] page:21:line:32 | •
    [course-intro-1-14-26-0304] page:21:line:33 | http://www.tsb.gc.ca/eng/
    [course-intro-1-14-26-0305] page:21:line:34 | •
    [course-intro-1-14-26-0306] page:21:line:35 | https://www.iihs.org/
    [course-intro-1-14-26-0307] page:21:line:36 | •
    [course-intro-1-14-26-0308] page:21:line:37 | https://lessonslearned.faa.gov/general.cfm
    [course-intro-1-14-26-0309] page:21:line:38 | •
    [course-intro-1-14-26-0310] page:21:line:39 | https://www.askthepilot.com/
    [course-intro-1-14-26-0311] page:21:line:40 | •
    [course-intro-1-14-26-0312] page:21:line:41 | http://www.volpe.dot.gov
    [course-intro-1-14-26-0313] page:21:line:42 | •
    [course-intro-1-14-26-0314] page:21:line:43 | http://zoox.com
    [course-intro-1-14-26-0315] page:21:line:44 | •
    [course-intro-1-14-26-0316] page:21:line:45 | https://visionzeronetwork.org/
    [course-intro-1-14-26-0317] page:21:line:46 | •
    [course-intro-1-14-26-0318] page:21:line:47 | http://www.umtri.umich.edu/
    [course-intro-1-14-26-0319] page:21:line:48 | •
    [course-intro-1-14-26-0320] page:21:line:49 | https://aaafoundation.org/
    [course-intro-1-14-26-0321] page:21:line:50 | •
    [course-intro-1-14-26-0322] page:21:line:51 | https://www.vtti.vt.edu/
    [course-intro-1-14-26-0323] page:21:line:52 | •
    [course-intro-1-14-26-0324] page:21:line:53 | http://enotrans.org
    [course-intro-1-14-26-0325] page:21:line:54 | •
    [course-intro-1-14-26-0326] page:21:line:55 | https://cars.stanford.edu/
    [course-intro-1-14-26-0327] page:21:line:56 | •
    [course-intro-1-14-26-0328] page:21:line:57 | https://trb.secure-
    [course-intro-1-14-26-0329] page:21:line:58 | platform.com/a/page/AutomatedRoadTransportationSymposium
    [course-intro-1-14-26-0330] page:21:line:59 | •
    [course-intro-1-14-26-0331] page:21:line:60 | https://www.csail.mit.edu/research/self-driving-vehicles
    [course-intro-1-14-26-0332] page:21:line:61 | •
    [course-intro-1-14-26-0333] page:21:line:62 | http://Autosafety.org
    [course-intro-1-14-26-0334] page:21:line:63 | •
    [course-intro-1-14-26-0335] page:21:line:64 | http://pavecampaign.org
    [course-intro-1-14-26-0336] page:21:line:65 | •
    [course-intro-1-14-26-0337] page:21:line:66 | http://driverless.mit.edu/
    [course-intro-1-14-26-0338] page:21:line:67 | •
    [course-intro-1-14-26-0339] page:21:line:68 | http://nsc.org
    [course-intro-1-14-26-0340] page:21:line:69 | •
    [course-intro-1-14-26-0341] page:21:line:70 | https://www-nrd.nhtsa.dot.gov/departments/esv/27th/
    [course-intro-1-14-26-0342] page:21:line:71 | •
    [course-intro-1-14-26-0343] page:21:line:72 | www.nfpa.org
    [course-intro-1-14-26-0344] page:21:line:73 | •
    [course-intro-1-14-26-0345] page:21:line:74 | https://www.nist.gov/
    [course-intro-1-14-26-0346] page:21:line:75 | •
    [course-intro-1-14-26-0347] page:21:line:76 | http://agelab.mit.edu/
    [course-intro-1-14-26-0348] page:21:line:77 | •
    [course-intro-1-14-26-0349] page:21:line:78 | https://www.nasa.gov/centers/hq/nsc
    [course-intro-1-14-26-0350] page:21:line:79 | •
    [course-intro-1-14-26-0351] page:21:line:80 | https://www.faasafety.gov
    [course-intro-1-14-26-0352] page:21:line:81 | •
    [course-intro-1-14-26-0353] page:21:line:82 | https://www.youtube.com/playlist?list=PL5vHkqHi51DT2Y54kjRtmjJ3Dgaj_Sv7V
    [course-intro-1-14-26-0354] page:21:line:83 | •
    [course-intro-1-14-26-0355] page:21:line:84 | https://www.towardzerodeaths.org/
    [course-intro-1-14-26-0356] page:21:line:85 | •
    [course-intro-1-14-26-0357] page:21:line:86 | https://www.skybrary.aero/
    [course-intro-1-14-26-0358] page:21:line:87 | •
    [course-intro-1-14-26-0359] page:21:line:88 | https://www.apta.com/
    [course-intro-1-14-26-0360] page:21:line:89 | 21
    [course-intro-1-14-26-0361] page:22:line:1 | Some context…
    [course-intro-1-14-26-0362] page:22:line:2 | Perhaps one of the more valuable results of reviewing a series of accident reports is
    [course-intro-1-14-26-0363] page:22:line:3 | an appreciation for the complex chain of events which often underlies an accident.
    [course-intro-1-14-26-0364] page:22:line:4 | This is particularly true of accidents involving human error and human factors in
    [course-intro-1-14-26-0365] page:22:line:5 | general. Often, the basic causes assigned to an accident are, in fact, symptoms, in
    [course-intro-1-14-26-0366] page:22:line:6 | contrast to root causes, a concept of considerable interest and importance. …
    [course-intro-1-14-26-0367] page:22:line:7 | Technical deficiencies, when discovered, can be corrected rather easily, but most of
    [course-intro-1-14-26-0368] page:22:line:8 | the repeat causes include human factors related deficiencies. These are more
    [course-intro-1-14-26-0369] page:22:line:9 | difficult to correct, because these repeat causes are not usually root causes. For
    [course-intro-1-14-26-0370] page:22:line:10 | example, one of the most common and serious repeat cause factors is flying in
    [course-intro-1-14-26-0371] page:22:line:11 | adverse weather conditions; it is quite obvious that this is not a root cause. A root
    [course-intro-1-14-26-0372] page:22:line:12 | cause has to answer the question “Why”? (Hopf-Weichel et al., 1979, p. 5-17)
    [course-intro-1-14-26-0373] page:22:line:13 | Hopf-Weichel, R., Lucaccini, L.F., Saleh, J., & Freedy, A. (1979). Aircraft Emergency Decisions: Cognitive and Situational
    [course-intro-1-14-26-0374] page:22:line:14 | Variables. Air Force Office of Scientific Research (AFOSR). Report No. AOFSR-TR-1175. https://doi.org/10.21236/ADA077413
    [course-intro-1-14-26-0375] page:22:line:15 | 22
    [course-intro-1-14-26-0376] page:23:line:1 | “Mitigations” - How to address human factors issues
    [course-intro-1-14-26-0377] page:23:line:2 | Individual
    [course-intro-1-14-26-0378] page:23:line:3 | • Selection and training (Knowledge, Skills, and Abilities)
    [course-intro-1-14-26-0379] page:23:line:4 | • Motivation, arousal (optimize attention)
    [course-intro-1-14-26-0380] page:23:line:5 | Organization
    [course-intro-1-14-26-0381] page:23:line:6 | • Policies and procedures (e.g., checklists)
    [course-intro-1-14-26-0382] page:23:line:7 | • Safety culture
    [course-intro-1-14-26-0383] page:23:line:8 | System Design
    [course-intro-1-14-26-0384] page:23:line:9 | • Controls (soft or hard), “Usability” (e.g., visibility of system state, interaction with data)
    [course-intro-1-14-26-0385] page:23:line:10 | • Automated systems? (take the operator out of the system)
    [course-intro-1-14-26-0386] page:23:line:11 | Operational Risk
    [course-intro-1-14-26-0387] page:23:line:12 | • Variation across each operation (e.g., across flights)
    [course-intro-1-14-26-0388] page:23:line:13 | • Work as imagined (theory) vs. work as done (reality)
    ```
