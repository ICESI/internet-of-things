from flask import Flask
import logging
from logging_load import setup_logging

app = Flask(__name__)

'''
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#creating a file handler
handler = logging.FileHandler('pillbox.log')
handler.setLevel(logging.DEBUG)
#creating a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
#adding the handler to the logger
logger.addHandler(handler)
'''

setup_logging()
logger = logging.getLogger(__name__)

button_box_open = True

@app.route("/api/v1.0")
@app.route("/api")
@app.route("/")
def api_version():
	logger.info('Showing api version')
	return "pillbox api version 1.0"

@app.route("/api/v1.0/pillbox/status")
def get_status():
	global button_box_open
	logger.info('Showing box status')
	if button_box_open == True:
		button_box_open = False
		logger.debug('button box status: %s', button_box_open)
		return "pillbox is open"
	else:
		button_box_open = True    
		logger.debug('button box status: %s', button_box_open)
		return "pillbox is close"
	return "done"

@app.route("/api/v1.0/pillbox/boxes/<int:box_id>")
def get_box(box_id):
	logger.info('Selecting a box')
	box_id = str(box_id)
	return 'You selected box ' + box_id

@app.route("/api/v1.0/pillbox/pills/<pill_name>")
def get_pill(pill_name):
	logger.info('Selecting a pill')
	return 'You selected pill ' + pill_name

if __name__ == "__main__":
	
	#allow to make changes in the source code and test
	app.run('0.0.0.0',debug=True)


# Review this
#import flask
#flask.__version__
#http://flask.pocoo.org/docs/0.10/config/