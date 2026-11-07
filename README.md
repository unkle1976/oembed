# Health reset

A personal project: lose weight, lower cholesterol, rebuild nutrition, and get back to running. Started 2026-11-07.

This repo replaced an unrelated oEmbed providers list. The old content lives in the `master` branch history.

## Layout

| Path | What it is |
|---|---|
| `profile.md` | Stats, energy arithmetic, targets. The single source of truth for numbers. |
| `QUESTIONS.md` | Open questions that change the plan. Answer them and the plan gets updated. |
| `plan/nutrition-plan.md` | How to eat on 1600 kcal: targets, food lists, a week of meals, shopping list. |
| `plan/running-plan.md` | Walk-run progression back to running, 3 sessions a week. |
| `plan/strength-plan.md` | Two gym sessions a week for Hevy. |
| `plan/gp-checklist.md` | What to ask the GP for and why. |
| `research/` | Evidence summaries with references, one per topic. The plans are built from these. |
| `tracking/weight.csv` | Daily or near-daily weight. Morning, after the loo, before food. |
| `tracking/bloods.md` | Blood test and vitals log with targets. |
| `tracking/weekly-review.md` | Five-minute Sunday review. |
| `tracking/food-log.md` | Meals that worked, slips and triggers. |
| `tools/progress.py` | Prints the weight trend and projected dates. `python3 tools/progress.py` |

## How to use it with Claude

- Add a line to `tracking/weight.csv` whenever you weigh in. Ask Claude to review the trend.
- Paste a MyFitnessPal weekly summary and ask for a review against the targets in `profile.md`.
- When bloods come back, put them in `tracking/bloods.md` and ask what changed and what to adjust.
- If a plan is not working, say so. Adherence beats optimisation. The plan should bend to your life.

## Principles

1. The deficit does the weight loss. Food quality does the cholesterol and nutrient repair. Both matter, in that order.
2. Protein and fibre at every meal. These two control hunger more than anything else.
3. Saturated fat is the main dietary lever on LDL. Swap, do not just cut: butter to olive oil, fatty meat to fish, beans and lean poultry.
4. Running fitness comes back fast. Tendons and bones do not. Progress the running slower than feels necessary.
5. Track the trend, not the day. Weight bounces by a kilo or two from water alone.
6. Nothing here replaces a GP. Get the bloods done early so there is a baseline to compare against.
