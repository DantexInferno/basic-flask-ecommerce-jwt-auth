from flask import Blueprint, request, session

from src.validate_field.validate_schema import validate_schema_flask, SUCCESS_CODE, FAIL_CODE

from src.sellers.http.validation import seller_validation_fields

from src.auth.auth import token_required, admin_required


def create_sellers_blueprint(manage_seller_usecase):

    blueprint = Blueprint("sellers", __name__)

    

    @blueprint.route("/sellers", methods = ["GET"])
    @token_required
    @admin_required
    def get_sellers():

        sellers = manage_seller_usecase.get_sellers()

        sellers_dict = [seller.serialize() for seller in sellers]
        
        data = sellers_dict
        code = SUCCESS_CODE
        message = "sellers obtained succesfully"
        http_code = 200

        response = {
            "code": code,
            "message": message,
            "data": data,
        }
        
        return response, http_code


    @blueprint.route("/sellers", methods = ["POST"])
    @validate_schema_flask(seller_validation_fields.SELLER_CREATION_VALIDATION_FIELDS)
    @token_required
    @admin_required
    def create_seller():

        body = request.get_json()

        try:
            seller = manage_seller_usecase.create_seller(body)
            data = seller.serialize()
            code = SUCCESS_CODE
            message = "seller created succesfully"
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

    @blueprint.route("/sellers/<string:seller_id>", methods = ["GET"])
    @token_required
    @admin_required
    def get_seller(seller_id):

        seller = manage_seller_usecase.get_seller(seller_id)

        if seller:
            data = seller.serialize()
            code = SUCCESS_CODE
            message = "seller obtained succesfully"
            http_code = 200

        else:
            data = None
            code = FAIL_CODE
            message = f"seller of ID {seller_id} does not exist."
            http_code = 404

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data
        
        return response, http_code

    @blueprint.route("/sellers/<string:seller_id>", methods = ["PUT"])
    @validate_schema_flask(seller_validation_fields.SELLER_UPDATE_VALIDATION_FIELDS)
    @token_required
    @admin_required
    def update_seller(seller_id):

        body = request.get_json()

        try:
            seller = manage_seller_usecase.update_seller(seller_id, body)
            data = seller.serialize()
            message = "seller updated succesfully"
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

    @blueprint.route("/sellers/<string:seller_id>", methods = ["DELETE"])
    @token_required
    @admin_required
    def delete_seller(seller_id):

        try:
            manage_seller_usecase.delete_seller(seller_id)
            code = SUCCESS_CODE
            message = f"seller of ID {seller_id} deleted succesfully."
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

