from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)

COURSE_SEARCH_URL = 'http://course-api.herokuapp.com/'

@app.route('/')
def index():
    return render_template('browse.html')

@hackathon.route('/results', methods=['POST'])
def results():
	search_term = request.form['term']
	department = request.form['department']

	api_url =  "%s/%s" % (COURSE_SEARCH_URL, department)
	response = requests.get(api_url)
	json_response = json.loads(response.text)

	return render_template('results.html',
							search_term=search_term,
							location=department,
							courses=json_response)

if __name__ == '__main__':
    app.run(debug=True)