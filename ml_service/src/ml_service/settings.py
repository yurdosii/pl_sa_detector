from sklearn.feature_extraction.text import BaseEstimator

# ML models path
PL_MODEL_PATH = "pl_model.pkl"
SA_MODEL_PATH = "sa_model.pkl"

ML_MODELS: dict[str, BaseEstimator] = {}
