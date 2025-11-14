from fastapi import HTTPException
from supabase import supabase
from model import ItemUpdate

def update_item(item_id: int, item: ItemUpdate):
    try:
        update_data = item.model_dump(exclude_unset=True)
        
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        response = supabase.table("items").update(update_data).eq("id", item_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return {"message": "編集完了しました", "data": response.data[0]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating item: {str(e)}")

