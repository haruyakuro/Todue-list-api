from fastapi import HTTPException
from supabase import supabase

def get_all_items():
    try:
        response = supabase.table("items").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching items: {str(e)}")

