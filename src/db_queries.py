"""

This module contains functions for setting up the database and executing SQL queries based on the challenges.
"""

def create_table(con, df):
    con.execute("CREATE TABLE listens AS SELECT * FROM df")


def top_10_users(con):
    return con.execute(
        """
        SELECT user_name, COUNT(*) as listen
        FROM listens
        GROUP BY user_name
        ORDER BY listen DESC
        LIMIT 10
        ;
    """
    ).fetchdf()


def users_on_march_1(con):
    return con.execute(
        """
        SELECT COUNT(DISTINCT user_name) AS users_count
        FROM listens
        WHERE CAST(listened_at AS DATE) = '2019-03-01';
    """
    ).fetchdf()


def first_song_per_user(con):
    return con.execute(
        """
        WITH Firstlisten AS(
        SELECT  user_name,track_name,listened_at,
                ROW_NUMBER() OVER(PARTITION BY user_name
                ORDER BY listened_at) AS rn
        FROM listens)
        SELECT user_name,listened_at AS first_listen_time,track_name
        FROM Firstlisten
        WHERE rn = 1
        ORDER BY user_name
        ;
    """
    ).fetchdf()


def top_3_days_per_user(con):
    return con.execute(
        """
        WITH DailyListens AS (
            SELECT
                user_name,
                CAST(listened_at AS DATE) AS listen_date,
                COUNT(*) AS number_of_listens
            FROM listens
            GROUP BY user_name, listen_date
        ),
        RankedDays AS (
            SELECT
                user_name,
                listen_date,
                number_of_listens,
                RANK() OVER(PARTITION BY user_name
                ORDER BY number_of_listens DESC) AS rn
            FROM DailyListens
        )
        SELECT user_name, number_of_listens, listen_date
        FROM RankedDays
        WHERE rn <= 3
        ORDER BY user_name, number_of_listens DESC;
    """
    ).fetchdf()


def daily_active_users(con):
    return con.execute(
        """
        WITH AllDates AS (
            SELECT DISTINCT CAST(listened_at AS DATE) AS date
            FROM listens
        ),
        UserActivity AS (
            SELECT
                date,
                user_name
            FROM listens,
            AllDates
            WHERE CAST(listened_at AS DATE)
            BETWEEN date - INTERVAL 6 DAY AND date
        ),
        DailyActiveUsers AS (
            SELECT
                date,
                COUNT(DISTINCT user_name) AS number_active_users
            FROM UserActivity
            GROUP BY date
        ),
        TotalUsers AS (
            SELECT COUNT(DISTINCT user_name) AS total_users
            FROM listens
        )
        SELECT
            DailyActiveUsers.date,
            number_active_users,
            (number_active_users * 100.0 / TotalUsers.total_users)
            AS percentage_active_users
        FROM DailyActiveUsers, TotalUsers
        ORDER BY DailyActiveUsers.date;
    """
    ).fetchdf()
