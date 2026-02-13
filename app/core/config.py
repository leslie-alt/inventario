
#todas las variables que no se deben de ve
# r (variables a la bd)

from  pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Config(BaseSettings):  #hereda de BaseSettings
    #PRUEBA1="hola"  puedes usar el default o no, si no lo usas, es obligatorio que esté en el .env, pero es mejor de la otra manera
    prueba1: str = Field(default="HOLA", alias="PRUEBA1")  #alias es el nombre de la variable en el .env
    prueba2: int = Field(default=123, alias="PRUEBA2")
    supabase_url: str = Field(default="", alias="SUPABASE_URL")
    supabase_key: str = Field(default="", alias="SUPABASE_KEY")
    supabase_schema: str = Field(default="public", alias="SUPABASE_SCHEMA")
    supabase_table: str = Field(default="producto", alias="SUPABASE_TABLE")
    allowed_origins: list[str] = Field(default=[], alias="ALLOWED_ORIGINS")
    


    #configuración para leer el .env
    model_config = SettingsConfigDict( 
        env_file=".env", 
        env_file_encoding="utf-8",
        extra= "ignore" #ignora las variables que no estén en el modelo, si no lo pones, te va a dar error si hay una variable en el .env que no esté en el modelo
    )  

config = Config()  #crea una instancia de la clase Config, esto es lo que se va a usar en el resto del código para acceder a las variables de configuración




