#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

engine = create_engine('sqlite:///devdata.db')
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

class Contact(DeclarativeBase):
    __tablename__ = 'contacts'

    #column definitions
    email = Column(u'email', Text(length=None, convert_unicode=False, assert_unicode=None))
    first_name = Column(u'first_name', Text(length=None, convert_unicode=False, assert_unicode=None))
    id = Column(u'id', Integer(), primary_key=True, nullable=False)
    last_name = Column(u'last_name', Text(length=None, convert_unicode=False, assert_unicode=None))

    #relation definitions


