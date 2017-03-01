from flask import Flask,render_template,redirect,request
import MySQLdb 

from flask_mail import Mail, Message


app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shreyanshss7@gmail.com'
app.config['MAIL_PASSWORD'] = 'shreyanshthess7'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result')
def result():
	return render_template('results.html')	

@app.route('/form_submission' ,methods=['GET','POST'])
def contact_form():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		number = request.form['number']
		message = request.form['message']

		msg = Message('%s' % (name) , sender='shreyanshss7@gmail.com' , recipients=['%s' % (email)])
		msg.body = ( '%s , %s ' % (message, number))
		mail.send(msg)
		return render_template('index.html')



if __name__ == '__main__':
		app.run(debug=True)	