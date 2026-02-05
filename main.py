from flask import Flask

from infra.db import close_db, init_db
from routes.users import users_blueprint

app = Flask(__name__)

app.teardown_appcontext(close_db)
app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    with app.app_context():
        init_db()

    app.run()
