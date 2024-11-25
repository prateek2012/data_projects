"""

This module contains functions for performing initial data analysis on the dataset to understand the data structure.
"""

import pandas as pd
from pandas import json_normalize


def init_data_analysis(df):

    # Datatype of each column
    print(df.dtypes)

    # Exploring the data
    print("\nStructure of 'track metadata' field")
    print(df["track_metadata"].apply(
        lambda x: x.keys() if pd.notnull(x) else {}).head()
    )

    df_metadata = json_normalize(df["track_metadata"])
    print("\nFlattened 'track_metadata structure: '")
    print(df_metadata.head())
