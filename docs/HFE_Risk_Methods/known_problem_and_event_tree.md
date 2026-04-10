# Known Problem Analysis 与事件树

这一页把两种补盲方法放在一起：Known Problem Analysis 是向后看历史问题，Event Tree 是向前看起始事件的后果分支。

!!! note "本页主问题"
    当主流程分析已经做完之后，团队怎样继续问：我们还漏掉了哪些已知问题和后果分支？

## 本章重点

- Known Problem Analysis 用历史问题提醒团队别把旧坑重新挖一遍。
- Event Tree 用分支展开提醒团队别低估一个起始事件后面的后果路径。
- 两者共同作用，是把视角从主路径扩展到边缘路径和遗漏风险。
- 这不是额外文书，而是补盲机制。

## 先记住方法定位

!!! tip "先记住这个方法的定位"
    先记住这个方法的定位：主流程分析负责把主路径看清，Known Problem 和 Event Tree 负责提醒你别忘了系统的边角和分支。

## 这两个方法分别补什么

`Known Problem Analysis` 补的是团队“其实早就知道”的东西，例如历史投诉、事故、CAPA、文献或竞品问题。

`Event Tree` 补的是起始事件之后的后果展开：如果这一层没拦住，会往哪些分支继续走？哪些节点是真正的防线？

!!! warning "最容易做错的地方"
    最容易出现的误解，是把 known problem 当作旧问题清单，把 event tree 当作画图练习。它们真正的作用，是改变团队对遗漏风险的敏感度。

## 操作步骤怎么走

可以把它们分开记：

1. Known Problem：先扫历史问题，再判断哪些仍适用于当前设计。
2. Event Tree：先定起始事件，再往后画分支，看后果、拦截点和严重程度如何变化。

两者都不是凭空发散，而是为了逼团队回到证据和可预见路径。

!!! example "worked example：主路径没问题，边缘路径仍然可能出事"
    例如某设备的正常使用流程已经分析清楚，但历史投诉显示用户在清洁后重新组装时经常装反部件。主流程分析可能没把这个低频分支放进去；Known Problem Analysis 会把它拉回来，而 Event Tree 会进一步展开“装反之后如果未被发现，会走向什么后果”。

## 和主流程分析是什么关系

主流程分析最擅长看正常任务流里的风险；这两个方法最擅长看主路径之外的已知隐患和分支后果。所以它们不是替代关系，而是补位关系。

!!! note "一句话结论"
    这页的真正价值，是逼团队从“我们已经分析完了”退一步，重新问“我们还可能漏了什么”。

## 本章总结

!!! tip "复习时重点记这几条"
    - Known Problem 看历史问题，Event Tree 看后果分支。
    - 两者共同作用，是补盲而不是替代主流程分析。
    - 它们都要求团队回到证据和可预见路径。
    - 真正目标是发现“我们还漏了什么”。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `风险方法`
- 关联源文件数: 2
- 文本单元数: 112
- 配图/预览数: 18

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `11 Known Problem Analysis.pptx` | `pptx` | 43 | 17 | [open](../assets/source_files/ENP_111_Use_related_Risks/11 Known Problem Analysis.pptx) |
| `Event Tree Supplemental.pptx` | `pptx` | 69 | 1 | [open](../assets/source_files/ENP_111_Use_related_Risks/Event Tree Supplemental.pptx) |

## 相关主题

- [错误分析与调查流程](error_analysis_methods.md)
- [URRA 方法](urra_methods.md)
- [Operational Risk](../HFE_Cases_Ethics/operational_risk.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "11 Known Problem Analysis.pptx | 43 text units"
    下载原件: [11 Known Problem Analysis.pptx](../assets/source_files/ENP_111_Use_related_Risks/11 Known Problem Analysis.pptx)
    映射页面: `known_problem_and_event_tree`
    
    ```text
    [11-known-problem-analysis-0001] slide:1:p:1 | Erin Davis, MS, CHFP
    [11-known-problem-analysis-0002] slide:1:p:2 | Known Problems Analysis (KPA)
    [11-known-problem-analysis-0003] slide:2:p:1 | Example: Developing a new blood glucose meter
    [11-known-problem-analysis-0004] slide:3:p:1 | Learn about use problems with existing devices
    [11-known-problem-analysis-0005] slide:4:p:1 | 4
    [11-known-problem-analysis-0006] slide:4:p:2 | Select sources
    [11-known-problem-analysis-0007] slide:4:p:3 | Collect and analyze data
    [11-known-problem-analysis-0008] slide:4:p:4 | Document findings
    [11-known-problem-analysis-0009] slide:4:p:5 | KPA process
    [11-known-problem-analysis-0010] slide:5:p:1 | 5
    [11-known-problem-analysis-0011] slide:5:p:2 | Public regulatory databases
    [11-known-problem-analysis-0012] slide:5:p:3 | FDA’s MAUDE database
    [11-known-problem-analysis-0013] slide:5:p:4 | Recall notices
    [11-known-problem-analysis-0014] slide:5:p:5 | Public safety publications
    [11-known-problem-analysis-0015] slide:5:p:6 | ECRI Medical Device Safety Reports
    [11-known-problem-analysis-0016] slide:5:p:7 | ISMP Medication Safety Alert Newsletters
    [11-known-problem-analysis-0017] slide:5:p:8 | Internal resources
    [11-known-problem-analysis-0018] slide:5:p:9 | Post-market surveillance data
    [11-known-problem-analysis-0019] slide:5:p:10 | Feedback from sales, trainers, etc.
    [11-known-problem-analysis-0020] slide:5:p:11 | Step 1: Select sources
    [11-known-problem-analysis-0021] slide:6:p:1 | 6
    [11-known-problem-analysis-0022] slide:6:p:2 | Step 2: Collect and analyze data
    [11-known-problem-analysis-0023] slide:7:p:1 | 7
    [11-known-problem-analysis-0024] slide:7:p:2 | Concise description
    [11-known-problem-analysis-0025] slide:7:p:3 | Source
    [11-known-problem-analysis-0026] slide:7:p:4 | Mitigation
    [11-known-problem-analysis-0027] slide:7:p:5 | Step 3: Document findings
    [11-known-problem-analysis-0028] slide:7:p:6 | Known problem
    [11-known-problem-analysis-0029] slide:7:p:7 | Source
    [11-known-problem-analysis-0030] slide:7:p:8 | Mitigation
    [11-known-problem-analysis-0031] slide:7:p:9 | Applied blood droplet to strip prematurely.
    [11-known-problem-analysis-0032] slide:7:p:10 | MAUDE; report 2954323-2008-02271
    [11-known-problem-analysis-0033] slide:7:p:11 | On-screen directions prompt user to add blood to test strip (using text and icons) at the appropriate time.
    [11-known-problem-analysis-0034] slide:7:p:12 | Did not apply blood to test strip correctly
    [11-known-problem-analysis-0035] slide:7:p:13 | MAUDE; report 2954323-2009-00280
    [11-known-problem-analysis-0036] slide:7:p:14 | Test strips included in pack feature symbol showing user where to put blood.
    [11-known-problem-analysis-0037] slide:8:p:1 | 8
    [11-known-problem-analysis-0038] slide:8:p:2 | Ensure use-related risk analysis contains all findings
    [11-known-problem-analysis-0039] slide:8:p:3 | Identify mitigations for any new use-related issues
    [11-known-problem-analysis-0040] slide:8:p:4 | Next steps after performing a KPA
    [11-known-problem-analysis-0041] notes:1:p:1 | When developing a product, you need to identify all of the different use errors – or mistakes – a user could potentially make.
    [11-known-problem-analysis-0042] notes:1:p:2 | In previous sessions, you’ve learned about different methods for identifying these use errors, and why that’s important to developing a use-related risk analysis. Today we’ll cover a specific method for identifying use errors, which is Known Problems Analysis.
    [11-known-problem-analysis-0043] notes:1:p:3 | At a high level, Known Problems Analysis (or a KPA), is the process of reviewing use-related issues that have occurred with devices that are already on the market that are similar to the new one being developed. The idea is to understand these issues, and then design the new product so that it isn’t prone to same sorts of known problems. So basically, don’t let history repeat itself, and instead, make the new product better.
    ```

??? info "Event Tree Supplemental.pptx | 69 text units"
    下载原件: [Event Tree Supplemental.pptx](../assets/source_files/ENP_111_Use_related_Risks/Event Tree Supplemental.pptx)
    映射页面: `known_problem_and_event_tree`
    
    ```text
    [event-tree-supplemental-0001] slide:1:p:1 | Sami Durrani PhD
    [event-tree-supplemental-0002] slide:1:p:2 | Event Tree Supplemental
    [event-tree-supplemental-0003] slide:2:p:1 | Think of events in the casual chain as items that happen or don’t happen
    [event-tree-supplemental-0004] slide:2:p:2 | Depending on the situation, the event happening could either be considered a success or failure
    [event-tree-supplemental-0005] slide:2:p:3 | Consider how the data is provided. Is it the probability that the event happens or doesn’t happen?
    [event-tree-supplemental-0006] slide:2:p:4 | Key points
    [event-tree-supplemental-0007] slide:3:p:1 | A Simple (and Ghoulish) Event Tree Example
    [event-tree-supplemental-0008] slide:3:p:2 | S
    [event-tree-supplemental-0009] slide:3:p:3 | F
    [event-tree-supplemental-0010] slide:3:p:4 | Perceive vampire
    [event-tree-supplemental-0011] slide:3:p:5 | Know to use garlic
    [event-tree-supplemental-0012] slide:3:p:6 | Shove garlic in vampire’s face
    [event-tree-supplemental-0013] slide:3:p:7 | S1
    [event-tree-supplemental-0014] slide:3:p:8 | F1
    [event-tree-supplemental-0015] slide:3:p:9 | F2
    [event-tree-supplemental-0016] slide:3:p:10 | F3
    [event-tree-supplemental-0017] slide:3:p:11 | P(S)  = S1 = (0.95 x 0.80 x 0.10) = 0.076
    [event-tree-supplemental-0018] slide:3:p:12 | P(F)  = F1 + F2 + F3 = 1 – P(S) = 1 – 0.076 = 0.924
    [event-tree-supplemental-0019] slide:3:p:13 | 0.05
    [event-tree-supplemental-0020] slide:3:p:14 | 0.95
    [event-tree-supplemental-0021] slide:3:p:15 | Vampire
    [event-tree-supplemental-0022] slide:3:p:16 | attack
    [event-tree-supplemental-0023] slide:3:p:17 | 0.20
    [event-tree-supplemental-0024] slide:3:p:18 | 0.90
    [event-tree-supplemental-0025] slide:3:p:19 | 0.80
    [event-tree-supplemental-0026] slide:3:p:20 | 0.10
    [event-tree-supplemental-0027] slide:4:p:1 | 4
    [event-tree-supplemental-0028] slide:4:p:2 | Probability of fault (in this case the “event”)
    [event-tree-supplemental-0029] slide:4:p:3 | Example data:
    [event-tree-supplemental-0030] slide:4:p:4 | System Error:    	P(F) = 0.5
    [event-tree-supplemental-0031] slide:4:p:5 | Human Error 1: 	P(F) = 0.3
    [event-tree-supplemental-0032] slide:4:p:6 | Human Error 2: 	P(F) = 0.2
    [event-tree-supplemental-0033] slide:4:p:7 | FAULT Tree
    [event-tree-supplemental-0034] slide:5:p:1 | A FAULT Tree Example
    [event-tree-supplemental-0035] slide:5:p:2 | Failure (F)
    [event-tree-supplemental-0036] slide:5:p:3 | Not Failure (NF)
    [event-tree-supplemental-0037] slide:5:p:4 | System Error
    [event-tree-supplemental-0038] slide:5:p:5 | Human  Error 1
    [event-tree-supplemental-0039] slide:5:p:6 | Human Error 2
    [event-tree-supplemental-0040] slide:5:p:7 | F = 0.03
    [event-tree-supplemental-0041] slide:5:p:8 | NF = 0.12
    [event-tree-supplemental-0042] slide:5:p:9 | NF = 0.35
    [event-tree-supplemental-0043] slide:5:p:10 | NF = 0.5
    [event-tree-supplemental-0044] slide:5:p:11 | P(F) = (0.5 x 0.3 x 0.2) = 0.03
    [event-tree-supplemental-0045] slide:5:p:12 | P(NF)  = 0.12 + 0.35 + 0.5 = 0.97  OR  1 – P(F) = 1 – 0.03 = 0.97
    [event-tree-supplemental-0046] slide:5:p:13 | 0.5
    [event-tree-supplemental-0047] slide:5:p:14 | 0.5
    [event-tree-supplemental-0048] slide:5:p:15 | System Failure
    [event-tree-supplemental-0049] slide:5:p:16 | 0.7
    [event-tree-supplemental-0050] slide:5:p:17 | 0.8
    [event-tree-supplemental-0051] slide:5:p:18 | 0.3
    [event-tree-supplemental-0052] slide:5:p:19 | 0.2
    [event-tree-supplemental-0053] slide:6:p:1 | If they are independent (i.e., one or the other can occur) and both lead to the same end result (same top-level event)
    [event-tree-supplemental-0054] slide:6:p:2 | Can calculate the the P(F) of each chain
    [event-tree-supplemental-0055] slide:6:p:3 | Total probability of top-level event occurring is the Union of the P(F) of each chain: P(FA) + P(FB) – P(FA) P(FB)
    [event-tree-supplemental-0056] slide:6:p:4 | If chain A and B are mutually exclusive, then P(FA) P(FB) = 0
    [event-tree-supplemental-0057] slide:6:p:5 | If there are multiple casual chains
    [event-tree-supplemental-0058] slide:7:p:1 | Multiple casual chains that can lead to failure
    [event-tree-supplemental-0059] slide:7:p:2 | P(FA) = 0.06
    [event-tree-supplemental-0060] slide:7:p:3 | P(Bad Outcomes) = 0.06 + 0.03 – (0.06 x 0.03) = 0.0882
    [event-tree-supplemental-0061] slide:7:p:4 | Bad outcome
    [event-tree-supplemental-0062] slide:7:p:5 | 0.3
    [event-tree-supplemental-0063] slide:7:p:6 | 0.2
    [event-tree-supplemental-0064] slide:7:p:7 | Chain A
    [event-tree-supplemental-0065] slide:7:p:8 | Chain B
    [event-tree-supplemental-0066] slide:7:p:9 | 0.2
    [event-tree-supplemental-0067] slide:7:p:10 | P(FB) = 0.03
    [event-tree-supplemental-0068] slide:7:p:11 | 0.15
    [event-tree-supplemental-0069] notes:1:p:1 | Quick introductions
    ```
