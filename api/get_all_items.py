from fastapi import HTTPException
from db import supabase_client

def get_all_items():
    try:
        response = supabase_client.table("items").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching items: {str(e)}")

