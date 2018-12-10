from flask_restful import Api

from App.api.user_login import LoginModel

api = Api()

# 例子
api.add_resource(LoginModel, '/user/')


def init_url(app):
    api.init_app(app)
