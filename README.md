# ML2 Semestral Project

We predict whether a football match ends with more than 2.5 goals, with two models: a baseline model on the data the company has today and an extended model on the richer data offered by a provider. The difference in accuracy decides how much the richer data is worth.

Everything is in `modelling/semestral_project.ipynb`. Sections 1 to 4 (loading, cleaning, feature engineering, feature checks) are finished. Sections 5 to 9 (split, models, profit, correctness checks, conclusion) are still to do. **Read `HANDOVER.txt` before you continue**: it explains what was done and what to watch out for in the split and the models.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/majkkl11/ml2.git
   ```

2. The data is not in this repository. Unzip `football_data.zip` from MS Teams into a folder `data/` inside `modelling/`, next to the notebook, so that the files are at `modelling/data/<country>/<league>/<season>.csv`.
3. Create an environment and install the packages (Python 3.12):

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   On macOS or Linux the second line is `source .venv/bin/activate`.
4. Open `modelling/semestral_project.ipynb` and run it from top to bottom. It takes under a minute.

## Files

| File | What it is |
|---|---|
| `modelling/semestral_project.ipynb` | the project notebook, which is also what we submit |
| `modelling/` | the main notebook, and one notebook per person for the models and the prices, which are added to the main notebook at the end; `data/` and `exports/` go here too |
| `HANDOVER.txt` | summary of the work so far, with warnings and recommendations for the next steps |
| `notes.txt` | description of the original data columns, from the data provider |
| `requirements.txt` | Python packages |
| `load_data.py` | an early standalone copy of the data loader; the notebook does not use it |

## Working together

Every team member can push directly to `main`. There is no review step, so a push is visible to the whole team immediately. That keeps things simple, but it means we have to be careful with the notebook: if two people change it at the same time, git cannot merge the two versions cleanly and one of them has to be redone by hand.

The routine for every working session:

1. **Say that you are taking the notebook.** Only one person edits `semestral_project.ipynb` at a time. Tell the others in the team chat before you start and when you are done.
2. **Pull first**, so you start from the latest version:

   ```
   git pull
   ```

3. **Do your work**, then run the notebook from top to bottom and save it, so the saved outputs match the code.
4. **Commit and push when you are done**, not days later:

   ```
   git add modelling/semestral_project.ipynb
   git commit -m "Short description of what you did"
   git push
   ```

Things to be careful about:

* **If `git push` is rejected**, someone else pushed in the meantime. Do not force the push (`git push --force` deletes their work). Run `git pull` and, if git reports a conflict in the notebook, ask in the team chat before you try to fix it.
* **Never commit the data.** The `data/` and `exports/` folders are ignored on purpose; do not add them with `git add -f`.
* **Do not rename or reorder the existing sections** without telling the others; `HANDOVER.txt` refers to them by number.
* **Small changes outside the notebook** (README, `HANDOVER.txt`) can be made by anyone at any time. They merge without problems.

## Working in your own notebook

The models (sections 5 and 6) and the prices (section 7) are developed in separate notebooks in the folder `modelling/`, one per person (see `modelling/README.md`), and added to `semestral_project.ipynb` at the end. Everyone edits only their own notebook, so these notebooks can be pushed at any time without asking the others.

You do not need to run the main notebook: you get the cleaned data as two files, `model_data.csv` and `model_features.json`, created in section 4.6 of the main notebook. Put both into a folder `exports/` inside `modelling/`, next to the notebooks. Like `data/`, this folder is not in the repository; never commit it.

Load them like this from a notebook in `modelling/`:

```python
import json
import pandas as pd

model_spec = json.load(open("exports/model_features.json", encoding="utf-8"))
id_cols, target = model_spec["id_cols"], model_spec["target"]
baseline_features, extended_features = model_spec["baseline_features"], model_spec["extended_features"]

extended_data = pd.read_csv("exports/model_data.csv", parse_dates=["Date"], dtype={"season": str})
baseline_data = extended_data[id_cols + baseline_features + [target]]
```

`dtype={"season": str}` matters: without it the season `"1920"` becomes the number 1920 and the split by season breaks.

To make adding your work to the main notebook easy:
* **Start from exactly these names**: `extended_data`, `baseline_data`, `baseline_features`, `extended_features`, `id_cols` and `target` exist in the main notebook too. Then your cells can be pasted after section 4 and only the loading cell above is dropped.
* **Use the feature lists, not all columns.** The id columns (`country`, `season`, `Date`, ...) are for splitting and for results per country; they are not features.
* **Do not change the data in your notebook.** If a feature should change, it is changed in section 4 of the main notebook and exported again, so that everyone works with the same data.
