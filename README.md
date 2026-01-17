
# Retail Demand Forecasting Workshop

## Overview

This project demonstrates a **retail demand forecasting pipeline** using Python. It covers the full workflow: **data preprocessing, feature engineering, model training, evaluation**, and **logging**.

It is designed for **students and beginners** to understand how real-world forecasting pipelines are built and maintained.

---

## Features

* **Data Preprocessing**: Clean and prepare raw sales data.
* **Feature Engineering**: Create time-based and derived features.
* **Train/Test Split**: Separate features and target variables for model training and evaluation.
* **Model Training**: Train a `RandomForestRegressor` on historical sales data.
* **Model Evaluation**: Evaluate predictions using `MAE`, `MSE`, and `R2 Score`.
* **Logging**: Track all steps of the pipeline using Python's logging module.

---

## Project Structure

```
retail-demand-forecasting-workshop_NIBM/
│
├── main.py                  # Entry point of the pipeline
├── requirements.txt         # Python dependencies
├── models/                  # Folder to save trained models
├── src/                     # Source code
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── utils/
│       ├── io_utils.py
│       └── metrics.py
└── config/
    ├── __init__.py
    └── config.py            # Paths and configuration variables
```

---

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd retail-demand-forecasting-workshop_NIBM
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the full pipeline:

```bash
python main.py
```

Expected steps in logs:

1. Preprocessing the data
2. Feature engineering
3. Features preparation & train/test split
4. Model training & saving
5. Model evaluation
6. Pipeline completion

---

## Sample Data

The CSV file should have at least the following columns:

```
date,store_id,item_id,sales_qty
2024-01-01,S001,I001,12
2024-01-02,S001,I001,15
...
```

---

## Logging

* Logging is enabled in `main.py` using Python's `logging` module.
* Logs show the progress of each pipeline step.
* Example log output:

```
2026-01-16 19:09:54,122 - RetailForecastPipeline - INFO - Starting Retail Demand Forecasting Pipeline
2026-01-16 19:09:54,132 - RetailForecastPipeline - INFO - Features prepared & train/test split done
2026-01-16 19:09:54,260 - RetailForecastPipeline - INFO - Model training & saving completed
2026-01-16 19:09:54,271 - RetailForecastPipeline - INFO - Model evaluation completed
```

---

## Notes

* ✅ Logging helps **monitor pipeline execution** and **debug issues**.
* ✅ Feature engineering should **always return a DataFrame** ready for modeling.
* ✅ Train/test split ensures **model evaluation is reliable**.
* ✅ Use `RandomForestRegressor` as an example — in production, you can experiment with other algorithms.

---

## License

This project is for **educational purposes** and can be freely used and modified.

---

If you want, I can also **add a "Step-by-Step Classroom Guide" section** to this README, so your students can **follow each pipeline step visually** with instructions on where to add their own features, logs, or train/test experiments.

Do you want me to add that?
