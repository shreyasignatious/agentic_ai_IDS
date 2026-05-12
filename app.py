import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import numpy as np

from agents.llm_agent import analyze_with_llm
from agents.threat_agent import predict_uploaded_dataset

from utils.encryption import encrypt_data
from utils.encryption import decrypt_data
from utils.hashing import generate_hash

from database.database import insert_log


st.set_page_config(
    page_title="AI Cybersecurity Framework",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00FFAA;
}

.stButton > button {
    background-color: #00AAFF;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 15em;
}

</style>
""", unsafe_allow_html=True)


metrics = joblib.load(
    "models/model_metrics.pkl"
)

model = joblib.load(
    "models/saved_model.pkl"
)

feature_names = joblib.load(
    "models/feature_names.pkl"
)

comparison_df = joblib.load(
    "models/comparison_results.pkl"
)


st.title(
    "AI-Assisted Cybersecurity Analysis Framework"
)


st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Threat Analysis",
        "Dataset Analysis",
        "Encryption",
        "Hashing",
        "Dashboard"
    ]
)


if menu == "Threat Analysis":

    st.header("AI Threat Analysis")

    user_input = st.text_area(
        "Enter suspicious activity"
    )

    if st.button("Analyze Threat"):

        if user_input.strip() != "":

            try:

                with st.spinner(
                    "Analyzing cybersecurity threat..."
                ):

                    result = analyze_with_llm(
                        user_input,
                        "Text Analysis",
                        95
                    )

                st.subheader(
                    "Threat Analysis Result"
                )

                st.write(result)

                insert_log(
                    user_input,
                    "Threat Analysis Completed",
                    95
                )

            except Exception as error:

                st.error(
                    f"Analysis failed: {error}"
                )

        else:

            st.warning(
                "Please enter suspicious activity."
            )


elif menu == "Dataset Analysis":

    st.header("Dataset Threat Analysis")

    uploaded_file = st.file_uploader(
        "Upload CICIDS2017 CSV File",
        type=["csv"]
    )

    if uploaded_file:

        try:

            df = pd.read_csv(
                uploaded_file
            ).sample(
                10000,
                random_state=42
            )

            st.subheader(
                "Dataset Preview"
            )

            st.dataframe(
                df.head()
            )

            with st.spinner(
                "Running machine learning analysis..."
            ):

                predictions, probabilities = (
                    predict_uploaded_dataset(df)
                )

            df['Prediction'] = predictions

            df['Prediction'] = df[
                'Prediction'
            ].map({
                0: 'Benign',
                1: 'Malicious'
            })

            df['Severity'] = df[
                'Prediction'
            ].map({
                'Benign': 'Low',
                'Malicious': 'Critical'
            })

            st.subheader(
                "Prediction Results"
            )

            st.dataframe(
                df[
                    ['Prediction', 'Severity']
                ].head()
            )

            prediction_counts = (
                df['Prediction']
                .value_counts()
                .reset_index()
            )

            prediction_counts.columns = [
                'Threat Type',
                'Count'
            ]

            fig = px.bar(
                prediction_counts,
                x='Threat Type',
                y='Count',
                title='Threat Distribution'
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            severity_counts = (
                df['Severity']
                .value_counts()
                .reset_index()
            )

            severity_counts.columns = [
                'Severity',
                'Count'
            ]

            severity_fig = px.pie(
                severity_counts,
                names='Severity',
                values='Count',
                title='Threat Severity Distribution'
            )

            st.plotly_chart(
                severity_fig,
                use_container_width=True
            )

            benign_count = (
                df['Prediction']
                .value_counts()
                .get('Benign', 0)
            )

            malicious_count = (
                df['Prediction']
                .value_counts()
                .get('Malicious', 0)
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Benign Traffic",
                    benign_count
                )

            with col2:
                st.metric(
                    "Malicious Traffic",
                    malicious_count
                )

            csv = df.to_csv(
                index=False
            ).encode('utf-8')

            st.download_button(
                label="Download Prediction Report",
                data=csv,
                file_name="threat_predictions.csv",
                mime="text/csv"
            )

        except Exception as error:

            st.error(
                f"Dataset analysis failed: {error}"
            )


elif menu == "Encryption":

    st.header("AES Encryption Module")

    plain_text = st.text_area(
        "Enter sensitive text"
    )

    if st.button("Encrypt Data"):

        try:

            encrypted = encrypt_data(
                plain_text
            )

            st.subheader(
                "Encrypted Output"
            )

            st.code(encrypted)

            decrypted = decrypt_data(
                encrypted
            )

            st.subheader(
                "Decrypted Output"
            )

            st.success(decrypted)

        except Exception as error:

            st.error(
                f"Encryption failed: {error}"
            )


elif menu == "Hashing":

    st.header("SHA256 Hash Generator")

    hash_input = st.text_area(
        "Enter text for hashing"
    )

    if st.button("Generate Hash"):

        try:

            hash_result = generate_hash(
                hash_input
            )

            st.subheader(
                "Generated Hash"
            )

            st.code(hash_result)

        except Exception as error:

            st.error(
                f"Hash generation failed: {error}"
            )


elif menu == "Dashboard":

    st.header(
        "Cybersecurity Analytics Dashboard"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Accuracy",
            f"{metrics['accuracy']:.4f}"
        )

    with col2:
        st.metric(
            "Precision",
            f"{metrics['precision']:.4f}"
        )

    with col3:
        st.metric(
            "Recall",
            f"{metrics['recall']:.4f}"
        )

    with col4:
        st.metric(
            "F1 Score",
            f"{metrics['f1_score']:.4f}"
        )

    st.subheader(
        "Model Performance Comparison"
    )

    st.dataframe(
        comparison_df
    )

    fig_models = px.bar(
        comparison_df,
        x="Model",
        y=[
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],
        barmode='group',
        title="Machine Learning Model Comparison"
    )

    st.plotly_chart(
        fig_models,
        use_container_width=True
    )

    st.subheader(
        "Confusion Matrix"
    )

    cm = np.array([
        [4236, 0],
        [2, 5761]
    ])

    fig_cm = px.imshow(
        cm,
        text_auto=True,
        title="Confusion Matrix",
        labels=dict(
            x="Predicted",
            y="Actual"
        )
    )

    st.plotly_chart(
        fig_cm,
        use_container_width=True
    )

    st.subheader(
        "Top Important Features"
    )

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": model.feature_importances_

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).head(10)

    fig_importance = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation='h',
        title="Top 10 Important Features"
    )

    st.plotly_chart(
        fig_importance,
        use_container_width=True
    )