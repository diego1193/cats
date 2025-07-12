from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.infrastructure.database.config import db_config
from app.presentation.controllers.user_controller import router as user_router
from app.presentation.controllers.cat_controller import router as cat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_config.connect()
    yield
    await db_config.disconnect()


app = FastAPI(
    title="Cat Breeds & Users API",
    description="A FastAPI application with cat breeds and user management",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(cat_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Cat Breeds & Users API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 