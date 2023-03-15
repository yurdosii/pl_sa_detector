from fastapi import FastAPI

from src.api.pl_sa.views import router as pl_sa_router

app = FastAPI(title="My API")
app.include_router(pl_sa_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}
