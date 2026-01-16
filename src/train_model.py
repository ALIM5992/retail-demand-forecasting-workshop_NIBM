from src.utils.io_utils import load_csv
from src.config.config import DATA_FEATURE_PATH, FEATURE_COLS, TARGET_COL, MODEL_PATH

# src/train_model.py


def train_model(X_train, y_train, model_path="models/model.pkl"):
    """
    Train a RandomForestRegressor on X_train and y_train
    and save the model to model_path.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    import os
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    print(f"Model saved to {model_path}")
    return model

