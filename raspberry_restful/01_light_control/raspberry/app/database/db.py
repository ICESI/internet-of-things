from app.settings import SQLALCHEMY_DATABASE_URI

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Establish a connection with the database
engine = create_engine(SQLALCHEMY_DATABASE_URI) #echo=True
Session = sessionmaker(bind=engine)
session = Session()
