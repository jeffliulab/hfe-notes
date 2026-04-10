# Error Analysis and Investigation Flow

This page asks how to analyze an accident, incident, or near miss in a disciplined way instead of collapsing it into a story with a premature conclusion.

!!! note "Core Question"
    How do error analysis and investigation convert “what happened” into “why it happened and what should be changed next”?

## Key Takeaways

- Investigation moves from facts to timeline to causal layers to interventions.
- The NTSB-style discipline is evidence first, explanation second.
- One outcome usually has multiple contributing paths, so analysis cannot collapse too early.
- Strong error analysis ends in design, workflow, training, or policy change rather than in a report alone.

## What This Method Is For

!!! tip "Start with the Purpose"
    Start with the purpose of the method: investigation is not about reaching a conclusion quickly, but about grounding the conclusion in reliable facts and an explainable causal chain.

## What Problem This Method Solves

Error analysis and investigation are valuable because they turn a complex event into a verifiable structure. The method asks:

- what state the system was in
- how the event unfolded over time
- which factors were direct triggers and which were preconditions
- which system-level issues made the error more likely or harder to recover from

## What the Inputs and Outputs Are

Typical inputs include interviews, records, logs, timing information, procedures, environmental conditions, and equipment state.

The output should not be only a “most likely cause.” It should include:

- a clear timeline
- separation of fact from interpretation
- separation of triggers from deeper conditions
- actionable recommendations

## How the Method Proceeds

The flow can be remembered in four steps:

1. gather facts without rushing into explanation
2. build the timeline so the sequence is clear
3. separate triggers, preconditions, and organizational or design contributors
4. translate the findings into interventions across interface, procedure, training, resources, or policy

!!! note "One-Sentence Conclusion"
    The main thing an investigation must avoid is not too much information, but the premature feeling that the answer is already obvious.

!!! warning "The Most Common Failure Mode"
    The most common failure is to see one visible human action and immediately write it down as “the cause.” That collapses a system explanation into a description of the last visible move.

!!! example "Worked Example: How a Medication Error Gets Decomposed"
    If the report only says “the nurse selected the wrong medication,” the output is blame. A stronger investigation adds the timeline, packaging similarity, verification process, workload, shift fatigue, and alarm context, turning one visible action into an explainable causal chain.

## How It Connects to Later Methods

This page explains how a completed event is interpreted. Later pages such as task analysis, URRA, and operational risk push the same logic forward so risk can be recognized before an event fully unfolds.

## Chapter Summary

!!! tip "What To Carry Forward"
    - Investigation clarifies facts before explaining causes.
    - One outcome often has multiple causal paths, so early closure is dangerous.
    - The strongest output combines timeline, layered causation, and intervention.
    - This method provides the base logic for the more proactive risk-analysis pages that follow.


## Source Scope and Related Topics

The teaching notes come first. This section lists the source files used on the page, and the appendix keeps the full line-by-line transcription for verification.

- Section: `Risk Methods`
- Source files: 2
- Text units: 584
- Visuals/previews: 6

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Sp26_Investigative Process-NTSB_20260121.pdf` | `pdf` | 267 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Sp26_Investigative Process-NTSB_20260121.pdf) |
| `Sp26_ErrorAnalysisMethods_20260121.pdf` | `pdf` | 317 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Sp26_ErrorAnalysisMethods_20260121.pdf) |

## Related Topics

- [Human Error Frameworks](../HFE_Foundations/human_error_frameworks.en.md)
- [Task Analysis](task_analysis.en.md)
- [Operational Risk](../HFE_Cases_Ethics/operational_risk.en.md)

## Original Transcription and Coverage Mapping

The collapsible blocks below preserve page/slide-level source transcription. Each `unit_id` maps one-to-one in `data/coverage_map.json`.

??? info "Sp26_Investigative Process-NTSB_20260121.pdf | 267 text units"
    Download source: [Sp26_Investigative Process-NTSB_20260121.pdf](../assets/source_files/Lectures_Spring_2026/Sp26_Investigative Process-NTSB_20260121.pdf)
    Mapped page: `error_analysis_methods`
    
    ```text
    [sp26-investigative-process-ntsb-20260121-0001] page:1:line:1 | The NTSB
    [sp26-investigative-process-ntsb-20260121-0002] page:1:line:2 | Investigative Process
    [sp26-investigative-process-ntsb-20260121-0003] page:1:line:3 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0004] page:1:line:4 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0005] page:1:line:5 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0006] page:1:line:6 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0007] page:1:line:7 | 1
    [sp26-investigative-process-ntsb-20260121-0008] page:2:line:1 | NTSB Primer
    [sp26-investigative-process-ntsb-20260121-0009] page:2:line:2 | • Established in 1967 as part of the Department of Transportation
    [sp26-investigative-process-ntsb-20260121-0010] page:2:line:3 | • 1975 became fully independent
    [sp26-investigative-process-ntsb-20260121-0011] page:2:line:4 | • Five board members are Presidential appointments (5 yr terms)
    [sp26-investigative-process-ntsb-20260121-0012] page:2:line:5 | • ~400 employees
    [sp26-investigative-process-ntsb-20260121-0013] page:2:line:6 | • Investigates ~2500 accidents per year (link)
    [sp26-investigative-process-ntsb-20260121-0014] page:2:line:7 | • Aviation: ~2000; Marine, rail, highway, pipeline: ~500
    [sp26-investigative-process-ntsb-20260121-0015] page:2:line:8 | • “Accident/incident investigations are fact-finding proceedings with no formal
    [sp26-investigative-process-ntsb-20260121-0016] page:2:line:9 | issues and no adverse parties … and are not conducted for the purpose of
    [sp26-investigative-process-ntsb-20260121-0017] page:2:line:10 | determining the rights or liabilities of any person.”
    [sp26-investigative-process-ntsb-20260121-0018] page:2:line:11 | • Title 49 Code of Federal Regulations section 831.4
    [sp26-investigative-process-ntsb-20260121-0019] page:2:line:12 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0020] page:2:line:13 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0021] page:2:line:14 | 2
    [sp26-investigative-process-ntsb-20260121-0022] page:3:line:1 | NTSB Mission
    [sp26-investigative-process-ntsb-20260121-0023] page:3:line:2 | • Maintaining our congressionally mandated independence
    [sp26-investigative-process-ntsb-20260121-0024] page:3:line:3 | • Conducting objective, thorough investigations and safety studies
    [sp26-investigative-process-ntsb-20260121-0025] page:3:line:4 | • Deciding fairly and objectively appeals of enforcement actions by the
    [sp26-investigative-process-ntsb-20260121-0026] page:3:line:5 | FAA and US Coast Guard and certificate denials by the FAA
    [sp26-investigative-process-ntsb-20260121-0027] page:3:line:6 | • Advocating for implementation of safety recommendations
    [sp26-investigative-process-ntsb-20260121-0028] page:3:line:7 | • Assisting victims and survivors of transportation disasters and their
    [sp26-investigative-process-ntsb-20260121-0029] page:3:line:8 | families
    [sp26-investigative-process-ntsb-20260121-0030] page:3:line:9 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0031] page:3:line:10 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0032] page:3:line:11 | 3
    [sp26-investigative-process-ntsb-20260121-0033] page:3:line:12 | From “About the NTSB”
    [sp26-investigative-process-ntsb-20260121-0034] page:4:line:1 | Selecting Accidents to Investigate
    [sp26-investigative-process-ntsb-20260121-0035] page:4:line:2 | • NTSB’s responsibility to investigate accidents varies by transportation mode
    [sp26-investigative-process-ntsb-20260121-0036] page:4:line:3 | • NTSB is required to investigate all civil aviation accidents, and all railroad and
    [sp26-investigative-process-ntsb-20260121-0037] page:4:line:4 | pipeline accidents that result in fatalities or substantial property damage.
    [sp26-investigative-process-ntsb-20260121-0038] page:4:line:5 | • For highway crashes, NTSB may initiate an investigation at its discretion.
    [sp26-investigative-process-ntsb-20260121-0039] page:4:line:6 | • In determining whether to investigate, NTSB considers:
    [sp26-investigative-process-ntsb-20260121-0040] page:4:line:7 | 1.
    [sp26-investigative-process-ntsb-20260121-0041] page:4:line:8 | Are there national safety issues as opposed to site-specific issues?
    [sp26-investigative-process-ntsb-20260121-0042] page:4:line:9 | 2.
    [sp26-investigative-process-ntsb-20260121-0043] page:4:line:10 | Does the crash involve emerging technologies or public safety issues?
    [sp26-investigative-process-ntsb-20260121-0044] page:4:line:11 | 3.
    [sp26-investigative-process-ntsb-20260121-0045] page:4:line:12 | Is there potential for safety recommendations?
    [sp26-investigative-process-ntsb-20260121-0046] page:4:line:13 | 4.
    [sp26-investigative-process-ntsb-20260121-0047] page:4:line:14 | Does NTSB have the resources (i.e., staff availability and capacity)?
    [sp26-investigative-process-ntsb-20260121-0048] page:4:line:15 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0049] page:4:line:16 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0050] page:4:line:17 | 4
    [sp26-investigative-process-ntsb-20260121-0051] page:5:line:1 | Investigative Process Overview
    [sp26-investigative-process-ntsb-20260121-0052] page:5:line:2 | • Initial notification and decision to investigate
    [sp26-investigative-process-ntsb-20260121-0053] page:5:line:3 | • Gathering facts on-site
    [sp26-investigative-process-ntsb-20260121-0054] page:5:line:4 | • Analysis facts and determination of probable cause
    [sp26-investigative-process-ntsb-20260121-0055] page:5:line:5 | • Acceptance of a final report
    [sp26-investigative-process-ntsb-20260121-0056] page:5:line:6 | • Advocating for acceptance of safety recommendations arising from the
    [sp26-investigative-process-ntsb-20260121-0057] page:5:line:7 | investigation
    [sp26-investigative-process-ntsb-20260121-0058] page:5:line:8 | • Invoke subpoena and prosecutorial power
    [sp26-investigative-process-ntsb-20260121-0059] page:5:line:9 | https://www.ntsb.gov/investigations/process/Pages/default.aspx
    [sp26-investigative-process-ntsb-20260121-0060] page:5:line:10 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0061] page:5:line:11 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0062] page:5:line:12 | 5
    [sp26-investigative-process-ntsb-20260121-0063] page:6:line:1 | NTSB On Site “Go Team”
    [sp26-investigative-process-ntsb-20260121-0064] page:6:line:2 | • Investigator-in-Charge  (IIC) – a senior investigator with years of NTSB and industry experience
    [sp26-investigative-process-ntsb-20260121-0065] page:6:line:3 | • NTSB investigators
    [sp26-investigative-process-ntsb-20260121-0066] page:6:line:4 | • Board member, who acts as official spokesperson;
    [sp26-investigative-process-ntsb-20260121-0067] page:6:line:5 | • Public affairs officer, who facilitates media briefings and responds to press inquiries
    [sp26-investigative-process-ntsb-20260121-0068] page:6:line:6 | • Transportation disaster assistant specialist
    [sp26-investigative-process-ntsb-20260121-0069] page:6:line:7 | • NTSB investigators are specialists in a clearly defined area of the investigation such as:
    [sp26-investigative-process-ntsb-20260121-0070] page:6:line:8 | • OPERATIONS, STRUCTURES, SYSTEMS, ATC:
    [sp26-investigative-process-ntsb-20260121-0071] page:6:line:9 | • Accident flight history, crewmembers' duties prior to the crash; airframe analysis, vehicle systems, etc.
    [sp26-investigative-process-ntsb-20260121-0072] page:6:line:10 | • HUMAN PERFORMANCE:
    [sp26-investigative-process-ntsb-20260121-0073] page:6:line:11 | • Study crew performance, before-the-accident factors possibly involved in human error, e.g., fatigue, training, etc
    [sp26-investigative-process-ntsb-20260121-0074] page:6:line:12 | • SURVIVAL FACTORS:
    [sp26-investigative-process-ntsb-20260121-0075] page:6:line:13 | • Document impact forces and injuries, evacuation, community emergency planning and all crash-fire-rescue efforts.
    [sp26-investigative-process-ntsb-20260121-0076] page:6:line:14 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0077] page:6:line:15 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0078] page:6:line:16 | 6
    [sp26-investigative-process-ntsb-20260121-0079] page:7:line:1 | “Go Team” Working Groups
    [sp26-investigative-process-ntsb-20260121-0080] page:7:line:2 | Each NTSB investigator heads a working group in an area of expertise
    [sp26-investigative-process-ntsb-20260121-0081] page:7:line:3 | • Groups are staffed by representatives of "parties" to the investigation
    [sp26-investigative-process-ntsb-20260121-0082] page:7:line:4 | • Aviation accident-parties include FAA, airline, pilots' and flight attendants' unions, airframe and
    [sp26-investigative-process-ntsb-20260121-0083] page:7:line:5 | engine manufacturers
    [sp26-investigative-process-ntsb-20260121-0084] page:7:line:6 | • Surface accident investigations, fewer working groups, same team technique
    [sp26-investigative-process-ntsb-20260121-0085] page:7:line:7 | • Locomotive engineers, signal system specialists and track engineers head working groups at
    [sp26-investigative-process-ntsb-20260121-0086] page:7:line:8 | railroad accidents.
    [sp26-investigative-process-ntsb-20260121-0087] page:7:line:9 | • Highway crashes include a truck or bus mechanical expert and a highway engineer.
    [sp26-investigative-process-ntsb-20260121-0088] page:7:line:10 | • Weather, human performance and survival factors specialists respond to all accidents
    [sp26-investigative-process-ntsb-20260121-0089] page:7:line:11 | • Working groups remain at the accident scene for a few days to several weeks.
    [sp26-investigative-process-ntsb-20260121-0090] page:7:line:12 | • Work at Washington HQ forms the basis for analysis and drafting of report.
    [sp26-investigative-process-ntsb-20260121-0091] page:7:line:13 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0092] page:7:line:14 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0093] page:7:line:15 | 7
    [sp26-investigative-process-ntsb-20260121-0094] page:8:line:1 | The “Party” System
    [sp26-investigative-process-ntsb-20260121-0095] page:8:line:2 | • Board designates organizations as parties to its investigations
    [sp26-investigative-process-ntsb-20260121-0096] page:8:line:3 | • FAA, by law, is automatically designated a party
    [sp26-investigative-process-ntsb-20260121-0097] page:8:line:4 | • NTSB has complete discretion to designate parties
    [sp26-investigative-process-ntsb-20260121-0098] page:8:line:5 | • Only organizations that can provide expertise are granted party status
    [sp26-investigative-process-ntsb-20260121-0099] page:8:line:6 | • Only persons who can provide the Board with needed technical or specialized expertise are
    [sp26-investigative-process-ntsb-20260121-0100] page:8:line:7 | permitted to serve on the investigation
    [sp26-investigative-process-ntsb-20260121-0101] page:8:line:8 | • Persons in legal positions are not allowed
    [sp26-investigative-process-ntsb-20260121-0102] page:8:line:9 | • All party members report to the NTSB
    [sp26-investigative-process-ntsb-20260121-0103] page:8:line:10 | • Each investigative group chairman prepares a factual report for public docket
    [sp26-investigative-process-ntsb-20260121-0104] page:8:line:11 | https://www.ntsb.gov/investigations/process/Pages/partysystem.aspx
    [sp26-investigative-process-ntsb-20260121-0105] page:8:line:12 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0106] page:8:line:13 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0107] page:8:line:14 | 8
    [sp26-investigative-process-ntsb-20260121-0108] page:9:line:1 | Being Part of the NTSB Go Team
    [sp26-investigative-process-ntsb-20260121-0109] page:9:line:2 | Robert Sumwalt (right)
    [sp26-investigative-process-ntsb-20260121-0110] page:9:line:3 | • Former NTSB Chair and Board
    [sp26-investigative-process-ntsb-20260121-0111] page:9:line:4 | Member;
    [sp26-investigative-process-ntsb-20260121-0112] page:9:line:5 | • Associate Professor and Executive
    [sp26-investigative-process-ntsb-20260121-0113] page:9:line:6 | Director, Center for Aviation and
    [sp26-investigative-process-ntsb-20260121-0114] page:9:line:7 | Aerospace Safety,
    [sp26-investigative-process-ntsb-20260121-0115] page:9:line:8 | Embry Riddle Aeronautical University
    [sp26-investigative-process-ntsb-20260121-0116] page:9:line:9 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0117] page:9:line:10 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0118] page:9:line:11 | 9
    [sp26-investigative-process-ntsb-20260121-0119] page:9:line:12 | “It always happens when you least expect it.”
    [sp26-investigative-process-ntsb-20260121-0120] page:10:line:1 | Excerpts from “Being Part of the NTSB Go Team,”  Aviation Week,  Robert
    [sp26-investigative-process-ntsb-20260121-0121] page:10:line:2 | Sumwalt, June 09, 2022
    [sp26-investigative-process-ntsb-20260121-0122] page:10:line:3 | • Go Team schedule runs from 5pm on Monday to 5pm the following Monday.
    [sp26-investigative-process-ntsb-20260121-0123] page:10:line:4 | • Phone may ring or receive a text to notify you of an upcoming call with the
    [sp26-investigative-process-ntsb-20260121-0124] page:10:line:5 | Response Operations Center (ROC) in 15 minutes.
    [sp26-investigative-process-ntsb-20260121-0125] page:10:line:6 | • In 15 years as an NTSB board member, dispatched on 36 Go Team accidents.
    [sp26-investigative-process-ntsb-20260121-0126] page:10:line:7 | • As Chairman, involved in numerous other calls and meetings at all hours of the day
    [sp26-investigative-process-ntsb-20260121-0127] page:10:line:8 | where we made decisions about our level of response.”
    [sp26-investigative-process-ntsb-20260121-0128] page:10:line:9 | • “Launch decision starts with “Chairman’s Call” where key NTSB officials discuss
    [sp26-investigative-process-ntsb-20260121-0129] page:10:line:10 | known details of the situation and decide whether a full Go Team will be sent and
    [sp26-investigative-process-ntsb-20260121-0130] page:10:line:11 | whether board member will accompany the team.
    [sp26-investigative-process-ntsb-20260121-0131] page:10:line:12 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0132] page:10:line:13 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0133] page:10:line:14 | 10
    [sp26-investigative-process-ntsb-20260121-0134] page:11:line:1 | Excerpts (cont.)
    [sp26-investigative-process-ntsb-20260121-0135] page:11:line:2 | • We get to the accident site however we can. Often, FAA provides use of its
    [sp26-investigative-process-ntsb-20260121-0136] page:11:line:3 | aircraft. If not available, we fly on airlines.
    [sp26-investigative-process-ntsb-20260121-0137] page:11:line:4 | • “FAA’s plane could work around our schedule and take us to airports not served by
    [sp26-investigative-process-ntsb-20260121-0138] page:11:line:5 | air carriers. Accidents don’t always happen close to airports served by airlines.”
    [sp26-investigative-process-ntsb-20260121-0139] page:11:line:6 | • Initial media briefing would provide footage that media could show throughout the
    [sp26-investigative-process-ntsb-20260121-0140] page:11:line:7 | day until we held a more detailed briefing upon arrival.
    [sp26-investigative-process-ntsb-20260121-0141] page:11:line:8 | • Board member on scene would conduct media briefings, meet with families and
    [sp26-investigative-process-ntsb-20260121-0142] page:11:line:9 | elected officials.
    [sp26-investigative-process-ntsb-20260121-0143] page:11:line:10 | • “Meeting with family members was hardest part of my job. Only solace I could
    [sp26-investigative-process-ntsb-20260121-0144] page:11:line:11 | provide was that NTSB was going to find out what happened, so others didn’t have
    [sp26-investigative-process-ntsb-20260121-0145] page:11:line:12 | to go through what they were going through.”
    [sp26-investigative-process-ntsb-20260121-0146] page:11:line:13 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0147] page:11:line:14 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0148] page:11:line:15 | 11
    [sp26-investigative-process-ntsb-20260121-0149] page:12:line:1 | NTSB Safety Recommendations
    [sp26-investigative-process-ntsb-20260121-0150] page:12:line:2 | • Issue recommendations to the organizations best able to take corrective
    [sp26-investigative-process-ntsb-20260121-0151] page:12:line:3 | action in the specific transportation area.
    [sp26-investigative-process-ntsb-20260121-0152] page:12:line:4 | • Examples : US DOT and its modal administrations, the Coast Guard, other federal and
    [sp26-investigative-process-ntsb-20260121-0153] page:12:line:5 | state agencies, manufacturers, operators, labor unions, and industry and trade
    [sp26-investigative-process-ntsb-20260121-0154] page:12:line:6 | organizations
    [sp26-investigative-process-ntsb-20260121-0155] page:12:line:7 | • Monitor the progress of action to implement each recommendation until it is
    [sp26-investigative-process-ntsb-20260121-0156] page:12:line:8 | closed, which usually takes several years.
    [sp26-investigative-process-ntsb-20260121-0157] page:12:line:9 | • Case Analysis and Reporting Online (CAROL)
    [sp26-investigative-process-ntsb-20260121-0158] page:12:line:10 | • Online search tool for investigations and recommendations across all modes.
    [sp26-investigative-process-ntsb-20260121-0159] page:12:line:11 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0160] page:12:line:12 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0161] page:12:line:13 | 12
    [sp26-investigative-process-ntsb-20260121-0162] page:13:line:1 | NTSB’s “Most Wanted List 1990-2023”
    [sp26-investigative-process-ntsb-20260121-0163] page:13:line:2 | (see the MWL Archive)
    [sp26-investigative-process-ntsb-20260121-0164] page:13:line:3 | Aviation
    [sp26-investigative-process-ntsb-20260121-0165] page:13:line:4 | Require and Verify the Effectiveness of Safety Management Systems in all Revenue Passenger-Carrying Aviation Operations
    [sp26-investigative-process-ntsb-20260121-0166] page:13:line:5 | Install Crash-Resistant Recorders and Establish Flight Data Monitoring Programs  (video recorders)
    [sp26-investigative-process-ntsb-20260121-0167] page:13:line:6 | Highway
    [sp26-investigative-process-ntsb-20260121-0168] page:13:line:7 | Implement a Comprehensive Strategy to Eliminate Speeding-Related Crashes
    [sp26-investigative-process-ntsb-20260121-0169] page:13:line:8 | Protect Vulnerable Road Users through a Safe System Approach
    [sp26-investigative-process-ntsb-20260121-0170] page:13:line:9 | Require Collision-Avoidance and Connected-Vehicle Technologies on all Vehicles
    [sp26-investigative-process-ntsb-20260121-0171] page:13:line:10 | Eliminate Distracted Driving
    [sp26-investigative-process-ntsb-20260121-0172] page:13:line:11 | Marine
    [sp26-investigative-process-ntsb-20260121-0173] page:13:line:12 | Improve Passenger and Fishing Vessel Safety
    [sp26-investigative-process-ntsb-20260121-0174] page:13:line:13 | Rail, Pipeline, and Hazardous Materials
    [sp26-investigative-process-ntsb-20260121-0175] page:13:line:14 | Improve Pipeline Leak Detection and Mitigation
    [sp26-investigative-process-ntsb-20260121-0176] page:13:line:15 | Improve Rail Worker Safety
    [sp26-investigative-process-ntsb-20260121-0177] page:13:line:16 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0178] page:13:line:17 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0179] page:13:line:18 | 13
    [sp26-investigative-process-ntsb-20260121-0180] page:14:line:1 | NTSB - Information Format
    [sp26-investigative-process-ntsb-20260121-0181] page:14:line:2 | Uses docket system
    [sp26-investigative-process-ntsb-20260121-0182] page:14:line:3 | https://data.ntsb.gov/Docket/Forms/recentlypublisheddockets
    [sp26-investigative-process-ntsb-20260121-0183] page:14:line:4 | https://data.ntsb.gov/Docket/Forms/searchdocket
    [sp26-investigative-process-ntsb-20260121-0184] page:14:line:5 | Similar to federal courts
    [sp26-investigative-process-ntsb-20260121-0185] page:14:line:6 | • Federal courts create and maintain a case file which contains a docket sheet
    [sp26-investigative-process-ntsb-20260121-0186] page:14:line:7 | and all documents filed in a case.
    [sp26-investigative-process-ntsb-20260121-0187] page:14:line:8 | • Case files and court records can be found on (public access to court electronic
    [sp26-investigative-process-ntsb-20260121-0188] page:14:line:9 | records) PACER.gov. https://www.uscourts.gov/court-records
    [sp26-investigative-process-ntsb-20260121-0189] page:14:line:10 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0190] page:14:line:11 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0191] page:14:line:12 | 14
    [sp26-investigative-process-ntsb-20260121-0192] page:15:line:1 | Investigation example - Conception
    [sp26-investigative-process-ntsb-20260121-0193] page:15:line:2 | • September 2, 2019, Conception
    [sp26-investigative-process-ntsb-20260121-0194] page:15:line:3 | dive boat caught fire at 3 am,
    [sp26-investigative-process-ntsb-20260121-0195] page:15:line:4 | burned to the waterline, and sank
    [sp26-investigative-process-ntsb-20260121-0196] page:15:line:5 | less than 100 feet from shore.
    [sp26-investigative-process-ntsb-20260121-0197] page:15:line:6 | • Anchored off Santa Cruz island
    [sp26-investigative-process-ntsb-20260121-0198] page:15:line:7 | • 34 people asleep below deck in
    [sp26-investigative-process-ntsb-20260121-0199] page:15:line:8 | the bunkroom were trapped.
    [sp26-investigative-process-ntsb-20260121-0200] page:15:line:9 | • None survived.
    [sp26-investigative-process-ntsb-20260121-0201] page:15:line:10 | NTSB investigation page
    [sp26-investigative-process-ntsb-20260121-0202] page:15:line:11 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0203] page:15:line:12 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0204] page:15:line:13 | 15
    [sp26-investigative-process-ntsb-20260121-0205] page:15:line:14 | 75-foot dive boat; 33 passengers, 6 crew
    [sp26-investigative-process-ntsb-20260121-0206] page:16:line:1 | Example
    [sp26-investigative-process-ntsb-20260121-0207] page:16:line:2 | NTSB Opens Public Docket on Conception Dive Boat Fire
    [sp26-investigative-process-ntsb-20260121-0208] page:16:line:3 | • https://www.ntsb.gov/news/press-releases/Pages/NR20200916.aspx
    [sp26-investigative-process-ntsb-20260121-0209] page:16:line:4 | Initial Report (20 Oct 2020)
    [sp26-investigative-process-ntsb-20260121-0210] page:16:line:5 | • https://www.ntsb.gov/news/events/Documents/2020-DCA19MM047-BMG-
    [sp26-investigative-process-ntsb-20260121-0211] page:16:line:6 | abstract.pdf
    [sp26-investigative-process-ntsb-20260121-0212] page:16:line:7 | Final Report
    [sp26-investigative-process-ntsb-20260121-0213] page:16:line:8 | • https://www.ntsb.gov/investigations/AccidentReports/Reports/MAR2003.pd
    [sp26-investigative-process-ntsb-20260121-0214] page:16:line:9 | f
    [sp26-investigative-process-ntsb-20260121-0215] page:16:line:10 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0216] page:16:line:11 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0217] page:16:line:12 | 16
    [sp26-investigative-process-ntsb-20260121-0218] page:17:line:1 | After the Investigation, What Happens?
    [sp26-investigative-process-ntsb-20260121-0219] page:17:line:2 | • Probable cause was failure of the operator, Truth Aquatics, to provide effective oversight of its vessel and
    [sp26-investigative-process-ntsb-20260121-0220] page:17:line:3 | crewmember operations allowing  fire to grow undetected.
    [sp26-investigative-process-ntsb-20260121-0221] page:17:line:4 | • Example of need for rigorous fire safety standards for small passenger vessels
    [sp26-investigative-process-ntsb-20260121-0222] page:17:line:5 | • Lack of USCG regulatory requirement for smoke detection in all accommodation spaces and inadequate
    [sp26-investigative-process-ntsb-20260121-0223] page:17:line:6 | emergency escape arrangements from the vessel’s bunkroom contributed to the undetected growth of the fire
    [sp26-investigative-process-ntsb-20260121-0224] page:17:line:7 | • 21 open NTSB recommendations to USCG focused on improving passenger vessel safety.
    [sp26-investigative-process-ntsb-20260121-0225] page:17:line:8 | • Reiterated recommendation to USCG to require safety management systems (SMS) on U.S. flag passenger
    [sp26-investigative-process-ntsb-20260121-0226] page:17:line:9 | vessels.
    [sp26-investigative-process-ntsb-20260121-0227] page:17:line:10 | • Congress codified these safety recommendations into law, mandated USCG implement recommendations in the
    [sp26-investigative-process-ntsb-20260121-0228] page:17:line:11 | Elijah E. Cummings Coast Guard Authorization Act of 2020 as part of the National Defense Authorization Act.
    [sp26-investigative-process-ntsb-20260121-0229] page:17:line:12 | https://www.ntsb.gov/investigations/AccidentReports/Reports/MAR2003.pdf
    [sp26-investigative-process-ntsb-20260121-0230] page:17:line:13 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0231] page:17:line:14 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0232] page:17:line:15 | 17
    [sp26-investigative-process-ntsb-20260121-0233] page:18:line:1 | https://www.tsb.gc.ca/eng/enquetes-investigations/index.html
    [sp26-investigative-process-ntsb-20260121-0234] page:18:line:2 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0235] page:18:line:3 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0236] page:18:line:4 | 18
    [sp26-investigative-process-ntsb-20260121-0237] page:19:line:1 | Other Transportation Investigative Entities
    [sp26-investigative-process-ntsb-20260121-0238] page:19:line:2 | • Federal Railroad Administration
    [sp26-investigative-process-ntsb-20260121-0239] page:19:line:3 | https://railroads.dot.gov/railroad-safety/accident-data-reporting-
    [sp26-investigative-process-ntsb-20260121-0240] page:19:line:4 | and-investigations
    [sp26-investigative-process-ntsb-20260121-0241] page:19:line:5 | • Federal Motor Carrier Safety Administration
    [sp26-investigative-process-ntsb-20260121-0242] page:19:line:6 | https://ai.fmcsa.dot.gov/NewEntrant/MC/Content.aspx?nav=Accidents
    [sp26-investigative-process-ntsb-20260121-0243] page:19:line:7 | • US Coast Guard
    [sp26-investigative-process-ntsb-20260121-0244] page:19:line:8 | https://cgmix.uscg.mil/IIR/Default.aspx
    [sp26-investigative-process-ntsb-20260121-0245] page:19:line:9 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0246] page:19:line:10 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0247] page:19:line:11 | 19
    [sp26-investigative-process-ntsb-20260121-0248] page:20:line:1 | NASA Mishap Investigation Team (MIT)
    [sp26-investigative-process-ntsb-20260121-0249] page:20:line:2 | A NASA mishap is an unplanned event resulting in at least one of the following:
    [sp26-investigative-process-ntsb-20260121-0250] page:20:line:3 | • Occupational injury or occupational illness to NASA or non-NASA personnel caused by NASA
    [sp26-investigative-process-ntsb-20260121-0251] page:20:line:4 | operations
    [sp26-investigative-process-ntsb-20260121-0252] page:20:line:5 | • Destruction of, or damage to, NASA property, public or private property, including foreign property,
    [sp26-investigative-process-ntsb-20260121-0253] page:20:line:6 | caused by NASA operations or NASA-funded research and development projects
    [sp26-investigative-process-ntsb-20260121-0254] page:20:line:7 | • NASA mission failure before the scheduled completion of the planned mission
    [sp26-investigative-process-ntsb-20260121-0255] page:20:line:8 | • “Close call”
    [sp26-investigative-process-ntsb-20260121-0256] page:20:line:9 | • no injury or only minor injury requiring first aid, no damage or minor damage (less than
    [sp26-investigative-process-ntsb-20260121-0257] page:20:line:10 | $20,000) to equipment or property or both, but possesses potential to cause a mishap
    [sp26-investigative-process-ntsb-20260121-0258] page:20:line:11 | A Quick Reference Guide for Mishap Investigations (2020)
    [sp26-investigative-process-ntsb-20260121-0259] page:20:line:12 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0260] page:20:line:13 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0261] page:20:line:14 | 20
    [sp26-investigative-process-ntsb-20260121-0262] page:21:line:1 | References
    [sp26-investigative-process-ntsb-20260121-0263] page:21:line:2 | • Kenneth, L. Carper, Forensic Engineering, Second Edition, 2001.
    [sp26-investigative-process-ntsb-20260121-0264] page:21:line:3 | Chapter 7
    [sp26-investigative-process-ntsb-20260121-0265] page:21:line:4 | 21 Jan 2026
    [sp26-investigative-process-ntsb-20260121-0266] page:21:line:5 | ENP-0112
    [sp26-investigative-process-ntsb-20260121-0267] page:21:line:6 | 21
    ```

??? info "Sp26_ErrorAnalysisMethods_20260121.pdf | 317 text units"
    Download source: [Sp26_ErrorAnalysisMethods_20260121.pdf](../assets/source_files/Lectures_Spring_2026/Sp26_ErrorAnalysisMethods_20260121.pdf)
    Mapped page: `error_analysis_methods`
    
    ```text
    [sp26-erroranalysismethods-20260121-0001] page:1:line:1 | ANALYSIS METHODS &
    [sp26-erroranalysismethods-20260121-0002] page:1:line:2 | FRAMEWORKS
    [sp26-erroranalysismethods-20260121-0003] page:1:line:3 | Dr. Andrew Liu
    [sp26-erroranalysismethods-20260121-0004] page:1:line:4 | ENP-0112
    [sp26-erroranalysismethods-20260121-0005] page:2:line:1 | Issues/ sidebars
    [sp26-erroranalysismethods-20260121-0006] page:2:line:2 | Issues/theory ("Sidebars”)
    [sp26-erroranalysismethods-20260121-0007] page:2:line:3 | Analysis Methods and
    [sp26-erroranalysismethods-20260121-0008] page:2:line:4 | Frameworks
    [sp26-erroranalysismethods-20260121-0009] page:2:line:5 | Mitigations
    [sp26-erroranalysismethods-20260121-0010] page:2:line:6 | Cases
    [sp26-erroranalysismethods-20260121-0011] page:2:line:7 | 2
    [sp26-erroranalysismethods-20260121-0012] page:2:line:8 | 1/21/26
    [sp26-erroranalysismethods-20260121-0013] page:2:line:9 | ENP-0112
    [sp26-erroranalysismethods-20260121-0014] page:3:line:1 | A WORD ABOUT MODELS (FRAMEWORKS)
    [sp26-erroranalysismethods-20260121-0015] page:3:line:2 | "All models are wrong, but some are useful”
    [sp26-erroranalysismethods-20260121-0016] page:3:line:3 | - George E.P. Box, British statistician
    [sp26-erroranalysismethods-20260121-0017] page:3:line:4 | 1/21/26
    [sp26-erroranalysismethods-20260121-0018] page:3:line:5 | ENP-0112
    [sp26-erroranalysismethods-20260121-0019] page:3:line:6 | 3
    [sp26-erroranalysismethods-20260121-0020] page:4:line:1 | HOW DO YOU DEFINE
    [sp26-erroranalysismethods-20260121-0021] page:4:line:2 | “HUMAN ERROR”?
    [sp26-erroranalysismethods-20260121-0022] page:4:line:3 | 75 – 95% industrial accidents are caused by human error (Norman, 2013)
    [sp26-erroranalysismethods-20260121-0023] page:4:line:4 | “90% of automotive accidents are due to human error” (Too many unnamed automotive researchers!)
    [sp26-erroranalysismethods-20260121-0024] page:4:line:5 | 1/21/26
    [sp26-erroranalysismethods-20260121-0025] page:4:line:6 | ENP-0112
    [sp26-erroranalysismethods-20260121-0026] page:4:line:7 | 4
    [sp26-erroranalysismethods-20260121-0027] page:5:line:1 | TYPES OF HUMAN ERROR
    [sp26-erroranalysismethods-20260121-0028] page:5:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0029] page:5:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0030] page:5:line:4 | 5
    [sp26-erroranalysismethods-20260121-0031] page:5:line:5 | Adapted from Reason, 1990
    [sp26-erroranalysismethods-20260121-0032] page:5:line:6 | Unsafe
    [sp26-erroranalysismethods-20260121-0033] page:5:line:7 | Acts
    [sp26-erroranalysismethods-20260121-0034] page:5:line:8 | Unintended
    [sp26-erroranalysismethods-20260121-0035] page:5:line:9 | Action
    [sp26-erroranalysismethods-20260121-0036] page:5:line:10 | Intended
    [sp26-erroranalysismethods-20260121-0037] page:5:line:11 | Action
    [sp26-erroranalysismethods-20260121-0038] page:5:line:12 | Slip
    [sp26-erroranalysismethods-20260121-0039] page:5:line:13 | Violation
    [sp26-erroranalysismethods-20260121-0040] page:5:line:14 | Lapse
    [sp26-erroranalysismethods-20260121-0041] page:5:line:15 | Mistake
    [sp26-erroranalysismethods-20260121-0042] page:5:line:16 | Basic Error
    [sp26-erroranalysismethods-20260121-0043] page:5:line:17 | Types
    [sp26-erroranalysismethods-20260121-0044] page:5:line:18 | Incorrect actions performed in a
    [sp26-erroranalysismethods-20260121-0045] page:5:line:19 | sequence that was otherwise good.
    [sp26-erroranalysismethods-20260121-0046] page:5:line:20 | Omission of a step, the intended
    [sp26-erroranalysismethods-20260121-0047] page:5:line:21 | action was not performed
    [sp26-erroranalysismethods-20260121-0048] page:5:line:22 | Human does what was intended, but
    [sp26-erroranalysismethods-20260121-0049] page:5:line:23 | planned action is incorrect.
    [sp26-erroranalysismethods-20260121-0050] page:5:line:24 | Failure to follow established
    [sp26-erroranalysismethods-20260121-0051] page:5:line:25 | procedures or guidelines
    [sp26-erroranalysismethods-20260121-0052] page:6:line:1 | EXAMPLES OF HUMAN ERRORS
    [sp26-erroranalysismethods-20260121-0053] page:6:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0054] page:6:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0055] page:6:line:4 | 6
    [sp26-erroranalysismethods-20260121-0056] page:6:line:5 | Slips
    [sp26-erroranalysismethods-20260121-0057] page:6:line:6 | • Intrusion
    [sp26-erroranalysismethods-20260121-0058] page:6:line:7 | • Omission
    [sp26-erroranalysismethods-20260121-0059] page:6:line:8 | • Reversal
    [sp26-erroranalysismethods-20260121-0060] page:6:line:9 | • Misordering
    [sp26-erroranalysismethods-20260121-0061] page:6:line:10 | Lapses
    [sp26-erroranalysismethods-20260121-0062] page:6:line:11 | • Omitting planned
    [sp26-erroranalysismethods-20260121-0063] page:6:line:12 | items
    [sp26-erroranalysismethods-20260121-0064] page:6:line:13 | • Place-losing
    [sp26-erroranalysismethods-20260121-0065] page:6:line:14 | • Forgetting
    [sp26-erroranalysismethods-20260121-0066] page:6:line:15 | intentions
    [sp26-erroranalysismethods-20260121-0067] page:6:line:16 | Mistakes
    [sp26-erroranalysismethods-20260121-0068] page:6:line:17 | • Misapplication of
    [sp26-erroranalysismethods-20260121-0069] page:6:line:18 | good rule
    [sp26-erroranalysismethods-20260121-0070] page:6:line:19 | • Application of bad
    [sp26-erroranalysismethods-20260121-0071] page:6:line:20 | rule
    [sp26-erroranalysismethods-20260121-0072] page:6:line:21 | • Decision with no
    [sp26-erroranalysismethods-20260121-0073] page:6:line:22 | previous domain
    [sp26-erroranalysismethods-20260121-0074] page:6:line:23 | knowledge
    [sp26-erroranalysismethods-20260121-0075] page:6:line:24 | Violations
    [sp26-erroranalysismethods-20260121-0076] page:6:line:25 | • Routine violations
    [sp26-erroranalysismethods-20260121-0077] page:6:line:26 | • Exceptional
    [sp26-erroranalysismethods-20260121-0078] page:6:line:27 | violations
    [sp26-erroranalysismethods-20260121-0079] page:7:line:1 | EXAMPLE: ERROR DUE TO DESIGN
    [sp26-erroranalysismethods-20260121-0080] page:7:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0081] page:7:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0082] page:7:line:4 | 7
    [sp26-erroranalysismethods-20260121-0083] page:7:line:5 | https://www.faa.gov/lessons_learned/transport_airplane/accidents/F-GGED
    [sp26-erroranalysismethods-20260121-0084] page:7:line:6 | Display difference -
    [sp26-erroranalysismethods-20260121-0085] page:7:line:7 | Flight Path Angle vs.
    [sp26-erroranalysismethods-20260121-0086] page:7:line:8 | Vertical Speed
    [sp26-erroranalysismethods-20260121-0087] page:7:line:9 | Flight Control Unit
    [sp26-erroranalysismethods-20260121-0088] page:7:line:10 | display
    [sp26-erroranalysismethods-20260121-0089] page:7:line:11 | Air Inter A320
    [sp26-erroranalysismethods-20260121-0090] page:8:line:1 | HEINRICH’S TRIANGLE
    [sp26-erroranalysismethods-20260121-0091] page:8:line:2 | o Herbert William Heinrich
    [sp26-erroranalysismethods-20260121-0092] page:8:line:3 | o “Industrial Accident Prevention: A Scientific Approach” (1931)
    [sp26-erroranalysismethods-20260121-0093] page:8:line:4 | o Relationship between accident types was derived from
    [sp26-erroranalysismethods-20260121-0094] page:8:line:5 | >75,000 industrial accident reports.
    [sp26-erroranalysismethods-20260121-0095] page:8:line:6 | o Suggested that 88% of all accidents results from an unsafe act.
    [sp26-erroranalysismethods-20260121-0096] page:8:line:7 | o Proposed that reducing the number of minor accidents
    [sp26-erroranalysismethods-20260121-0097] page:8:line:8 | would results in a corresponding drop in serious
    [sp26-erroranalysismethods-20260121-0098] page:8:line:9 | accidents.
    [sp26-erroranalysismethods-20260121-0099] page:8:line:10 | o Focus on workplace hazards and worker behavior
    [sp26-erroranalysismethods-20260121-0100] page:8:line:11 | 1/21/26
    [sp26-erroranalysismethods-20260121-0101] page:8:line:12 | ENP-0112
    [sp26-erroranalysismethods-20260121-0102] page:8:line:13 | 8
    [sp26-erroranalysismethods-20260121-0103] page:8:line:14 | Credit: Wikipedia
    [sp26-erroranalysismethods-20260121-0104] page:9:line:1 | CRITICISMS OF THIS APPROACH?
    [sp26-erroranalysismethods-20260121-0105] page:9:line:2 | o Blame is focused on the worker (“The Bad Apple Theory”)
    [sp26-erroranalysismethods-20260121-0106] page:9:line:3 | o Complex systems would be fine, were it not for the erratic behavior of some unreliable people (Bad Apples) in it.
    [sp26-erroranalysismethods-20260121-0107] page:9:line:4 | o What is the relationship between minor and major accidents?
    [sp26-erroranalysismethods-20260121-0108] page:9:line:5 | o Generalizable?
    [sp26-erroranalysismethods-20260121-0109] page:9:line:6 | o Commonality of the root causes?
    [sp26-erroranalysismethods-20260121-0110] page:9:line:7 | o What is the role of the system design?
    [sp26-erroranalysismethods-20260121-0111] page:9:line:8 | o What is the role of system management?
    [sp26-erroranalysismethods-20260121-0112] page:9:line:9 | 1/21/26
    [sp26-erroranalysismethods-20260121-0113] page:9:line:10 | ENP-0112
    [sp26-erroranalysismethods-20260121-0114] page:9:line:11 | 9
    [sp26-erroranalysismethods-20260121-0115] page:10:line:1 | ORIGIN OF ERRORS – ROOT CAUSE ANALYSIS
    [sp26-erroranalysismethods-20260121-0116] page:10:line:2 | 5 Whys
    [sp26-erroranalysismethods-20260121-0117] page:10:line:3 | Ishikawa Diagram
    [sp26-erroranalysismethods-20260121-0118] page:10:line:4 | 1/21/26
    [sp26-erroranalysismethods-20260121-0119] page:10:line:5 | ENP-0112
    [sp26-erroranalysismethods-20260121-0120] page:10:line:6 | 10
    [sp26-erroranalysismethods-20260121-0121] page:10:line:7 | Norman, 2013
    [sp26-erroranalysismethods-20260121-0122] page:10:line:8 | Credit: Wikipedia
    [sp26-erroranalysismethods-20260121-0123] page:11:line:1 | “Rather than being the main instigators of an accident, operators tend to
    [sp26-erroranalysismethods-20260121-0124] page:11:line:2 | be the inheritors of system defects created by poor design, incorrect
    [sp26-erroranalysismethods-20260121-0125] page:11:line:3 | installation, faulty maintenance and bad management decisions. Their
    [sp26-erroranalysismethods-20260121-0126] page:11:line:4 | part is usually that of adding the final garnish to a lethal brew whose
    [sp26-erroranalysismethods-20260121-0127] page:11:line:5 | ingredients have already been long in the cooking.” – James Reason
    [sp26-erroranalysismethods-20260121-0128] page:11:line:6 | (1990)
    [sp26-erroranalysismethods-20260121-0129] page:11:line:7 | 1/21/26
    [sp26-erroranalysismethods-20260121-0130] page:11:line:8 | ENP-0112
    [sp26-erroranalysismethods-20260121-0131] page:11:line:9 | 11
    [sp26-erroranalysismethods-20260121-0132] page:12:line:1 | UNDERSTANDING HAZARDS: LATENT FAILURE MODEL
    [sp26-erroranalysismethods-20260121-0133] page:12:line:2 | o Factor: condition that leads to an incident
    [sp26-erroranalysismethods-20260121-0134] page:12:line:3 | o Latent condition: a factor that exists prior to the incident
    [sp26-erroranalysismethods-20260121-0135] page:12:line:4 | o Active failure: unsafe act with immediate consequences
    [sp26-erroranalysismethods-20260121-0136] page:12:line:5 | o Latent failure: latent conditions may be dormant within a system and only become evident when they
    [sp26-erroranalysismethods-20260121-0137] page:12:line:6 | combine with other factors
    [sp26-erroranalysismethods-20260121-0138] page:12:line:7 | o Removed in space and time
    [sp26-erroranalysismethods-20260121-0139] page:12:line:8 | o Inherent system defects
    [sp26-erroranalysismethods-20260121-0140] page:12:line:9 | o Caused by designers, decision makers, etc.
    [sp26-erroranalysismethods-20260121-0141] page:12:line:10 | o Greatest threat to high tech systems, e.g., Challenger
    [sp26-erroranalysismethods-20260121-0142] page:12:line:11 | o Caused by circumstances, i.e., scheduling problems, inadequate training, lack of resources
    [sp26-erroranalysismethods-20260121-0143] page:12:line:12 | 12
    [sp26-erroranalysismethods-20260121-0144] page:12:line:13 | Woods et al., 2010
    [sp26-erroranalysismethods-20260121-0145] page:12:line:14 | 1/21/26
    [sp26-erroranalysismethods-20260121-0146] page:12:line:15 | ENP-0112
    [sp26-erroranalysismethods-20260121-0147] page:13:line:1 | LATENT FAILURE MODEL
    [sp26-erroranalysismethods-20260121-0148] page:13:line:2 | o Layers of defenses and safeguards are in place to prevent hazards from
    [sp26-erroranalysismethods-20260121-0149] page:13:line:3 | becoming incidents
    [sp26-erroranalysismethods-20260121-0150] page:13:line:4 | o Safeguards can include presence of warning alarms, use of checklists,
    [sp26-erroranalysismethods-20260121-0151] page:13:line:5 | sensibility checks, etc.
    [sp26-erroranalysismethods-20260121-0152] page:13:line:6 | o More layers → more complexity but safer?
    [sp26-erroranalysismethods-20260121-0153] page:13:line:7 | o Defenses could include training, maintenance, safety culture,
    [sp26-erroranalysismethods-20260121-0154] page:13:line:8 | psychological precursors could be fatigue, organizational culture
    [sp26-erroranalysismethods-20260121-0155] page:13:line:9 | o Defenses have weaknesses though (the holes in each layer) that are
    [sp26-erroranalysismethods-20260121-0156] page:13:line:10 | varying in size and location over time
    [sp26-erroranalysismethods-20260121-0157] page:13:line:11 | o The active and latent failures open the holes in defense layers
    [sp26-erroranalysismethods-20260121-0158] page:13:line:12 | o Presence of holes in a particular “slice” does not normally cause a bad
    [sp26-erroranalysismethods-20260121-0159] page:13:line:13 | outcome, but if momentarily there is a scenario that causes these to line
    [sp26-erroranalysismethods-20260121-0160] page:13:line:14 | up, there is opportunity for an accident
    [sp26-erroranalysismethods-20260121-0161] page:13:line:15 | 1/21/26
    [sp26-erroranalysismethods-20260121-0162] page:13:line:16 | ENP-0112
    [sp26-erroranalysismethods-20260121-0163] page:13:line:17 | 13
    [sp26-erroranalysismethods-20260121-0164] page:13:line:18 | Reason, 1990
    [sp26-erroranalysismethods-20260121-0165] page:14:line:1 | EXAMPLE SCENARIO
    [sp26-erroranalysismethods-20260121-0166] page:14:line:2 | “The aircraft lost oil pressure in all three of its engines in mid-flight. Two of the engines stopped, and the third gave out at about the time
    [sp26-erroranalysismethods-20260121-0167] page:14:line:3 | the crew safely landed the aircraft ….
    [sp26-erroranalysismethods-20260121-0168] page:14:line:4 | One of the tasks of mechanics is to replace an engine part, called a master chip detector, at scheduled intervals. The master chip
    [sp26-erroranalysismethods-20260121-0169] page:14:line:5 | detector fits into the engine and is used to detect engine wear. O-rings are used to prevent oil leakage when the part is inserted. The two
    [sp26-erroranalysismethods-20260121-0170] page:14:line:6 | mechanics for the flight in question had always gotten replacement master chip detectors from their foreman’s cabinet. These chip
    [sp26-erroranalysismethods-20260121-0171] page:14:line:7 | detectors were all ready to go, with new O-rings installed. The mechanics’ work cards specified that new O-rings should be installed with
    [sp26-erroranalysismethods-20260121-0172] page:14:line:8 | a space next to this instruction for their initials when the task was completed. However, their usual work situation meant that this step
    [sp26-erroranalysismethods-20260121-0173] page:14:line:9 | was unnecessary, because someone else (apparently their supervisor) was already installing new O-rings on the chip detectors.
    [sp26-erroranalysismethods-20260121-0174] page:14:line:10 | The night before the incident, an unusual event occurred. When the mechanics were ready to replace master chip detectors, they
    [sp26-erroranalysismethods-20260121-0175] page:14:line:11 | found there were no chip detectors in the foreman’s cabinet. The mechanics had to get the parts from the stockroom. The chip detectors
    [sp26-erroranalysismethods-20260121-0176] page:14:line:12 | were wrapped in a ‘semi-transparent sealed plastic package with a serviceable parts tag.’ The mechanics took the packages to the
    [sp26-erroranalysismethods-20260121-0177] page:14:line:13 | aircraft and replaced the detectors in low light conditions. It turned out the chip detectors did not have O-rings attached. The mechanics
    [sp26-erroranalysismethods-20260121-0178] page:14:line:14 | had not checked for them before installing them. There was a check procedure against improper seals: monitoring the engines to see if oil
    [sp26-erroranalysismethods-20260121-0179] page:14:line:15 | leaked. The technicians did this, but apparently not for a long enough time to detect oil leaks. … They could not work strictly from
    [sp26-erroranalysismethods-20260121-0180] page:14:line:16 | procedure; for example, the work card read ‘motor engine and check chip detector for leaks’ but it didn’t specify how long.”
    [sp26-erroranalysismethods-20260121-0181] page:14:line:17 | 1/21/26
    [sp26-erroranalysismethods-20260121-0182] page:14:line:18 | ENP-0112
    [sp26-erroranalysismethods-20260121-0183] page:14:line:19 | 14
    [sp26-erroranalysismethods-20260121-0184] page:14:line:20 | Excerpt from Woods et al., 2010
    [sp26-erroranalysismethods-20260121-0185] page:15:line:1 | 15
    [sp26-erroranalysismethods-20260121-0186] page:15:line:2 | LATENT FAILURE MODEL: CRITICISMS
    [sp26-erroranalysismethods-20260121-0187] page:15:line:3 | o This is a model for investigating incidents retrospectively and can be prone to hindsight bias.
    [sp26-erroranalysismethods-20260121-0188] page:15:line:4 | o Does not explain how latent failures (holes)…
    [sp26-erroranalysismethods-20260121-0189] page:15:line:5 | o Are created within the defensive layers
    [sp26-erroranalysismethods-20260121-0190] page:15:line:6 | o Become ”aligned” to be primed for the initiating event/act
    [sp26-erroranalysismethods-20260121-0191] page:15:line:7 | o Evolve over time
    [sp26-erroranalysismethods-20260121-0192] page:15:line:8 | o Interact with unsafe acts
    [sp26-erroranalysismethods-20260121-0193] page:15:line:9 | o Assumes a linear causality or precedence in the layers
    [sp26-erroranalysismethods-20260121-0194] page:15:line:10 | o Limited predictive capability
    [sp26-erroranalysismethods-20260121-0195] page:15:line:11 | o Cannot describe how changes in the system will affect safety
    [sp26-erroranalysismethods-20260121-0196] page:15:line:12 | 1/21/26
    [sp26-erroranalysismethods-20260121-0197] page:15:line:13 | ENP-0112
    [sp26-erroranalysismethods-20260121-0198] page:16:line:1 | THE HUMAN FACTORS ANALYSIS AND
    [sp26-erroranalysismethods-20260121-0199] page:16:line:2 | CLASSIFICATION SYSTEM  (HFACS)
    [sp26-erroranalysismethods-20260121-0200] page:16:line:3 | • Drawing upon Reason’s concept of latent and active failures
    [sp26-erroranalysismethods-20260121-0201] page:16:line:4 | • HFACS describes four levels of failure:
    [sp26-erroranalysismethods-20260121-0202] page:16:line:5 | 1) Unsafe Acts
    [sp26-erroranalysismethods-20260121-0203] page:16:line:6 | 2) Preconditions for Unsafe Acts
    [sp26-erroranalysismethods-20260121-0204] page:16:line:7 | 3) Unsafe Supervision
    [sp26-erroranalysismethods-20260121-0205] page:16:line:8 | 4) Organizational Influences
    [sp26-erroranalysismethods-20260121-0206] page:16:line:9 | 17
    [sp26-erroranalysismethods-20260121-0207] page:16:line:10 | https://commons.erau.edu/cgi/viewcontent.cgi?article=1777&context=publication
    [sp26-erroranalysismethods-20260121-0208] page:16:line:11 | 1/21/26
    [sp26-erroranalysismethods-20260121-0209] page:16:line:12 | ENP-0112
    [sp26-erroranalysismethods-20260121-0210] page:16:line:13 | Credit: HFACS, Inc.
    [sp26-erroranalysismethods-20260121-0211] page:17:line:1 | 18
    [sp26-erroranalysismethods-20260121-0212] page:17:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0213] page:17:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0214] page:18:line:1 | 19
    [sp26-erroranalysismethods-20260121-0215] page:18:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0216] page:18:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0217] page:19:line:1 | 20
    [sp26-erroranalysismethods-20260121-0218] page:19:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0219] page:19:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0220] page:20:line:1 | 21
    [sp26-erroranalysismethods-20260121-0221] page:20:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0222] page:20:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0223] page:21:line:1 | HUMAN RELIABILITY ANALYSIS
    [sp26-erroranalysismethods-20260121-0224] page:21:line:2 | Broadly applied in a variety of domains to understand, manage and prevent the potential for
    [sp26-erroranalysismethods-20260121-0225] page:21:line:3 | human errors.
    [sp26-erroranalysismethods-20260121-0226] page:21:line:4 | • Potentially time consuming and may require subject matter experts to perform
    [sp26-erroranalysismethods-20260121-0227] page:21:line:5 | 1.
    [sp26-erroranalysismethods-20260121-0228] page:21:line:6 | Identify critical tasks.
    [sp26-erroranalysismethods-20260121-0229] page:21:line:7 | 2.
    [sp26-erroranalysismethods-20260121-0230] page:21:line:8 | Perform a Hierarchical Task Analysis
    [sp26-erroranalysismethods-20260121-0231] page:21:line:9 | 3.
    [sp26-erroranalysismethods-20260121-0232] page:21:line:10 | Identify errors, consequences, defenses (Tabular Task Analysis)
    [sp26-erroranalysismethods-20260121-0233] page:21:line:11 | 4.
    [sp26-erroranalysismethods-20260121-0234] page:21:line:12 | Estimate human error probabilities
    [sp26-erroranalysismethods-20260121-0235] page:21:line:13 | • HRA Example: Crane operations in shipping facility
    [sp26-erroranalysismethods-20260121-0236] page:21:line:14 | • HTA Example: Naweed et al., Applied Ergonomics, 2018
    [sp26-erroranalysismethods-20260121-0237] page:21:line:15 | 1/21/26
    [sp26-erroranalysismethods-20260121-0238] page:21:line:16 | ENP-0112
    [sp26-erroranalysismethods-20260121-0239] page:21:line:17 | 22
    [sp26-erroranalysismethods-20260121-0240] page:22:line:1 | IDENTIFY CRITICAL TASKS
    [sp26-erroranalysismethods-20260121-0241] page:22:line:2 | o Through formal hazard and operability studies (HAZOPs) which inevitably raise human error as a
    [sp26-erroranalysismethods-20260121-0242] page:22:line:3 | source of risk
    [sp26-erroranalysismethods-20260121-0243] page:22:line:4 | o By examining historical data, accident and near miss records to find out what happened in the past
    [sp26-erroranalysismethods-20260121-0244] page:22:line:5 | and establish whether it is under better control now.
    [sp26-erroranalysismethods-20260121-0245] page:22:line:6 | o By ‘brainstorming’ – ask experts (designers or users of systems and equipment) which errors could
    [sp26-erroranalysismethods-20260121-0246] page:22:line:7 | lead to a major problem
    [sp26-erroranalysismethods-20260121-0247] page:22:line:8 | o By behavioral safety observation.
    [sp26-erroranalysismethods-20260121-0248] page:22:line:9 | Example: The task is to move a container by crane to a new location. This task is ‘critical’ because the
    [sp26-erroranalysismethods-20260121-0249] page:22:line:10 | only available route for the load is over a production area. If the load drops during transit, it could break
    [sp26-erroranalysismethods-20260121-0250] page:22:line:11 | vessels and pipework releasing highly flammable gas.
    [sp26-erroranalysismethods-20260121-0251] page:22:line:12 | 1/21/26
    [sp26-erroranalysismethods-20260121-0252] page:22:line:13 | ENP-0112
    [sp26-erroranalysismethods-20260121-0253] page:22:line:14 | 23
    [sp26-erroranalysismethods-20260121-0254] page:23:line:1 | Plan 1: 1.1 – 1.2 – 1.3 – 1.4 …
    [sp26-erroranalysismethods-20260121-0255] page:23:line:2 | Plan 1.2: 1.2.1 – 1.2.2 – 1.2.3 – 1.2.4
    [sp26-erroranalysismethods-20260121-0256] page:23:line:3 | HIERARCHICAL TASK ANALYSIS (HTA)
    [sp26-erroranalysismethods-20260121-0257] page:23:line:4 | oDescribe an activity as a hierarchy of goals, sub-goals, operations, and plans.
    [sp26-erroranalysismethods-20260121-0258] page:23:line:5 | o HTA is one of many forms of task analysis (see Stanton et al, 2013)
    [sp26-erroranalysismethods-20260121-0259] page:23:line:6 | o Widely used in many domains
    [sp26-erroranalysismethods-20260121-0260] page:23:line:7 | o More art than science?
    [sp26-erroranalysismethods-20260121-0261] page:23:line:8 | 1/21/26
    [sp26-erroranalysismethods-20260121-0262] page:23:line:9 | ENP-0112
    [sp26-erroranalysismethods-20260121-0263] page:23:line:10 | 24
    [sp26-erroranalysismethods-20260121-0264] page:24:line:1 | TABULAR TASK ANALYSIS
    [sp26-erroranalysismethods-20260121-0265] page:24:line:2 | oTake each bottom level task step from the HTA and analyzes specific aspects of
    [sp26-erroranalysismethods-20260121-0266] page:24:line:3 | each step such as possible errors, consequences, defenses, etc.
    [sp26-erroranalysismethods-20260121-0267] page:24:line:4 | 1/21/26
    [sp26-erroranalysismethods-20260121-0268] page:24:line:5 | 25
    [sp26-erroranalysismethods-20260121-0269] page:24:line:6 | ENP-0112
    [sp26-erroranalysismethods-20260121-0270] page:25:line:1 | ESTIMATE HUMAN ERROR PROBABILITIES
    [sp26-erroranalysismethods-20260121-0271] page:25:line:2 | • Many models have been developed to estimate probabilities
    [sp26-erroranalysismethods-20260121-0272] page:25:line:3 | • THERP (Technique for Human Error Rate Prediction) is one of the oldest  and most
    [sp26-erroranalysismethods-20260121-0273] page:25:line:4 | widely used.
    [sp26-erroranalysismethods-20260121-0274] page:25:line:5 | • Human performance has an intrinsic dynamic nature, and HRA experts are focusing
    [sp26-erroranalysismethods-20260121-0275] page:25:line:6 | on including this aspect in novel analysis methods. For instance, the Simulator for
    [sp26-erroranalysismethods-20260121-0276] page:25:line:7 | Human Error Probability Analysis (SHERPA) [81] aims to merge the advantages of
    [sp26-erroranalysismethods-20260121-0277] page:25:line:8 | simulation tools and the principles of traditional HRA methods.
    [sp26-erroranalysismethods-20260121-0278] page:25:line:9 | 1/21/26
    [sp26-erroranalysismethods-20260121-0279] page:25:line:10 | 26
    [sp26-erroranalysismethods-20260121-0280] page:25:line:11 | ENP-0112
    [sp26-erroranalysismethods-20260121-0281] page:26:line:1 | “A systems approach to accident causation starts from the premise that
    [sp26-erroranalysismethods-20260121-0282] page:26:line:2 | human error is a symptom of a system that needs to be redesigned.
    [sp26-erroranalysismethods-20260121-0283] page:26:line:3 | Accident analysis should identify the design flaws and recommend ways
    [sp26-erroranalysismethods-20260121-0284] page:26:line:4 | they can be fixed, not blame the operators for the consequences of those
    [sp26-erroranalysismethods-20260121-0285] page:26:line:5 | design flaws.” – Nancy Leveson (2019)
    [sp26-erroranalysismethods-20260121-0286] page:26:line:6 | 1/21/26
    [sp26-erroranalysismethods-20260121-0287] page:26:line:7 | ENP-0112
    [sp26-erroranalysismethods-20260121-0288] page:26:line:8 | 27
    [sp26-erroranalysismethods-20260121-0289] page:27:line:1 | 28
    [sp26-erroranalysismethods-20260121-0290] page:27:line:2 | UNDERSTANDING HAZARDS: SYSTEMS THEORY
    [sp26-erroranalysismethods-20260121-0291] page:27:line:3 | Leveson, 2011
    [sp26-erroranalysismethods-20260121-0292] page:27:line:4 | 1/21/26
    [sp26-erroranalysismethods-20260121-0293] page:27:line:5 | ENP-0112
    [sp26-erroranalysismethods-20260121-0294] page:28:line:1 | CAUSAL ANALYSIS BASED ON SYSTEM THEORY
    [sp26-erroranalysismethods-20260121-0295] page:28:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0296] page:28:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0297] page:28:line:4 | 29
    [sp26-erroranalysismethods-20260121-0298] page:28:line:5 | Leveson, 2019
    [sp26-erroranalysismethods-20260121-0299] page:29:line:1 | SYSTEM THEORETIC PROCESS ANALYSIS
    [sp26-erroranalysismethods-20260121-0300] page:29:line:2 | 1/21/26
    [sp26-erroranalysismethods-20260121-0301] page:29:line:3 | ENP-0112
    [sp26-erroranalysismethods-20260121-0302] page:29:line:4 | 30
    [sp26-erroranalysismethods-20260121-0303] page:29:line:5 | Leveson, 2018
    [sp26-erroranalysismethods-20260121-0304] page:30:line:1 | REFERENCES
    [sp26-erroranalysismethods-20260121-0305] page:30:line:2 | • Dekker, S. The Field Guide to Understanding 'Human Error' (3rd ed.). CRC Press, 2014. https://doi.org/10.1201/9781317031833
    [sp26-erroranalysismethods-20260121-0306] page:30:line:3 | • Leveson, N. Engineering a Safer World: Systems Thinking Applied to Safety. The MIT Press, 2011.
    [sp26-erroranalysismethods-20260121-0307] page:30:line:4 | • Leveson, N. STPA HANDBOOK, 2019. https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf
    [sp26-erroranalysismethods-20260121-0308] page:30:line:5 | • Leveson, N. CAST HANDBOOK: How to Learn More from Incidents and Accidents, 2019.
    [sp26-erroranalysismethods-20260121-0309] page:30:line:6 | https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_Handbook.pdf
    [sp26-erroranalysismethods-20260121-0310] page:30:line:7 | • Norman, D. The Design of Everyday Things. The MIT Press, 2013.
    [sp26-erroranalysismethods-20260121-0311] page:30:line:8 | • Reason, J. Human Error. Cambridge University Press, 1990.
    [sp26-erroranalysismethods-20260121-0312] page:30:line:9 | • Stanton,  N., Paul M. Salmon  Laura A. Rafferty  Guy H. Walker, Human Factors Methods, 2nd ed., Ashgate Publishing, 2013.
    [sp26-erroranalysismethods-20260121-0313] page:30:line:10 | • Woods, D., Dekker, S., Cook, R., Johannesen, L., & Sarter, N. Behind Human Error (2nd ed.). CRC Press, 2010.
    [sp26-erroranalysismethods-20260121-0314] page:30:line:11 | https://doi.org/10.1201/9781315568935
    [sp26-erroranalysismethods-20260121-0315] page:30:line:12 | 1/21/26
    [sp26-erroranalysismethods-20260121-0316] page:30:line:13 | ENP-0112
    [sp26-erroranalysismethods-20260121-0317] page:30:line:14 | 31
    ```
