# ML2 Semestral Project

We predict whether a football match ends with more than 2.5 goals, with two models: a baseline model on the data the company has today and an extended model on the richer data offered by a provider. The difference in accuracy decides how much the richer data is worth.

Everything is in `semestral_project.ipynb`. Sections 1 to 4 (loading, cleaning, feature engineering, feature checks) are finished. Sections 5 to 9 (split, models, profit, correctness checks, conclusion) are still to do. **Read `HANDOVER.txt` before you continue**: it explains what was done and what to watch out for in the split and the models.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/majkkl11/ml2.git
   ```

2. The data is not in this repository. Unzip `football_data.zip` from MS Teams into a folder `data/` next to the notebook, so that the files are at `data/<country>/<league>/<season>.csv`.
3. Create an environment and install the packages (Python 3.12):

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   On macOS or Linux the second line is `source .venv/bin/activate`.
4. Open `semestral_project.ipynb` and run it from top to bottom. It takes under a minute.

## Files

| File | What it is |
|---|---|
| `semestral_project.ipynb` | the project notebook, which is also what we submit |
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
   git add semestral_project.ipynb
   git commit -m "Short description of what you did"
   git push
   ```

Things to be careful about:

* **If `git push` is rejected**, someone else pushed in the meantime. Do not force the push (`git push --force` deletes their work). Run `git pull` and, if git reports a conflict in the notebook, ask in the team chat before you try to fix it.
* **Never commit the data.** The `data/` folder is ignored on purpose; do not add it with `git add -f`.
* **Do not rename or reorder the existing sections** without telling the others; `HANDOVER.txt` refers to them by number.
* **Small changes outside the notebook** (README, `HANDOVER.txt`) can be made by anyone at any time. They merge without problems.
