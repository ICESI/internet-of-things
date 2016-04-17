from flask import Flask, render_template
from flask_restful import Api
from app.resources.mode import Mode
from app.resources.state import State

app = Flask(__name__,static_url_path='/static')

#Load default configurations, usually from developer environment
app.config.from_object('app.settings')
print("DATABASE " + str(app.config['SQLALCHEMY_DATABASE_URI']))

# CORS
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response

# Init
@app.route('/')
def location():
	return render_template('index.html')

# Error Page
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Routes
# API REST
#http://flask-restful-cn.readthedocs.org/en/0.3.5/reqparse.html
api = Api(app)
api.add_resource(Mode, '/lightcontrol/v1.0/<int:roomid>/mode')
api.add_resource(State, '/lightcontrol/v1.0/<int:roomid>/state')