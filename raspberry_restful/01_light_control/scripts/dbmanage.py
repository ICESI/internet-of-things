import sys
sys.path.append("..") # Adds higher directory to python modules path.

from app.database.db import session
from app.database.db import engine
from app.database.models import Base
from app.database.models import Room

#If there is just one argument exit, first argument is the script name
if len(sys.argv) <= 1:
	print("usage:\n\
	 python dbmanage.py create\n\
	 python dbmanage.py drop\n\
	 python dbmanage.py truncate\n\
	 python dbmanage.py insert_room id\n")
	sys.exit()

action = sys.argv[1]

if action == "create":
	Base.metadata.create_all(engine)

if action == "drop":
	Base.metadata.drop_all(engine)

if action == "truncate":
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

if action == "insert_room":

	if len(sys.argv) <= 2:
		print("usage: python dbmanage.py insert_room id")
		sys.exit()

	id = sys.argv[2]
	state = "off"
	mode = "manual"
	url = "192.168.130.2"
	room = Room(id, state, mode, url)
	session.add(room)
	session.commit()

if action == "query_all":

	rooms = session.query(Room)
	for room in rooms:
		print(room.id,room.state,room.mode,room.url)