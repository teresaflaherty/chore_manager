# flask_app.py
from flask import Flask, jsonify

from database_functions import read_query, execute_query, create_db_connection

app = Flask(__name__)


@app.route("/chores", methods=["GET"])
def get_all_chores():
    db_connection = create_db_connection()
    get_chores_query = f"SELECT * FROM chores;"
    chores = read_query(db_connection, get_chores_query)
    return jsonify(chores)


@app.route("/chores/<chore_id>", methods=["GET"])
def get_chore(chore_id):
    db_connection = create_db_connection()
    get_chore_query = f"SELECT * FROM chores WHERE id = {chore_id};"
    chore = read_query(db_connection, get_chore_query)
    return jsonify(chore)


@app.route("/chores/expired", methods=["GET"])
def get_expired_chores():
    db_connection = create_db_connection()
    get_expired_chores_query = f"SELECT * FROM chores WHERE time_remaining = 0;"
    chores = read_query(db_connection, get_expired_chores_query)
    return jsonify(chores)


@app.route("/chores/expiring", methods=["GET"])
def get_expiring_chores():
    db_connection = create_db_connection()
    get_expired_chores_query = f"SELECT * FROM chores WHERE time_remaining = 1;"
    chores = read_query(db_connection, get_expired_chores_query)
    return jsonify(chores)


@app.route("/chores/<chore_id>", methods=["PATCH"])
def reset_finished_chore(chore_id):
    db_connection = create_db_connection()
    reset_query = f"UPDATE chores SET time_remaining = frequency WHERE id = {chore_id};"
    execute_query(db_connection, reset_query)

    get_chore_query = f"SELECT * FROM chores WHERE id = {chore_id};"
    chore_as_list = read_query(db_connection, get_chore_query)

    with open("chores_to_do.txt", "r+") as chore_file:
        lines = chore_file.readlines()
        chore_file.seek(0)
        for line in lines:
            if line != chore_as_list[0]['name']:
                chore_file.write(line)
        chore_file.truncate()
    return jsonify(success=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
