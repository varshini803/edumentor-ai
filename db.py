import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("user_history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature TEXT,
            topic TEXT,
            detail TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def log_interaction(feature, topic, detail):
    conn = sqlite3.connect("user_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (feature, topic, detail) VALUES (?, ?, ?)", 
              (feature, topic, detail))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect("user_history.db")
    c = conn.cursor()
    c.execute("SELECT feature, topic, detail, timestamp FROM history ORDER BY timestamp DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return rows
