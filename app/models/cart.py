from sqlalchemy import Column, Integer, ForeignKey
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)

    user = relationship("User", back_populates="carts")
    product = relationship("Product", back_populates="carts")
    items = relationship("CartItem", back_populates="cart")