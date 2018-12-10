from flask_cache import Cache
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
cache = Cache(config={'CACHE_TYPE': 'redis'})
login_manager = LoginManager()


def init_ext(app):
    migrate.init_app(app)

    db.init_app(app)

    sess = Session()

    sess.init_app(app)

    mail.init_app(app)

    cache.init_app(app)

    login_manager.init_app(app)
