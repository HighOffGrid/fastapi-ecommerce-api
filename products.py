from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from app.database.connection import get_db
from app.models.product import Product
from app.schemas.product import ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@router.post("/", response_model=ProductResponse)
def create_product(
    name: str = Form(...),
    description: str = Form(...),
    price: str= Form(...),
    stock: int = Form(...),
    db: Session = Depends(get_db)
):
    price_float = float(price.replace(",", "."))

    db_product = Product(
    name=name,
    description=description,
    price=price_float,
    stock=stock,
    category_id=3 
)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
     db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = name
    product.description = description
    product.price = price
    product.stock = stock

    db.commit()
    db.refresh(product)
    return product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    

    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}