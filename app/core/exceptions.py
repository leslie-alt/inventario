
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

MENSAJES_ERROR = {
    "listar_productos": {
        "limit": {
            "greater_than_equal": "El parámetro 'limit' no puede ser negativo ni menor que 1.",
            "less_than_equal": "El parámetro 'limit' no puede ser mayor a 200.",
            "int_parsing": "El parámetro 'limit' debe ser un número entero.",
            "missing": "El parámetro 'limit' es obligatorio.",
        },
        "offset": {
            "greater_than_equal": "El parámetro 'offset' no puede ser negativo.",
            "int_parsing": "El parámetro 'offset' debe ser un número entero.",
            "missing": "El parámetro 'offset' es obligatorio.",
        },
    },
    "listar_productos_slash": {
        "limit": {
            "greater_than_equal": "El parámetro 'limit' no puede ser negativo ni menor que 1.",
            "less_than_equal": "El parámetro 'limit' no puede ser mayor a 200.",
            "int_parsing": "El parámetro 'limit' debe ser un número entero.",
            "missing": "El parámetro 'limit' es obligatorio.",
        },
        "offset": {
            "greater_than_equal": "El parámetro 'offset' no puede ser negativo.",
            "int_parsing": "El parámetro 'offset' debe ser un número entero.",
            "missing": "El parámetro 'offset' es obligatorio.",
        },
    },
    "crear_producto": {
        "quantity": {
            "greater_than_equal": "El campo 'quantity' no puede ser negativo ni menor que 1.",
            "int_parsing": "El campo 'quantity' debe ser un número entero.",
        },
        "min_stock": {
            "greater_than_equal": "El campo 'min_stock' no puede ser negativo.",
            "int_parsing": "El campo 'min_stock' debe ser un número entero.",
        },
        "max_stock": {
            "greater_than_equal": "El campo 'max_stock' no puede ser negativo.",
            "int_parsing": "El campo 'max_stock' debe ser un número entero.",
        },
    },
    "crear_producto_slash": {
        "quantity": {
            "greater_than_equal": "El campo 'quantity' no puede ser negativo ni menor que 1.",
            "int_parsing": "El campo 'quantity' debe ser un número entero.",
        },
        "min_stock": {
            "greater_than_equal": "El campo 'min_stock' no puede ser negativo.",
            "int_parsing": "El campo 'min_stock' debe ser un número entero.",
        },
        "max_stock": {
            "greater_than_equal": "El campo 'max_stock' no puede ser negativo.",
            "int_parsing": "El campo 'max_stock' debe ser un número entero.",
        },
    },
    "actualizar_producto": {
        "product_id": {
            "uuid_parsing": "El parámetro 'product_id' debe ser un UUID válido.",
            "missing": "El parámetro 'product_id' es obligatorio.",
        },
        "quantity": {
            "greater_than_equal": "El campo 'quantity' no puede ser negativo ni menor que 1.",
            "int_parsing": "El campo 'quantity' debe ser un número entero.",
        },
        "min_stock": {
            "greater_than_equal": "El campo 'min_stock' no puede ser negativo.",
            "int_parsing": "El campo 'min_stock' debe ser un número entero.",
        },
        "max_stock": {
            "greater_than_equal": "El campo 'max_stock' no puede ser negativo.",
            "int_parsing": "El campo 'max_stock' debe ser un número entero.",
        },
    },
    "eliminar_producto": {
        "product_id": {
            "uuid_parsing": "El parámetro 'product_id' debe ser un UUID válido.",
            "missing": "El parámetro 'product_id' es obligatorio.",
        },
    },
}

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = [] # Lista para almacenar los mensajes de error personalizados
    ruta_obj= request.scope.get("route") #entrga el objeto ruta completa
    ruta_name= getattr(ruta_obj, "name", "") #obtiene el nombre de la ruta
    print(f"Ruta name: {ruta_name}")
    print(exc.errors())
    for error in exc.errors():
        parametro = error.get("loc")[-1] #obtiene el nombre del parametro con error
        tipo = error.get("type") #obtiene el tipo de error
        ruta_dicc=MENSAJES_ERROR.get(ruta_name,{}) #diccionario de errores para la ruta
        parametro_dicc=ruta_dicc.get(parametro,{}) #diccionario de errores para el parametro
        mensaje_dicc= parametro_dicc.get(tipo, f"ERROR EN EL PARAMETRO {parametro}") #mensaje personalizado o el por defecto
        errores.append(mensaje_dicc)    
    
    return JSONResponse(
        status_code=422, #Unprocessable Entity
        content={"detalles": errores}
    )