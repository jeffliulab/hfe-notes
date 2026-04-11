# Known Problem Analysis and Event Trees

This page pairs two gap-finding methods: Known Problem Analysis looks backward to historical issues, while Event Tree analysis looks forward from an initiating event into downstream consequence branches.

!!! note "Core Question"
    Once the main workflow analysis is complete,
    how does the team continue asking what historical issues and downstream consequence branches may still be missing?

## Key Takeaways

- Known Problem Analysis prevents the team from rediscovering old failure modes too late.
- Event Trees prevent the team from underestimating the downstream branches of an initiating event.
- Together they expand the view from the main path to edge paths and missed risk.
- These methods are not administrative extras;
  they are deliberate blind-spot checks.

## What This Method Is For

!!! tip "Start with the Purpose"
    Remember the role of these methods this way:
    main workflow analysis clarifies the main path,
    while Known Problem Analysis and Event Trees protect against forgetting the edges and branches of the system.

## What Each Method Adds

`Known Problem Analysis` captures what the team may already know through complaints,
incidents,
CAPA records,
literature,
or competitor history.

`Event Tree` expands what happens after an initiating event:
if one barrier fails,
what branches follow,
and which nodes function as real defenses?

!!! warning "The Most Common Failure Mode"
    The most common misunderstanding is to treat known problems as an old-issue list and event trees as a drawing exercise.
    Their real function is to change the team’s sensitivity to missed risk.

## How the Methods Proceed

The two methods can be remembered separately:

1. Known Problem: scan historical problems first, then decide which still apply to the current design.
2. Event Tree: define the initiating event first, then expand the downstream branches, intercept points, and consequence severity.

Neither method is about free-form brainstorming.
Both force the team back toward evidence and foreseeable pathways.

!!! example "Worked Example: The Main Path Looks Fine, but the Edge Path Still Fails"
    Suppose the normal use flow of a device is well analyzed,
    but complaint history shows users often reverse a component after cleaning and reassembly.
    Main-path analysis may miss that low-frequency branch.
    Known Problem Analysis pulls it back into view,
    and Event Tree analysis then asks what happens if that reversed assembly is not detected.

## How They Relate to the Main Workflow Analysis

Main workflow analysis is strongest on the normal task path.
These two methods are strongest at exposing historical blind spots and branch consequences outside that main path.
They complement rather than replace the main analysis.

!!! note "One-Sentence Conclusion"
    The real value of this page is that it forces the team to step back from “we already analyzed it” and ask “what might still be missing?”

## Why Known Problem Analysis Also Has to Learn Signal Selection

Known problems come from many places,
but not every historical signal carries the same weight.
A more mature practice is learning how to separate scattered noise from repeated signals that point to the same structural weakness across complaints,
recalls,
literature,
and competitor events.

This page therefore teaches more than where to look.
It also trains you to compress historical material into actionable risk cues rather than accumulating sources without analytic direction.

## Why Known Problem Analysis Prevents the Team from Repeating Old Failures

Many system risks are not novel.
They have already appeared as complaints,
CAPA records,
accidents,
literature findings,
or competitor failures.
Known Problem Analysis matters because it forces the team to recognize that history is itself risk evidence;
every project does not begin from zero.

When done well,
this step makes the team notice problems that are not new,
but are still likely to recur in the present environment.

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/11-known-problem-analysis/slide-06-image17.png" alt="This figure should show that known problem analysis is not casual memory. It requires going into real databases such as MAUDE to identify recurring device problems and complaint patterns." loading="lazy">
  <figcaption>This figure should show that known problem analysis is not casual memory. It requires going into real databases such as MAUDE to identify recurring device problems and complaint patterns.</figcaption>
</figure>

## Why Event Trees Pull Side-Branch Risk Back into View

Main workflow analysis often stays focused on the most common path,
but many serious system outcomes emerge on the branches.
The value of an Event Tree is that it begins with one initiating event and keeps asking:

- what happens if this defense succeeds
- what happens if it fails
- which outcomes are rare but extremely costly

Event Trees therefore do more than predict consequences.
They force the team to reinterpret what each defense branch actually means.

!!! example "Example: Why “An Alarm Occurs” Is Not the End but the Start of an Event Tree"
    If the initiating event is “a critical alarm occurs,” the real analysis begins afterward:
    was it noticed,
    was it understood,
    was the correct action taken,
    did the system continue degrading,
    and did backup defenses engage?
    Once expanded this way,
    the team sees that the real risk is not the alarm itself but the whole chain of later defense branches.

## Why KPA Is Not Just “Finding Cases” but a Three-Step Filtering Process

The lecture explicitly breaks KPA into `select sources -> collect and analyze -> document findings` to show that this is not a contest in gathering material.
Strong KPA first decides which sources matter,
then judges which issues are actually relevant to the current product,
interface,
and use conditions,
and only then translates the useful findings into risk and mitigation clues.

That sequence matters because without source and similarity filtering,
teams quickly drown in historical material.
The core of KPA is not merely knowing that many bad things happened before.
It is recognizing which old problems still have a realistic chance to recur in the current project.

!!! example "Example: Why an Old Blood-Glucose-Meter Problem Cannot Stop at “Copying a Complaint Summary”"
    If KPA only copies an old complaint into documentation,
    the team still does not know why it matters for the current design.
    A stronger KPA continues by asking whether the current strip-insertion method,
    prompt timing,
    blood-drop icon placement,
    and action rhythm could still induce the same failure.
    Only then does the historical issue become a design input for the present project rather than background reading.

## Why the Point of an Event Tree Is Not Drawing a Tree but Seeing Where Defenses Break

Many people first encounter Event Trees as branching diagrams and focus on the diagram itself.
What the course really trains is something else:
once you move forward from the initiating event,
where were the opportunities to block escalation,
and how did those opportunities fail one by one.

In that sense,
the value of an Event Tree is not only consequence branching.
It is that every branch becomes a statement about whether a defense succeeded or failed.
Once read that way,
the tree stops being only an outcome picture and becomes a structured inventory of recovery opportunity.

## Why This Page Is Especially Good at Recovering Low-Frequency High-Consequence Paths Missed by Main Workflow Analysis

Main workflow analysis is usually strongest on the most common and stable path,
yet many of the most costly accident chains live on edge branches.
Known Problem Analysis reminds the team whether those branches have already surfaced historically,
and Event Trees then ask how the consequence would amplify if they happened again.

The most useful lesson of this page is therefore that low frequency does not mean low importance.
Many branches are rare,
but still deserve serious design,
validation,
and training attention.

## Chapter Summary

!!! tip "What To Carry Forward"
    - Known Problem Analysis looks backward to prior issues;
      Event Trees look forward to consequence branches.
    - Together they fill gaps rather than replace main workflow analysis.
    - Both methods force the team back to evidence and foreseeable paths.
    - The true target is discovering what the team still missed.


## Source Scope and Related Topics

The teaching notes come first. This section lists the source files used on the page, and the appendix keeps the full line-by-line transcription for verification.

- Section: `ENP111 Use-related Risks`
- Source files: 2
- Text units: 112
- Visuals/previews: 18

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `11 Known Problem Analysis.pptx` | `pptx` | 43 | 17 | [open](../assets/source_files/ENP111/11 Known Problem Analysis.pptx) |
| `Event Tree Supplemental.pptx` | `pptx` | 69 | 1 | [open](../assets/source_files/ENP111/Event Tree Supplemental.pptx) |

## Related Topics

- [Error Analysis and Investigation Flow](../ENP112/error_analysis_methods.en.md)
- [URRA Methods](urra_methods.en.md)
- [Operational Risk](../ENP112/operational_risk.en.md)

## Original Transcription and Coverage Mapping

The collapsible blocks below preserve page/slide-level source transcription. Each `unit_id` maps one-to-one in `data/coverage_map.json`.

??? info "11 Known Problem Analysis.pptx | 43 text units"
    Download source: [11 Known Problem Analysis.pptx](../assets/source_files/ENP111/11 Known Problem Analysis.pptx)
    Mapped page: `known_problem_and_event_tree`
    
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
    Download source: [Event Tree Supplemental.pptx](../assets/source_files/ENP111/Event Tree Supplemental.pptx)
    Mapped page: `known_problem_and_event_tree`
    
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
