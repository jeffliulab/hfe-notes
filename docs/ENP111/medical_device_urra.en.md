# URRA in Medical Devices

This page places URRA inside the medical-device regulatory context, where use-related risk is tied more explicitly to patient harm, critical tasks, and traceable controls.

!!! note "Core Question"
    Inside medical devices,
    what additional judgment demands does URRA impose beyond a generic task-risk analysis?

## Key Takeaways

- Medical-device URRA places stronger emphasis on foreseeable use scenarios,
  critical tasks,
  and patient-harm pathways.
- Controls cannot stop at training;
  interface,
  labeling,
  IFU,
  and physical design changes take priority.
- The regulatory context requires the risk chain to be traceable,
  verifiable,
  and reviewable.
- This page bridges ISO 14971 and concrete use-error work.

## What This Method Is For

!!! tip "Start with the Purpose"
    Remember the purpose of medical-device URRA this way:
    it is not a generic risk table;
    it must be written clearly enough to show how patients may be harmed and how design should respond.

## What Problem This Method Solves

Medical-device URRA solves the problem of turning use risk into evidence that is acceptable in a regulated setting.
It requires the team to write use scenario,
critical task,
use error,
hazardous situation,
harm,
and control as one complete chain.

## What the Inputs and Outputs Are

Typical inputs include task analysis,
user groups,
use environment,
device design,
labeling and IFU,
known issues,
and harm assessment.

The output should make it clear:

- which steps are critical tasks
- which errors can lead directly to patient harm
- which controls must appear in design
- which points must enter validation

## How the Method Proceeds

The logic is similar to generic URRA but held to a stricter standard:
begin with the use scenario,
identify the critical task,
define the concrete use error,
push the chain into hazardous situation,
harm,
and control,
and then feed the row back into validation planning.

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/06-urra-in-medical-devices/slide-09-image30.png" alt="This figure should show that medical-device URRA loops repeatedly between user definition, critical-task identification, control design, and validation rather than ending once a row has been written." loading="lazy">
  <figcaption>This figure should show that medical-device URRA loops repeatedly between user definition, critical-task identification, control design, and validation rather than ending once a row has been written.</figcaption>
</figure>

!!! note "One-Sentence Conclusion"
    The key move in medical-device URRA is not simply stating that risk exists,
    but specifying how the patient may be harmed and how the system intends to intercept that path.

!!! warning "The Most Common Failure Mode"
    The weakest recurring control is to write everything as “better training.” If interface,
    feedback,
    labeling,
    or physical form can be redesigned,
    the primary risk should not be left to training and attention.

!!! example "Worked Example: Why a Critical Task Must Be Marked Explicitly"
    Suppose the syringe step is “set dose.” If failure there can lead directly to patient harm,
    that step must be marked as a critical task.
    Only then will the design review and validation plan allocate the higher level of control and testing attention it deserves.

## How It Connects to the Neighboring Pages

This page inherits the standardized language of ISO 14971 and feeds forward into use-error analysis and the EpiPen workbook.
It is the hub page inside the medical-device section.

## Why Medical-Device URRA Puts Special Weight on Critical Tasks

In medical devices,
a critical task is not just an “important step” in everyday language.
It is a threshold inside risk management.
If performing the step incorrectly could directly affect patient safety or treatment effectiveness,
the step must be elevated analytically.

That changes at least three later decisions:

- whether design needs stronger error-prevention or confirmation logic
- whether IFU, labeling, and interface need stronger support around that step
- whether validation must observe that step as a high-priority use scenario

!!! example "Example: Why “Remove the Cap” and “Confirm Orientation” Can Matter More Than the Injection Itself"
    In self-injection devices,
    the highest-risk node is not always the final act of pressing.
    Earlier actions such as orientation confirmation,
    end recognition,
    cap-removal sequence,
    and device alignment may matter more because once they fail,
    every later action is pulled off track.
    That is why medical-device URRA cannot focus only on the most visible use action.

## Why This Page Cares More About Traceability Than Generic URRA

When generic risk analysis is weak,
the consequences are already serious.
In medical devices,
weak analysis also distorts design decisions,
validation planning,
and regulatory communication.
That is why this page cares so much about traceability.

The team has to be able to trace one chain backward:

- why the step was judged critical
- which task and scenario the use error came from
- whether the control really answers that risk path
- where the control was later validated

## Why Medical-Device URRA Demands Very Specific Scenario and Action Wording

In medical-device URRA,
the phrase “the user misused the device” carries almost no analytic value.
Wording that can support design and validation has to specify the action,
interface object,
environment,
and direction of error,
such as misreading the dose,
reversing the orientation,
withdrawing too early,
or failing to complete confirmation.

This is not about making the table more complicated.
Patient harm often grows out of those concrete moves.
If the action wording stays vague,
later controls and validation plans inevitably become vague as well.

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/06-urra-in-medical-devices/slide-02-image5.png" alt="This figure should make one point concrete: device interfaces and physical forms differ widely, so use-related risk cannot stay abstract and has to return to the actual device and task." loading="lazy">
  <figcaption>This figure should make one point concrete: device interfaces and physical forms differ widely, so use-related risk cannot stay abstract and has to return to the actual device and task.</figcaption>
</figure>

## Why URRA Is Both a Process and a Document

One of the easiest misreadings on this page is to treat URRA as “the table you submit at the end.” The lecture is actually pointing out that URRA is both an analysis process and the working document that carries the result.
The process determines how the team identifies use scenarios,
critical tasks,
and harm paths;
the document determines whether those judgments can be reused by design,
regulatory,
and validation teams.

In other words,
URRA is not something you think through first and then casually write down.
It is a tracked record formed while the analysis is happening.
If it is treated only as a document template,
the content becomes hollow.
If it is treated only as thinking with no clear written chain,
the team cannot share or review it.
In the medical-device context,
both layers matter.

## Why the User Interface in Medical Devices Is Far More Than a Screen

The course uses a broad definition of the medical-device user interface.
It includes not only screens,
buttons,
and physical controls,
but also the IFU,
packaging,
labeling,
training material,
and the entire interaction surface through which the user learns and operates the device.

That definition directly changes how URRA should be written.
Once the interface is understood as the whole system the user truly encounters,
many controls no longer land only on the core device body.
They land on instructions,
packaging differentiation,
confirmation prompts,
end identification,
and training scaffolds.
That is also why the lecture keeps repeating `Use Error,
not User Error`,
pulling risk back toward design and interface support.

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/06-urra-in-medical-devices/slide-18-image31.jpeg" alt="This figure should make one thing concrete: the medical-device interface is not only screen text. On a device such as an infusion pump, display, keypad, units, labeling, and action rhythm all combine into the real user interface." loading="lazy">
  <figcaption>This figure should make one thing concrete: the medical-device interface is not only screen text. On a device such as an infusion pump, display, keypad, units, labeling, and action rhythm all combine into the real user interface.</figcaption>
</figure>

## How to Tell Whether One URRA Row Is Strong Enough to Support Design Decisions

A strong URRA row should read like one complete risk story rather than a pile of column labels.
The team should at least be able to read from one row:

- who is performing which step in what scenario
- what the actual direction of error is
- which hazardous situation becomes possible
- where patient harm appears
- whether the current control prevents early, interrupts in the middle, or merely reduces consequence late

If a row still leaves the team with only phrases like “possible misuse,” “possible injury,” and “recommend training,” it is not yet supporting design.
URRA that can drive design must write the risk chain concretely enough that the team knows which layer actually needs change.

!!! example "Example: Why One Numeric-Entry Step on an Infusion Pump Can Reveal Whether the URRA Row Is Mature"
    If the row only says “the user sets the wrong infusion rate,” the team still cannot see what to redesign.
    A stronger row specifies whether 12.5 was misread as 125 under high workload,
    whether the user missed the mL/hr unit during a mode change,
    or whether the confirmation step lacked a second verification.
    Only when the error direction is concrete can the team decide whether to redesign display hierarchy,
    unit presentation,
    confirmation flow,
    or training support.

## Chapter Summary

!!! tip "What To Carry Forward"
    - Medical-device URRA places stronger emphasis on critical tasks and patient harm.
    - Its inputs include task flow,
      user context,
      design,
      and labeling information.
    - Its outputs must support both controls and validation planning.
    - Training cannot become the default primary control.


## Source Scope and Related Topics

The teaching notes come first. This section lists the source files used on the page, and the appendix keeps the full line-by-line transcription for verification.

- Section: `ENP111`
- Source files: 1
- Text units: 477
- Visuals/previews: 20

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `06 URRA in Medical Devices.pptx` | `pptx` | 477 | 20 | [open](../assets/source_files/ENP111/06 URRA in Medical Devices.pptx) |

## Related Topics

- [ISO 14971 and Medical Device Risk Management](iso_14971.en.md)
- [Use Errors in Medical Devices](medical_device_use_errors.en.md)
- [The EpiPen URRA Workbook](epipen_workbook.en.md)

## Original Transcription and Coverage Mapping

The collapsible blocks below preserve page/slide-level source transcription. Each `unit_id` maps one-to-one in `data/coverage_map.json`.

??? info "06 URRA in Medical Devices.pptx | 477 text units"
    Download source: [06 URRA in Medical Devices.pptx](../assets/source_files/ENP111/06 URRA in Medical Devices.pptx)
    Mapped page: `medical_device_urra`
    
    ```text
    [06-urra-in-medical-devices-0001] slide:1:p:1 | Sami Durrani PhD and Eric Bergman PhD
    [06-urra-in-medical-devices-0002] slide:1:p:2 | Use Related Risk in Medical Devices
    [06-urra-in-medical-devices-0003] slide:2:p:1 | 2
    [06-urra-in-medical-devices-0004] slide:2:p:2 | Examples of medical devices
    [06-urra-in-medical-devices-0005] slide:3:p:1 | 3
    [06-urra-in-medical-devices-0006] slide:3:p:2 | Assigned reading:
    [06-urra-in-medical-devices-0007] slide:3:p:3 | Medical device definition
    [06-urra-in-medical-devices-0008] slide:3:p:4 | https://www.fda.gov/media/131268/download
    [06-urra-in-medical-devices-0009] slide:4:p:1 | 4
    [06-urra-in-medical-devices-0010] slide:4:p:2 | Medical device “user interface” includes…
    [06-urra-in-medical-devices-0011] slide:4:p:3 | The IFU (instructions for use)
    [06-urra-in-medical-devices-0012] slide:4:p:4 | Packaging & Labeling
    [06-urra-in-medical-devices-0013] slide:4:p:5 | Training
    [06-urra-in-medical-devices-0014] slide:4:p:6 | In the end, all the elements of the system with which the user interacts to learn and operate the device
    [06-urra-in-medical-devices-0015] slide:5:p:1 | Business goal
    [06-urra-in-medical-devices-0016] slide:5:p:2 | Regulatory Requirement
    [06-urra-in-medical-devices-0017] slide:5:p:3 | 5
    [06-urra-in-medical-devices-0018] slide:5:p:4 | Goal of medical device development is to make products:
    [06-urra-in-medical-devices-0019] slide:5:p:5 | Safe
    [06-urra-in-medical-devices-0020] slide:5:p:6 | Effective
    [06-urra-in-medical-devices-0021] slide:5:p:7 | Efficient
    [06-urra-in-medical-devices-0022] slide:5:p:8 | Satisfying user experience
    [06-urra-in-medical-devices-0023] slide:5:p:9 | Use-related risk in medical device design
    [06-urra-in-medical-devices-0024] slide:5:p:10 | User interface designs that do not mitigate use errors detract from all the above goals!
    [06-urra-in-medical-devices-0025] slide:5:p:11 | Yes – designs!
    [06-urra-in-medical-devices-0026] slide:5:p:12 | KEY CONCEPT: Use errors are a consequence of the device’s design
    [06-urra-in-medical-devices-0027] slide:6:p:1 | 6
    [06-urra-in-medical-devices-0028] slide:6:p:2 | Use Error, not User Error
    [06-urra-in-medical-devices-0029] slide:6:p:3 | KEY CONCEPT: Potential for use errors can be mitigated by good design
    [06-urra-in-medical-devices-0030] slide:6:p:4 | (by applying a robust Human Factors Engineering process)
    [06-urra-in-medical-devices-0031] slide:7:p:1 | 7
    [06-urra-in-medical-devices-0032] slide:7:p:2 | Key Guidance & Standards
    [06-urra-in-medical-devices-0033] slide:8:p:1 | 8
    [06-urra-in-medical-devices-0034] slide:8:p:2 | Key activities – HF med device process
    [06-urra-in-medical-devices-0035] slide:9:p:1 | Use-related risk analysis process (as defined by FDA)
    [06-urra-in-medical-devices-0036] slide:9:p:2 | Residual risk analysis
    [06-urra-in-medical-devices-0037] slide:9:p:3 | Formative testing
    [06-urra-in-medical-devices-0038] slide:9:p:4 | Image source: Applying Human Factors and Usability Engineering to Medical Devices. FDA Feb 2016
    [06-urra-in-medical-devices-0039] slide:10:p:1 | 10
    [06-urra-in-medical-devices-0040] slide:10:p:2 | Its both
    [06-urra-in-medical-devices-0041] slide:10:p:3 | The process to identify your use related risks
    [06-urra-in-medical-devices-0042] slide:10:p:4 | A	nd the document that you use to compile your use-related risks
    [06-urra-in-medical-devices-0043] slide:10:p:5 | Important note: Nomenclature and exact process varies by companies
    [06-urra-in-medical-devices-0044] slide:10:p:6 | Wait? Is URRA a process or document?
    [06-urra-in-medical-devices-0045] slide:11:p:1 | 11
    [06-urra-in-medical-devices-0046] slide:11:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0047] slide:11:p:3 | Reference number
    [06-urra-in-medical-devices-0048] slide:11:p:4 | Task description
    [06-urra-in-medical-devices-0049] slide:11:p:5 | Potential use errors
    [06-urra-in-medical-devices-0050] slide:11:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0051] slide:11:p:7 | Severity of harm
    [06-urra-in-medical-devices-0052] slide:11:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0053] slide:11:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0054] slide:11:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0055] slide:11:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0056] slide:12:p:1 | 12
    [06-urra-in-medical-devices-0057] slide:12:p:2 | URRA in a tabular format
    [06-urra-in-medical-devices-0058] slide:12:p:3 | Ref #
    [06-urra-in-medical-devices-0059] slide:12:p:4 | Use Task Description
    [06-urra-in-medical-devices-0060] slide:12:p:5 | Potential Use Error
    [06-urra-in-medical-devices-0061] slide:12:p:6 | Potential Hazard/Clinical Harm
    [06-urra-in-medical-devices-0062] slide:12:p:7 | Severity of Harm
    [06-urra-in-medical-devices-0063] slide:12:p:8 | Critical Task (Y/N)
    [06-urra-in-medical-devices-0064] slide:12:p:9 | Risk Control (Mitigation)
    [06-urra-in-medical-devices-0065] slide:12:p:10 | Evaluation Method
    [06-urra-in-medical-devices-0066] slide:12:p:11 | 1
    [06-urra-in-medical-devices-0067] slide:12:p:12 | Read blood glucose from display
    [06-urra-in-medical-devices-0068] slide:12:p:13 | Incorrectly identifies BG value
    [06-urra-in-medical-devices-0069] slide:12:p:14 | Incorrect insulin dose leading to coma or death
    [06-urra-in-medical-devices-0070] slide:12:p:15 | 5
    [06-urra-in-medical-devices-0071] slide:12:p:16 | Y
    [06-urra-in-medical-devices-0072] slide:12:p:17 | Increase font size
    [06-urra-in-medical-devices-0073] slide:12:p:18 | usability study
    [06-urra-in-medical-devices-0074] slide:12:p:19 | Is font change an adequate control?
    [06-urra-in-medical-devices-0075] slide:13:p:1 | 13
    [06-urra-in-medical-devices-0076] slide:13:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0077] slide:13:p:3 | Reference number
    [06-urra-in-medical-devices-0078] slide:13:p:4 | Task description
    [06-urra-in-medical-devices-0079] slide:13:p:5 | Potential use errors
    [06-urra-in-medical-devices-0080] slide:13:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0081] slide:13:p:7 | Severity of harm
    [06-urra-in-medical-devices-0082] slide:13:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0083] slide:13:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0084] slide:13:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0085] slide:13:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0086] slide:14:p:1 | 14
    [06-urra-in-medical-devices-0087] slide:14:p:2 | Using straight sequential numbers can cause challenges in risk management documents if additional tasks, use steps, or features are added to a device
    [06-urra-in-medical-devices-0088] slide:14:p:3 | Companies often use various coding schema to mitigate
    [06-urra-in-medical-devices-0089] slide:14:p:4 | For example: Task AB 1.0.0
    [06-urra-in-medical-devices-0090] slide:14:p:5 | Note: FDA refers to this as Task Number in their guidance, I recommend calling it URRA # (or some other signifier) to avoid confusion with HF validation task numbers.
    [06-urra-in-medical-devices-0091] slide:14:p:6 | Reference number
    [06-urra-in-medical-devices-0092] slide:15:p:1 | 15
    [06-urra-in-medical-devices-0093] slide:15:p:2 | Imagine adding another task after task #1
    [06-urra-in-medical-devices-0094] slide:15:p:3 | Ref #
    [06-urra-in-medical-devices-0095] slide:15:p:4 | Use Task Description
    [06-urra-in-medical-devices-0096] slide:15:p:5 | Potential Use Error
    [06-urra-in-medical-devices-0097] slide:15:p:6 | Potential Hazard/Clinical Harm
    [06-urra-in-medical-devices-0098] slide:15:p:7 | Severity of Harm
    [06-urra-in-medical-devices-0099] slide:15:p:8 | Critical Task (Y/N)
    [06-urra-in-medical-devices-0100] slide:15:p:9 | Risk Control (Mitigation)
    [06-urra-in-medical-devices-0101] slide:15:p:10 | Evaluation Method
    [06-urra-in-medical-devices-0102] slide:15:p:11 | 1
    [06-urra-in-medical-devices-0103] slide:15:p:12 | Task
    [06-urra-in-medical-devices-0104] slide:15:p:13 | Error description
    [06-urra-in-medical-devices-0105] slide:15:p:14 | Infection
    [06-urra-in-medical-devices-0106] slide:15:p:15 | 4
    [06-urra-in-medical-devices-0107] slide:15:p:16 | Y
    [06-urra-in-medical-devices-0108] slide:15:p:17 | Control description
    [06-urra-in-medical-devices-0109] slide:15:p:18 | usability study
    [06-urra-in-medical-devices-0110] slide:15:p:19 | 2
    [06-urra-in-medical-devices-0111] slide:15:p:20 | Task that follows
    [06-urra-in-medical-devices-0112] slide:15:p:21 | Error description
    [06-urra-in-medical-devices-0113] slide:15:p:22 | Death
    [06-urra-in-medical-devices-0114] slide:15:p:23 | 5
    [06-urra-in-medical-devices-0115] slide:15:p:24 | Y
    [06-urra-in-medical-devices-0116] slide:15:p:25 | Control description
    [06-urra-in-medical-devices-0117] slide:15:p:26 | usability study
    [06-urra-in-medical-devices-0118] slide:15:p:27 | 3
    [06-urra-in-medical-devices-0119] slide:15:p:28 | Task that follows
    [06-urra-in-medical-devices-0120] slide:15:p:29 | Error description
    [06-urra-in-medical-devices-0121] slide:15:p:30 | Delay of treatment
    [06-urra-in-medical-devices-0122] slide:15:p:31 | 2
    [06-urra-in-medical-devices-0123] slide:15:p:32 | N
    [06-urra-in-medical-devices-0124] slide:15:p:33 | Control description
    [06-urra-in-medical-devices-0125] slide:15:p:34 | usability study
    [06-urra-in-medical-devices-0126] slide:15:p:35 | Ref #
    [06-urra-in-medical-devices-0127] slide:15:p:36 | Use Task Description
    [06-urra-in-medical-devices-0128] slide:15:p:37 | Potential Use Error
    [06-urra-in-medical-devices-0129] slide:15:p:38 | Potential Hazard/Clinical Harm
    [06-urra-in-medical-devices-0130] slide:15:p:39 | Severity of Harm
    [06-urra-in-medical-devices-0131] slide:15:p:40 | Critical Task (Y/N)
    [06-urra-in-medical-devices-0132] slide:15:p:41 | Risk Control (Mitigation)
    [06-urra-in-medical-devices-0133] slide:15:p:42 | Evaluation Method
    [06-urra-in-medical-devices-0134] slide:15:p:43 | 1.0
    [06-urra-in-medical-devices-0135] slide:15:p:44 | Task
    [06-urra-in-medical-devices-0136] slide:15:p:45 | Error description
    [06-urra-in-medical-devices-0137] slide:15:p:46 | Infection
    [06-urra-in-medical-devices-0138] slide:15:p:47 | 4
    [06-urra-in-medical-devices-0139] slide:15:p:48 | Y
    [06-urra-in-medical-devices-0140] slide:15:p:49 | Control description
    [06-urra-in-medical-devices-0141] slide:15:p:50 | usability study
    [06-urra-in-medical-devices-0142] slide:15:p:51 | 1.1
    [06-urra-in-medical-devices-0143] slide:15:p:52 | Task inserted
    [06-urra-in-medical-devices-0144] slide:15:p:53 | Error description
    [06-urra-in-medical-devices-0145] slide:15:p:54 | Paralysis
    [06-urra-in-medical-devices-0146] slide:15:p:55 | 5
    [06-urra-in-medical-devices-0147] slide:15:p:56 | Y
    [06-urra-in-medical-devices-0148] slide:15:p:57 | Control description
    [06-urra-in-medical-devices-0149] slide:15:p:58 | Usability study
    [06-urra-in-medical-devices-0150] slide:15:p:59 | 2.0
    [06-urra-in-medical-devices-0151] slide:15:p:60 | Task that follows
    [06-urra-in-medical-devices-0152] slide:15:p:61 | Error description
    [06-urra-in-medical-devices-0153] slide:15:p:62 | Death
    [06-urra-in-medical-devices-0154] slide:15:p:63 | 5
    [06-urra-in-medical-devices-0155] slide:15:p:64 | Y
    [06-urra-in-medical-devices-0156] slide:15:p:65 | Control description
    [06-urra-in-medical-devices-0157] slide:15:p:66 | usability study
    [06-urra-in-medical-devices-0158] slide:15:p:67 | 3.0
    [06-urra-in-medical-devices-0159] slide:15:p:68 | Task that follows
    [06-urra-in-medical-devices-0160] slide:15:p:69 | Error description
    [06-urra-in-medical-devices-0161] slide:15:p:70 | Delay of treatment
    [06-urra-in-medical-devices-0162] slide:15:p:71 | 2
    [06-urra-in-medical-devices-0163] slide:15:p:72 | N
    [06-urra-in-medical-devices-0164] slide:15:p:73 | Control description
    [06-urra-in-medical-devices-0165] slide:15:p:74 | usability study
    [06-urra-in-medical-devices-0166] slide:16:p:1 | 16
    [06-urra-in-medical-devices-0167] slide:16:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0168] slide:16:p:3 | Reference number
    [06-urra-in-medical-devices-0169] slide:16:p:4 | Task description
    [06-urra-in-medical-devices-0170] slide:16:p:5 | Potential use errors
    [06-urra-in-medical-devices-0171] slide:16:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0172] slide:16:p:7 | Severity of harm
    [06-urra-in-medical-devices-0173] slide:16:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0174] slide:16:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0175] slide:16:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0176] slide:16:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0177] slide:17:p:1 | 17
    [06-urra-in-medical-devices-0178] slide:17:p:2 | A short description of the specific action or goal that is required to be achieved by the user
    [06-urra-in-medical-devices-0179] slide:17:p:3 | Forms the basis for evaluating potential use errors
    [06-urra-in-medical-devices-0180] slide:17:p:4 | Terms you might also use:
    [06-urra-in-medical-devices-0181] slide:17:p:5 | Sub-task: Break down the broader task into its component actions. They are the smaller individual actions that collectively make up a task.
    [06-urra-in-medical-devices-0182] slide:17:p:6 | Use-step: Detailed, step-by-step actions or interactions that the user takes with the device. They are finer-grained than subtasks and provide explicit instructions or sequences.
    [06-urra-in-medical-devices-0183] slide:17:p:7 | Task description
    [06-urra-in-medical-devices-0184] slide:18:p:1 | 18
    [06-urra-in-medical-devices-0185] slide:18:p:2 | Device: Infusion pump
    [06-urra-in-medical-devices-0186] slide:18:p:3 | Task: Deliver medication to patient
    [06-urra-in-medical-devices-0187] slide:18:p:4 | Sub-tasks:
    [06-urra-in-medical-devices-0188] slide:18:p:5 | Select the correct drug from the pump’s on-screen menu
    [06-urra-in-medical-devices-0189] slide:18:p:6 | Set the appropriate dosage
    [06-urra-in-medical-devices-0190] slide:18:p:7 | Set infusion rate
    [06-urra-in-medical-devices-0191] slide:18:p:8 | Start infusion
    [06-urra-in-medical-devices-0192] slide:18:p:9 | Use steps for sub-task 2 above:
    [06-urra-in-medical-devices-0193] slide:18:p:10 | Press the Menu button on home screen
    [06-urra-in-medical-devices-0194] slide:18:p:11 | Press Dosage Settings
    [06-urra-in-medical-devices-0195] slide:18:p:12 | Enter the prescribed dose amount using keypad
    [06-urra-in-medical-devices-0196] slide:18:p:13 | Press Enter
    [06-urra-in-medical-devices-0197] slide:18:p:14 | Task - Example # 1
    [06-urra-in-medical-devices-0198] slide:19:p:1 | 19
    [06-urra-in-medical-devices-0199] slide:19:p:2 | Device: Pen-injector
    [06-urra-in-medical-devices-0200] slide:19:p:3 | Task: Inject medication to self
    [06-urra-in-medical-devices-0201] slide:19:p:4 | Sub-tasks:
    [06-urra-in-medical-devices-0202] slide:19:p:5 | Inspect drug for expiration
    [06-urra-in-medical-devices-0203] slide:19:p:6 | Dial dose to correct amount
    [06-urra-in-medical-devices-0204] slide:19:p:7 | Inject into correct location on skin
    [06-urra-in-medical-devices-0205] slide:19:p:8 | Press knob till fully depressed
    [06-urra-in-medical-devices-0206] slide:19:p:9 | Hold for 5 seconds
    [06-urra-in-medical-devices-0207] slide:19:p:10 | Use steps for sub-task 1 above:
    [06-urra-in-medical-devices-0208] slide:19:p:11 | Is there any more granularity needed than the above?
    [06-urra-in-medical-devices-0209] slide:19:p:12 | Task - Example # 2
    [06-urra-in-medical-devices-0210] slide:19:p:13 | Wait, should this be a task?
    [06-urra-in-medical-devices-0211] slide:19:p:14 | There often isn’t one “right” way of defining tasks vs subtasks vs use-steps, often requires judgement.
    [06-urra-in-medical-devices-0212] slide:19:p:15 | What’s important is that your analysis is comprehensive and consistent
    [06-urra-in-medical-devices-0213] slide:20:p:1 | 20
    [06-urra-in-medical-devices-0214] slide:20:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0215] slide:20:p:3 | Reference number
    [06-urra-in-medical-devices-0216] slide:20:p:4 | Task description
    [06-urra-in-medical-devices-0217] slide:20:p:5 | Potential use errors
    [06-urra-in-medical-devices-0218] slide:20:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0219] slide:20:p:7 | Severity of harm
    [06-urra-in-medical-devices-0220] slide:20:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0221] slide:20:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0222] slide:20:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0223] slide:20:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0224] slide:21:p:1 | 21
    [06-urra-in-medical-devices-0225] slide:21:p:2 | FDA definition: User action or lack of action that was different from that expected by the manufacturer and caused a result that:
    [06-urra-in-medical-devices-0226] slide:21:p:3 | (1) was different from the result expected by the user and
    [06-urra-in-medical-devices-0227] slide:21:p:4 | (2) was not caused solely by device failure and
    [06-urra-in-medical-devices-0228] slide:21:p:5 | (3) did or could result in harm
    [06-urra-in-medical-devices-0229] slide:21:p:6 | Potential use errors
    [06-urra-in-medical-devices-0230] slide:22:p:1 | 22
    [06-urra-in-medical-devices-0231] slide:22:p:2 | Identifying potential use errors?
    [06-urra-in-medical-devices-0232] slide:23:p:1 | 23
    [06-urra-in-medical-devices-0233] slide:23:p:2 | Product: Surgical Suction Device
    [06-urra-in-medical-devices-0234] slide:23:p:3 | Task: Connect hose to canister
    [06-urra-in-medical-devices-0235] slide:23:p:4 | Task Analysis:
    [06-urra-in-medical-devices-0236] slide:23:p:5 | Sub-task 1: Select correct hose
    [06-urra-in-medical-devices-0237] slide:23:p:6 | Potential use errors:
    [06-urra-in-medical-devices-0238] slide:23:p:7 | User selects wrong hose
    [06-urra-in-medical-devices-0239] slide:23:p:8 | Sub-task 2: Slide blue tip of hose onto canister’s inflow connector completely
    [06-urra-in-medical-devices-0240] slide:23:p:9 | Potential use errors:
    [06-urra-in-medical-devices-0241] slide:23:p:10 | Does not attach hose at all
    [06-urra-in-medical-devices-0242] slide:23:p:11 | User does not fully slide hose onto connector (poor connection)
    [06-urra-in-medical-devices-0243] slide:23:p:12 | User attaches hose to canister’s outflow connector
    [06-urra-in-medical-devices-0244] slide:23:p:13 | Example
    [06-urra-in-medical-devices-0245] slide:24:p:1 | 24
    [06-urra-in-medical-devices-0246] slide:24:p:2 | Product: Surgical Suction Device
    [06-urra-in-medical-devices-0247] slide:24:p:3 | Task: Connect hose to canister
    [06-urra-in-medical-devices-0248] slide:24:p:4 | BUT from post market surveillance data:
    [06-urra-in-medical-devices-0249] slide:24:p:5 | A case where a tech rubbed lubricant  onto the connecter to make it easier to connect hose  led to hose being pulled off during surgery
    [06-urra-in-medical-devices-0250] slide:24:p:6 | Use error: User lubricates connectors
    [06-urra-in-medical-devices-0251] slide:24:p:7 | Example
    [06-urra-in-medical-devices-0252] slide:25:p:1 | 25
    [06-urra-in-medical-devices-0253] slide:25:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0254] slide:25:p:3 | Reference number
    [06-urra-in-medical-devices-0255] slide:25:p:4 | Task description
    [06-urra-in-medical-devices-0256] slide:25:p:5 | Potential use errors
    [06-urra-in-medical-devices-0257] slide:25:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0258] slide:25:p:7 | Severity of harm
    [06-urra-in-medical-devices-0259] slide:25:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0260] slide:25:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0261] slide:25:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0262] slide:25:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0263] slide:26:p:1 | 26
    [06-urra-in-medical-devices-0264] slide:26:p:2 | Task: Removing cap from pre-filled syringe
    [06-urra-in-medical-devices-0265] slide:26:p:3 | Hazard: Needle
    [06-urra-in-medical-devices-0266] slide:26:p:4 | Hazardous situation: Uncapped needle
    [06-urra-in-medical-devices-0267] slide:26:p:5 | Harm: Needlestick
    [06-urra-in-medical-devices-0268] slide:26:p:6 | Task: Cleaning reusable surgical equipment
    [06-urra-in-medical-devices-0269] slide:26:p:7 | Hazard: Pathogens
    [06-urra-in-medical-devices-0270] slide:26:p:8 | Hazardous situation: Incomplete surgical equipment disinfection
    [06-urra-in-medical-devices-0271] slide:26:p:9 | Harm: Infection
    [06-urra-in-medical-devices-0272] slide:26:p:10 | Task: Configuring ventilator
    [06-urra-in-medical-devices-0273] slide:26:p:11 | Hazard: Oxygen
    [06-urra-in-medical-devices-0274] slide:26:p:12 | Hazardous situation: Ventilator provides too much oxygen
    [06-urra-in-medical-devices-0275] slide:26:p:13 | Harm: Hyperoxia (oxygen toxicity)
    [06-urra-in-medical-devices-0276] slide:26:p:14 | Potential hazards and harms
    [06-urra-in-medical-devices-0277] slide:27:p:1 | 27
    [06-urra-in-medical-devices-0278] slide:27:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0279] slide:27:p:3 | Reference number
    [06-urra-in-medical-devices-0280] slide:27:p:4 | Task description
    [06-urra-in-medical-devices-0281] slide:27:p:5 | Potential use errors
    [06-urra-in-medical-devices-0282] slide:27:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0283] slide:27:p:7 | Severity of harm
    [06-urra-in-medical-devices-0284] slide:27:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0285] slide:27:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0286] slide:27:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0287] slide:27:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0288] slide:28:p:1 | 28
    [06-urra-in-medical-devices-0289] slide:28:p:2 | Potential degree of injury or negative health impact
    [06-urra-in-medical-devices-0290] slide:28:p:3 | Typically graded on a numerical scale on a 1-5 scale
    [06-urra-in-medical-devices-0291] slide:28:p:4 | Common example:
    [06-urra-in-medical-devices-0292] slide:28:p:5 | Severity 1 - Negligible: No injury or only a slight inconvenience.
    [06-urra-in-medical-devices-0293] slide:28:p:6 | Severity 2 - Minor: Temporary injury or impairment, not requiring professional medical intervention.
    [06-urra-in-medical-devices-0294] slide:28:p:7 | Severity 3 - Moderate: Temporary injury or impairment requiring professional medical intervention.
    [06-urra-in-medical-devices-0295] slide:28:p:8 | Severity 4 - Severe: Permanent impairment or injury that has a substantial impact on the patient's life.
    [06-urra-in-medical-devices-0296] slide:28:p:9 | Severity 5 - Catastrophic: Death or an injury leading to a long-term or permanent severe decrease in the patient's quality of life.
    [06-urra-in-medical-devices-0297] slide:28:p:10 | Severity of harm
    [06-urra-in-medical-devices-0298] slide:29:p:1 | 29
    [06-urra-in-medical-devices-0299] slide:29:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0300] slide:29:p:3 | Reference number
    [06-urra-in-medical-devices-0301] slide:29:p:4 | Task description
    [06-urra-in-medical-devices-0302] slide:29:p:5 | Potential use errors
    [06-urra-in-medical-devices-0303] slide:29:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0304] slide:29:p:7 | Severity of harm
    [06-urra-in-medical-devices-0305] slide:29:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0306] slide:29:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0307] slide:29:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0308] slide:29:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0309] slide:30:p:1 | 30
    [06-urra-in-medical-devices-0310] slide:30:p:2 | A user task that, if performed incorrectly or not performed at all, could lead to [serious  / any] harm
    [06-urra-in-medical-devices-0311] slide:30:p:3 | Examples:
    [06-urra-in-medical-devices-0312] slide:30:p:4 | Infusion pump, a critical task might be setting the correct drug dosage.
    [06-urra-in-medical-devices-0313] slide:30:p:5 | Defibrillator, a critical task might be correctly placing the electrode pads.
    [06-urra-in-medical-devices-0314] slide:30:p:6 | Typically, the focus of design, formative, and validation testing
    [06-urra-in-medical-devices-0315] slide:30:p:7 | Regulators require documentation that demonstrates how critical tasks were identified, evaluated, and tested to ensure the safe use of the device.
    [06-urra-in-medical-devices-0316] slide:30:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0317] slide:31:p:1 | 31
    [06-urra-in-medical-devices-0318] slide:31:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0319] slide:31:p:3 | Reference number
    [06-urra-in-medical-devices-0320] slide:31:p:4 | Task description
    [06-urra-in-medical-devices-0321] slide:31:p:5 | Potential use errors
    [06-urra-in-medical-devices-0322] slide:31:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0323] slide:31:p:7 | Severity of harm
    [06-urra-in-medical-devices-0324] slide:31:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0325] slide:31:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0326] slide:31:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0327] slide:31:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0328] slide:32:p:1 | 32
    [06-urra-in-medical-devices-0329] slide:32:p:2 | Preferred Risk Control Strategy: Inherent Safety by Design
    [06-urra-in-medical-devices-0330] slide:32:p:3 | Design device such that a hazard is eliminated
    [06-urra-in-medical-devices-0331] slide:32:p:4 | Example: Design a device for single use and distribute it sterilized in the package so that infection related to contamination cannot occur.
    [06-urra-in-medical-devices-0332] slide:32:p:5 | Less Preferred Risk Control Strategy: Protective Measures
    [06-urra-in-medical-devices-0333] slide:32:p:6 | Reduce risk by incorporating protective measures that reduce the probability of occurrence of a hazardous situation.
    [06-urra-in-medical-devices-0334] slide:32:p:7 | Example: Sound an alarm when a device is about to deliver radiation therapy
    [06-urra-in-medical-devices-0335] slide:32:p:8 | Least Preferred Risk Control Strategy: Information for Safety
    [06-urra-in-medical-devices-0336] slide:32:p:9 | Provide information for safety in instructions for use and warnings.
    [06-urra-in-medical-devices-0337] slide:32:p:10 | Example: A diagnostic device label states “do not use in a moving vehicle”
    [06-urra-in-medical-devices-0338] slide:32:p:11 | Example: The manual states “always unplug before cleaning”
    [06-urra-in-medical-devices-0339] slide:32:p:12 | Risk mitigation (or controls)
    [06-urra-in-medical-devices-0340] slide:33:p:1 | 33
    [06-urra-in-medical-devices-0341] slide:33:p:2 | Task: Removing cap from pre-filled syringe
    [06-urra-in-medical-devices-0342] slide:33:p:3 | Hazard: Needle
    [06-urra-in-medical-devices-0343] slide:33:p:4 | Harm: Infection
    [06-urra-in-medical-devices-0344] slide:33:p:5 | Potential controls:
    [06-urra-in-medical-devices-0345] slide:33:p:6 | Improved package formatting/labeling (good)
    [06-urra-in-medical-devices-0346] slide:33:p:7 | Needle guard (better)
    [06-urra-in-medical-devices-0347] slide:33:p:8 | Needle only presents at injection (best)
    [06-urra-in-medical-devices-0348] slide:33:p:9 | Risk mitigation (or controls)
    [06-urra-in-medical-devices-0349] slide:34:p:1 | 34
    [06-urra-in-medical-devices-0350] slide:34:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0351] slide:34:p:3 | Reference number
    [06-urra-in-medical-devices-0352] slide:34:p:4 | Task description
    [06-urra-in-medical-devices-0353] slide:34:p:5 | Potential use errors
    [06-urra-in-medical-devices-0354] slide:34:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0355] slide:34:p:7 | Severity of harm
    [06-urra-in-medical-devices-0356] slide:34:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0357] slide:34:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0358] slide:34:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0359] slide:34:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0360] slide:35:p:1 | 35
    [06-urra-in-medical-devices-0361] slide:35:p:2 | Simply a pointer to where the risk controls were validated as effective
    [06-urra-in-medical-devices-0362] slide:35:p:3 | Typically, a task # in a simulated-use validation study, a knowledge question #, or other acceptable source
    [06-urra-in-medical-devices-0363] slide:35:p:4 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0364] slide:36:p:1 | 36
    [06-urra-in-medical-devices-0365] slide:36:p:2 | A URRA needs to contain the following:
    [06-urra-in-medical-devices-0366] slide:36:p:3 | Reference number
    [06-urra-in-medical-devices-0367] slide:36:p:4 | Task description
    [06-urra-in-medical-devices-0368] slide:36:p:5 | Potential use errors
    [06-urra-in-medical-devices-0369] slide:36:p:6 | Potential hazards and harms
    [06-urra-in-medical-devices-0370] slide:36:p:7 | Severity of harm
    [06-urra-in-medical-devices-0371] slide:36:p:8 | Critical task (yes or no)
    [06-urra-in-medical-devices-0372] slide:36:p:9 | Risk mitigations
    [06-urra-in-medical-devices-0373] slide:36:p:10 | Reference to validation of risk mitigation effectiveness
    [06-urra-in-medical-devices-0374] slide:36:p:11 | URRA document decomposed
    [06-urra-in-medical-devices-0375] slide:37:p:1 | 37
    [06-urra-in-medical-devices-0376] slide:37:p:2 | According to 14971: Risk = probability of occurrence x severity of harm
    [06-urra-in-medical-devices-0377] slide:37:p:3 | FDA's stance: "probability is very difficult to determine for use errors, and in fact many use errors cannot be anticipated until device use is simulated and observed, the severity of the potential harm is more meaningful for determining the need to eliminate (design out) or reduce resulting harm"
    [06-urra-in-medical-devices-0378] slide:37:p:4 | Wait! - What about the frequency, Kenneth?
    [06-urra-in-medical-devices-0379] slide:37:p:5 | (i.e., probability)
    [06-urra-in-medical-devices-0380] slide:38:p:1 | 38
    [06-urra-in-medical-devices-0381] slide:38:p:2 | Simply a collection of tools (e.g., task analysis)
    [06-urra-in-medical-devices-0382] slide:38:p:3 | A formula that will make decisions for you
    [06-urra-in-medical-devices-0383] slide:38:p:4 | A one-time activity
    [06-urra-in-medical-devices-0384] slide:38:p:5 | Something to do at the end of the design process / for submission documentation only
    [06-urra-in-medical-devices-0385] slide:38:p:6 | Use related risk analysis is not…
    [06-urra-in-medical-devices-0386] notes:1:p:1 | Quick introductions
    [06-urra-in-medical-devices-0387] notes:2:p:1 | Sami
    [06-urra-in-medical-devices-0388] notes:2:p:2 | Medical devices encompass a wide range of equipment, instruments, implants, or software used in healthcare for diagnosis, treatment, monitoring, or prevention of diseases. They play a crucial role in modern medicine.
    [06-urra-in-medical-devices-0389] notes:2:p:3 | They help improve patient outcomes, enhance the efficiency of healthcare delivery, and contribute to the overall quality of care. They are used across various medical specialties, from diagnostics to life support.
    [06-urra-in-medical-devices-0390] notes:2:p:4 | Here are some examples of medical devices, and you can see that they can range from something as “simple” (in air quotes) as drug deliver devices like an insulin pen or an inhaler to complex machines like a home dialysis machine to a robotic surgical system.
    [06-urra-in-medical-devices-0391] notes:3:p:1 | Sami: FDA has a great presentation available on their website
    [06-urra-in-medical-devices-0392] notes:3:p:2 | A medical device, according to the FDA, is a tool or apparatus intended for diagnosing, treating, or preventing disease, not primarily functioning through chemical action in the body.
    [06-urra-in-medical-devices-0393] notes:3:p:3 | Defining medical devices can be tricky, FDA has a great presentation on this that we can review together quickly.
    [06-urra-in-medical-devices-0394] notes:4:p:1 | Eric
    [06-urra-in-medical-devices-0395] notes:4:p:2 | Can also use this slide as a bridge to the next one about guidance and standards
    [06-urra-in-medical-devices-0396] notes:4:p:3 | 4
    [06-urra-in-medical-devices-0397] notes:5:p:1 | In descending order.
    [06-urra-in-medical-devices-0398] notes:5:p:2 | Key concept: we do not blame the user for making errors. Use errors are a function of the device design
    [06-urra-in-medical-devices-0399] notes:6:p:1 | "Humans are flawed in that we have limitations, imperfections, or tendencies in human behavior, cognition, and decision-making that can lead to errors, mistakes, or suboptimal outcomes. These flaws are a natural part of being human.
    [06-urra-in-medical-devices-0400] notes:7:p:1 | Sami: What are the bodies and standards that govern how we assess use related risk in medical device design.
    [06-urra-in-medical-devices-0401] notes:7:p:2 | Covered extensively in other classes – insert class name.
    [06-urra-in-medical-devices-0402] notes:7:p:3 | So why is this important? Essentially, medical device development is a risk based approach. What the FDA and most other regulators want to see is that your device is “safe and effective”. What does that mean? It means that people can use it to deliver the therapeutic value, and they can use it safely.
    [06-urra-in-medical-devices-0403] notes:7:p:4 | 7
    [06-urra-in-medical-devices-0404] notes:8:p:1 | 8
    [06-urra-in-medical-devices-0405] notes:9:p:1 | Again, as mentioned in the previous slide there are different ways to implement steps in this process – they may have slightly different names or formats, but fundamentally will have to address to process steps defined in the diagram above.
    [06-urra-in-medical-devices-0406] notes:9:p:2 | (e.g., uFMEA, Task Analysis, FTA, etc0
    [06-urra-in-medical-devices-0407] notes:10:p:1 | This is perhaps one of the most confusing aspects of human factors in risk analysis.
    [06-urra-in-medical-devices-0408] notes:10:p:2 | Important to note that URRA is a “term of art” – there are many approaches and formats to creating a URRA.
    [06-urra-in-medical-devices-0409] notes:10:p:3 | In fact, many companies don’t even have a document with the name “URRA”, but they have a document (and associated process) that serves this purpose (use related risk analysis).
    [06-urra-in-medical-devices-0410] notes:11:p:1 | Highlight briefly and mention that we will speak to URRA in more detail in slides ahead
    [06-urra-in-medical-devices-0411] notes:11:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0412] notes:11:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0413] notes:11:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0414] notes:11:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0415] notes:11:p:6 | Let’s discuss this in detail:
    [06-urra-in-medical-devices-0416] notes:13:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0417] notes:13:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0418] notes:13:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0419] notes:13:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0420] notes:13:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0421] notes:13:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0422] notes:15:p:1 | It is common to identify additional tasks during the human factors engineering process, or to realize that a task could be decomposed into several tasks. For this reason, the reference numbers must evolve/scale over time.
    [06-urra-in-medical-devices-0423] notes:15:p:2 | Let’s consider one way to reference tasks instead of an integer sequence…
    [06-urra-in-medical-devices-0424] notes:16:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0425] notes:16:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0426] notes:16:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0427] notes:16:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0428] notes:16:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0429] notes:16:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0430] notes:20:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0431] notes:20:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0432] notes:20:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0433] notes:20:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0434] notes:20:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0435] notes:20:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0436] notes:22:p:1 | When you write this up in an actual excel, you might call this sub task, instead of calling them step
    [06-urra-in-medical-devices-0437] notes:23:p:1 | When you write this up in an actual excel, you might call this sub task, instead of calling them step
    [06-urra-in-medical-devices-0438] notes:24:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0439] notes:24:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0440] notes:24:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0441] notes:24:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0442] notes:24:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0443] notes:24:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0444] notes:26:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0445] notes:26:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0446] notes:26:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0447] notes:26:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0448] notes:26:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0449] notes:26:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0450] notes:27:p:1 | Requires medical profession to assess.
    [06-urra-in-medical-devices-0451] notes:27:p:2 | Speak to cross-functional nature of URRA.
    [06-urra-in-medical-devices-0452] notes:28:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0453] notes:28:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0454] notes:28:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0455] notes:28:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0456] notes:28:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0457] notes:28:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0458] notes:29:p:1 | Critical tasks are especially significant because they directly impact the safety and effectiveness of a medical device.
    [06-urra-in-medical-devices-0459] notes:29:p:2 | Identifying and thoroughly evaluating critical tasks during the device design and testing process ensures that potential use-related hazards are addressed.
    [06-urra-in-medical-devices-0460] notes:30:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0461] notes:30:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0462] notes:30:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0463] notes:30:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0464] notes:30:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0465] notes:30:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0466] notes:32:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0467] notes:32:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0468] notes:32:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0469] notes:32:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0470] notes:32:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0471] notes:32:p:6 | Lets discuss this in detail:
    [06-urra-in-medical-devices-0472] notes:34:p:1 | Highlight briefly and mention that we will speak to in more detail
    [06-urra-in-medical-devices-0473] notes:34:p:2 | Task vs use step or sub-task vs scenario
    [06-urra-in-medical-devices-0474] notes:34:p:3 | Probabilities are not included
    [06-urra-in-medical-devices-0475] notes:34:p:4 | What is a critical task?
    [06-urra-in-medical-devices-0476] notes:34:p:5 | What are risk mitigations (also referred to as risk controls by some)
    [06-urra-in-medical-devices-0477] notes:34:p:6 | Lets discuss this in detail:
    ```
