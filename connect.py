from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///sample.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
    print(result.all())

