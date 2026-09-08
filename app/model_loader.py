import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)


model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "xgb_delivery_model.pkl"
    )
)


preprocessor = joblib.load(
    os.path.join(
        MODEL_DIR,
        "preprocessor.pkl"
    )
)


threshold = joblib.load(
    os.path.join(
        MODEL_DIR,
        "threshold.pkl"
    )
)