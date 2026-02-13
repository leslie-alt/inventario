

from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.producto import ProductCreate, productOut
from app.services.productos_services import create_product, get_product, list_products, delete_product, update_product


router = APIRouter(prefix="/productos", tags=["productos"])


@router.get("", name="listar_productos")
@router.get("/", name="listar_productos_slash")
def listar_productos(
    limit: int = Query(100, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    return list_products(limit, offset)


@router.get("/{product_id}", response_model=productOut, name="obtener_producto")
def api_get_product(product_id: UUID = Path(...)):
    return get_product(product_id)

@router.post("", response_model=productOut, name="crear_producto")
@router.post("/", response_model=productOut, name="crear_producto_slash")
def api_create_product(body: ProductCreate):
    return create_product(body.model_dump())


@router.delete("/{product_id}", name="eliminar_producto")
def api_delete_product(product_id: UUID):
    return delete_product(product_id)

@router.put("/{product_id}", response_model=productOut, name="actualizar_producto")
def api_update_product(product_id: UUID, body: ProductCreate):
    return update_product(product_id, body.model_dump())






