import pandas as pd
import joblib

from utils.preprocessing import preprocess_data


model = joblib.load(
    "models/saved_model.pkl"
)

scaler = joblib.load(
    "models/scaler.pkl"
)

feature_names = joblib.load(
    "models/feature_names.pkl"
)


def predict_uploaded_dataset(df):

    try:

        df = preprocess_data(df)

        df = df.select_dtypes(
            include=['number']
        )

        df = df.reindex(
            columns=feature_names,
            fill_value=0
        )

        scaled_data = scaler.transform(df)

        predictions = model.predict(
            scaled_data
        )

        probabilities = model.predict_proba(
            scaled_data
        )

        return predictions, probabilities

    except Exception as error:

        raise Exception(
            f"Prediction failed: {error}"
        )