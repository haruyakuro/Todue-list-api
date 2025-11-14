from fastapi import HTTPException
from db import supabase_client

def get_item(item_id: int):
    try:
        response = supabase_client.table("items").select("*").eq("id", item_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching item: {str(e)}")

