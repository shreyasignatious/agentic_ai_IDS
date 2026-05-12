import pandas as pd
import numpy as np


def preprocess_data(df):

    df.columns = df.columns.str.strip()

    df = df.loc[
        :,
        ~df.columns.duplicated()
    ]

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    df.fillna(
        0,
        inplace=True
    )

    df.drop_duplicates(
        inplace=True
    )

    numeric_columns = df.select_dtypes(
        include=['number']
    ).columns

    df[numeric_columns] = df[
        numeric_columns
    ].clip(
        lower=-1e10,
        upper=1e10
    )

    return df