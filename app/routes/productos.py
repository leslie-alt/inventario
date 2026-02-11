

from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.producto import productOut, ProductUpdate,ProductCreate
from app.models.producto import Productlist
from app.services.productos_services import list_products, get_product, create_product, update_product, delete_product

router= APIRouter(prefix="/productos")

@router.get("/", name="listar productos")
def listar_productos(limit: int=Query(100, ge=1, le=200),offset: int=Query(0, ge=0)): #validar lo que llega
    return list_products(limit, offset)

@router.get("/{product_id}", response_model=productOut, name="obtener producto")
def api_get_product(product_id:UUID=Path(...)):
    return get_product(product_id)

@router.post("/", response_model=ProductCreate, name="crear_producto")

@router.post("/", response_model=productOut, name="crear_producto")
def api_create_product(body: ProductCreate):
    return create_product(body.model_dump())





