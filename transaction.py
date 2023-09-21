from connect import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Transaction(Base):
    __tablename__="transaction"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id:Mapped[int] = mapped_column(ForeignKey('customer.id'),nullable=False)
    customer:Mapped["Customer"] = relationship(back_populates='transaction')

    def __repr__(self) -> str:
        return f"<Transaction id: {self.id}. Customer: {self.customer.name}"
