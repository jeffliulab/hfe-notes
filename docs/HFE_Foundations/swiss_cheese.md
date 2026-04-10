# Swiss Cheese 模型

这页把课程里的系统视角再往前推一步：事故不是因为某一个人突然犯了大错，而是因为多层防线同时出现漏洞，并在某个时刻被串成了一条穿透路径。

!!! note "本页主问题"
    为什么高风险系统明明有很多防线，事故还是会发生？这些防线的漏洞又为什么会在同一个时刻被串起来？

## 本章重点

- Swiss Cheese 模型把事故看成“多层防线被穿透”，而不是“单个人失手”。
- 每一层防线都可能既有保护作用，也有漏洞。
- 真正危险的不是某一个洞存在，而是多个洞在时空上对齐。
- 这套模型的价值，是把注意力从 blame 拉回 barrier design 和 system resilience。

## 先记住一句话

!!! tip "复习时先记住这句话"
    记这页时先抓一句话：事故往往不是因为“最后一个人太差”，而是因为系统里的多层保护在同一时刻都没能把问题挡住。

## Swiss Cheese 模型到底在解释什么

这套模型的核心不是“奶酪上有洞”这个比喻本身，而是它背后的解释逻辑：任何高风险系统都不会只靠一层保护，而是靠多层屏障、程序、检查、人员配合和组织控制共同维持安全。

一旦你接受这个前提，事故就不再是“某个点突然失败”，而更像是一条本来应该被多次拦截的问题链，最终一路穿透到了结果层。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/05-swiss-cheese-model/page-01.png" alt="这张图要看懂的是：事故不是绕过一层防线，而是沿着多层漏洞被连续放行。" loading="lazy">
  <figcaption>这张图要看懂的是：事故不是绕过一层防线，而是沿着多层漏洞被连续放行。</figcaption>
</figure>

## 防线和漏洞为什么会同时存在

课程用这页提醒你一个很关键的现实：有防线，并不等于防线总是有效。

- 有些漏洞是长期存在的设计弱点、资源不足、流程不合理或组织容忍。
- 有些漏洞是短时出现的，例如疲劳、分心、时间压力、天气、沟通失误。

真正危险的时刻，是这些长期条件和短时触发在同一时间叠在一起。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/05-swiss-cheese-model/page-06.png" alt="这张图要看懂的是：漏洞既可能来自长期潜伏条件，也可能来自当下触发因素，真正危险的是两者在同一时刻重合。" loading="lazy">
  <figcaption>这张图要看懂的是：漏洞既可能来自长期潜伏条件，也可能来自当下触发因素，真正危险的是两者在同一时刻重合。</figcaption>
</figure>

!!! note "一句话结论"
    系统防线不是“有了就行”，而是要持续问：它们在真实运行条件下还挡得住吗？

!!! warning "最容易误读的地方"
    不要把模型读成“只要多加几层防线就一定更安全”。如果新增的层级本身很弱、彼此冲突，或者和真实工作脱节，层数增加并不等于韧性增加。

## 这套模型为什么会把分析拉回系统设计

如果事故被理解成防线穿透，那改进方向就不会只剩下“提醒人更小心”。更成熟的追问会变成：

- 哪一层防线原本应该拦住问题
- 为什么那一层防线没有起作用
- 有没有哪一层本来就设计得太脆弱
- 多层防线之间是不是留下了彼此都以为对方会负责的空白

这也是为什么 Swiss Cheese 模型在课程里不是一个独立比喻，而是后面 risk methods、operational risk 和案例页的共同底板。

!!! example "案例：一条事故路径是怎样穿透多层防线的"
    想象一台医疗设备在夜班里被错误设定剂量。最后那一下输入错误只是 `sharp end`。更上游可能已经同时存在：界面字段易混、标签不清、双人核对流于形式、工作负荷过高、培训把重点放错。单看最后一步，很像“某个人输错了”；从 Swiss Cheese 看，真正的问题是多层防线一起失守。

## 本章总结

!!! tip "复习时重点记这几条"
    - Swiss Cheese 模型把事故理解成多层防线穿透。
    - 每一层屏障都可能同时具有保护作用和漏洞。
    - 长期潜伏条件和短时触发叠加时，事故路径最容易形成。
    - 这套模型的真正价值是把改进方向拉回 barrier design 和 system resilience。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `HFE基础`
- 关联源文件数: 1
- 文本单元数: 145
- 配图/预览数: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `05 Swiss Cheese Model.pdf` | `pdf` | 145 | 3 | [open](../assets/source_files/ENP_111_Use_related_Risks/05 Swiss Cheese Model.pdf) |

## 相关主题

- [人为失误框架](human_error_frameworks.md)
- [Operational Risk](../HFE_Cases_Ethics/operational_risk.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "05 Swiss Cheese Model.pdf | 145 text units"
    下载原件: [05 Swiss Cheese Model.pdf](../assets/source_files/ENP_111_Use_related_Risks/05 Swiss Cheese Model.pdf)
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
