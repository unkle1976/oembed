#!/usr/bin/env python3
"""Print a weight trend from tracking/weight.csv.

Usage: python3 tools/progress.py

Daily weight bounces by 1 to 2 kg from water, salt and glycogen. This script
prints a 7-day rolling average and the rate of loss so you judge the trend,
not the noise.
"""
import csv
import sys
from datetime import date
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "tracking" / "weight.csv"
START_WEIGHT = 96.0
GOALS = {"5% lost": 91.2, "10% lost": 86.4, "BMI < 25": 79.0}


def main() -> int:
    rows = []
    with CSV.open() as f:
        for r in csv.DictReader(f):
            if r.get("weight_kg"):
                rows.append((date.fromisoformat(r["date"]), float(r["weight_kg"])))
    rows.sort()
    if not rows:
        print("No weights recorded yet.")
        return 0

    print(f"{'date':<12}{'kg':>7}{'7d avg':>9}")
    for i, (d, w) in enumerate(rows):
        window = [x[1] for x in rows if 0 <= (d - x[0]).days < 7]
        avg = sum(window) / len(window)
        print(f"{d.isoformat():<12}{w:>7.1f}{avg:>9.1f}")

    first_d, first_w = rows[0]
    last_d, last_w = rows[-1]
    days = (last_d - first_d).days
    lost = first_w - last_w
    print(f"\nTotal change: {-lost:+.1f} kg over {days} days")
    if days >= 14:
        rate = lost / (days / 7)
        print(f"Rate: {rate:.2f} kg/week")
        if rate > 0:
            for name, goal in GOALS.items():
                if last_w > goal:
                    weeks = (last_w - goal) / rate
                    print(f"  {name} ({goal} kg): ~{weeks:.0f} weeks at this rate")
        if rate > 1.0:
            print("Faster than 1 kg/week for a sustained period. Consider adding 100 to 200 kcal.")
        elif 0 < rate < 0.25:
            print("Slower than 0.25 kg/week. Check logging accuracy first, then consider a 100 kcal cut.")
    else:
        print("Need at least two weeks of data to judge the rate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
