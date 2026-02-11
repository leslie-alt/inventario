from fastapi import FastAPI
from app.routes import productos 
from app.core.exceptions import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.types import ExceptionHandler
from typing import cast


app = FastAPI()
app.include_router(productos.router)

#registrar el manejador de excepciones personalizado
app.add_exception_handler(
    RequestValidationError,cast(ExceptionHandler, validation_exception_handler))

#registar archivo de rutas (productos.py)
app.include_router(productos.router)