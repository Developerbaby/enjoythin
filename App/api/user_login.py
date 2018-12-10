from flask_restful import Resource


class LoginModel(Resource):
    def get(self):
        return {"msg": "user is not existed", "status": "404"}

    def post(self):
        pass
