from flask import Blueprint, request

from src.validate_field.validate_schema import validate_schema_flask, SUCCESS_CODE, FAIL_CODE

from src.orders.http.validation import order_validation_fields

from src.auth.auth import token_required


def create_orders_blueprint(manage_order_usecase):

    blueprint = Blueprint("orders", __name__)

    @blueprint.route("/orders", methods = ["GET"])
    @token_required
    def get_orders():

        orders = manage_order_usecase.get_orders()

        orders_dict = [order.serialize() for order in orders]
        
        data = orders_dict
        code = SUCCESS_CODE
        message = "Orders obtained succesfully"
        http_code = 200

        response = {
            "code": code,
            "message": message,
            "data": data,
        }
        
        return response, http_code


    @blueprint.route("/orders", methods = ["POST"])
    @validate_schema_flask(order_validation_fields.ORDER_CREATION_VALIDATION_FIELDS)
    @token_required
    def create_order():

        body = request.get_json()

        try:
            order = manage_order_usecase.create_order(body)
            data = order.serialize()
            code = SUCCESS_CODE
            message = "Order created succesfully"
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

    @blueprint.route("/orders/<string:order_id>", methods = ["GET"])
    @token_required
    def get_order(order_id):

        order = manage_order_usecase.get_order(order_id)

        if order:
            data = order.serialize()
            code = SUCCESS_CODE
            message = "order obtained succesfully"
            http_code = 200

        else:
            data = None
            code = FAIL_CODE
            message = f"Order of ID {order_id} does not exist."
            http_code = 404

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data
        
        return response, http_code

    @blueprint.route("/orders/<string:order_id>", methods = ["PUT"])
    @validate_schema_flask(order_validation_fields.ORDER_UPDATE_VALIDATION_FIELDS)
    @token_required
    def update_order(order_id):

        body = request.get_json()

        try:
            order = manage_order_usecase.update_order(order_id, body)
            data = order.serialize()
            message = "order updated succesfully"
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

    @blueprint.route("/orders/<string:order_id>", methods = ["DELETE"])
    @token_required
    def delete_order(order_id):

        try:
            manage_order_usecase.delete_order(order_id)
            code = SUCCESS_CODE
            message = f"order of ID {order_id} deleted succesfully."
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

