from app.database.db import session
from app.database.models import Room
from flask_restful import Resource
from flask import Flask, jsonify, request
import json
import requests

class State(Resource):

	# url: 127.0.0.1:5000/lightcontrol/v1.0/1/state
	def get(self,roomid):
		query_result = session.query(Room).filter_by(id=roomid).first()
		state = query_result.state
		return {'state': state}

	# url: 127.0.0.1:5000/lightcontrol/v1.0/1/state
	# data: {"state":"off"}
	def put(self,roomid):
		state = request.json['state']
		room = session.query(Room).filter_by(id=roomid).first()
		room.state = state
		session.commit()

		#enviar nuevo estado al mkr1000, el nuevo estado cambia el estado de la luz

		return {'state': state}

		
		