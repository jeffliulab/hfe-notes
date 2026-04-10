# The Swiss Cheese Model

This chapter pushes accident explanation from single-point failure toward the way multiple defenses fail together. The value of the Swiss Cheese model is not the metaphor itself, but the way it redirects attention to barriers and aligned vulnerabilities.

!!! note "Core Question"
    Why do accidents still happen in high-risk systems that appear to have many defenses, and is the real danger one failed layer or multiple defenses failing together at the same time?

## Key Takeaways

- The Swiss Cheese model treats accidents as penetration of multiple defenses rather than a single dramatic personal failure.
- Each layer can protect while still containing vulnerabilities, so the existence of a barrier does not guarantee dependable protection.
- The real danger is not one hole by itself, but several holes aligning across time and conditions.
- The model redirects blame-oriented thinking toward barrier design, latent conditions, and system resilience.
- It is useful, but it should not be treated as the full endpoint of analysis; dynamic change and deeper causal analysis still matter.

## Remember This First

!!! tip "Keep This Sentence in Mind"
    The shortest memory line is this: accidents usually do not happen because the last operator was uniquely weak, but because several defenses that should have intercepted the problem failed at the same time.

## What the Swiss Cheese Model Explains

What the model really explains is that harm paths in complex systems rarely emerge in one step. They move through barriers, procedures, checks, people, and organizational controls before reaching the outcome layer.

Once that is accepted, an accident no longer looks like an isolated explosion point. It looks like a problem chain that should have been intercepted several times. The natural focus therefore shifts from “who made the final wrong move” to “why so many prior layers failed to intercept it.”

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/05-swiss-cheese-model/page-06.png" alt="This figure should make one idea visible: accidents do not bypass only one barrier; they pass through a chain of weaknesses across several layers." loading="lazy">
  <figcaption>This figure should make one idea visible: accidents do not bypass only one barrier; they pass through a chain of weaknesses across several layers.</figcaption>
</figure>

## Why Defenses Protect and Still Contain Holes

This is where the model becomes concrete: defenses are never absolute.

- some holes are latent and persistent, such as design weakness, limited resources, unrealistic procedure, organizational tolerance, or poor incentives
- some holes are immediate triggers, such as fatigue, distraction, communication breakdown, time pressure, weather, or workload

The dangerous moment is not the existence of one hole alone, but the overlap between latent conditions and active triggers that opens a path which should never have been continuous.

!!! note "The Main Conclusion of This Section"
    The right question for a barrier is not only whether it exists, but whether it still works under real operating conditions.

!!! warning "The Most Common Misreading"
    Do not read the model as “more layers always mean more safety.” If the added layers are weak, conflicting, or detached from real work, more layers do not automatically produce more resilience.

## Why This Model Is Used So Widely

The model is widely used not just because the graphic is memorable, but because it makes complex risk legible very quickly:

- it shows that safety depends on layered defense rather than a single barrier
- it turns risk reduction into concrete questions: add a layer, strengthen a layer, shrink holes, reduce alignment
- it transfers well across aviation, nuclear power, healthcare, and other high-risk domains because all of them rely on multiple interception layers

That makes the model highly effective as a first explanatory tool and as a shared language across mixed teams.

<figure class="note-inline-figure">
  <img src="https://jeffliulab.github.io/hfe-notes/assets/visuals/05-swiss-cheese-model/page-07.png" alt="This figure should show that each measure is imperfect on its own, yet layering still sharply reduces the chance that a risk path stays open." loading="lazy">
  <figcaption>This figure should show that each measure is imperfect on its own, yet layering still sharply reduces the chance that a risk path stays open.</figcaption>
</figure>

!!! example "Example: Why the COVID Illustration Explains the Model So Quickly"
    Masks, distancing, cleaning, and handwashing are not perfect barriers, but together they reduce the chance that a harm path remains open. The example works because it makes one idea intuitive: every layer can have holes and still contribute meaningfully when stacked with others.

## What the Model Cannot Do on Its Own

The lecture does not treat Swiss Cheese as a perfect answer. Its listed criticisms matter:

- the model can imply that barriers are independent and the system is relatively static
- it emphasizes barriers, but may hide the deeper question of why holes keep appearing
- if the analysis stops at the graphic, it becomes too generic and too detached from real work

That is why later updates such as the `Hot Cheese Model` matter: real systems change over time, and even a new mitigation can introduce fresh risk.

!!! note "One-Sentence Conclusion"
    Swiss Cheese is a strong starting point, but it cannot replace dynamic systems thinking or deeper causal analysis.

!!! warning "Another Common Trap"
    Do not assume that drawing the Swiss Cheese picture completes the analysis. The picture helps reveal layers and holes, but the hard part is still explaining why those holes persist and how organizational conditions magnify them.

## How to Actually Use the Framework in Accident Analysis

To actually use the framework, a practical sequence is:

1. identify the harm vector, meaning how the final harm path formed
2. work backward through the barriers that should have intercepted it
3. ask for each layer whether it was absent, failed, or only looked effective on paper
4. separate latent conditions from active failures and map mitigation back to specific layers

The result is that the analysis no longer ends with a single “responsible operator.” It becomes a system vulnerability map.

!!! example "Example: How One Accident Path Penetrates Several Layers"
    Imagine a medical device receiving an incorrect dose setting during a night shift. The final wrong entry is only the `sharp end`. Upstream there may already be a confusable interface, unclear labeling, a superficial double-check process, excessive workload, and training that emphasized the wrong cues. If only the final action is inspected, the story becomes “someone typed it incorrectly.” Through Swiss Cheese, the deeper story is that several defenses failed together.

!!! example "Example: Why Both Deepwater Horizon and Challenger Fit This Framework"
    Neither case reduces cleanly to “one part failed.” Deepwater Horizon involved data misinterpretation, equipment failure, and time or budget pressure; Challenger involved material and testing problems together with schedule pressure and oversight or culture failures. Swiss Cheese helps place those seemingly scattered factors back onto one penetration path.

## Chapter Summary

!!! tip "What To Carry Forward"
    - The Swiss Cheese model explains accidents as sequential penetration of multiple defenses.
    - The deepest danger appears when latent conditions overlap with active triggers.
    - The model is highly effective for building shared language and a first-pass accident explanation.
    - Its limitation is that it can become too static and purely graphical, so deeper causal analysis still has to follow.
    - To use it well, map the harm vector, barriers, holes, and mitigation layer by layer.


## Source Scope and Related Topics

The teaching notes come first. This section lists the source files used on the page, and the appendix keeps the full line-by-line transcription for verification.

- Section: `HFE Foundations`
- Source files: 1
- Text units: 145
- Visuals/previews: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `05 Swiss Cheese Model.pdf` | `pdf` | 145 | 3 | [open](../assets/source_files/ENP_111_Use_related_Risks/05 Swiss Cheese Model.pdf) |

## Related Topics

- [Human Error Frameworks](human_error_frameworks.en.md)
- [Operational Risk](../HFE_Cases_Ethics/operational_risk.en.md)

## Original Transcription and Coverage Mapping

The collapsible blocks below preserve page/slide-level source transcription. Each `unit_id` maps one-to-one in `data/coverage_map.json`.

??? info "05 Swiss Cheese Model.pdf | 145 text units"
    Download source: [05 Swiss Cheese Model.pdf](../assets/source_files/ENP_111_Use_related_Risks/05 Swiss Cheese Model.pdf)
    Mapped page: `swiss_cheese`
    
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
