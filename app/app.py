
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host="db"
        )
        return "✅ Connected to PostgreSQL!"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
