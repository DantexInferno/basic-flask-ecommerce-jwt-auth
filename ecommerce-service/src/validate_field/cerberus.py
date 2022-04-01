from functools import wraps

from cerberus import Validator

# Funciónes para realizar la validación con Cerberus y su posterior traducción
# al formato usado a nivel de empresa.

FAIL_CODE = "fail"
SUCCESS_CODE = "success"

ERROR_TRANSLATIONS = [
    ["required field", "required"],
    ["must be of", "incorrect_type"],
    ["unknown field", "unknown"],
]

ERROR_MESSAGES = {
    "required": "Field required",
    "incorrect_type": "Field must be ",
    "unknown": "Unknown field",
}

def validate_schema(data, schema):

    # Recibe un diccionario con los datos por validar, y retorna un objeto con
    # los posibles errores con el formato correcto, de lo contrario retorna None.

    errors = None

    if data:

        validator = Validator()
        is_valid = validator.validate(data, schema)

        if is_valid:
            return None
        else:
            errors = _format_errors(validator.errors)

    else:
        
        errors = [{
            "code": "empty_body",
            "message": "Body must not be empty"
        }]

    results = {
        "code" : FAIL_CODE,
        "message": "There was an error in the input data",
        "errors": errors,
    }

    return results

def _format_errors(errors, parent_field = None):

    # Transforma el objeto de errores entregado por Cerberus al formato de errores
    # definido a nivel de empresa.

    # Si un error internamente contiene más errores, entonces se aplica recursión.

    formatted_errors = []

    for field_name, error_list in errors.items():

        if parent_field:
            field_name = f"{parent_field}.{field_name}"

        for value in error_list:

            if isinstance(value, str):
                
                code, message = _get_translation(value)

                formatted_error = {
                    "field": field_name,
                    "code": code,
                    "message": message,
                }

                formatted_errors.append(formatted_error)

            elif isinstance(value, dict):
                formatted_errors += _format_errors(value, parent_field = field_name)

    return formatted_errors

def _get_translation(text):

    # Busca el texto en la lista de traducciones y retorna su código y mensaje traducido.
    # De no encontrarlo, retorna la traducción por defecto.

    code = ERROR_TRANSLATIONS[0][1]

    for row in ERROR_TRANSLATIONS:

        value = row[0]
        translation = row[1]

        if value in text or text in value:
            code = translation

    # Buscar el mensaje según la traducción.

    message = ERROR_MESSAGES.get(code)

    if code == "incorrect_type":

        field_type = text.replace("must be of ", "").replace(" type", "")

        prefix = "a"
        if field_type in ["integer"]:
            prefix = "an"
        
        message += f"{prefix} {field_type}"

    return code, message