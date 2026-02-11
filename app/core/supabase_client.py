
#coneccion con supabase
#instalar "pip install supabase" 
#instalar pip freeze >requirements.txt

from supabase import create_client, Client
from app.core.config import Config

def get_supabase_client() -> Client:
    return create_client(Config.supabase_url, Config.supabase_key)
