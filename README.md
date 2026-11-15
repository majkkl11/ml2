# ML2 Semestral Project

We predict whether a football match ends with more than 2.5 goals, with two models: a baseline model on the data the company has today and an extended model on the richer data offered by a provider. The difference in accuracy decides how much the richer data is worth.

Everything is in `semestral_project.ipynb`. Sections 1 to 4 (loading, cleaning, feature engineering, feature checks) are finished. Sections 5 to 9 (split, models, profit, correctness checks, conclusion) are still to do. **Read `HANDOVER.txt` before you continue**: it explains what was done and what to watch out for in the split and the models.

## Setup

1. The data is not in this repository. Unzip `football_data.zip` from MS Teams into a folder `data/` next to the notebook, so that the files are at `data/<country>/<league>/<season>.csv`.
2. Create an environment and install the packages (Python 3.12):

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   On macOS or Linux the second line is `source .venv/bin/activate`.
3. Open `semestral_project.ipynb` and run it from top to bottom. It takes under a minute.

## Files

| File | What it is |
|---|---|
| `semestral_project.ipynb` | the project notebook, which is also what we submit |
| `HANDOVER.txt` | summary of the work so far, with warnings and recommendations for the next steps |
| `notes.txt` | description of the original data columns, from the data provider |
| `requirements.txt` | Python packages |
| `load_data.py` | an early standalone copy of the data loader; the notebook does not use it |

## Working together

Notebooks are hard to merge. Pull before you start, agree who is editing the notebook, and push when you are done. Before committing, run the notebook from top to bottom and save it, so the saved outputs match the code.
