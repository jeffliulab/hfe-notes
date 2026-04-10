# Situation Awareness

This page breaks “seeing information” into three layers: perception, comprehension, and projection. The goal is to show that visible information and understandable situation are not the same thing.

!!! note "Core Question"
    Why can a system display large amounts of information and still leave the operator unable to understand the current situation or predict what happens next?

## Key Takeaways

- Situation awareness includes at least perception,
  comprehension,
  and projection.
- Visible information does not guarantee meaning,
  and meaning does not guarantee prediction.
- Many display,
  CRM,
  monitoring,
  and automation problems ultimately return to breaks in SA.
- The essence of SA is not information quantity but whether information is organized into an actionable mental model.

## Remember This First

!!! tip "Keep This Sentence in Mind"
    Keep one sentence in mind:
    situation awareness is not merely about looking harder;
    it is about turning seen cues into an accurate current picture and one step of forward projection.

## What the Three Layers Actually Mean

The three layers in the course are:

1. `perception`: whether the critical cues were noticed
2. `comprehension`: whether the cues were integrated into the correct current picture
3. `projection`: where the system is likely to go next if nobody intervenes

## Why the Second and Third Layers Break So Easily

Operators may see the readings,
alerts,
and state changes yet still not know which cue has priority,
how several signals relate,
or how the situation will evolve over the next seconds.
In other words,
the hard part of SA is often not noticing but organizing and projecting.

!!! warning "The Most Common Misunderstanding"
    Seeing the data does not mean SA has been achieved.
    Many accidents unfold in the state where the data is present but the situation has not actually been assembled in the operator’s mind.

!!! example "Example: Why “Visible Information” Is Still Not Enough"
    A flight crew may see altitude,
    speed,
    and alerts and still fail to realize that the signals collectively point to a diverging flight state.
    The issue is not whether the data exists,
    but whether it has been integrated into the right picture and converted into early intervention.

## Why So Many Course Topics Return to SA

The display page asks how information becomes visible,
the CRM page asks how information becomes shared across the team,
the monitoring page asks how state awareness is sustained,
and the spatial-disorientation page asks whether the operator can still build the correct picture when sensory intuition conflicts with instruments.
At root they all ask whether the system helps people form sufficient SA.

!!! note "One-Sentence Conclusion"
    The core of situation awareness is not “more information,” but whether information has been organized into understanding and prediction that support action.

## How the Three SA Breakdowns Appear in Real Analysis

The most useful takeaway is not only the three-layer definition,
but how to use the layers during review:

- if the critical cue was never noticed, the breakdown is often Level 1
- if the cue was seen but interpreted wrongly, the breakdown is often Level 2
- if current state was understood reasonably well but the future path was predicted badly, the breakdown is often Level 3

Once the break layer is identified,
mitigation becomes far more targeted:
improve detectability,
improve mental-model support,
or improve projection support.

## Why SA Is Not Only an Individual State but Also a Team State

Later in the course a recurring reminder appears:
even if individuals each notice part of the information,
the team may still fail to form one shared picture.
Individual SA and team SA are therefore not automatically the same thing.

At that point the problem is no longer only in the display.
It also belongs to communication,
briefing,
cross-check,
and authority structure.
Whether the team rebuilds one common picture from distributed cues often determines whether later action becomes coordinated.

!!! example "Example: Why “Everyone Saw a Piece of It” Does Not Mean the Team Understood the Situation"
    One person may notice the speed anomaly,
    another the alert,
    and a third the procedure-state change,
    yet the team can still continue along the wrong path if those cues are never assembled into one shared picture.
    The key to SA is not whether cues exist in distributed form,
    but whether they are organized into one coherent picture.

## Why SA Also Depends on How Fast the Picture Gets Updated

SA is not the static possession of one picture.
It is the continuous updating of that picture.
In high-risk systems the state keeps changing,
and if the team is still operating from the understanding of a few minutes earlier,
the picture may already be stale even if it was once correct.

SA analysis therefore cannot ask only whether a picture existed.
It also has to ask whether the picture was updated quickly enough.
Many events do not begin with total ignorance,
but with failure to replace the old picture in time.

## Chapter Summary

!!! tip "What To Carry Forward"
    - SA includes perception,
      comprehension,
      and projection.
    - Visible information does not equal true understanding.
    - Many HFE topics ultimately return to whether SA breaks down.
    - The key is forming an actionable mental model.


## Source Scope and Related Topics

The teaching notes come first. This section lists the source files used on the page, and the appendix keeps the full line-by-line transcription for verification.

- Section: `Human Performance`
- Source files: 1
- Text units: 200
- Visuals/previews: 3

| Source | Type | Text Units | Visuals | Download |
| --- | --- | ---: | ---: | --- |
| `Sp26_SituationAwareness_20260325.pdf` | `pdf` | 200 | 3 | [open](../assets/source_files/Lectures_Spring_2026/Sp26_SituationAwareness_20260325.pdf) |

## Related Topics

- [Attention and Monitoring](attention_and_monitoring.en.md)
- [Crew Resource Management](../HFE_Aviation_Automation/crew_resource_management.en.md)
- [Spatial Disorientation](spatial_disorientation.en.md)

## Original Transcription and Coverage Mapping

The collapsible blocks below preserve page/slide-level source transcription. Each `unit_id` maps one-to-one in `data/coverage_map.json`.

??? info "Sp26_SituationAwareness_20260325.pdf | 200 text units"
    Download source: [Sp26_SituationAwareness_20260325.pdf](../assets/source_files/Lectures_Spring_2026/Sp26_SituationAwareness_20260325.pdf)
    Mapped page: `situation_awareness`
    
    ```text
    [sp26-situationawareness-20260325-0001] page:1:line:1 | SITUATION
    [sp26-situationawareness-20260325-0002] page:1:line:2 | AWARENESS
    [sp26-situationawareness-20260325-0003] page:1:line:3 | Dr. Andrew Liu
    [sp26-situationawareness-20260325-0004] page:1:line:4 | ENP-0112
    [sp26-situationawareness-20260325-0005] page:1:line:5 | Credit: Gary Larson, The Far Side
    [sp26-situationawareness-20260325-0006] page:2:line:1 | SITUATION AWARENESS
    [sp26-situationawareness-20260325-0007] page:2:line:2 | “Situation awareness is the perception of the elements in the environment within a
    [sp26-situationawareness-20260325-0008] page:2:line:3 | volume of time and space, the comprehension of their meaning, and the projection of
    [sp26-situationawareness-20260325-0009] page:2:line:4 | their status in the near future.”     -- Endsley (1995)
    [sp26-situationawareness-20260325-0010] page:2:line:5 | 3
    [sp26-situationawareness-20260325-0011] page:2:line:6 | • Perception (Level 1): Recognizing the status, attributes and dynamics of relevant
    [sp26-situationawareness-20260325-0012] page:2:line:7 | elements in the environment.
    [sp26-situationawareness-20260325-0013] page:2:line:8 | • Comprehension (Level 2): Understanding the significance of the relevant
    [sp26-situationawareness-20260325-0014] page:2:line:9 | elements in the context of operator goals.
    [sp26-situationawareness-20260325-0015] page:2:line:10 | • Projection (Level 3): Projecting the future actions of the elements in the
    [sp26-situationawareness-20260325-0016] page:2:line:11 | environment while accounting for their status and dynamics.
    [sp26-situationawareness-20260325-0017] page:2:line:12 | 3/25/26
    [sp26-situationawareness-20260325-0018] page:2:line:13 | ENP-0112
    [sp26-situationawareness-20260325-0019] page:3:line:1 | SITUATION AWARENESS IN DECISION MAKING
    [sp26-situationawareness-20260325-0020] page:3:line:2 | 4
    [sp26-situationawareness-20260325-0021] page:3:line:3 | 3/25/26
    [sp26-situationawareness-20260325-0022] page:3:line:4 | ENP-0112
    [sp26-situationawareness-20260325-0023] page:3:line:5 | Endsley, 1995
    [sp26-situationawareness-20260325-0024] page:4:line:1 | EXAMPLE OF SA ELEMENTS: DRIVING A CAR
    [sp26-situationawareness-20260325-0025] page:4:line:2 | Perception (Level 1)                  Comprehension (Level 2)                 Projection (Level 3)
    [sp26-situationawareness-20260325-0026] page:4:line:3 | 6
    [sp26-situationawareness-20260325-0027] page:4:line:4 | 3/25/26
    [sp26-situationawareness-20260325-0028] page:4:line:5 | ENP-0112
    [sp26-situationawareness-20260325-0029] page:5:line:1 | BREAKDOWNS IN SA
    [sp26-situationawareness-20260325-0030] page:5:line:2 | • Perception (Level 1):
    [sp26-situationawareness-20260325-0031] page:5:line:3 | •
    [sp26-situationawareness-20260325-0032] page:5:line:4 | Lack of detectability or distinguishability
    [sp26-situationawareness-20260325-0033] page:5:line:5 | •
    [sp26-situationawareness-20260325-0034] page:5:line:6 | Lack of attention
    [sp26-situationawareness-20260325-0035] page:5:line:7 | •
    [sp26-situationawareness-20260325-0036] page:5:line:8 | Visual obstructions, auditory masking
    [sp26-situationawareness-20260325-0037] page:5:line:9 | •
    [sp26-situationawareness-20260325-0038] page:5:line:10 | …
    [sp26-situationawareness-20260325-0039] page:5:line:11 | • Comprehension (Level 2):
    [sp26-situationawareness-20260325-0040] page:5:line:12 | •
    [sp26-situationawareness-20260325-0041] page:5:line:13 | No mental model for environment/observations
    [sp26-situationawareness-20260325-0042] page:5:line:14 | •
    [sp26-situationawareness-20260325-0043] page:5:line:15 | Incorrect mental model used to interpret perceived data
    [sp26-situationawareness-20260325-0044] page:5:line:16 | •
    [sp26-situationawareness-20260325-0045] page:5:line:17 | Data inappropriately used (e.g.,  auditory alarms that can have multiple meanings)
    [sp26-situationawareness-20260325-0046] page:5:line:18 | •
    [sp26-situationawareness-20260325-0047] page:5:line:19 | …
    [sp26-situationawareness-20260325-0048] page:5:line:20 | • Projection (Level 3):
    [sp26-situationawareness-20260325-0049] page:5:line:21 | •
    [sp26-situationawareness-20260325-0050] page:5:line:22 | Lack of a good enough mental model
    [sp26-situationawareness-20260325-0051] page:5:line:23 | •
    [sp26-situationawareness-20260325-0052] page:5:line:24 | Limited attentional or memory resources to perform projection
    [sp26-situationawareness-20260325-0053] page:5:line:25 | •
    [sp26-situationawareness-20260325-0054] page:5:line:26 | …
    [sp26-situationawareness-20260325-0055] page:5:line:27 | 3/25/26
    [sp26-situationawareness-20260325-0056] page:5:line:28 | ENP-0112
    [sp26-situationawareness-20260325-0057] page:5:line:29 | 7
    [sp26-situationawareness-20260325-0058] page:5:line:30 | A breakdown in a level is when you do not
    [sp26-situationawareness-20260325-0059] page:5:line:31 | have the relevant output from the SA level
    [sp26-situationawareness-20260325-0060] page:6:line:1 | AMTRAK ACCIDENT REVISITED
    [sp26-situationawareness-20260325-0061] page:6:line:2 | • Where did the breakdown in
    [sp26-situationawareness-20260325-0062] page:6:line:3 | situation awareness occur?
    [sp26-situationawareness-20260325-0063] page:6:line:4 | • Level 1 – Perception
    [sp26-situationawareness-20260325-0064] page:6:line:5 | • Level 2 – Comprehension
    [sp26-situationawareness-20260325-0065] page:6:line:6 | • Level 3 - Projection
    [sp26-situationawareness-20260325-0066] page:6:line:7 | 3/25/26
    [sp26-situationawareness-20260325-0067] page:6:line:8 | ENP-0112
    [sp26-situationawareness-20260325-0068] page:6:line:9 | 8
    [sp26-situationawareness-20260325-0069] page:7:line:1 | TEAM SITUATION AWARENESS
    [sp26-situationawareness-20260325-0070] page:7:line:2 | 9
    [sp26-situationawareness-20260325-0071] page:7:line:3 | Endsley, 1995
    [sp26-situationawareness-20260325-0072] page:7:line:4 | 3/25/26
    [sp26-situationawareness-20260325-0073] page:7:line:5 | ENP-0112
    [sp26-situationawareness-20260325-0074] page:8:line:1 | UBER ACCIDENT, MARCH 2018
    [sp26-situationawareness-20260325-0075] page:8:line:2 | • Operator took self-driving car out of garage to
    [sp26-situationawareness-20260325-0076] page:8:line:3 | begin evaluations at 9:14 pm
    [sp26-situationawareness-20260325-0077] page:8:line:4 | • Self-driving system in computer control mode
    [sp26-situationawareness-20260325-0078] page:8:line:5 | struck a pedestrian at 9:58 pm
    [sp26-situationawareness-20260325-0079] page:8:line:6 | • Human operator intervened <1 sec before impact
    [sp26-situationawareness-20260325-0080] page:8:line:7 | (engaged the steering wheel)
    [sp26-situationawareness-20260325-0081] page:8:line:8 | • The vehicle speed at impact was 39 mph.
    [sp26-situationawareness-20260325-0082] page:8:line:9 | • Operator began braking less than a second after
    [sp26-situationawareness-20260325-0083] page:8:line:10 | the impact.
    [sp26-situationawareness-20260325-0084] page:8:line:11 | • The data showed that all aspects of the self-driving
    [sp26-situationawareness-20260325-0085] page:8:line:12 | system were operating normally at the time of the
    [sp26-situationawareness-20260325-0086] page:8:line:13 | crash, and that there were no faults or diagnostic
    [sp26-situationawareness-20260325-0087] page:8:line:14 | messages.
    [sp26-situationawareness-20260325-0088] page:8:line:15 | 11
    [sp26-situationawareness-20260325-0089] page:8:line:16 | NTSB/HAR-19/03
    [sp26-situationawareness-20260325-0090] page:8:line:17 | 3/25/26
    [sp26-situationawareness-20260325-0091] page:8:line:18 | ENP-0112
    [sp26-situationawareness-20260325-0092] page:9:line:1 | UBER ACCIDENT, MARCH 2018
    [sp26-situationawareness-20260325-0093] page:9:line:2 | • Software classified the pedestrian as an unknown
    [sp26-situationawareness-20260325-0094] page:9:line:3 | object, vehicle, and bicycle with varying
    [sp26-situationawareness-20260325-0095] page:9:line:4 | probabilities and expectations of future travel
    [sp26-situationawareness-20260325-0096] page:9:line:5 | path (first registered 6 seconds prior to impact).
    [sp26-situationawareness-20260325-0097] page:9:line:6 | • 1.3 seconds before impact, the software
    [sp26-situationawareness-20260325-0098] page:9:line:7 | determined that an emergency braking maneuver
    [sp26-situationawareness-20260325-0099] page:9:line:8 | was needed to mitigate a collision
    [sp26-situationawareness-20260325-0100] page:9:line:9 | • Emergency braking maneuvers are not enabled
    [sp26-situationawareness-20260325-0101] page:9:line:10 | while the vehicle is under computer control, to
    [sp26-situationawareness-20260325-0102] page:9:line:11 | reduce the potential for erratic vehicle behavior.
    [sp26-situationawareness-20260325-0103] page:9:line:12 | • The vehicle relies on the operator to intervene
    [sp26-situationawareness-20260325-0104] page:9:line:13 | and take action.
    [sp26-situationawareness-20260325-0105] page:9:line:14 | 12
    [sp26-situationawareness-20260325-0106] page:9:line:15 | Video released by Uber
    [sp26-situationawareness-20260325-0107] page:9:line:16 | 3/25/26
    [sp26-situationawareness-20260325-0108] page:9:line:17 | ENP-0112
    [sp26-situationawareness-20260325-0109] page:10:line:1 | DESIGN AN INTERFACE FOR TRANSITIONS
    [sp26-situationawareness-20260325-0110] page:10:line:2 | SUV interior
    [sp26-situationawareness-20260325-0111] page:10:line:3 | • Locations that could mount a cell
    [sp26-situationawareness-20260325-0112] page:10:line:4 | phone (yellow region in center
    [sp26-situationawareness-20260325-0113] page:10:line:5 | console)
    [sp26-situationawareness-20260325-0114] page:10:line:6 | • ADS engagement/disengagement
    [sp26-situationawareness-20260325-0115] page:10:line:7 | knob (red)
    [sp26-situationawareness-20260325-0116] page:10:line:8 | • ADS engagement button (blue)
    [sp26-situationawareness-20260325-0117] page:10:line:9 | • HMI (green)
    [sp26-situationawareness-20260325-0118] page:10:line:10 | • inset illustrating image on tablet.
    [sp26-situationawareness-20260325-0119] page:10:line:11 | 3/25/26
    [sp26-situationawareness-20260325-0120] page:10:line:12 | ENP-0112
    [sp26-situationawareness-20260325-0121] page:10:line:13 | 14
    [sp26-situationawareness-20260325-0122] page:11:line:1 | EXPERIMENTAL MEASURES OF SA
    [sp26-situationawareness-20260325-0123] page:11:line:2 | • Explicit: Questions are defined that specifically ask operators about their SA
    [sp26-situationawareness-20260325-0124] page:11:line:3 | • Implicit: Responses are used to infer an operator’s SA
    [sp26-situationawareness-20260325-0125] page:11:line:4 | • Subjective: Measures that are provided by the operator self-assessments or an
    [sp26-situationawareness-20260325-0126] page:11:line:5 | observer
    [sp26-situationawareness-20260325-0127] page:11:line:6 | • Objective?  What objective measures could we use?  What are the pitfalls?
    [sp26-situationawareness-20260325-0128] page:11:line:7 | 3/25/26
    [sp26-situationawareness-20260325-0129] page:11:line:8 | ENP-0112
    [sp26-situationawareness-20260325-0130] page:11:line:9 | 15
    [sp26-situationawareness-20260325-0131] page:12:line:1 | EXPLICIT MEASURES OF SA
    [sp26-situationawareness-20260325-0132] page:12:line:2 | Asks operators questions about their perception of the state of the system/environment
    [sp26-situationawareness-20260325-0133] page:12:line:3 | • Retrospective
    [sp26-situationawareness-20260325-0134] page:12:line:4 | • Time dependent
    [sp26-situationawareness-20260325-0135] page:12:line:5 | • Are you testing memory or SA?
    [sp26-situationawareness-20260325-0136] page:12:line:6 | • Concurrent (Situation Presence Assessment Method, SPAM)
    [sp26-situationawareness-20260325-0137] page:12:line:7 | • Workload may be high
    [sp26-situationawareness-20260325-0138] page:12:line:8 | • Adding another task
    [sp26-situationawareness-20260325-0139] page:12:line:9 | • Freeze (SA Global Assessment Technology, SAGAT)
    [sp26-situationawareness-20260325-0140] page:12:line:10 | • Intrusive
    [sp26-situationawareness-20260325-0141] page:12:line:11 | 16
    [sp26-situationawareness-20260325-0142] page:12:line:12 | (Durso et al., 1995)
    [sp26-situationawareness-20260325-0143] page:12:line:13 | (Endsley et al., 1988)
    [sp26-situationawareness-20260325-0144] page:12:line:14 | 3/25/26
    [sp26-situationawareness-20260325-0145] page:12:line:15 | ENP-0112
    [sp26-situationawareness-20260325-0146] page:13:line:1 | IMPLICIT MEASURES OF SA
    [sp26-situationawareness-20260325-0147] page:13:line:2 | Experimenter infers SA from performance-based measures
    [sp26-situationawareness-20260325-0148] page:13:line:3 | • Advantages
    [sp26-situationawareness-20260325-0149] page:13:line:4 | • Objective and unobtrusive
    [sp26-situationawareness-20260325-0150] page:13:line:5 | • Can be through embedded task measures
    [sp26-situationawareness-20260325-0151] page:13:line:6 | • Disadvantages
    [sp26-situationawareness-20260325-0152] page:13:line:7 | • Poor performance isn’t necessarily a function of low SA
    [sp26-situationawareness-20260325-0153] page:13:line:8 | 17
    [sp26-situationawareness-20260325-0154] page:13:line:9 | 3/25/26
    [sp26-situationawareness-20260325-0155] page:13:line:10 | ENP-0112
    [sp26-situationawareness-20260325-0156] page:14:line:1 | SUBJECTIVE MEASURES OF SA
    [sp26-situationawareness-20260325-0157] page:14:line:2 | • Self-assessment or observer assessment
    [sp26-situationawareness-20260325-0158] page:14:line:3 | • Situation Awareness Rating Technique (SART)
    [sp26-situationawareness-20260325-0159] page:14:line:4 | • Instability - Likelihood of situation changing suddenly
    [sp26-situationawareness-20260325-0160] page:14:line:5 | • Observer with system knowledge rates user’s
    [sp26-situationawareness-20260325-0161] page:14:line:6 | performance
    [sp26-situationawareness-20260325-0162] page:14:line:7 | • Advantages
    [sp26-situationawareness-20260325-0163] page:14:line:8 | • Doesn’t rely on memory
    [sp26-situationawareness-20260325-0164] page:14:line:9 | • Non-intrusive
    [sp26-situationawareness-20260325-0165] page:14:line:10 | • Disadvantages
    [sp26-situationawareness-20260325-0166] page:14:line:11 | • Are you testing confidence or SA?
    [sp26-situationawareness-20260325-0167] page:14:line:12 | • Rating workload or SA?
    [sp26-situationawareness-20260325-0168] page:14:line:13 | • Observer only has limited idea of the subject’s internal knowledge states
    [sp26-situationawareness-20260325-0169] page:14:line:14 | 18
    [sp26-situationawareness-20260325-0170] page:14:line:15 | SA = Understanding − (Demand − Supply)
    [sp26-situationawareness-20260325-0171] page:14:line:16 | 3/25/26
    [sp26-situationawareness-20260325-0172] page:14:line:17 | ENP-0112
    [sp26-situationawareness-20260325-0173] page:15:line:1 | REFERENCES
    [sp26-situationawareness-20260325-0174] page:15:line:2 | •
    [sp26-situationawareness-20260325-0175] page:15:line:3 | Durso, F.T., Truitt, T.R., Hackworth, C.A., Crutchfield, J.M., Nikolic, D., Moertl, P.M., Ohrt, D. & Manning, C.A. (1995). Expertise and Chess: a Pilot
    [sp26-situationawareness-20260325-0176] page:15:line:4 | Study Comparing Situation Awareness Methodologies. In: D.J. Garland & M. Endsley (Eds), Experimental Analysis and Measurement of Situation
    [sp26-situationawareness-20260325-0177] page:15:line:5 | Awareness. Embry-Riddle Aeronautical University Press.
    [sp26-situationawareness-20260325-0178] page:15:line:6 | •
    [sp26-situationawareness-20260325-0179] page:15:line:7 | Durso, F. T., et al. (1999). Situation Awareness As a Predictor of Performance in En Route Air Traffic Controllers. Technical Report DOT/FAA/AM-
    [sp26-situationawareness-20260325-0180] page:15:line:8 | 99/3, US Dept. of Transportation/Federal Aviation Administration.
    [sp26-situationawareness-20260325-0181] page:15:line:9 | •
    [sp26-situationawareness-20260325-0182] page:15:line:10 | Endsley M.R., (1988) Situation awareness global assessment technique (SAGAT), Proc. of the IEEE 1988 National Aerospace and Electronics
    [sp26-situationawareness-20260325-0183] page:15:line:11 | Conf., 23-27 May, pp. 789-795 vol.3.
    [sp26-situationawareness-20260325-0184] page:15:line:12 | •
    [sp26-situationawareness-20260325-0185] page:15:line:13 | Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. Human Factors: The Journal of the Human Factors and
    [sp26-situationawareness-20260325-0186] page:15:line:14 | Ergonomics Society, 37(1), 32-64. https://doi.org/10.1518/001872095779049543
    [sp26-situationawareness-20260325-0187] page:15:line:15 | •
    [sp26-situationawareness-20260325-0188] page:15:line:16 | Ma R, Kaber D. (2005) Situation awareness and workload in driving while using adaptive cruise control and a cell phone. International Journal of
    [sp26-situationawareness-20260325-0189] page:15:line:17 | Industrial Ergonomics 35: 939-953.
    [sp26-situationawareness-20260325-0190] page:15:line:18 | •
    [sp26-situationawareness-20260325-0191] page:15:line:19 | National Transportation Safety Board. (2019). Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian
    [sp26-situationawareness-20260325-0192] page:15:line:20 | [Highway Accident Report]. https://www.ntsb.gov/investigations/accidentreports/reports/har1903.pdf
    [sp26-situationawareness-20260325-0193] page:15:line:21 | •
    [sp26-situationawareness-20260325-0194] page:15:line:22 | Proctor R, Van Zandt T. (2018) Human Factors in Simple and Complex Systems 3rd Edition. CRC Press.
    [sp26-situationawareness-20260325-0195] page:15:line:23 | •
    [sp26-situationawareness-20260325-0196] page:15:line:24 | Taylor R. (1990) Situational awareness rating technique (SART): The development of a tool for aircrew systems design. In Situational Awareness
    [sp26-situationawareness-20260325-0197] page:15:line:25 | in Aerospace Operations, AGARD-CP-478, pp. 311 - 3117. Neuilly Sur Seine, France: NATO – AGARD.
    [sp26-situationawareness-20260325-0198] page:15:line:26 | 3/25/26
    [sp26-situationawareness-20260325-0199] page:15:line:27 | 25
    [sp26-situationawareness-20260325-0200] page:15:line:28 | ENP-0112
    ```
