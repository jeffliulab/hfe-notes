# 医疗器械中的使用错误

这一页专门解决“用错了到底算什么”的问题：device failure、无意 use error、异常使用和故意偏离规则，不能混成一个桶。

!!! note "本页主问题"
    当医疗器械使用出了问题时，
    我们怎样区分设计诱发的 use error、
    器械本身失效、
    异常使用和故意违规？

## 本章重点

- 不是所有不良使用都叫 use error。
- 判断时必须看行为是否在可预见使用范围内、
  设计是否放大了错误机会、
  恢复空间是否存在。
- use error 分析的重点，
  是把问题重新拉回具体任务和具体情境。
- 如果问题类型定义错了，
  后面的控制措施也会跑偏。

## 先记住一句话

!!! tip "复习时先记住这句话"
    记这一页最简单的方法是：
    先别急着说“用户用错了”，
    先问设计、
    环境和情境是不是已经把正确操作变得很难。

## 什么叫医疗器械中的 use error

这页不是在扩大 blame，
而是在缩小误判。
它要求团队把“错误行为”放回可预见使用场景里，
看它到底是无意偏差、
器械失效、
异常使用，
还是故意偏离规则。

## 为什么这个区分会直接影响控制策略

一旦定义错了，
改法就会跟着错：

- 明明是界面诱发错误，却只补培训，风险会回来。
- 明明是异常使用，却按普通 use error 写，控制会失焦。
- 明明是器械失效，却把责任压给用户，设计问题就被遮掉了。

!!! warning "最容易做错的地方"
    最常见的误区，
    是把所有不良后果都收成一句“user error”。
    这样一来，
    界面、
    标签、
    环境和组织条件都会从视野里消失。

## 这页真正想建立的分析习惯

看到错误行为时，
不要立刻贴标签。
先回到具体 use step、
具体场景、
具体信息显示和具体环境条件，
再问设计有没有让误选、
漏做、
误判或顺序错误变得更容易。

!!! note "一句话结论"
    医疗器械里的 use error 分析，
    本质上是在判断系统有没有把使用者推到容易出错的位置。

!!! example "案例：明明看起来像“用错了”，其实是界面在诱发错误"
    如果两种给药模式在界面上只用细小字母区分，
    用户在紧急场景中选错模式后，
    表面上像是“user selected the wrong mode”。
    但更重要的分析结论可能是：
    系统把高后果选择设计得过于难辨认。

## 为什么这页真正难的是划清边界

医疗器械 use error 分析最容易被写浅的地方，
就是团队太快把所有坏结果都装进“user error”这个桶里。
真正的分析难点在于区分：

- 是器械自己没有按设计工作
- 还是用户在可预见场景里被设计推向了错误
- 还是发生了明显超出预期的 abnormal use
- 还是操作者明知规则却故意偏离

这几个边界一旦没划清，
后面的控制、
责任判断和验证重点都会跟着乱掉。

## 为什么分类会直接改变你最后改什么

这页最实用的价值在这里：
不同类型的问题，
对应的控制策略完全不同。

- 如果是 device failure，重点回到 engineering reliability
- 如果是 design-induced use error，重点回到界面、标签、流程和可恢复性
- 如果是 abnormal use，重点回到边界说明和风险沟通
- 如果是 violation，重点还要看激励、文化和程序现实性

所以分类不是学术洁癖，
而是决定后面到底改哪里。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/07-use-errors/slide-13-image5.jpeg" alt="这张图要看懂的是：像 AED 这类设备会把引导直接做进产品里，说明很多所谓 user error 实际上可以通过界面与流程设计显著降低。" loading="lazy">
  <figcaption>这张图要看懂的是：像 AED 这类设备会把引导直接做进产品里，说明很多所谓 user error 实际上可以通过界面与流程设计显著降低。</figcaption>
</figure>

!!! example "案例：同样是“剂量不对”，为什么可能导向完全不同的改进"
    如果剂量错误来自设备内部故障，
    改进重点应是硬件或软件可靠性；
    如果来自用户把 1.0 读成 10，
    重点就应回到显示、
    对比度、
    标记和确认流程；
    如果来自故意跳过检查，
    则还要看流程是不是过于脱离现实。
    结果一样，
    但控制路径完全不同。

## 为什么 PCA 模型会帮助你把 use error 写得更准

很多医疗器械错误表面上都像“动作做错了”，
但真正导致动作错掉的，
可能是前面的 perception 没抓到、
cognition 解释错了，
或者 action 执行本身不稳定。
PCA 模型的价值，
就是把这些层级重新拆开。

一旦拆开，
团队就不会停在“用户按错了”这种表述，
而会继续问：
是没有看到关键信息、
理解错了界面含义，
还是姿态与动作本身就容易失稳。
这个差别会直接决定 mitigation 应该改显示、
改理解支持，
还是改物理操作。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/07-use-errors/slide-16-image6.png" alt="这张图要看懂的是：同一个 visible use error 可以向前追到 perception、cognition 或 action 三层里的不同断裂点，所以分析不能只盯最后那个动作。" loading="lazy">
  <figcaption>这张图要看懂的是：同一个 visible use error 可以向前追到 perception、cognition 或 action 三层里的不同断裂点，所以分析不能只盯最后那个动作。</figcaption>
</figure>

## 为什么 FDA 定义里特别强调“not caused solely by device failure”

这一句非常关键，
因为它把 use error 和纯器械失效切开了。
如果设备自己坏了，
团队当然也要分析，
但那条线更多会回到硬件、
软件、
材料和可靠性；
只有当用户动作或缺少动作参与了后果链，
而且这条链不是单靠 device failure 就能解释时，
use error 分析才真正站得住。

这也是为什么这页不能只看结果，
而必须回到动作与情境。
相同的坏结果，
有时是机械失效，
有时是界面诱发误判，
有时是多名使用者在交接中连续漏掉关键动作。
定义里这句限制，
正是在逼团队把这些路径分开。

## 为什么“最后没人受伤”也可能已经构成 use error

课件里 AED 例子特别适合讲这一点。
使用者把电极片贴错了位置，
但患者最后仍然被救回。
这里最容易犯的错，
是事后因为结局“还不错”，
就误以为前面的错误不算问题。

FDA 定义强调的是 `did or could result in harm`。
也就是说，
只要那条错误路径本来足以把系统推进到伤害边缘，
它就已经值得被当成 use error 来分析。
分析关注的是风险链是否成立，
不只是最后结果有没有变成最坏情况。

## hospital bed 例子真正要你看到的是一条多错误链

hospital bed 例子的重要性，
在于它明确告诉你：
一次场景里完全可能出现多个 use error，
而且它们发生在不同人、
不同节点、
不同交接边界上。
课件里至少拆出了几层：

- 第一位工作人员没有锁刹车
- 本来打算口头提醒护士，却忘了交接
- 后续护士在协助病人上床前，也没有先确认床已固定

这类场景最容易被简化成“某个人忘了做一件事”。
但更成熟的读法是：
系统在搬运、
交接、
再定位和病人接触这几段之间，
没有把关键状态稳定传下去。
也就是说，
问题不只是一个人漏做，
而是一条 handoff 链条没有形成可靠屏障。

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/07-use-errors/slide-09-image2.jpeg" alt="这张图要看懂的是：hospital bed 场景的风险不是孤立动作，而是搬运、交接和再次接触病人之间的状态信息没有被稳定传下去。" loading="lazy">
  <figcaption>这张图要看懂的是：hospital bed 场景的风险不是孤立动作，而是搬运、交接和再次接触病人之间的状态信息没有被稳定传下去。</figcaption>
</figure>

!!! warning "最容易漏掉的判断"
    一个场景里不一定只有一个 use error。
    只要任务跨人、
    跨时间或跨交接边界展开，
    多个小错误就可能串成同一条 harm path。
    把它硬压成单点错误，
    会让后面的控制设计过于单薄。

!!! example "案例：为什么 hospital bed 场景不该写成“护士粗心”"
    如果最后只写成“护士在病人上床前没检查床是否锁住”，
    分析就会漏掉前面已经发生的两件关键事：
    前一位工作人员为了便于 reposition 故意先不锁刹车，
    以及原本应该发生的口头交接没有发生。
    真正要写出来的不是一个人的粗心，
    而是关键状态没有被稳定传递、
    也没有被下一层防线重新确认。

## 本章总结

!!! tip "复习时重点记这几条"
    - 不是所有不良使用都等于 use error。
    - 分类时要看可预见性、
      设计诱发和恢复空间。
    - 如果问题定义错了，
      控制策略也会错。
    - 分析必须回到具体任务和具体情境。


## 资料范围与相关主题

正文先把知识点讲清楚；这里列出本页用到的原始文件，页尾折叠区块则保留完整逐行转写，便于你核对。

- 所属分区: `ENP111`
- 关联源文件数: 1
- 文本单元数: 156
- 配图/预览数: 10

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `07 Use Errors.pptx` | `pptx` | 156 | 10 | [open](../assets/source_files/ENP111/07 Use Errors.pptx) |

## 相关主题

- [ISO 14971 与医疗器械风险管理](iso_14971.md)
- [医疗器械中的 URRA](medical_device_urra.md)
- [任务分析](task_analysis.md)

## 原文转写与来源映射

下面的折叠区块保留逐页/逐幻灯/逐单元原文。每一行前面的 `unit_id` 都能在 `data/coverage_map.json` 中找到对应页面映射。

??? info "07 Use Errors.pptx | 156 text units"
    下载原件: [07 Use Errors.pptx](../assets/source_files/ENP111/07 Use Errors.pptx)
    映射页面: `medical_device_use_errors`
    
    ```text
    [07-use-errors-0001] slide:1:p:1 | ENP  111 – Use Related Risk Analysis
    [07-use-errors-0002] slide:1:p:2 | Sami Durrani PhD and Eric Bergman PhD
    [07-use-errors-0003] slide:1:p:3 | Use Errors
    [07-use-errors-0004] slide:2:p:1 | 2
    [07-use-errors-0005] slide:2:p:2 | FDA definition: User action or lack of action that was different from that expected by the manufacturer and caused a result that:
    [07-use-errors-0006] slide:2:p:3 | (1) was different from the result expected by the user and
    [07-use-errors-0007] slide:2:p:4 | (2) was not caused solely by device failure and
    [07-use-errors-0008] slide:2:p:5 | (3) did or could result in harm
    [07-use-errors-0009] slide:2:p:6 | What is a use error?
    [07-use-errors-0010] slide:3:p:1 | Let’s look at a few case studies
    [07-use-errors-0011] slide:4:p:1 | Hospital Bed
    [07-use-errors-0012] slide:4:p:2 | A hospital staff member is transporting a hospital bed from one room to another.
    [07-use-errors-0013] slide:4:p:3 | After positioning the hospital bed in the new room, the staff member is unsure of the exact desired bed placement, so decides to leave without locking the brakes to enable the station nurse to easily reposition the bed.
    [07-use-errors-0014] slide:4:p:4 | The staff member meant to inform the duty nurse that the bed’s brakes were not set but forgets to do.
    [07-use-errors-0015] slide:4:p:5 | 4
    [07-use-errors-0016] slide:5:p:1 | Hospital Bed
    [07-use-errors-0017] slide:5:p:2 | New patient arrives and the duty nurse helps patient into bed. Nurse starts to pull the side rails up, which causes the bed to move and spin out of control.
    [07-use-errors-0018] slide:5:p:3 | 5
    [07-use-errors-0019] slide:6:p:1 | 6
    [07-use-errors-0020] slide:6:p:2 | Hospital Bed
    [07-use-errors-0021] slide:6:p:3 | 6
    [07-use-errors-0022] slide:6:p:4 | Thankfully, the nurse was able to catch the bed and secure it before anyone was hurt
    [07-use-errors-0023] slide:7:p:1 | 7
    [07-use-errors-0024] slide:7:p:2 | In a bustling hospital's echoing hall, a bed transported, wheels and all. From one room to next, it made its trip, with each turn and twist, a careful grip.
    [07-use-errors-0025] slide:7:p:3 | The staffer, with intent so kind, left the brakes unset, it slipped his mind. Thinking the nurse would adjust its station, he left, lost in his next task's fascination.
    [07-use-errors-0026] slide:7:p:4 | But as fate would have it, the tale unfolds, a new patient arrives, a story yet untold. The duty nurse, with care profound, helps the patient, with soft voices around.
    [07-use-errors-0027] slide:7:p:5 | Yet as he reached to secure the rail, the bed began to drift, starting a frail tale. It spun and twirled, a dance so wild, danger lurking, for nurse and the beguiled.
    [07-use-errors-0028] slide:7:p:6 | But quick in thought and swift in action, the nurse's grip became the main attraction. With strength and grace, he steadied the ride, ensuring the patient's safety, with pride on his side.
    [07-use-errors-0029] slide:7:p:7 | A lesson learned in that fleeting spell, in a hospital’s dance, where stories dwell. For in moments of haste, things may go astray, but vigilance and care will save the day!
    [07-use-errors-0030] slide:7:p:8 | Previous scenario as a poem
    [07-use-errors-0031] slide:8:p:1 | 8
    [07-use-errors-0032] slide:8:p:2 | Was there a use error?
    [07-use-errors-0033] slide:8:p:3 | Was there only one? Or multiple?
    [07-use-errors-0034] slide:8:p:4 | Hospital Bed
    [07-use-errors-0035] slide:9:p:1 | Hospital Bed
    [07-use-errors-0036] slide:9:p:2 | A hospital staff member is transporting a hospital bed from one room to another.
    [07-use-errors-0037] slide:9:p:3 | After positioning the hospital bed in the new room, the staff member is unsure of the exact desired bed placement, so decides to leave without locking the brakes to enable the station nurse to easily reposition the bed.
    [07-use-errors-0038] slide:9:p:4 | The staff member meant to inform the duty nurse that the bed’s brakes were not set but forgets to do.
    [07-use-errors-0039] slide:9:p:5 | 9
    [07-use-errors-0040] slide:10:p:1 | Hospital Bed
    [07-use-errors-0041] slide:10:p:2 | New patient comes.
    [07-use-errors-0042] slide:10:p:3 | Duty nurse helps patient into bed, and starts to pull the side rails up, which causes the bed to move and spin out of control
    [07-use-errors-0043] slide:10:p:4 | 10
    [07-use-errors-0044] slide:11:p:1 | 11
    [07-use-errors-0045] slide:11:p:2 | Hospital Bed
    [07-use-errors-0046] slide:11:p:3 | 11
    [07-use-errors-0047] slide:11:p:4 | Thankfully the nurse was able to catch the bed and secure it before anyone was hurt
    [07-use-errors-0048] slide:12:p:1 | 12
    [07-use-errors-0049] slide:12:p:2 | Was there a use error?
    [07-use-errors-0050] slide:12:p:3 | Yes
    [07-use-errors-0051] slide:12:p:4 | Was there only one? Or multiple?
    [07-use-errors-0052] slide:12:p:5 | Errors:
    [07-use-errors-0053] slide:12:p:6 | Unsure of bed placement/location
    [07-use-errors-0054] slide:12:p:7 | Does not lock brakes
    [07-use-errors-0055] slide:12:p:8 | Forgets to inform nurse that brakes not set
    [07-use-errors-0056] slide:12:p:9 | Does not set brakes before helping patient into bed
    [07-use-errors-0057] slide:12:p:10 | Hospital Bed
    [07-use-errors-0058] slide:12:p:11 | Not USE Error
    [07-use-errors-0059] slide:12:p:12 | Not USE Error
    [07-use-errors-0060] slide:12:p:13 | USE Error
    [07-use-errors-0061] slide:12:p:14 | USE Error
    [07-use-errors-0062] slide:13:p:1 | 13
    [07-use-errors-0063] slide:13:p:2 | Scenario: A layperson, trying to use an AED in an emergency, misreads the instructional graphics on the inside of the AED’s cover.
    [07-use-errors-0064] slide:13:p:3 | As a result, the layperson places the adhesive electrode pads in incorrect locations on the person suffering cardiac arrest’s chest before delivering the AED pulse. But thankfully, the AED pulse still saves the person’s life.
    [07-use-errors-0065] slide:13:p:4 | Did a use error occur?
    [07-use-errors-0066] slide:13:p:5 | Yes
    [07-use-errors-0067] slide:13:p:6 | Automated External Defibrillator (AED)
    [07-use-errors-0068] slide:14:p:1 | Errors in writing use errors
    [07-use-errors-0069] slide:15:p:1 | 15
    [07-use-errors-0070] slide:15:p:2 | User stores device incorrectly
    [07-use-errors-0071] slide:15:p:3 | User stores device in temperatures below -5F
    [07-use-errors-0072] slide:15:p:4 | User enters incorrect patient information
    [07-use-errors-0073] slide:15:p:5 | User enters patient’s date of birth incorrectly
    [07-use-errors-0074] slide:15:p:6 | User dials wrong dose amount
    [07-use-errors-0075] slide:15:p:7 | User dials dose amount 0% < 20% prescribed
    [07-use-errors-0076] slide:15:p:8 | User dials dose amount 20% < 50% prescribed
    [07-use-errors-0077] slide:15:p:9 | User dials dose amount >50% prescribed
    [07-use-errors-0078] slide:15:p:10 | User dials dose amount 0% > 20% prescribed
    [07-use-errors-0079] slide:15:p:11 | …and so on
    [07-use-errors-0080] slide:15:p:12 | Not being specific enough
    [07-use-errors-0081] slide:16:p:1 | 16
    [07-use-errors-0082] slide:16:p:2 | Before we go on: PCA model refresher
    [07-use-errors-0083] slide:16:p:3 | AAMI/IEC TIR62366-2
    [07-use-errors-0084] slide:17:p:1 | 17
    [07-use-errors-0085] slide:17:p:2 | FDA definition: User action or lack of action that was different from that expected by the manufacturer and caused a result that:
    [07-use-errors-0086] slide:17:p:3 | (1) was different from the result expected by the user and
    [07-use-errors-0087] slide:17:p:4 | (2) was not caused solely by device failure and
    [07-use-errors-0088] slide:17:p:5 | (3) did or could result in harm
    [07-use-errors-0089] slide:17:p:6 | Use error definition refresher
    [07-use-errors-0090] slide:17:p:7 | Key Point: Use errors are expressed by physical action or lack of required action
    [07-use-errors-0091] slide:18:p:1 | 18
    [07-use-errors-0092] slide:18:p:2 | Common mistake to use Perception Cognition and Action (PCA) model in task analysis to define a “use error” for each PCA line
    [07-use-errors-0093] slide:18:p:3 | For example:
    [07-use-errors-0094] slide:18:p:4 | User does not see warning
    [07-use-errors-0095] slide:18:p:5 | User does not comprehend instructions
    [07-use-errors-0096] slide:18:p:6 | Use errors are physical action based
    [07-use-errors-0097] slide:18:p:7 | You can’t be jailed for thinking about stealing You actually have to steal
    [07-use-errors-0098] slide:18:p:8 | Writing use errors that don’t include an action
    [07-use-errors-0099] slide:18:p:9 | These are not use errors
    [07-use-errors-0100] slide:19:p:1 | 19
    [07-use-errors-0101] slide:19:p:2 | User is inexperienced
    [07-use-errors-0102] slide:19:p:3 | User does not understand training
    [07-use-errors-0103] slide:19:p:4 | User does not hear alarm “X”
    [07-use-errors-0104] slide:19:p:5 | User does not respond to alarm “X”
    [07-use-errors-0105] slide:19:p:6 | User transposes numbers when reading prescription card
    [07-use-errors-0106] slide:19:p:7 | User dials dose amount 0% < +20% prescribed
    [07-use-errors-0107] slide:19:p:8 | …etc
    [07-use-errors-0108] slide:19:p:9 | Incorrectly writing causes as use errors
    [07-use-errors-0109] slide:20:p:1 | 20
    [07-use-errors-0110] slide:20:p:2 | User does not check drug for discoloring
    [07-use-errors-0111] slide:20:p:3 | User injects drug that is discolored
    [07-use-errors-0112] slide:20:p:4 | User does not check device for leaks
    [07-use-errors-0113] slide:20:p:5 | User uses vial with leaking fluid
    [07-use-errors-0114] slide:20:p:6 | Home patient does check not expiration date on oral medication
    [07-use-errors-0115] slide:20:p:7 | Patient takes expired oral medication
    [07-use-errors-0116] slide:20:p:8 | Use errors that are not testable/observable
    [07-use-errors-0117] slide:21:p:1 | 21
    [07-use-errors-0118] slide:21:p:2 | User enters incorrectly high blood glucose value into an insulin dose calculator, which provides a 3x dose recommendation, leading user to overdose
    [07-use-errors-0119] slide:21:p:3 | User incorrectly enters blood glucose value >X%
    [07-use-errors-0120] slide:21:p:4 | Writing a sequence of events as a use error
    [07-use-errors-0121] slide:22:p:1 | 22
    [07-use-errors-0122] slide:22:p:2 | User dials dose amount 0% < +20% prescribed
    [07-use-errors-0123] slide:22:p:3 | User injects dose amount 0% < 20% prescribed
    [07-use-errors-0124] slide:22:p:4 | Use words that imply actual device or medical operation, for example:
    [07-use-errors-0125] slide:22:p:5 | User injects
    [07-use-errors-0126] slide:22:p:6 | User infuses
    [07-use-errors-0127] slide:22:p:7 | User operates
    [07-use-errors-0128] slide:22:p:8 | ..etc
    [07-use-errors-0129] slide:22:p:9 | Bonus!
    [07-use-errors-0130] slide:22:p:10 | Where possible, write use actions so that they directly link to the action that can cause harm
    [07-use-errors-0131] notes:1:p:1 | Quick introductions
    [07-use-errors-0132] notes:10:p:1 | Worth noting that this entire topic is “fraught” and that there are some professionals out there who would say that some of these ARE use errors.We disagree, of course.
    [07-use-errors-0133] notes:11:p:1 | What is the use error?
    [07-use-errors-0134] notes:12:p:1 | Make sure to explain that here we provide tips to write use errors that are accurate and well described
    [07-use-errors-0135] notes:13:p:1 | The consequences, and hence harms or the severity of the harms (if the harms are the same) could be quite different for these different specific scenarios.
    [07-use-errors-0136] notes:13:p:2 | Being specific also helps with designers and engineers develop proper mitigations. Its important to note that often use errors will form the basis of requirements and unclear use errors can lead to unclear requirements which can lead to mitigations that are not sufficiently effective.
    [07-use-errors-0137] notes:13:p:3 | Also, being specific can help you when developing your validation test and setting your pass/fail criteria.
    [07-use-errors-0138] notes:13:p:4 | All this said, being too specific can also cause issues by leading to mitigations that don’t sufficiently generalize to a range of use scenarios.  For example, if you neglect to account for “user dials wrong dose amount” leading to underdose, then the analysis will be incomplete.
    [07-use-errors-0139] notes:14:p:1 | The Perception, Cognition, and manual Action (PCA) model may be used to further break down user interactions into specific user actions related to perceptual inputs, cognitive processing, and physical actions involved in performing the related step. [3].
    [07-use-errors-0140] notes:14:p:2 | Using the PCA model, tasks are decomposed down to the level of individual user interactions related to:
    [07-use-errors-0141] notes:14:p:3 | 1) Perception – Perceptual information to be noticed or detected by the user.
    [07-use-errors-0142] notes:14:p:4 | 2) Cognition – Cognitive components to be interpreted by the user.
    [07-use-errors-0143] notes:14:p:5 | 3) Action – Physical actions taken by the user.
    [07-use-errors-0144] notes:14:p:6 | Using the PCA model assists manufacturers in understanding the different PCA elements required for each task and further delineate use errors that may occur if the user if unable to meet these requirements. Additional steps or tasks may be revealed or uncovered that manufacturers were previously unaware of or may have glanced over in the initial task list.
    [07-use-errors-0145] notes:14:p:7 | Potential use-related problems can be identified by asking the following questions [2]:
    [07-use-errors-0146] notes:14:p:8 | 1) What if the user is unable to perceive x?
    [07-use-errors-0147] notes:14:p:9 | 2) What if the user is unable to interpret/process y?
    [07-use-errors-0148] notes:14:p:10 | 3) What if the user is unable to perform action z?
    [07-use-errors-0149] notes:14:p:11 | Although use errors are ultimately bound to an action (or inaction), analysis of perceptual information and cognitive elements may inform the cause of use errors that may occur. This breakdown of use errors then allow manufacturers to further inform their use-related risk analysis (URRA).
    [07-use-errors-0150] notes:17:p:1 | Another common error, often stemming from PCA analysis, observed issues in usability testing or field complaints. Do not confuse reasons for a use error for the use error itself.  This is a bit tricky, because the line isn’t always clear and here experience and judgement do come in. Sometimes its clear, sometimes its not. We’ll continue to tackle this via example throughout the semester.
    [07-use-errors-0151] notes:17:p:2 | For example, this first example. … I’ve seen 1000+ line items URRAs because they start listing every possible way something can get damaged.
    [07-use-errors-0152] notes:18:p:1 | This one is a bit about strategy. As an HF engineer, you want to develop a good product that safe and effective, but you also don’t want write user errors that artificially end up causing you to fail your HF validation study. There is no point in developing a great product that you can’t get to market because you hampered yourself in conducting your HF study.
    [07-use-errors-0153] notes:18:p:2 | On User does not check device for damage, be careful on wording selection. If you said user selects instead of uses, you might have ended up with a use error even the user did not actually intend to ever use it.
    [07-use-errors-0154] notes:19:p:1 | Particularly common in software as medical devices because often the harm is indirect.
    [07-use-errors-0155] notes:19:p:2 | It is important to note that the sequence of events is important, and that this point should not confuse you into thinking that one more use errors cannot contribute to a subsequent use error. They can, but in the example above, incorrectly entering the value is not necessarily a use error.
    [07-use-errors-0156] notes:20:p:1 | Ensure use action leading to harm is complete!
    ```
