
from uuid import UUID
from datetime import date
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase_client
from app.core.config import Config
from postgrest import CountMethod


def _table():
    sb = get_supabase_client()
    return sb.schema(Config.supabase_schema).table(Config.supabase_table)

def list_products(limit: int =100, offset:int=0):
    
    try:
        res=_table().select("*", count=CountMethod.exact).range(offset, offset+ + limit-1).execute() #sirve para
        if not res.data:
            raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
        return{"items": res.data , "total": res.count or 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
    


def get_product(product_id: UUID):
    try:
        res=_table().select("*").eq("id", str(product_id)).excecute()  #encontrar un limite 
        
        if not res.data:
            raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")
        return{"item": res.data[0] if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")


def create_product(product_id:UUID, datos:dict):
    try:
        if not datos or not product_id:
            raise HTTPException(status_code=500, detail=f"Error datos incompletos")
        datos= jsonable_encoder(datos)
        res=_table().update(datos).eq("id", str(product_id)).execute()
        return {"item": res.data[0]  if res.data else None}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")

def update_product(product_id:UUID, datos:dict):
    try:
        datos= jsonable_encoder(datos)
        res=_table().update(datos).eq("id", str(product_id)).execute()
        return {"item": res.data[0]  if res.data else None}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")

def delete_product(product_id:UUID, datos:dict):
    try:
        if not not  product_id:
            raise HTTPException(status_code=500, detail=f"Error datos incompletos")
        res=_table().delete().eq("id", str(product_id)).execute()
        return {"item": res.data[0]  if res.data else None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al mostar los registros{e}")