from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Miguel'}
	posts = [
		{
			'author':{'nickname':'John'},
			'body':'Portland what what'
		},
		{
			'author':{'nickname':'Susan'},
			'body':'SF is less awesome'
		}
	]
	return render_template('index.html',
				title='Home',
				user=user,
				posts=posts)
