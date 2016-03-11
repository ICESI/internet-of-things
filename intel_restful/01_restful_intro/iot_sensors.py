from flask import Flask
import logging
import random

#intel galileo libraries
import time
import mraa

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#creating a file handler
handler = logging.FileHandler('iot_sensors.log')
handler.setLevel(logging.DEBUG)
#creating a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
#adding the handler to the logger
logger.addHandler(handler)

@app.route("/api/v1.0/iot_sensors")
@app.route("/api/v1.0")
@app.route("/api")
def api_version():
	logger.info('Showing mraa version')
	return mraa.getVersion()

@app.route("/api/v1.0/iot_sensors/hygrometers/1")
def get_humidity_data():
        logger.info('Reading virtual humidity data')
	sensor_value = random.random() 
        logger.debug('virtual humidity value : %f', sensor_value)
        return str(sensor_value) 

@app.route("/api/v1.0/iot_sensors/<sensor_name>/")
def get_sensors_by_type(sensor_name):
        logger.info('listing sensors')
        return 'listing sensors of type: ' + sensor_name

@app.route("/api/v1.0/iot_sensors/<sensor_name>/<int:sensor_id>")
def get_sensors_by_typeid(sensor_name,sensor_id):
	logger.info('Selecting a sensor by type and id')
	sensor_id = str(sensor_id)
	return 'you selected a sensor of type ' + sensor_name + ' and id ' + sensor_id

if __name__ == "__main__":
	#allow to make changes in the source code and test
	app.run('0.0.0.0',debug=True)

# Get flask version
#import flask
#flask.__version__
#http://flask.pocoo.org/docs/0.10/config/