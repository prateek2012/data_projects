"""

Contains utility functions used across the project.
"""

import pandas as pd

def load_dataset(file_path):
    df = pd.read_json(file_path, lines=True)
    df["listened_at"] = pd.to_datetime(df["listened_at"], unit="s")
    return df


def flatten_dataset(df):
    return pd.DataFrame(
        {
            "user_name": df["user_name"],
            "track_name": df["track_metadata"].apply(
                lambda x: x["track_name"] if pd.notnull(x) else None
            ),
            "artist_name": df["track_metadata"].apply(
                lambda x: x["artist_name"] if pd.notnull(x) else None
            ),
            "listened_at": df["listened_at"],
        }
    )
