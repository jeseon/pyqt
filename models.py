from sqlalchemy import func, create_engine, Column, Integer, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:4447@localhost:3306/pandora', echo=True)
Base = declarative_base()


class BaseMixin(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(BaseMixin, Base):
    __tablename__ = 'user'

    name = Column(Unicode)
    email = Column(Unicode)
