# Instructions for Claude working in this repo

This is Nick's personal health project, not a software project. Read `profile.md` and `QUESTIONS.md` first.

## Context

- Nick is 50, male, 177.8 cm, started at 96 kg (BMI 30.4) on 2026-11-07. UK based.
- Goals in priority order: lower cardiovascular risk (cholesterol, blood pressure), lose weight to the mid 80s then reassess, repair a year of poor nutrition, return to running safely.
- Starting intake 1600 kcal/day by his choice. Former marathon runner, currently very unfit. Uses the Hevy app for strength.
- He sends outputs to other people. Everything must be factually correct and sourced. Do not state a number without being able to point to where it came from.

## How to work

- Numbers live in `profile.md`. Update there, then propagate.
- Evidence lives in `research/`. Plans in `plan/` must be consistent with it. If new evidence changes a recommendation, update the research file first and cite it.
- Prefer UK sources and UK units: kg, cm, mmol/L for lipids, mmol/mol for HbA1c, grams of salt not sodium unless both are given.
- Be direct. No motivational filler. No em dashes. Say when evidence is weak.
- Medical limits: Claude can summarise evidence and build plans, but cannot diagnose or replace a GP. If Nick reports chest pain, breathlessness out of proportion to effort, fainting, or palpitations during exercise, tell him to stop and seek medical advice. Do not soften that.
- When reviewing food logs, look at weekly averages, not single days. Check protein, fibre and saturated fat before anything else.
- When adjusting calories, change by 100 to 200 kcal at a time and wait 2 to 3 weeks before judging.

## Files not to invent

Do not create new top-level directories without reason. Tracking files are templates to fill, not to regenerate.
