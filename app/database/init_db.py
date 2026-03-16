from app.database.connection import Base, engine
from app.models.user import User
from app.models.product import Product
from app.models.cart import Cart
from app.models.category import Category

Base.metadata.create_all(bind=engine)
print("Banco inicializado com sucesso!")
