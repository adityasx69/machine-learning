# Exploratory Data Analysis

This folder contains two notebook studies that inspect and prepare tabular datasets for further modeling. Each notebook combines data quality checks, descriptive summaries, visual exploration, and feature preparation.

## Notebooks and data

| Notebook | Dataset | Focus |
| --- | --- | --- |
| [`Project_1.ipynb`](Project_1.ipynb) | [`insurance.csv`](insurance.csv) — 1,338 rows and 7 columns | Insurance charges, duplicate removal, categorical encoding, BMI bands, scaling, and feature relevance |
| [`Project_2.ipynb`](Project_2.ipynb) | [`heart.csv`](heart.csv) — 918 rows and 12 columns | Heart disease patterns, zero-value treatment, categorical encoding, and numeric scaling |

## Workflow

Both notebooks begin with dataset shape, types, descriptive statistics, and missing-value checks. They then explore distributions and relationships with Matplotlib and Seaborn.

`Project_1.ipynb` removes a duplicate record, encodes categorical fields, derives BMI categories, standardizes selected numeric columns, and examines Pearson and chi-square associations with insurance charges.

`Project_2.ipynb` treats zero values in `Cholesterol` and `RestingBP` as missing measurements, reviews outcome patterns, one-hot encodes categorical columns, and standardizes numeric features. Review its resting blood pressure replacement cell before relying on its output: the current expression uses the cholesterol mean variable for the replacement value.

The notebooks display charts inline. They do not write a processed dataset or fitted model to disk.

## Setup and run

From the repository root, activate the project environment and install the analysis dependencies as described in the [root README](../README.md). Then start Jupyter from this directory so each notebook can read its CSV by filename:

```bash
cd EDA
jupyter notebook
```

Open `Project_1.ipynb` or `Project_2.ipynb`, select the environment's Python kernel, and run the cells in order. `Project_2.ipynb` also imports `sheryanalysis` for an automated report. That helper is not listed in a repository dependency manifest; its report cell is optional to the remaining analysis.

## Libraries

The notebooks use Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, and scikit-learn. The optional automated report cell uses `sheryanalysis`.
