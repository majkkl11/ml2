# Working in `modelling/`

This folder holds the main notebook `semestral_project.ipynb`, which is what we submit, and one notebook per team member for sections 5 to 9 (see part 7 of `HANDOVER.txt`). At the end, the cells of these notebooks are added to the main notebook.

| Notebook | Person | Sections of the main notebook |
|---|---|---|
| `baseline.ipynb` | A | 5 (split) and 6.1 (baseline models) |
| `models_extended.ipynb` | B | 6.2, 6.3 (extended models and comparison) and 8.1 |
| `prices.ipynb` | C | 7 (prices), 8.2 and 9 |

## Setup

1. Clone the repository: `git clone https://github.com/majkkl11/ml2.git`
2. Create an environment and install the packages (Python 3.12):

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   On macOS or Linux the second line is `source .venv/bin/activate`.
3. Put the data into this folder. Neither folder is in the repository; never commit them.
   - `data/`: the unzipped `football_data.zip` from MS Teams, as `data/<country>/<league>/<season>.csv`. Only needed to run the main notebook.
   - `exports/`: `model_data.csv` and `model_features.json`, created in section 4.6 of the main notebook and shared directly. This is all you need for your own notebook.

## Loading the data in your own notebook

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

## Rules that make the final merge easy

* **Edit only your own notebook.** Then nobody's push conflicts with anyone else's. Only the author of sections 1 to 4 edits `semestral_project.ipynb`.
* **Start from exactly the names above** (`extended_data`, `baseline_data`, `baseline_features`, `extended_features`, `id_cols`, `target`). They exist in the main notebook too, so your cells can be pasted after section 4 and only the loading cell is dropped.
* **Use the feature lists, not all columns.** The id columns (`country`, `season`, `Date`, ...) are for splitting and for results per country; they are not features.
* **Do not change the data in your notebook.** If a feature should change, it is changed in section 4 of the main notebook and exported again, so that everyone works with the same data.
* **Reuse, do not rewrite.** Person B uses the split, the evaluation function and the model constructors of `baseline.ipynb` unchanged, so that both models are measured in exactly the same way.

## Git routine

1. `git pull` before you start.
2. Run your notebook from top to bottom and save it, so the saved outputs match the code.
3. Commit and push the same day: `git add modelling/<your notebook>`, `git commit -m "what you did"`, `git push`.

If `git push` is rejected, someone else pushed in the meantime: run `git pull` and push again. Never use `git push --force`, it deletes the others' work.
