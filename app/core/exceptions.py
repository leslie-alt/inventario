
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

MENSAJES_ERROR = {
    "multiplicacion1_1_10": {
        "num1": {
            "less_than_equal": "El primer parametro debe ser menor o igual a 10",
            "greater_than_equal": "El primer parametro debe ser mayor o igual a 1",
            "int_parsing": "El primer parametro debe ser un numero",
            "missing": "El primer parametro falta"
        },
        "num2": {
            "less_than_equal": "El segundo parametro debe ser menor o igual a 10",
            "greater_than_equal": "El segundo parametro debe ser mayor o igual a 1",
            "int_parsing": "El segundo parametro debe ser un numero",
            "missing": "El segundo parametro falta"
        }
    }
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