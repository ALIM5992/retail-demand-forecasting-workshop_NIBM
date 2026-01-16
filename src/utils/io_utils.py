import pandas as pd
import numpy as np
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def save_csv(df, path: str):
    df.to_csv(path, index=False)
