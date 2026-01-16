from src.utils.io_utils import load_csv, save_csv
from src.config.config import DATA_CLEAN_PATH, DATA_FEATURE_PATH

# src/feature_engineering.py


def add_features(df):
    """
    Add engineered features to the dataframe
    """
    df['day_of_week'] = df['date'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5,6]).astype(int)
    return df


# src/feature_engineering.py (or src/utils/data_utils.py)
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def prepare_features(df, target='sales_qty', test_size=0.2, random_state=42):
    """
    Encode categorical variables, separate X/y, split train/test
    """
    # Separate target
    y = df[target]

    # Drop columns not needed for features
    X = df.drop(columns=[target, 'date'])  # keep store_id/item_id for encoding

    # Encode categorical features
    for col in ['store_id', 'item_id']:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


