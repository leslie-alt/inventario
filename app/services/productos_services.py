
from uuid import UUID  #uuis es un identificador único universal, se utiliza para identificar de manera única un producto en la base de datos
from datetime import date
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase_client
from app.core.config import config
from postgrest import CountMethod


def _table():
    sb = get_supabase_client()
    return sb.schema(config.supabase_schema).table(config.supabase_table)

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


def create_product(datos:dict):
    try:
        if not datos:
            raise HTTPException(status_code=400, detail="Error datos incompletos")
        datos = jsonable_encoder(datos)
        res = _table().insert(datos).execute()
        return res.data[0] if res.data else None
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el registro: {e}")


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