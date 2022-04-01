from flask import Blueprint, request, session

from src.validate_field.validate_schema import validate_schema_flask, SUCCESS_CODE, FAIL_CODE

from src.users.http.validation import user_validation_fields

from src.auth.auth import token_required, load_logged


def create_users_blueprint(manage_user_usecase):


    blueprint = Blueprint("users", __name__)


    @blueprint.before_app_request
    def load_logged_in_user():
        user_id = session.get('user_id')
        user = manage_user_usecase.get_user(user_id)
        load_logged(user)


    @blueprint.route("/users", methods = ["GET"])
    @token_required
    def get_users():

        users = manage_user_usecase.get_users()

        users_dict = [user.serialize() for user in users]
        
        data = users_dict
        code = SUCCESS_CODE
        message = "Users obtained succesfully"
        http_code = 200

        response = {
            "code": code,
            "message": message,
            "data": data,
        }
        
        return response, http_code


    @blueprint.route("/users", methods = ["POST"])
    @validate_schema_flask(user_validation_fields.USER_CREATION_VALIDATION_FIELDS)
    def create_user():

        body = request.get_json()

        try:
            user = manage_user_usecase.create_user(body)
            data = user.serialize()
            code = SUCCESS_CODE
            message = "User created succesfully"
            http_code = 201

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code

    @blueprint.route("/users/<string:user_id>", methods = ["GET"])
    @token_required
    def get_user(user_id):

        user = manage_user_usecase.get_user(user_id)

        if user:
            data = user.serialize()
            code = SUCCESS_CODE
            message = "User obtained succesfully"
            http_code = 200

        else:
            data = None
            code = FAIL_CODE
            message = f"User of ID {user_id} does not exist."
            http_code = 404

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data
        
        return response, http_code


    @blueprint.route("/users/login", methods = ["POST"])
    @validate_schema_flask(user_validation_fields.USER_LOGIN_VALIDATION_FIELDS)
    def get_login():

        body = request.get_json()
        
        try:
            user = manage_user_usecase.login(body)
            data = user
            code = SUCCESS_CODE
            message = "User logged succesfully"
            http_code = 201

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code


    @blueprint.route('/users/logout')
    def logout():
        session.clear()
        return "You are logged out"

    @blueprint.route("/users/<string:user_id>", methods = ["PUT"])
    @validate_schema_flask(user_validation_fields.USER_UPDATE_VALIDATION_FIELDS)
    @token_required
    def update_user(user_id):

        body = request.get_json()

        try:
            user = manage_user_usecase.update_user(user_id, body)
            data = user.serialize()
            message = "User updated succesfully"
            code = SUCCESS_CODE
            http_code = 200

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code

    @blueprint.route("/users/<string:user_id>", methods = ["DELETE"])
    @token_required
    def delete_user(user_id):

        try:
            manage_user_usecase.delete_user(user_id)
            code = SUCCESS_CODE
            message = f"User of ID {user_id} deleted succesfully."
            http_code = 200

        except ValueError as e:
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        return response, http_code
    
    return blueprint

