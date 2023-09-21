from connect import engine, Base
from customer import Customer
from transaction import Transaction

print("Creating Tables")
Base.metadata.create_all(bind=engine)