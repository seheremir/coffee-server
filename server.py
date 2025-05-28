from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class MemeRequest(BaseModel):
    template_id: str
    username: str
    password: str
    text0: str
    text1: str

@app.post("/generate")
async def generate_meme(req: MemeRequest):
    url = "https://api.imgflip.com/caption_image"
    params = {
        "template_id": req.template_id,
        "username": req.username,
        "password": req.password,
        "text0": req.text0,
        "text1": req.text1
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params)
        data = response.json()

    if data.get("success"):
        return {"meme_url": data["data"]["url"]}
    else:
        raise HTTPException(status_code=400, detail=f"Meme oluşturulamadı: {data.get('error_message')}")

@app.get("/")
def root():
    return {"message": "Meme MCP FastAPI çalışıyor."}
