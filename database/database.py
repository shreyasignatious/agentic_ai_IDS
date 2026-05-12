import sqlite3
from datetime import datetime


connection = sqlite3.connect(
    "database/threats.db",
    check_same_thread=False
)

cursor = connection.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS threat_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    input_text TEXT,

    prediction TEXT,

    confidence REAL
)

""")

connection.commit()


def insert_log(
    input_text,
    prediction,
    confidence
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """

        INSERT INTO threat_logs (

            timestamp,
            input_text,
            prediction,
            confidence

        )

        VALUES (?, ?, ?, ?)

        """,

        (
            timestamp,
            input_text,
            prediction,
            confidence
        )
    )

    connection.commit()