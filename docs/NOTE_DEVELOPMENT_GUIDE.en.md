# HFE Note Development Guide

## Development Principles

- Every page answers three questions first: what this topic is, why it matters, and how to use it.
- The page line must be clear enough that a student understands the core question within the first 300-500 words.
- The main body exists to teach; source traceability belongs in the appendix.
- Images should explain the body, not appear as a standalone gallery.

## Content Principles

- Every page must define a `Core Question`.
- Every page must include key takeaways or a case verdict.
- Every page must include a difficult point, at least one example, and a closing review summary.
- Terms should be introduced through plain-language intuition before the English term.
- Sections must connect into one line rather than becoming isolated fragments.

## Prompt / Callout Rules

- `tip`: opening memory anchor and closing review points.
- `note`: core question, key conclusion, and method framing.
- `warning`: confusion points, analysis traps, and common misreadings.
- `example`: cases, worked examples, and practice scenarios.

## Workflow

1. Read the source file and identify the real teaching question and course position.
2. Extract the main line and decide whether the page is a `concept`, `method`, or `case` page.
3. Select only the visuals that help explain the body.
4. Write the Chinese teaching page first, then add the English mirror page.
5. Confirm that line-by-line source coverage still remains complete in the appendix.
6. Run `python scripts/build_hfe_notes.py` and `python -m mkdocs build` for final validation.

## Page Skeletons

- Concept page:
  `Key Takeaways -> Remember This First -> What the Concept Means -> Why It Matters -> Framework / Categories -> Difficult Point -> Example -> How to Use It -> Chapter Summary`
- Method page:
  `Key Takeaways -> What This Method Is For -> What Problem It Solves -> Inputs and Outputs -> Steps -> Common Failure Mode -> Worked Example -> Relation to Other Methods -> Chapter Summary`
- Case page:
  `Case Conclusions -> Start with the Case Verdict -> Background and Stakes -> Event / Failure Chain -> Concepts Used for Analysis -> System-Level Lesson -> Chapter Summary`

