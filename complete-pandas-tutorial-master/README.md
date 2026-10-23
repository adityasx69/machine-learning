# Pandas Tutorial

A notebook-based introduction to working with tabular data in Pandas. The tutorial moves from DataFrame basics through filtering, transformation, joining, missing values, aggregation, and newer CSV backends.

## Contents

- [Learning objectives](#learning-objectives)
- [Repository contents](#repository-contents)
- [Setup](#setup)
- [Run the tutorial](#run-the-tutorial)
- [Related resources](#related-resources)

## Learning objectives

The main lesson is [`tutorial.ipynb`](tutorial.ipynb). Its sections demonstrate:

- Creating, inspecting, selecting, and filtering DataFrames
- Reading CSV, Parquet, and Excel files
- Adding, removing, renaming, and deriving columns
- Merging and concatenating tables
- Handling missing values and converting dates
- Grouping, aggregation, pivot tables, ranking, cumulative operations, and rolling windows
- Reading CSV data with the PyArrow engine and dtype backend

## Repository contents

| Path | Description |
| --- | --- |
| [`tutorial.ipynb`](tutorial.ipynb) | Main tutorial notebook with relative data paths |
| [`tut.ipynb`](tut.ipynb) | Earlier practice notebook; some cells contain absolute paths from the original machine |
| [`requirements.txt`](requirements.txt) | Dependencies used by the tutorial material |
| [`warmup-data/coffee.csv`](warmup-data/coffee.csv) | Small coffee sales example |
| `data/` | Athlete bios, Olympic results, region mappings, and derived examples in CSV, Excel, Parquet, and Feather formats |
| [`pandas-cheat-sheet.md.html`](pandas-cheat-sheet.md.html) | HTML reference sheet |
| [`LICENSE`](LICENSE) | License included with this tutorial folder |

The notebook can write a derived `data/bios_new.csv` file when its export cell is run.

## Setup

From this directory, create and activate a virtual environment, then install the dependencies listed for this tutorial:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. The dependency list includes NumPy, Pandas, `openpyxl`, `pyarrow`, `pyjanitor`, and `ipykernel`.

## Run the tutorial

Start Jupyter from this folder so the notebook's relative dataset paths resolve:

```bash
jupyter notebook tutorial.ipynb
```

Choose the environment's Python kernel, then run the notebook from top to bottom. Excel input uses `openpyxl`; Parquet and Feather support is provided by `pyarrow`. Some cells install or import optional packages such as `skimpy`; those cells are separate from the main exercises and may require an additional installation.

The older `tut.ipynb` has absolute paths tied to a different computer. Prefer `tutorial.ipynb`, or update those paths to locations relative to this folder before running the older notebook.
