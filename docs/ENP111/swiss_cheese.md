# Swiss Cheese 模型

本章重点是把“事故为什么会发生”从单点失误，推进到多层防线如何一起失守。Swiss Cheese 模型最重要的价值，不是那个比喻本身，而是它把注意力重新拉回系统屏障和漏洞对齐。

!!! note "本页主问题"
    为什么高风险系统明明有很多防线，
    事故还是会发生？
    真正危险的到底是一层失效，
    还是多层屏障在同一时刻同时失守？

## 本章重点

- Swiss Cheese 模型把事故看成多层防线被穿透，
  而不是最后一个人突然犯了大错。
- 每一层防线都可能同时具有保护作用和漏洞，
  所以“有屏障”不等于“屏障可靠”。
- 真正危险的不是某一个洞存在，
  而是多个洞在时间和条件上对齐。
- 这套模型的价值，
  是把 blame 转回 barrier design、
  latent conditions 和 system resilience。
- 它很好用，
  但不能被当成完整终点，
  还要结合动态变化和更深层根因分析。

## 先记住一句话

!!! tip "复习时先记住这句话"
    记这页时先抓一句话：
    事故通常不是因为最后一个人太差，
    而是因为多层本来应该拦截问题的防线，
    在同一时刻都没有起作用。

## Swiss Cheese 模型到底在解释什么

这套模型真正解释的是：
复杂系统里的 harm path 往往不是“一步到位”形成的，
而是一路穿过屏障、
程序、
检查、
人和组织控制，
最后才落到结果层。

一旦接受这个前提，
事故就不再像一个孤立爆点，
而像一条原本应该被多次拦住的问题链。
也正因为如此，
模型的关注点天然不是“谁最后按错了”，
而是“为什么前面那么多层都没有拦住”。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/05-swiss-cheese-model/page-06.png" alt="这张图要看懂的是：事故不是绕过一层防线，而是沿着多层漏洞被连续放行。" loading="lazy">
  <figcaption>这张图要看懂的是：事故不是绕过一层防线，而是沿着多层漏洞被连续放行。</figcaption>
</figure>

## 防线为什么会一边保护、一边带着漏洞

这页最重要的现实感在这里：
防线从来不是绝对防线。

- 有些漏洞是长期潜伏的，例如设计弱点、资源不足、流程不现实、组织容忍或错误激励。
- 有些漏洞是当下触发的，例如疲劳、分心、沟通断裂、时间压力、天气和工作负荷。

真正危险的时候，
不是某一个洞单独存在，
而是长期潜伏条件和短时触发恰好叠在一起，
让一条原本不该贯通的路径被打通。

!!! note "这一节最重要的结论"
    系统防线不能只问“有没有”，
    而要问“在真实运行条件下还能不能挡得住”。

!!! warning "最容易误读的地方"
    不要把模型读成“只要多加几层防线就一定更安全”。
    如果新增层级本身很弱、
    互相冲突，
    或者和真实工作脱节，
    层数增加并不等于韧性增加。

## 这套模型为什么这么常用

Swiss Cheese 模型之所以流行，
不只是因为图好记，
而是因为它把复杂风险快速讲清楚了：

- 它让人一眼看到安全不是靠单一屏障，而是靠 layered defense。
- 它能把 risk reduction 讲成很具体的问题：加一层、补一层、缩小洞、减少对齐机会。
- 它适用于航空、核电、医疗等多种高风险系统，因为这些系统都依赖多层拦截。

所以这套模型非常适合做第一层讲解，
也非常适合在跨专业团队里建立共同语言。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/05-swiss-cheese-model/page-07.png" alt="这张图要看懂的是：每一层措施都不完美，但多层叠加仍然能明显降低风险路径被打通的概率。" loading="lazy">
  <figcaption>这张图要看懂的是：每一层措施都不完美，但多层叠加仍然能明显降低风险路径被打通的概率。</figcaption>
</figure>

!!! example "案例：为什么 COVID 图示能把模型一下子讲明白"
    口罩、
    社交距离、
    清洁消毒、
    洗手都不是完美屏障，
    但它们叠在一起时会显著降低 harm path 被打通的机会。
    这个例子好用，
    是因为它把“每层都有洞，
    但多层一起仍然有意义”直观地画出来了。

## 这套模型也有什么局限

课件没有把 Swiss Cheese 当成完美答案，
而是专门列了 criticism。
这个提醒很重要：

- 模型容易让人误以为各层屏障彼此独立、系统基本静态
- 它强调 barriers，却可能让人忽略“洞为什么会不断长出来”
- 如果只停在图示层面，分析会显得很 generic，不够贴近真实工作

这也是后来会出现 `Hot Cheese Model` 这类更新的原因：
真实系统是动态变化的，
新增 mitigation 甚至可能自己再引入新风险。

!!! note "一句话结论"
    Swiss Cheese 很适合当起点，
    但不能代替动态系统分析和更深层的 causal analysis。

!!! warning "另一个常见陷阱"
    不要把 Swiss Cheese 画成图以后就以为分析结束了。
    图只是帮助你看到层和洞，
    真正困难的是解释这些洞为什么会持续存在、
    怎样被组织条件放大。

## 这套框架怎么真正拿来分析事故

把这页真正用起来时，
可以按一条很实用的分析顺序走：

1. 先找 harm vector，也就是最后伤害是怎样形成的。
2. 再往回找原本应该拦截它的屏障有哪些。
3. 对每一层继续追问：它是不存在、失效了，还是看似存在但在真实条件下无效。
4. 最后区分哪些是 latent conditions，哪些是 active failures，并把 mitigation 对应回具体层级。

这样做的结果是，
事故分析就不会只剩一个“最后责任人”，
而会变成一张系统漏洞地图。

!!! example "案例：一条事故路径是怎样穿透多层防线的"
    想象一台医疗设备在夜班里被错误设定剂量。
    最后那一下输入错误只是 `sharp end`。
    更上游可能已经同时存在：
    界面字段易混、
    标签不清、
    双人核对流于形式、
    工作负荷过高、
    培训把重点放错。
    单看最后一步，
    很像“某个人输错了”；
    从 Swiss Cheese 看，
    真正的问题是多层防线一起失守。

!!! example "案例：为什么 Deepwater Horizon 和 Challenger 都适合用这套框架读"
    这两个案例都不是“一个零件坏了”这么简单。
    Deepwater Horizon 里既有数据误读、
    设备失效，
    也有时间和预算压力；
    Challenger 里既有材料和测试问题，
    也有 schedule pressure 和 oversight / culture 问题。
    Swiss Cheese 的作用，
    就是让这些看似分散的因素能被放回同一条穿透路径里。

## 本章总结

!!! tip "复习时重点记这几条"
    - Swiss Cheese 模型把事故解释成多层防线的连续穿透。
    - 真正危险的是 latent conditions 和 active triggers 在时间上重合。
    - 这套模型很适合建立共同语言和第一层事故解释。
    - 它的局限在于容易静态化、
      图像化，
      因此还需要更深层根因分析补上。
    - 真正用它时，
      要把 harm vector、
      barriers、
      holes 和 mitigation 一层一层对应起来。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `ENP111`
- 关联源文件数: 1
- 文本单元数: 145
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `05 Swiss Cheese Model.pdf` | `pdf` | 145 | 3 | [open](../assets/source_files/ENP111/05 Swiss Cheese Model.pdf) |

## 相关主题

- [人为失误框架](human_error_frameworks.md)
- [Operational Risk](../ENP112/operational_risk.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "05 Swiss Cheese Model.pdf | 145 text units"
    下载原件: [05 Swiss Cheese Model.pdf](../assets/source_files/ENP111/05 Swiss Cheese Model.pdf)
    映射页面: `swiss_cheese`
    
    ```text
    [05-swiss-cheese-model-0001] page:1:line:1 | Rachel Morgan, MS
    [05-swiss-cheese-model-0002] page:1:line:2 | Swiss Cheese Model
    [05-swiss-cheese-model-0003] page:2:line:1 | 2
    [05-swiss-cheese-model-0004] page:2:line:2 | Introduction
    [05-swiss-cheese-model-0005] page:2:line:3 | Rachel Morgan
    [05-swiss-cheese-model-0006] page:2:line:4 | Product Owner, Connected Care
    [05-swiss-cheese-model-0007] page:2:line:5 | Lilly Diabetes and Obesity
    [05-swiss-cheese-model-0008] page:2:line:6 | Eli Lilly and Company
    [05-swiss-cheese-model-0009] page:2:line:7 | 
    [05-swiss-cheese-model-0010] page:2:line:8 | BS in Biomedical Engineering
    [05-swiss-cheese-model-0011] page:2:line:9 | 
    [05-swiss-cheese-model-0012] page:2:line:10 | MS in Biomedical Engineering
    [05-swiss-cheese-model-0013] page:2:line:11 | 
    [05-swiss-cheese-model-0014] page:2:line:12 | MS in Systems Engineering (focus in Human Factors)
    [05-swiss-cheese-model-0015] page:2:line:13 | 
    [05-swiss-cheese-model-0016] page:2:line:14 | 10+ years in medical devices, 4+ years in human factors
    [05-swiss-cheese-model-0017] page:3:line:1 | 3
    [05-swiss-cheese-model-0018] page:3:line:2 | Swiss Cheese Model
    [05-swiss-cheese-model-0019] page:3:line:3 | Background
    [05-swiss-cheese-model-0020] page:3:line:4 | Benefits / Criticisms
    [05-swiss-cheese-model-0021] page:3:line:5 | Updates: Hot Cheese Model
    [05-swiss-cheese-model-0022] page:3:line:6 | Real Disasters
    [05-swiss-cheese-model-0023] page:3:line:7 | Deepwater Horizon
    [05-swiss-cheese-model-0024] page:3:line:8 | Challenger
    [05-swiss-cheese-model-0025] page:3:line:9 | Conclusion
    [05-swiss-cheese-model-0026] page:3:line:10 | Topics
    [05-swiss-cheese-model-0027] page:4:line:1 | Swiss Cheese Model
    [05-swiss-cheese-model-0028] page:5:line:1 | 5
    [05-swiss-cheese-model-0029] page:5:line:2 | The Swiss Cheese Model is a way to understand how
    [05-swiss-cheese-model-0030] page:5:line:3 | failures happen in complex systems
    [05-swiss-cheese-model-0031] page:5:line:4 | Introduced by James Reason (“Human Error,” 1990)
    [05-swiss-cheese-model-0032] page:5:line:5 | Layered prevention (slices of cheese)
    [05-swiss-cheese-model-0033] page:5:line:6 | Each layer has vulnerabilities (holes in cheese)
    [05-swiss-cheese-model-0034] page:5:line:7 | Accidents happen when:
    [05-swiss-cheese-model-0035] page:5:line:8 | Barrier does not exist (holes align)
    [05-swiss-cheese-model-0036] page:5:line:9 | Barriers fail (slice is removed, holes align)
    [05-swiss-cheese-model-0037] page:5:line:10 | Swiss Cheese Model – History
    [05-swiss-cheese-model-0038] page:6:line:1 | 6
    [05-swiss-cheese-model-0039] page:6:line:2 | Swiss Cheese Model – Graphic
    [05-swiss-cheese-model-0040] page:6:line:3 | Source: By User:BenAveling - File:Swiss cheese model.svg, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=133912327
    [05-swiss-cheese-model-0041] page:7:line:1 | Preventing the spread of COVID-19
    [05-swiss-cheese-model-0042] page:7:line:2 | 7
    [05-swiss-cheese-model-0043] page:7:line:3 | Swiss Cheese Model – Example
    [05-swiss-cheese-model-0044] page:7:line:4 | Source: https://www.linkedin.com/pulse/layered-defenses-addressing-holes-how-swiss-cheese-model-sam-lindgren/
    [05-swiss-cheese-model-0045] page:8:line:1 | 8
    [05-swiss-cheese-model-0046] page:8:line:2 | Used in multiple high-risk, high-complexity industries, such
    [05-swiss-cheese-model-0047] page:8:line:3 | as:
    [05-swiss-cheese-model-0048] page:8:line:4 | Aviation
    [05-swiss-cheese-model-0049] page:8:line:5 | Nuclear Power
    [05-swiss-cheese-model-0050] page:8:line:6 | Healthcare
    [05-swiss-cheese-model-0051] page:8:line:7 | Swiss Cheese Model – Applications
    [05-swiss-cheese-model-0052] page:9:line:1 | 9
    [05-swiss-cheese-model-0053] page:9:line:2 | Simplicity
    [05-swiss-cheese-model-0054] page:9:line:3 | Framework to understand risk reduction
    [05-swiss-cheese-model-0055] page:9:line:4 | Graphical
    [05-swiss-cheese-model-0056] page:9:line:5 | Highlights there are many approaches to prevent harms (e.g., adding
    [05-swiss-cheese-model-0057] page:9:line:6 | a slice, reducing hole size)
    [05-swiss-cheese-model-0058] page:9:line:7 | Swiss Cheese Model – Benefits
    [05-swiss-cheese-model-0059] page:10:line:1 | 10
    [05-swiss-cheese-model-0060] page:10:line:2 | Simplicity
    [05-swiss-cheese-model-0061] page:10:line:3 | Assumes independence of the barriers, static system
    [05-swiss-cheese-model-0062] page:10:line:4 | Focuses on implementing barriers to prevent issues, rather than
    [05-swiss-cheese-model-0063] page:10:line:5 | addressing the underlying causes of the issues themselves
    [05-swiss-cheese-model-0064] page:10:line:6 | Generic
    [05-swiss-cheese-model-0065] page:10:line:7 | Open to interpretation – creates confusion, disagreement
    [05-swiss-cheese-model-0066] page:10:line:8 | Limited practicality
    [05-swiss-cheese-model-0067] page:10:line:9 | Swiss Cheese Model – Criticisms
    [05-swiss-cheese-model-0068] page:11:line:1 | 11
    [05-swiss-cheese-model-0069] page:11:line:2 | Hot Cheese Model
    [05-swiss-cheese-model-0070] page:11:line:3 | Introduced by Li & Thimbleby (2014)
    [05-swiss-cheese-model-0071] page:11:line:4 | Dynamic (melting cheese)
    [05-swiss-cheese-model-0072] page:11:line:5 | Barriers change over time (new holes)
    [05-swiss-cheese-model-0073] page:11:line:6 | Poorly designed mitigations (holes change shape)
    [05-swiss-cheese-model-0074] page:11:line:7 | Each barrier can introduce new risks (drip)
    [05-swiss-cheese-model-0075] page:11:line:8 | Swiss Cheese Model – Updates
    [05-swiss-cheese-model-0076] page:11:line:9 | Source: Li Y & Thimbleby H. Hot cheese: a processed Swiss cheese model. J R Coll Physicians Edinb 2014; 44:116–21 http://dx.doi.org/10.4997/JRCPE.2014.205
    [05-swiss-cheese-model-0077] page:12:line:1 | 12
    [05-swiss-cheese-model-0078] page:12:line:2 | Model used in risk management based on the principle of
    [05-swiss-cheese-model-0079] page:12:line:3 | layered security
    [05-swiss-cheese-model-0080] page:12:line:4 | Helps reduce risk of accidents occurring and / or reduce
    [05-swiss-cheese-model-0081] page:12:line:5 | impact of accidents when they occur
    [05-swiss-cheese-model-0082] page:12:line:6 | Helps us understand how accidents happen
    [05-swiss-cheese-model-0083] page:12:line:7 | Swiss Cheese Model – Summary
    [05-swiss-cheese-model-0084] page:13:line:1 | Real Disasters
    [05-swiss-cheese-model-0085] page:15:line:1 | 15
    [05-swiss-cheese-model-0086] page:15:line:2 | Deepwater Horizon Disaster – Swiss Cheese Model
    [05-swiss-cheese-model-0087] page:15:line:3 | Harm vector:
    [05-swiss-cheese-model-0088] page:15:line:4 | Defective
    [05-swiss-cheese-model-0089] page:15:line:5 | cement cap at
    [05-swiss-cheese-model-0090] page:15:line:6 | base of well
    [05-swiss-cheese-model-0091] page:15:line:7 | Cheese slice:
    [05-swiss-cheese-model-0092] page:15:line:8 | Data
    [05-swiss-cheese-model-0093] page:15:line:9 | monitoring
    [05-swiss-cheese-model-0094] page:15:line:10 | Hole:
    [05-swiss-cheese-model-0095] page:15:line:11 | Misinterpretation
    [05-swiss-cheese-model-0096] page:15:line:12 | of results
    [05-swiss-cheese-model-0097] page:15:line:13 | Outcome:
    [05-swiss-cheese-model-0098] page:15:line:14 | Explosion,
    [05-swiss-cheese-model-0099] page:15:line:15 | giant oil
    [05-swiss-cheese-model-0100] page:15:line:16 | spill
    [05-swiss-cheese-model-0101] page:15:line:17 | Cheese slice:
    [05-swiss-cheese-model-0102] page:15:line:18 | Safety
    [05-swiss-cheese-model-0103] page:15:line:19 | equipment
    [05-swiss-cheese-model-0104] page:15:line:20 | Hole:
    [05-swiss-cheese-model-0105] page:15:line:21 | Equipment
    [05-swiss-cheese-model-0106] page:15:line:22 | failure
    [05-swiss-cheese-model-0107] page:15:line:23 | Cheese slice:
    [05-swiss-cheese-model-0108] page:15:line:24 | Safety
    [05-swiss-cheese-model-0109] page:15:line:25 | procedures
    [05-swiss-cheese-model-0110] page:15:line:26 | Holes:
    [05-swiss-cheese-model-0111] page:15:line:27 | Hubris, time
    [05-swiss-cheese-model-0112] page:15:line:28 | and budget
    [05-swiss-cheese-model-0113] page:15:line:29 | pressures
    [05-swiss-cheese-model-0114] page:16:line:1 | 16
    [05-swiss-cheese-model-0115] page:17:line:1 | 17
    [05-swiss-cheese-model-0116] page:17:line:2 | Challenger Disaster – Swiss Cheese Model
    [05-swiss-cheese-model-0117] page:17:line:3 | Harm vector:
    [05-swiss-cheese-model-0118] page:17:line:4 | O-rings
    [05-swiss-cheese-model-0119] page:17:line:5 | failed
    [05-swiss-cheese-model-0120] page:17:line:6 | Outcome:
    [05-swiss-cheese-model-0121] page:17:line:7 | Shuttle
    [05-swiss-cheese-model-0122] page:17:line:8 | explosion
    [05-swiss-cheese-model-0123] page:17:line:9 | Cheese pack:
    [05-swiss-cheese-model-0124] page:17:line:10 | Oversight / Culture
    [05-swiss-cheese-model-0125] page:17:line:11 | Hole:
    [05-swiss-cheese-model-0126] page:17:line:12 | Prioritized meeting the
    [05-swiss-cheese-model-0127] page:17:line:13 | launch schedule over
    [05-swiss-cheese-model-0128] page:17:line:14 | safety
    [05-swiss-cheese-model-0129] page:17:line:15 | Cheese pack:
    [05-swiss-cheese-model-0130] page:17:line:16 | Design & Testing
    [05-swiss-cheese-model-0131] page:17:line:17 | Holes:
    [05-swiss-cheese-model-0132] page:17:line:18 | - Material impacted by cold
    [05-swiss-cheese-model-0133] page:17:line:19 | - Redundant systems had
    [05-swiss-cheese-model-0134] page:17:line:20 | same material properties
    [05-swiss-cheese-model-0135] page:18:line:1 | 18
    [05-swiss-cheese-model-0136] page:18:line:2 | Major accidents and catastrophic systems failures tend to
    [05-swiss-cheese-model-0137] page:18:line:3 | be caused by multiple, smaller failures and hazardous
    [05-swiss-cheese-model-0138] page:18:line:4 | situations leading up to the actual harm
    [05-swiss-cheese-model-0139] page:18:line:5 | Identifying and mitigating hazards or potentials for error
    [05-swiss-cheese-model-0140] page:18:line:6 | can prevent catastrophes and save lives
    [05-swiss-cheese-model-0141] page:18:line:7 | Understanding risk mitigation by using models for analysis,
    [05-swiss-cheese-model-0142] page:18:line:8 | like the Swiss Cheese Model, can help reduce risk of
    [05-swiss-cheese-model-0143] page:18:line:9 | accidents occurring and / or reduce impact of accidents
    [05-swiss-cheese-model-0144] page:18:line:10 | when they occur
    [05-swiss-cheese-model-0145] page:18:line:11 | Conclusion
    ```
