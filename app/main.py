from fastapi import FastAPI
from app.core.exceptions import validation_exception_handler
from app.routes import productos
from fastapi.exceptions import RequestValidationError
from starlette.types import ExceptionHandler
from typing import cast
from app.core.config import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# registrar archivo de rutas
@app.get("/", tags=["health"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "message": "API inventario activa"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar archivo de rutas (productos.py)
app.include_router(productos.router)

# registrar el manejador de excepciones personalizado
app.add_exception_handler(
    RequestValidationError,
    cast(ExceptionHandler, validation_exception_handler),
)


