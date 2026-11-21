# Modelling notebooks

Sections 5 to 9 of the project are developed here, one notebook per person (see part 7 of `HANDOVER.txt`):

| Notebook | Person | Sections of the main notebook |
|---|---|---|
| `models_baseline.ipynb` | A | 5 (split) and 6.1 (baseline model) |
| `models_extended.ipynb` | B | 6.2, 6.3 (extended model and comparison) and 8.1 |
| `prices.ipynb` | C | 7 (prices), 8.2 and 9 |

Edit only your own notebook. Then nobody's push conflicts with anyone else's. If code is needed in more than one notebook (for example A's split and evaluation function, which B needs too), put it in a file in this folder, such as `evaluation.py`, and import it in both notebooks.

The data comes from `exports/` in the main folder of the repository; how to load it is in the main `README.md`, "Working in your own notebook". At the end, the cells of these notebooks are added to `semestral_project.ipynb`.
