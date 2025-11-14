from fastapi import HTTPException
from supabase import supabase
from model import ItemCreate

def add_item(item: ItemCreate):
    try:
        response = supabase.table("items").insert({
            "name": item.name,
            "kind": item.kind,
            "date": item.date,
            "score": item.score
        }).execute()
        
        return {"message": "取得完了", "data": response.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {str(e)}")

