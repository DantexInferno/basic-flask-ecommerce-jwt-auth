from functools import wraps

import logging

from werkzeug.exceptions import HTTPException

from flask import request

from .cerberus import validate_schema

# Decorador de conveniencia para validar el JSON de entrada en aplicaciones hechas en Flask.
# Toma los datos obtenidos del request y los compara con el esquema recibido. Si la validación
# resulta correcta, la ejecución continúa normalmente, de lo contrario retorna una respuesta de error.

FAIL_CODE = "fail"
SUCCESS_CODE = "success"

def validate_schema_flask(schema):
    
    def decorator(f):
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            
            json_data = request.get_json()
            errors = validate_schema(json_data, schema)

            if not errors:
                return f(*args, **kwargs)

            status_code = 400
            return errors, status_code 

        return wrapper
    
    return decorator


def flask_error_handler(e):

    # Manejador de errores para excepciones genéricas. De esta forma se retorna
    # un JSON con el error en vez de retornar una página HTML en caso de error.
    
    # Igual se deben manejar los errores específicos en el blueprint; este handler
    # es sólo para las excepciones que no son manejadas manualmente.

    logging.exception(e)

    code = "fail"
    message = "Internal error during request"
    http_code = 500

    if isinstance(e, HTTPException):
        message = str(e)
        http_code = e.code

    response = {
        "code": code,
        "message": message,
    }
    
    return response, http_code
