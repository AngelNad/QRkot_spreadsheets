from datetime import datetime

from sqlalchemy import DATETIME, Boolean, Column, Integer

from app.core.db import Base


class CharityBase(Base):

    __abstract__ = True

    full_amount = Column(Integer, nullable=False, )
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DATETIME, default=datetime.now)
    close_date = Column(DATETIME)

    def __repr__(self):
        return (
            f'full_amount: {self.full_amount}, '
            f'invested_amount: {self.invested_amount}, '
            f'create_date: {self.create_date}'
        )
