

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import ForeignKey
from typing import List
from connect import Base

"""
Customer -> Transaction
"""


class Customer(Base):
    __tablename__="customer"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str]
    transactions:Mapped[List["Transaction"]] = relationship(back_populates='customer')

    def __repr__(self) -> str:
        return f"<Customer name:{self.name}. Id:{self.id}."
