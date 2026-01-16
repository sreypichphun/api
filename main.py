from fastapi import FastAPI
import uvicorn

from api.v1.users import router as user_router
from core.config import settings
from db.base import Base
from db.session import engine

# ✅ import models here (register tables)
from models import user  # noqa

app = FastAPI(title=settings.APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
