import secrets
import sqlite3
import string

from flask import Blueprint, jsonify

from python_interview.infra import db

# Use this function to generate license keys
def generate_license_key(length=128):
    alphabet = (
        string.ascii_letters + string.digits
    )  # Character set for license key (62 characters a-zA-Z0-9)
    return "".join(secrets.choice(alphabet) for _ in range(length))


# POST /users/<user_id>/licenses

# GET /users/<user_id>/licenses
