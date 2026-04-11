# URRA 方法

URRA 这一页讲的不是一种表格格式，而是一条完整风险链：任务步骤、使用错误、危险情境、伤害后果和控制措施怎样被写到同一个结构里。

!!! note "本页主问题"
    Use-Related Risk Analysis 怎样把任务、
    错误、
    危害和控制措施串成一条可追踪、
    可验证、
    可回看的链？

## 本章重点

- URRA 的中心作用，
  是把 use step、
  use error、
  hazardous situation、
  harm 和 control 连成一条链。
- 书写顺序必须是任务与场景在前，
  错误与后果在后，
  控制措施最后。
- 写得好的 URRA 足够具体，
  能直接支持验证活动。
- 写得差的 URRA 往往只有笼统用语，
  既看不出真正风险，
  也支撑不了后续测试。

## 先记住方法定位

!!! tip "先记住这个方法的定位"
    先记住这个方法的定位：
    URRA 不是“把风险写进表里”，
    而是把风险路径写清楚到足以支持设计和验证。

## 这个方法解决什么问题

URRA 解决的是“风险信息分散在不同文件里”的问题。
它把使用流程、
潜在错误、
危险情境、
伤害和控制汇总到同一条链上，
让团队能看见风险是怎样一步步长出来的。

## 输入与输出是什么

URRA 的输入通常来自：

- task analysis
- user and use-environment assumptions
- 已知 use error 或投诉信息
- 设计特征、标签、IFU 和培训方案

输出则是一组可追踪条目，
能回答：

- 哪一步可能出错
- 错后会进入什么危险情境
- 最终可能带来什么 harm
- 现有控制够不够

## 操作步骤怎么走

写 URRA 时，
顺序非常关键：

1. 先从任务和 use scenario 出发。
2. 明确写出具体 use error，而不是“使用不当”这种大词。
3. 继续把错误推到 hazardous situation 和 harm。
4. 最后再看现有 control 是否足够，以及还要不要加设计或验证措施。

!!! note "一句话结论"
    如果控制措施写在前面，
    URRA 很容易变成设计辩护；
    如果风险链写在前面，
    URRA 才像真正的风险分析。

!!! warning "最容易做错的地方"
    最常见的问题有两个：
    把 error 写得太泛，
    比如“误用”；
    以及把 harm 写得太近，
    只写“剂量错误”却没有继续写到患者伤害。

!!! example "worked example：一条 URRA 记录应该怎样写"
    例如某一步是“设定剂量”。
    好的 URRA 不会只写“可能出错”，
    而会写成：
    用户把 1.0 mL 读成 10 mL，
    导致危险情境是过量给药，
    潜在 harm 是低血糖或更严重不良反应；
    然后才回头讨论剂量窗口、
    视觉区分、
    确认步骤和验证测试。

## 和前后方法是什么关系

task analysis 给 URRA 提供任务骨架；
medical-device pages 会进一步把这套逻辑放到监管语境里；
EpiPen workbook 页则展示一条 URRA 记录实际长什么样。

## 为什么一条 URRA 行本身就应该读得出完整风险故事

写 URRA 时，
一个常见问题是每一列都填了字，
但合起来仍然看不出真正发生了什么。
强的 URRA 行应该让人顺着一条线读下去：
谁在什么场景下做哪一步、
会错成什么、
错后会进入什么 hazardous situation、
最终伤害是什么、
现在靠什么拦。

如果一行读完后团队还看不见这条完整路径，
通常说明场景、
动作、
错误或 harm 写得还不够具体。
URRA 的质量，
不是表有多满，
而是链是否完整。

## 为什么 URRA 最怕写成抽象大词

URRA 一旦写成“误用”“使用不当”“可能受伤”这种大词，
后面几乎所有栏位都会一起失焦。
因为团队看不出到底是哪一步、
哪种错误、
哪条 harm path，
也就不知道控制到底该落在哪个设计点上。

所以一条好的 URRA 记录通常都有很强的具体性：
具体场景、
具体动作、
具体误判、
具体后果、
具体控制。
写到这个程度时，
验证场景和风险沟通才会自然长出来。

## 为什么 URRA 最终一定要回到验证

这门课不把 URRA 当成档案管理，
而把它当成设计与验证的接口。
原因很简单：
如果一条风险链已经被写出来，
团队就必须能回答“我们准备怎样证明控制真的有效”。

这意味着 URRA 不是写完就结束，
而是还要继续推动：

- 哪些 risk control 需要在原型或正式产品里被体现
- 哪些关键任务需要在 validation 中被专门观察
- 哪些情境需要通过 representative user 和 representative use condition 去复现

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/10-write-urra/slide-02-image2.png" alt="这张图要看懂的是：URRA 不是单向填表，它会在风险不可接受或引入新风险时反复回到控制和验证，直到链条站得住。" loading="lazy">
  <figcaption>这张图要看懂的是：URRA 不是单向填表，它会在风险不可接受或引入新风险时反复回到控制和验证，直到链条站得住。</figcaption>
</figure>

!!! warning "另一个常见失误"
    有些团队会把 URRA 写得看起来很完整，
    但没有任何一条真正能转进验证。
    这通常说明条目还不够具体，
    或者控制写得太空泛。

## 为什么 URRA 不应该只从团队脑子里“想风险”

课件里专门把 KPA、
MAUDE、
usability testing、
expert review 和 previous device data 拉进来，
是在强调一个很实用的判断：
强的 URRA 不是凭空想象出来的，
而是由多种证据源一起逼出来的。

这点很重要，
因为只靠会议室头脑风暴，
团队往往更容易想到显眼的大风险，
却漏掉那些历史上反复出现、
但平时不太起眼的 use error。
真正成熟的 URRA 会让 task analysis 提供任务骨架，
再让历史数据、
测试发现和专家判断把那条骨架补成可验证的风险链。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/10-write-urra/slide-05-image3.png" alt="这张图要看懂的是：URRA 的证据来源并不只来自当前任务流，像 MAUDE 这类历史数据库会把团队没想到的 use error 重新拉回分析里。" loading="lazy">
  <figcaption>这张图要看懂的是：URRA 的证据来源并不只来自当前任务流，像 MAUDE 这类历史数据库会把团队没想到的 use error 重新拉回分析里。</figcaption>
</figure>

## 为什么 URRA 的书写顺序本身就在保护分析质量

课程一直强调“先任务、
再错误、
再后果、
最后控制”，
这不只是书写习惯，
而是在防止分析变成设计辩护。
只要团队一开始就急着写 control，
很容易出现先有答案、
再回头找风险来配的情况。

正确顺序的价值在于：
它逼团队先把 scenario、
action、
error direction 和 harm path 写具体。
只有前半条链站住了，
后面的 mitigation 才不是拍脑袋。
URRA 的很多质量问题，
其实都不是不会写表，
而是把顺序写反了。

## 怎样判断一条 URRA 已经能顺利交给 validation 团队

一条 URRA 记录真正成熟时，
validation 团队应该能直接据此构造观察场景，
而不用再回头猜“这里到底想测什么”。
换句话说，
条目至少要清楚到能回答：

- 代表性用户是谁
- 代表性任务和环境是什么
- 哪一步必须被重点观察
- 如果 control 失效，哪种 use error 会出现
- 成功与失败的判据是什么

如果这些信息还读不出来，
就说明这条 URRA 还停在分析半成品阶段。
真正强的 URRA，
本来就是写给 design、
validation 和 regulatory 同时能继续用的。

!!! example "案例：为什么“用户注射错误浓度”这句话还不够拿去做 validation"
    如果条目只写“用户注射错误浓度”，
    validation 团队仍然不知道该复现什么。
    更成熟的写法会继续补清：
    是在确认产品规格时选错成人/儿童剂型，
    还是包装区分不明显，
    还是紧急状态下没有看到标签颜色提示。
    只有写到这个程度，
    团队才知道应当布置什么场景、
    观察什么行为，
    以及控制是否真的有效。

## 本章总结

!!! tip "复习时重点记这几条"
    - URRA 的核心是写清风险链，
      而不是填表本身。
    - 输入来自任务流、
      用户场景和已知问题。
    - 写作顺序必须是任务/错误/后果/控制，
      而不是倒着来。
    - 越具体的 URRA，
      越能支持后续验证。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `ENP111 Use-related Risks`
- 关联源文件数: 1
- 文本单元数: 52
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `10 Write URRA.pptx` | `pptx` | 52 | 3 | [open](../assets/source_files/ENP111/10 Write URRA.pptx) |

## 相关主题

- [任务分析](task_analysis.md)
- [医疗器械中的 URRA](medical_device_urra.md)
- [EpiPen URRA 工作簿](epipen_workbook.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "10 Write URRA.pptx | 52 text units"
    下载原件: [10 Write URRA.pptx](../assets/source_files/ENP111/10 Write URRA.pptx)
    映射页面: `urra_methods`
    
    ```text
    [10-write-urra-0001] slide:1:p:1 | Sami Durrani PhD and Eric Bergman PhD
    [10-write-urra-0002] slide:1:p:2 | Developing the URRA
    [10-write-urra-0003] slide:2:p:1 | Review: Use-related risk analysis process (as defined by FDA)
    [10-write-urra-0004] slide:2:p:2 | Ongoing activity
    [10-write-urra-0005] slide:3:p:1 | 3
    [10-write-urra-0006] slide:3:p:2 | Identifying potential use errors?
    [10-write-urra-0007] slide:4:p:1 | 4
    [10-write-urra-0008] slide:4:p:2 | Typical sources of data (not a comprehensive list)
    [10-write-urra-0009] slide:4:p:3 | Previous version of device
    [10-write-urra-0010] slide:4:p:4 | Similar devices, included competitors
    [10-write-urra-0011] slide:4:p:5 | Devices with a similar UI, user interactions, or uses
    [10-write-urra-0012] slide:4:p:6 | Post market surveillance data
    [10-write-urra-0013] slide:4:p:7 | In-house from your company’s post market surveillance group (typically part of a Quality department)
    [10-write-urra-0014] slide:4:p:8 | Customer support department
    [10-write-urra-0015] slide:4:p:9 | On-line databases, for example MAUDE
    [10-write-urra-0016] slide:4:p:10 | Known problems analysis (KPA)
    [10-write-urra-0017] slide:5:p:1 | 5
    [10-write-urra-0018] slide:5:p:2 | MAUDE
    [10-write-urra-0019] slide:5:p:3 | See separate video on conducting a known problems analysis
    [10-write-urra-0020] slide:6:p:1 | 6
    [10-write-urra-0021] slide:6:p:2 | Previously we conducted a Task Analysis…
    [10-write-urra-0022] slide:6:p:3 | …Assume now we performed a KPA, Expert Reviews, and Usability Testing and identified the following additional use errors:
    [10-write-urra-0023] slide:6:p:4 | User does not dispose of AI in sharps container
    [10-write-urra-0024] slide:6:p:5 | User injects with expired drug
    [10-write-urra-0025] slide:6:p:6 | User injects with damaged AI
    [10-write-urra-0026] slide:6:p:7 | User injects with leaking AI
    [10-write-urra-0027] slide:6:p:8 | Now, lets work through our EpiPen example to develop the URRA
    [10-write-urra-0028] slide:6:p:9 | Recall our EpiPen Auto-Injector (AI) Example
    [10-write-urra-0029] slide:7:p:1 | 7
    [10-write-urra-0030] slide:7:p:2 | A URRA needs to contain the following:
    [10-write-urra-0031] slide:7:p:3 | Reference number
    [10-write-urra-0032] slide:7:p:4 | Task description
    [10-write-urra-0033] slide:7:p:5 | Potential use errors
    [10-write-urra-0034] slide:7:p:6 | Potential hazards and harms
    [10-write-urra-0035] slide:7:p:7 | Severity of harm
    [10-write-urra-0036] slide:7:p:8 | Critical task (yes or no)
    [10-write-urra-0037] slide:7:p:9 | Risk mitigations
    [10-write-urra-0038] slide:7:p:10 | Reference to validation of risk mitigation effectiveness
    [10-write-urra-0039] slide:7:p:11 | URRA document decomposed
    [10-write-urra-0040] notes:1:p:1 | Quick introductions
    [10-write-urra-0041] notes:2:p:1 | As a reminder the HF process in medical device development is important because medical devices, whether they are simple tools or complex machines, are often used in critical situations where a mistake can have serious consequences. A design that does not consider the user's needs, abilities, and limitations can lead to errors and patient harm.
    [10-write-urra-0042] notes:2:p:2 | The overall process in begins by understanding who the users are, their needs, and the environments in which they will use the device, then we conduct an iterative use-related risk analysis. We then design the device, making sure to incorporate human factors principles into the design process to make the UI resistant to use errors (and to also increase usability and user satisfaction). As we design the device we update our use-related risk analysis to match the device design and uncover if any new use related risks have been introduced and we conduct testing along the way to ensure that the designs that we develop are effective in controlling risk.
    [10-write-urra-0043] notes:2:p:3 | In other lectures conducting a task analysis to identify potential use errors, as well as how to write good use errors.
    [10-write-urra-0044] notes:3:p:1 | But its also important to note that there are many other sources of use errors that we need to look to conduct a comprehensive use related risk analysis. In this lecture we will work though an example of going through from a task analysis to a URRA document.
    [10-write-urra-0045] notes:4:p:1 | A KPA helps identify how people have made mistakes or otherwise struggled using products similar to the one being developed. This can be your own products, a previous version of it, or similar ones you have in the market, or it could be products that competitors might make. Over even a product with just a similar user interfaces, user interactions and/or uses. Online data-sources, such as Manufacturer and User Facility Device Experience (MAUDE). Are a great source of data. Manufacturer and User Facility Device Experience (MAUDE) database represents reports of adverse events involving medical devices.
    [10-write-urra-0046] notes:4:p:2 | The searchable database contains the last 10 years of medical device report (MDR) data.
    [10-write-urra-0047] notes:6:p:1 | Important notes to mention:
    [10-write-urra-0048] notes:6:p:2 | -The URRA and your task analysis will go through several iterations.
    [10-write-urra-0049] notes:6:p:3 | -In practical sense, its easiest to use you task analysis as your draft URRA, add in all your other UEs there and when it comes time to make your final URRA draft, simplify for it for the agency.
    [10-write-urra-0050] notes:6:p:4 | When is it time to make your final URRA draft: once we have completed the process, our design is locked, we develop a final draft of our URRA. This final draft becomes the basis of the validation study. I say final draft because if we’ve done our jobs correctly, we shouldn’t expect to see any new use errors and our results should validate that all of our implemented are effective. But that’s not always the case, so you can’t really finalize your URRA until after you have had a successful validation study.
    [10-write-urra-0051] notes:7:p:1 | As a reminder, here is the structure of a URRA, as requested by the FDA>
    [10-write-urra-0052] notes:7:p:2 | When is it time to make your final URRA draft: once we have completed the process, our design is locked, we develop a final draft of our URRA. This final draft becomes the basis of the validation study. I say final draft because if we’ve done our jobs correctly, we shouldn’t expect to see any new use errors and our results should validate that all of our implemented are effective. But that’s not always the case, so you can’t really finalize your URRA until after you have had a successful validation study.
    ```
