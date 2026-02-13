
#coneccion con supabase
#instalar "pip install supabase" 
#instalar pip freeze >requirements.txt

from supabase import create_client, Client
from app.core.config import config

def get_supabase_client() -> Client:
    return create_client(config.supabase_url, config.supabase_key)
