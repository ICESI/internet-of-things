from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Boolean

Base = declarative_base()

class Room(Base):
	__tablename__ = 'room'
	id = Column(Integer, primary_key=True)
	state = Column(String(10), index=True)
	mode = Column(String(10), index=True)
	url = Column(String(120), index=True, unique=True)

	def __init__(self, id, state, mode, url):
		self.id = id
		self.state = state
		self.mode = mode
		self.url = url

	def __repr__(self):
		return '<identification %r>' % self.id
