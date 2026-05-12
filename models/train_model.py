import os

import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from utils.preprocessing import preprocess_data


os.makedirs(
    "reports",
    exist_ok=True
)


print(
    "Loading dataset...",
    flush=True
)

df = pd.read_csv(
    "datasets/CICIDS2017.csv"
).sample(
    50000,
    random_state=42
)


print(
    "Preprocessing dataset...",
    flush=True
)

df = preprocess_data(df)


print(
    "Converting labels...",
    flush=True
)

df['Label'] = df['Label'].apply(
    lambda x: 0 if x == 'BENIGN' else 1
)


print(
    "Separating features and target...",
    flush=True
)

X = df.drop(
    "Label",
    axis=1
)

y = df["Label"]


print(
    "Selecting numeric features...",
    flush=True
)

X = X.select_dtypes(
    include=['number']
)


print(
    "Saving feature names...",
    flush=True
)

feature_names = X.columns.tolist()

joblib.dump(
    feature_names,
    "models/feature_names.pkl"
)


print(
    "Splitting dataset...",
    flush=True
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print(
    "Scaling features...",
    flush=True
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


models = {

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=150,
        random_state=42,
        n_jobs=-1
    ),

    "SVM": SVC(
        probability=True
    )
}


results = []

best_accuracy = 0

best_model = None

best_model_name = None

best_predictions = None


for name, model in models.items():

    try:

        print(
            f"Training {name}...",
            flush=True
        )

        model.fit(
            X_train_scaled,
            y_train
        )

        y_pred = model.predict(
            X_test_scaled
        )

        accuracy = accuracy_score(
            y_test,
            y_pred
        )

        precision = precision_score(
            y_test,
            y_pred
        )

        recall = recall_score(
            y_test,
            y_pred
        )

        f1 = f1_score(
            y_test,
            y_pred
        )

        results.append({

            "Model": name,

            "Accuracy": round(
                accuracy,
                4
            ),

            "Precision": round(
                precision,
                4
            ),

            "Recall": round(
                recall,
                4
            ),

            "F1 Score": round(
                f1,
                4
            )
        })

        print(
            classification_report(
                y_test,
                y_pred
            ),
            flush=True
        )

        print(
            confusion_matrix(
                y_test,
                y_pred
            ),
            flush=True
        )

        if accuracy > best_accuracy:

            best_accuracy = accuracy

            best_model = model

            best_model_name = name

            best_predictions = y_pred

    except Exception as error:

        print(
            f"Error training {name}: {error}",
            flush=True
        )


results_df = pd.DataFrame(
    results
)

print(
    results_df,
    flush=True
)


metrics = {

    "accuracy": round(
        best_accuracy,
        4
    ),

    "precision": round(
        precision_score(
            y_test,
            best_predictions
        ),
        4
    ),

    "recall": round(
        recall_score(
            y_test,
            best_predictions
        ),
        4
    ),

    "f1_score": round(
        f1_score(
            y_test,
            best_predictions
        ),
        4
    )
}


print(
    f"Best model: {best_model_name}",
    flush=True
)

print(
    f"Best accuracy: {best_accuracy}",
    flush=True
)


cm = confusion_matrix(
    y_test,
    best_predictions
)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title(
    "Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.savefig(
    "reports/confusion_matrix.png"
)

plt.close()


if hasattr(
    best_model,
    "feature_importances_"
):

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": best_model.feature_importances_

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).head(10)

    plt.figure(figsize=(8, 5))

    sns.barplot(

        data=importance_df,

        x="Importance",

        y="Feature"
    )

    plt.title(
        "Top Feature Importances"
    )

    plt.savefig(
        "reports/feature_importance.png"
    )

    plt.close()

    importance_df.to_csv(
        "reports/feature_importance.csv",
        index=False
    )


results_df.to_csv(
    "reports/model_comparison.csv",
    index=False
)


joblib.dump(
    best_model,
    "models/saved_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

joblib.dump(
    metrics,
    "models/model_metrics.pkl"
)

joblib.dump(
    results_df,
    "models/comparison_results.pkl"
)

joblib.dump(
    feature_names,
    "models/feature_names.pkl"
)


confusion_data = {

    "y_test": y_test,

    "y_pred": best_predictions
}

joblib.dump(
    confusion_data,
    "models/confusion_matrix.pkl"
)


print(
    "Training completed successfully.",
    flush=True
)