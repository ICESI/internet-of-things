from flask import Flask
import logging

#intel galileo libraries
import mraa
import time
import random

#prepare the gpio for output
x_gpio = mraa.Gpio(8)
x_gpio.dir(mraa.DIR_OUT)
x_aio = mraa.Aio(0)

print (mraa.getVersion())

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

@app.route("/api/v1.0/iot_sensors/leds/1")
def get_led_status():
	logger.info('Changing led 1 status')
	if x_gpio.read() == 1:
		x_gpio.write(0)
		logger.debug('led 1 status: %d', x_gpio.read())
		return "turned off"
	else:
		x_gpio.write(1)
		logger.debug('led 1 status: %d', x_gpio.read())
		return "turned on"

@app.route("/api/v1.0/iot_sensors/photocells/1")
def get_photocell_value():
	try:
		logger.info('Reading photocell 1 intensity')
		print (x_aio.read())
		print ("%.5f" % x_aio.readFloat())
		logger.debug('the intensity of light is: %.5f', x_aio.readFloat())
        	return str(x_aio.read())
	except:
		print ("Are you sure you have an ADC?")
        	logger.debug('cannot read light intensity')
	        return "error"

if __name__ == "__main__":
	#allow to make changes in the source code and test
	app.run('0.0.0.0',debug=True)


# Get flask version
#import flask
#flask.__version__
#http://flask.pocoo.org/docs/0.10/config/