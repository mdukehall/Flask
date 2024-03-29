import os
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
#import Flask micro web framework
#import Jinja HTML Rendering Template
#import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return '<h1>Heyas world</h1>'

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

## ERROR HANDLING
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)

