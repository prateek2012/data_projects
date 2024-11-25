"""

Main script to execute the data analysis workflow.
"""

import duckdb
from utils import load_dataset, flatten_dataset
from data_analysis import init_data_analysis
from db_queries import (
    create_table,
    top_10_users,
    users_on_march_1,
    first_song_per_user,
    top_3_days_per_user,
    daily_active_users,
)


def main():
    file_path = "data/dataset.txt"

    # Load and preprocess dataset
    try:
        df = load_dataset(file_path)
    except Exception as e:
        print(f"Failed to load dataset: {e}")
        return

    df_flat = flatten_dataset(df)

    # Initial Data Analysis
    init_data_analysis(df)

    # Create DuckDB in-memory database
    con = duckdb.connect(database=":memory:")
    create_table(con, df_flat)

    # Execute queries
    print("Top 10 users by number of songs listened to:")
    print(top_10_users(con))

    print("Number of users who listened to a song on 1st March 2019:")
    print(users_on_march_1(con))

    print("First song each user listened to:")
    print(first_song_per_user(con))

    print("Top 3 days per user by the number of listens:")
    print(top_3_days_per_user(con))

    print("Daily active users and percentage of active users:")
    print(daily_active_users(con))


if __name__ == "__main__":
    main()
