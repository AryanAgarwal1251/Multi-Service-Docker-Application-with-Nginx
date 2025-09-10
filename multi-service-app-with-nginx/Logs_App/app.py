import flask
import sqlite3
import datetime
import os

app = flask.Flask(__name__)
DB_FILE = "logs.db"

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            service TEXT,
            message TEXT
        )''')
        conn.commit()
        conn.close()

@app.route("/log_post", methods=["POST"])
def log():
    data = flask.request.get_json()
    log_entry = (
        datetime.datetime.now().isoformat(),
        data.get("service", "unknown"),
        data.get("message", "")
    )

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, service, message) VALUES (?, ?, ?)", log_entry)
    conn.commit()
    conn.close()

    return flask.jsonify({"status": "logged", "entry": log_entry}), 201

@app.route("/log_get", methods=["GET"])
def get_logs():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT timestamp, service, message FROM logs ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    logs = [{"timestamp": r[0], "service": r[1], "message": r[2]} for r in rows]
    return flask.jsonify(logs)

if __name__ == "__main__":
    init_db()
    # Bind to all interfaces so accessible in Docker network
    app.run(host="0.0.0.0", port=6000, debug=True)
