import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

basedir = os.path.dirname(os.path.abspath(__file__))
path = 'sqlite:///' + os.path.join(basedir, 'data.db')
print(path)

Base = declarative_base()

engine = sqlalchemy.create_engine(path, echo=True)

# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

class Loans(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    spotreba = Column(Integer) # Float
    
    def __repr__(self):
        return "<Loans(Datum='', spotreba='%s)>" % (self.spotreba)

session = Session()

loan1 = Loans()
loan1.id = 0
loan1.spotreba=194785

session.add(loan1)
session.commit()

session.close()