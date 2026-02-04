import sqlite3

from flask import Blueprint, jsonify, request

from python_interview.infra import db

users_blueprint = Blueprint("users", __name__)


# GET /users
@users_blueprint.route("/users", methods=["GET"])
def get_users():
    conn = db.get_db()
    users = conn.execute("SELECT id, name, email FROM user").fetchall()
    return jsonify([dict(u) for u in users])


# POST /users
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400

    name = data["name"]
    email = data["email"]

    try:
        conn = db.get_db()
        conn.execute(
            "INSERT INTO user (name, email) VALUES (?, ?)",
            (name, email),
        )
        conn.commit()

    except sqlite3.IntegrityError:
        return jsonify({"error": "User already exists"}), 409

    return (
        jsonify(
            {
                "message": "User created",
                "user": {"name": name, "email": email},
            }
        ),
        201,
    )
