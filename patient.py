from fastapi import FastAPI
from routers import items
from db.session import Base, engine

app = FastAPI()

# Create all tables (you can also use Alembic later)
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(items.router)
