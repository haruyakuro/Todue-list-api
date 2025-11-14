from fastapi import HTTPException
from supabase import supabase

def get_item(item_id: int):
    try:
        response = supabase.table("items").select("*").eq("id", item_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching item: {str(e)}")

