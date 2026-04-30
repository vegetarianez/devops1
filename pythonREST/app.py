import os
import psycopg2
from flask import Flask
from datetime import datetime

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "hello_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "password")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            dt TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def hello():
    name = os.getenv("NAME", "Guest")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO visits (name, dt) VALUES (%s, %s)",
        (name, datetime.now())
    )
    conn.commit()

    cur.execute("SELECT name, dt FROM visits ORDER BY dt DESC LIMIT 5;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    history = "".join(
        [f"<li>{r[1].strftime('%H:%M:%S')} - {r[0]}</li>" for r in rows]
    )

    return f"""
    <h1>Hello {name}</h1>
    <h3>Recent visits:</h3>
    <ul>{history}</ul>
    """


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5001)