
#vamos a definir el esquema de datos para los productos y validaciones 

from pydantic import BaseModel, Field, field_validator
from datetime import datetime,date
from uuid import UUID

def validar_fecha_ingreso(value: date) -> date:   #funcion para validar que la fecha de ingreso no sea futura  
    if value < date.today():                        #-> compara la fecha ingresada con la fecha actual
        raise ValueError("La fecha de ingreso no puede ser menor a la fecha actual.")
    return value

class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=200)
    quantity: int = Field(ge=1)
    ingreso_date:date
    min_stock: int = Field(ge=0 )
    max_stock: int = Field(ge=0, le=1000) 

    @field_validator("ingreso_date")
    @classmethod
    def validar_fecha_ingreso(cls, value:date) ->date:   #cls es una referencia a la clase ProductCreate, se utiliza para acceder a los atributos y métodos de la clase dentro del validador
        return validar_fecha_ingreso(value)  #llama a la función validar_fecha_ingreso para realizar la validación de la fecha de ingreso


class ProductUpdate(BaseModel):
    name: str | None= Field(default=None, min_length=3, max_length=200) 
    quantity: int | None = Field(default=None, ge=1)
    ingreso_date:date
    min_stock: int | None = Field(default=None, ge=0 )
    max_stock: int | None = Field(default=None, ge=0, le=1000)

    @field_validator("ingreso_date")
    @classmethod
    def validar_fecha_ingreso(cls, value:date) ->date:   #cls es una referencia a la clase ProductCreate, se utiliza para acceder a los atributos y métodos de la clase dentro del validador
        return validar_fecha_ingreso(value)  #llama a la función validar_fecha_ingreso para realizar la validación de la fecha de ingreso
    



class productOut(BaseModel):
    id: UUID
    name: str
    quantity: int
    ingreso_date:date
    min_stock: int
    max_stock: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Productlist(BaseModel):
    total:int
    items:productOut

class OneProduct(BaseModel):
    items:list[productOut]
    


