# URRA Methods

URRA is not merely a table format. It is a full risk chain that links task steps, use errors, hazardous situations, harms, and controls in one structure.

!!! note "Core Question"
    How does Use-Related Risk Analysis connect tasks,
    errors,
    hazards,
    and controls into a chain that is traceable,
    verifiable,
    and reviewable?

## Key Takeaways

- The central job of URRA is linking use step,
  use error,
  hazardous situation,
  harm,
  and control in one chain.
- The writing order must keep task and scenario first,
  error and consequence next,
  and controls last.
- A strong URRA is specific enough to support validation work directly.
- A weak URRA uses vague language and supports neither real risk understanding nor later testing.

## What This Method Is For

!!! tip "Start with the Purpose"
    Remember the purpose of URRA this way:
    it is not about putting risk into a table,
    but about writing the risk path clearly enough to support design and validation.

## What Problem This Method Solves

URRA solves the problem of risk information being scattered across documents.
It places the use flow,
possible errors,
hazardous situations,
harms,
and controls in one chain so the team can see how risk develops step by step.

## What the Inputs and Outputs Are

Typical URRA inputs come from:

- task analysis
- user and use-environment assumptions
- known use errors or complaint history
- design features, labeling, IFU, and training plans

The output is a set of traceable rows that answer:

- where error may occur
- what hazardous situation follows
- what harm may result
- whether current controls are sufficient

## How the Method Proceeds

The order matters a lot when writing URRA:

1. start from the task and use scenario
2. write the specific use error rather than a vague label like “improper use”
3. push the error forward into hazardous situation and harm
4.
only then assess whether current controls are sufficient and what more is needed

!!! note "One-Sentence Conclusion"
    If controls are written first,
    URRA becomes design justification.
    If the risk chain is written first,
    URRA behaves like real risk analysis.

!!! warning "The Most Common Failure Mode"
    Two failures appear constantly:
    writing the error too vaguely,
    such as “misuse,” and stopping the harm too early,
    such as writing only “wrong dose” without the patient consequence.

!!! example "Worked Example: What One Strong URRA Row Looks Like"
    Suppose the step is “set dose.” A strong URRA row does not stop at “possible user error.” It says the user reads 1.0 mL as 10 mL,
    leading to an overdose hazardous situation and harm such as hypoglycemia or more severe injury;
    only then does it return to dose-window design,
    visual differentiation,
    confirmation steps,
    and validation testing.

## How It Connects to Earlier and Later Methods

Task analysis provides the task skeleton for URRA;
the medical-device pages place the same logic inside a regulatory context;
the EpiPen workbook shows what a concrete URRA row looks like in practice.

## Why URRA Fails When It Stays at a Vague Level

Once URRA is written in vague labels such as “misuse,” “incorrect use,” or “possible injury,” nearly every later column loses focus.
The team can no longer see which step is failing,
what specific error is happening,
or which harm path is in play,
so controls also become vague.

Strong URRA rows therefore stay concrete:
concrete scenario,
concrete action,
concrete misjudgment,
concrete consequence,
and concrete control.
At that level,
validation scenarios and risk communication can emerge naturally from the analysis.

## Why URRA Ultimately Has to Feed Validation

The course does not treat URRA as archive management.
It treats it as an interface between design and validation.
The reason is simple:
once a risk chain has been written,
the team must be able to answer how it will demonstrate that the control is actually effective.

That means URRA is not finished when the row is written.
It should continue to drive:

- which controls must appear in prototype or final design
- which critical tasks need focused observation in validation
- which scenarios need to be reproduced with representative users under representative conditions

!!! warning "Another Common Failure"
    Some teams produce URRA tables that look complete but do not yield a single usable validation scenario.
    That usually means the entries are still too vague or the controls are written at too abstract a level.

## Chapter Summary

!!! tip "What To Carry Forward"
    - URRA is about clarifying the risk chain,
      not about filling a table for its own sake.
    - Its inputs come from task flow,
      user context,
      and known problems.
    - The writing order must stay task/error/consequence/control rather than reversing that logic.
    - The more specific the URRA,
      the stronger the later validation work becomes.


## Source Scope and Related Topics

The teaching notes come first. This section lists the source files used on the page, and the appendix keeps the full line-by-line transcription for verification.

- Section: `Risk Methods`
- Source files: 1
- Text units: 52
- Visuals/previews: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `10 Write URRA.pptx` | `pptx` | 52 | 3 | [open](../assets/source_files/ENP_111_Use_related_Risks/10 Write URRA.pptx) |

## Related Topics

- [Task Analysis](task_analysis.en.md)
- [URRA in Medical Devices](../HFE_Medical_Devices/medical_device_urra.en.md)
- [The EpiPen URRA Workbook](../HFE_Medical_Devices/epipen_workbook.en.md)

## Original Transcription and Coverage Mapping

The collapsible blocks below preserve page/slide-level source transcription. Each `unit_id` maps one-to-one in `data/coverage_map.json`.

??? info "10 Write URRA.pptx | 52 text units"
    Download source: [10 Write URRA.pptx](../assets/source_files/ENP_111_Use_related_Risks/10 Write URRA.pptx)
    Mapped page: `urra_methods`
    
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
