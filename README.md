# Machine Learning Foundations

A structured collection of Python, data analysis, and visualization work that builds the groundwork for machine learning. The repository combines an end-to-end exploratory data analysis (EDA) and feature engineering project on a medical insurance dataset with focused practice modules covering Python fundamentals, NumPy, Matplotlib, and Pandas.

---

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Featured Project: Insurance Cost Analysis](#featured-project-insurance-cost-analysis)
4. [Getting Started](#getting-started)
5. [Technology Stack](#technology-stack)
6. [Author](#author)

---

## Overview

This repository documents a progression from core programming concepts to applied data analysis. Its main objective is to prepare clean, well-understood data for predictive modeling.

| Area | Focus |
| --- | --- |
| Exploratory Data Analysis | Distribution analysis, outlier detection, correlation analysis |
| Data Preprocessing | Duplicate removal, encoding, scaling |
| Feature Engineering | Binning, one-hot encoding, statistical feature selection |
| Foundations | Python, NumPy, Matplotlib, Pandas |

---

## Repository Structure

```
machine-learning/
|-- EDA/
|   |-- Project_1.ipynb          # Insurance cost EDA and feature engineering
|   `-- insurance.csv            # Dataset (1,338 records, 7 attributes)
|-- numpy/
|   |-- numpy_tut.ipynb          # Array creation, math, linear algebra, statistics
|   `-- data.txt                 # Sample data for file-loading exercises
|-- matplotlib/
|   `-- Untitled0-7.ipynb        # Line, bar, pie, scatter, histogram, subplot practice
|-- python-revision/
|   |-- variables.py
|   |-- datatypes.py
|   |-- constants.py
|   |-- functions.py
|   |-- classAndInitialiser.py
|   |-- methods.py
|   `-- dunderMethods.py
|-- complete-pandas-tutorial-master/   # Pandas tutorial (third-party, see Acknowledgements)
|-- assets/                      # Figures used in this README
`-- README.md
```

---

## Featured Project: Insurance Cost Analysis

**Location:** `EDA/Project_1.ipynb`

The project analyzes how demographic and lifestyle attributes relate to individual medical insurance charges, and prepares the dataset for regression modeling.

### Dataset

| Attribute | Type | Description |
| --- | --- | --- |
| `age` | Integer | Age of the primary beneficiary |
| `sex` | Categorical | Gender of the beneficiary |
| `bmi` | Float | Body mass index |
| `children` | Integer | Number of dependents covered |
| `smoker` | Categorical | Smoking status |
| `region` | Categorical | Residential region in the United States |
| `charges` | Float | Individual medical costs billed by insurance (target variable) |

The dataset contains 1,338 records and 7 columns with no missing values. One duplicate record was identified and removed, leaving 1,337 records.

### Summary Statistics

| Statistic | Age | BMI | Children | Charges |
| --- | --- | --- | --- | --- |
| Mean | 39.21 | 30.66 | 1.09 | 13,270.42 |
| Std. deviation | 14.05 | 6.10 | 1.21 | 12,110.01 |
| Minimum | 18 | 15.96 | 0 | 1,121.87 |
| Median | 39 | 30.40 | 1 | 9,382.03 |
| Maximum | 64 | 53.13 | 5 | 63,770.43 |

### Methodology

1. **Exploratory analysis.** Shape, data types, null counts, descriptive statistics, histograms with density curves, count plots, box plots, and a correlation heatmap.
2. **Cleaning.** Removal of duplicate records and verification of missing values and data types.
3. **Encoding.** Binary mapping of `sex` and `smoker` (renamed to `is_female` and `is_smoker`) and one-hot encoding of `region`.
4. **Feature engineering.** BMI categorized into Underweight, Normal, Overweight, and Obese bands and one-hot encoded.
5. **Scaling.** Standardization of `age`, `bmi`, and `children` with `StandardScaler`.
6. **Feature selection.** Pearson correlation for numeric relationships with `charges`, and a chi-square test of independence (alpha = 0.05) between each categorical feature and quartile-binned charges.

### Results

#### Distribution of Charges

Medical charges are strongly right-skewed. Most beneficiaries incur lower costs, while a smaller secondary group sits in a much higher cost range.

<p align="center">
  <img src="assets/charges_distribution.png" alt="Distribution of insurance charges" width="48%">
  <img src="assets/charges_boxplot.png" alt="Box plot of insurance charges showing outliers" width="48%">
</p>

The box plot confirms a substantial number of high-value outliers above roughly 35,000, which is relevant when choosing a modeling approach and error metric.

#### Distribution of Predictors

<p align="center">
  <img src="assets/age_distribution.png" alt="Distribution of age" width="32%">
  <img src="assets/bmi_distribution.png" alt="Distribution of BMI" width="32%">
  <img src="assets/smoker_counts.png" alt="Smoker versus non-smoker counts" width="32%">
</p>

- Age is close to uniform across the 18 to 64 range, with a spike at the youngest age.
- BMI is approximately normally distributed, centered near 30.
- Non-smokers outnumber smokers: 1,063 versus 274 after duplicate removal.

#### Correlation Analysis

<p align="center">
  <img src="assets/correlation_heatmap.png" alt="Correlation heatmap of numeric features" width="60%">
</p>

Among numeric variables, age (0.30) and BMI (0.20) show the strongest linear association with charges, while the number of children shows a weak association (0.07).

#### Feature Relevance

Pearson correlation with `charges` after encoding:

| Feature | Pearson Correlation |
| --- | --- |
| `is_smoker` | 0.787 |
| `age` | 0.298 |
| `bmi_category_Obese` | 0.200 |
| `bmi` | 0.196 |
| `region_southeast` | 0.074 |
| `children` | 0.067 |
| `is_female` | -0.058 |

Chi-square test results (alpha = 0.05):

| Feature | Chi-square | p-value | Decision |
| --- | --- | --- | --- |
| `is_smoker` | 848.22 | < 0.001 | Keep |
| `region_southeast` | 16.00 | 0.0011 | Keep |
| `is_female` | 10.26 | 0.0165 | Keep |
| `bmi_category_Obese` | 8.52 | 0.0365 | Keep |
| `region_southwest` | 5.09 | 0.1652 | Drop |
| `bmi_category_Overweight` | 4.25 | 0.2356 | Drop |
| `bmi_category_Normal` | 3.71 | 0.2948 | Drop |
| `region_northwest` | 1.13 | 0.7688 | Drop |

### Key Findings

- Smoking status is by far the strongest predictor of insurance charges, with a correlation of roughly 0.79 and the largest chi-square statistic.
- Age and obesity are secondary drivers of cost.
- The final feature set retained for modeling is: `age`, `is_female`, `bmi`, `children`, `is_smoker`, `region_southeast`, and `bmi_category_Obese`, with `charges` as the target.

---

## Getting Started

### Prerequisites

- Python 3.9 or later
- pip

---

## Technology Stack

| Category | Tools |
| --- | --- |
| Language | Python |
| Data manipulation | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Statistics and preprocessing | SciPy, scikit-learn |
| Environment | Jupyter Notebook |


---

## Author

**Aditya Saraswat**
