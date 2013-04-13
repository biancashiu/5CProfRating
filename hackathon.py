from flask import (
	Flask,
	render_template,
	session,
	redirect,
	request,
	url_for
)
import urllib
import json
import requests

hackathon = Flask(__name__)

COURSE_SEARCH_URL = 'http://course-api.herokuapp.com/'

@hackathon.route('/')
def index():
	return render_template('index.html')

@hackathon.route('/browse')
def browse():
	return render_template('browse.html')

@hackathon.route('/write')
def write():
	return render_template('enterReviews.html')

@hackathon.route('/results', methods=['POST'])
def results():
	department = request.form['department']

	api_url =  "%s/%s" % (COURSE_SEARCH_URL, department)
	response = requests.get(api_url)
	print response
	json_response = json.loads(response.text)

	return render_template('results.html',
							location=department,
							courses=json_response)

@hackathon.route('/save',methods=['POST'])
def save():
	return str(request.form)

if __name__ == '__main__':
	hackathon.run(debug=True)