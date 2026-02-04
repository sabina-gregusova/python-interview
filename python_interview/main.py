from flask import Flask

from python_interview.infra.db import close_db, init_db
from python_interview.routes.users import users_blueprint

app = Flask(__name__)

app.teardown_appcontext(close_db)
app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    with app.app_context():
        init_db()

    app.run()
