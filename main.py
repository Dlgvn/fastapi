from supabase import create_client, Client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# https://docs.render.com/deploy-fastapi

url: str = "https://fhbnbquxzuumvhmycflu.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZoYm5icXV4enV1bXZobXljZmx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE4Mzk0NDksImV4cCI6MjA1NzQxNTQ0OX0.odm7X9uZO6DEkynv4AVIgllDtOojWnIwU1zAtafRMnI"

supabase: Client = create_client(url, key)

app = FastAPI()

class ChocolateBar(BaseModel):
    company: str
    specific_bean_origin_or_bar_name: str
    ref: int
    review_date: int
    cocoa_percent: str
    company_location: str
    rating: float
    bean_type: str
    broad_bean_origin: str

@app.post("/chocolate_bar/")
def create_chocolate_bar(chocolatebar: ChocolateBar):
    data = supabase.table("chocolate_bars").insert(chocolatebar.dict()).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=400, detail="Chocolate bar could not be created")
    

@app.get("/chocolate_bars/")
def read_chocolate_bars():
    data = supabase.table("chocolate_bars").select("*").execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Chocolate bar not found")
    

@app.put("/chocolate_bars/{chocolate_bar_id}")
def update_chocolate_bars(chocolate_bar_id: int, chocolatebar: ChocolateBar):
    data = supabase.table("chocolate_bars").update(chocolatebar.dict()).eq("id", chocolate_bar_id).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Chocolate bar not found")

@app.delete("/chocolate_bars/{chocolate_bar_id}")
def delete_chocolate_bars(chocolate_bar_id: int):
    data = supabase.table("chocolate_bars").delete().eq("id", chocolate_bar_id).execute()
    if data.data:
        return {"message": "Chocolate bar deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Chocolate bar not found")
    
