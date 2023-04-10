from fastapi import FastAPI

from .api.messages_views import router as messages_router
from .api.users_views import router as users_router

app = FastAPI(title="My API")
app.include_router(messages_router)
app.include_router(users_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "API World"}
