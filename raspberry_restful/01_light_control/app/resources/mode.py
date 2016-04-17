from app.database.db import session
from app.database.models import Room
from flask_restful import Resource
from flask import Flask, jsonify, request
import json
import requests

class Mode(Resource):

	# url: 127.0.0.1:5000/lightcontrol/v1.0/1/mode
	def get(self,roomid):
		query_result = session.query(Room).filter_by(id=roomid).first()
		mode = query_result.mode
		return {'mode': mode}

	# url: 127.0.0.1:5000/lightcontrol/v1.0/1/mode
	# data: {"mode":"automatic"}
	def put(self,roomid):
		mode = request.json['mode']
		room = session.query(Room).filter_by(id=roomid).first()
		room.mode = mode
		session.commit()

		# si envia modo automatico al mkr1000, el nuevo modo pone en envio continuo de ajuste de estado al mkr1000
		# si envio modo manual al mkr1000, desactiva el envio continuo de ajuste de estado

		return {'mode': mode}

		