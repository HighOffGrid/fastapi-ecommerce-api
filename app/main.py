from fastapi import FastAPI
from app.models.user import User
from app.models.product import Product
from app.models.cart import Cart
from app.routers import products, auth, users

app = FastAPI()
title = "E-commerce API"
version = "1.0.0"

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API!"}

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(auth.router)
app.include_router(users.router, prefix="/users", tags=["users"])
