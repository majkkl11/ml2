# ML2 Semestral Project: what is better data worth?

A betting company sets its odds with predictions of football matches. It currently predicts from a basic data set (teams, date, goals, result) and has been offered a richer data set with match statistics and bookmaker odds. This project determines the **maximum yearly price the company should pay for the richer data in each market (country)**.

## Approach

1. **Data.** 6 seasons (2019/20 to 2024/25) of 21 leagues in 11 countries: about 42,500 matches. The data is cleaned and validated in detail, including corrected input errors and the removal of 41 matches whose result was awarded without the match being played.
2. **Target.** Whether a match ends with more than 2.5 goals (over/under 2.5), a binary classification. The two classes are almost exactly balanced.
3. **Features.** Every feature uses only information known before kick-off:
   - **Baseline (41 features)** from the current data: recent and long-term form of both teams, Elo strength ratings, the scoring level of the division, and a flag for the Covid period behind closed doors.
   - **Extended (47 more)** from the richer data: form in shots, shots on target, corners, fouls and cards, and probabilities derived from the opening odds.
4. **Models.** XGBoost, with logistic regression as a benchmark, each trained once on the baseline features (accuracy A0) and once on all features (accuracy A1). The split is by time: train 2020/21 to 2022/23, validate on 2023/24, test once on 2024/25.
5. **Price.** For each market, the profit-maximising margin is found for A0 and for A1, analytically and numerically. The increase in yearly profit is the maximum price for the data in that market.

## Status

| Part | Status |
|---|---|
| Data loading, cleaning, validation, features, feature checks (sections 1 to 4) | done |
| Split and baseline models (sections 5 and 6.1) | done: baseline XGBoost 57.1% accuracy on the validation season |
| Extended models and comparison (sections 6.2, 6.3) | in progress |
| Prices per market (section 7), correctness checks (8), conclusion (9) | in progress |

## Repository

| Path | Content |
|---|---|
| `modelling/semestral_project.ipynb` | the main notebook, which is what we submit |
| `modelling/` | one notebook per team member, added to the main notebook at the end; how to work there is in `modelling/README.md` |
| `HANDOVER.txt` | what was done so far, the decisions behind it, and who does what next |
| `notes.txt` | description of the original data columns, from the data provider |
| `requirements.txt` | Python packages |

The data is not in the repository. The course data (`football_data.zip`) and the exported data for the models are shared directly; where they go is described in `modelling/README.md`.
