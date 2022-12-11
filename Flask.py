def base_page():
	return render_template(
		'index.html',  # Template file path, starting from the templates folder. 
	)

@app.route('/<name>/<email>')
def index(name, email):
	file_object = open(r"email.json", "a")
	file


@app.route('/read')
def readFile():
	file_object = open("email.json")
	return eval(file_object.read())
