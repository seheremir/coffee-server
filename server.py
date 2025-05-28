from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/random")
async def get_random_coffee():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://coffee.alexflipnote.dev/random.json")
        data = response.json()
    return data

@app.get("/")
def root():
    return {"message": "Coffee Server çalışıyor!"}
