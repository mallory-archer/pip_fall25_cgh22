from flask import Flask, jsonify, render_template, request
import os
import psycopg2

app = Flask(__name__)


# add database connection
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = ""

def get_db_connection():
    return psycopg2.connect(
        dbname="railway",
        user="postgres",
        password="dwRMljIdxRNYICcJFIjbWrknYfcGyZqr",
        host="trolley.proxy.rlwy.net",
        port="34517"
    )


@app.route("/", methods=["GET", "POST"])
def home():
    custom_greeting = "Custom hello world"
    if request.method == "POST":
        custom_greeting = request.form.get("customGreeting")
    return render_template("hello_world.html", greeting=custom_greeting)


@app.route("/db-test", methods=["GET", "POST"])
def db_test():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW() AS server_time;")
    row = cur.fetchone()
    cur.close()
    conn.close()
    return f"Postgres says the time is: {row[0]}"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))







# def get_db_data():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM subway_data")
#     db_data = cur.fetchall()
#     cur.close()
#     conn.close()
#     return db_data

