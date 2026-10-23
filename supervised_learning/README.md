# Supervised Learning

This folder contains two notebook workflows that use linear regression to estimate a continuous target: medical insurance charges and Ford vehicle prices. The notebooks explore their data, prepare features, fit models, and calculate evaluation metrics.

## Notebooks and data

| Notebook | Dataset | Target |
| --- | --- | --- |
| [`insurance_ml_model.ipynb`](insurance_ml_model.ipynb) | [`insurance.csv`](insurance.csv) — 1,338 rows and 7 columns | `charges` |
| [`car_price_pred.ipynb`](car_price_pred.ipynb) | [`ford.csv`](ford.csv) | `price` |

## Workflows

### Insurance charges

The notebook explores the insurance data, removes duplicate rows, encodes sex, smoking status, region, and BMI categories, and standardizes selected numeric features. It selects features for a linear regression model, uses an 80/20 train/test split with a fixed random seed, and reports R² and adjusted R².

### Ford vehicle prices

The notebook explores vehicle price relationships, prepares categorical features with one-hot and label encoding, standardizes numeric columns, and fits linear regression models using a 67/33 train/test split. It reports R² and adjusted R². In the label-encoded evaluation cells, the prediction currently calls the one-hot model variable; use those results with care if comparing the two encoding approaches.

Charts are displayed inline in the notebooks. Model objects and predictions are not exported to files.

## Setup and run

From the repository root, activate the project environment and install the analysis dependencies described in the [root README](../README.md). Then launch Jupyter from this folder so the notebook-relative CSV paths resolve:

```bash
cd supervised_learning
jupyter notebook
```

Open `insurance_ml_model.ipynb` or `car_price_pred.ipynb`, select the environment's Python kernel, and run cells in order.

## Libraries

The notebooks use Python, Pandas, NumPy, Matplotlib, Seaborn, and scikit-learn.
