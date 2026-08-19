# svedala-toolbox

Your personal course repository for **EG2140 Computer Applications and
Machine Learning in Electric Power Systems**. During Period 1 you build
this package by hand, lab by lab: a network loader, an N-1 contingency
screener, a data pipeline, and the analysis on top.

## Getting started (Lab 1)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt  # installs deps + this package (editable)
svedala info                     # works once you have done Lab 1
```

Two things to know on day one:

- A fresh clone has a **red test suite on purpose**: the loader tests fail
  until Lab 1 is done — that failing list is your Lab 1 todo list, and CI
  turns green when you finish it.
- The package must be installed *editable* (the `-e .` line inside
  requirements.txt does this). A plain `pip install .` will not find the
  data folder.

Follow the lab instructions in the course material. Each lab has a
self-check, run from the repo root: `python checks/lab1_check.py`.

## Layout

```
src/svedala_toolbox/   the package — everything you keep goes here
tests/                 pytest tests — they grow every lab
data/svedala/          the Svedala model as five CSV files
checks/                per-lab self-check scripts (not hand-ins)
```

No AI coding tools in Period 1 — see the course rules on Canvas.
