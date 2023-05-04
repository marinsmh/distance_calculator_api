from fastapi import FastAPI
import uvicorn

from services.distance_calculator import router

app = FastAPI()

description = """
Distance Calculator API
"""

app = FastAPI(
    title="Distance Calculator API",
    description=description,
    version="0.0.1",
    contact={
        "name": "Marina",
        "email": "marina.martin.hernandez@outlook.com",
    },
    docs_url="/docs",
    responses={404: {"description": "Not found"}}
)

# Routers
app.include_router(router)


@app.get("/")
async def main_route():
    return {"message": "Welcome to the Fastapi core API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
