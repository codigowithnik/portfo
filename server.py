from flask import Flask, render_template, url_for, request, redirect
import csv 				# <--- DB
import time

app = Flask(__name__)
# print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


# contact us for - send btn with .csv file

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database:
		name = data["name"]
		email = data["email"]
		phone = data["phone"]
		message = data["message"]
		localtime = time.asctime(time.localtime(time.time()))

		csv_writer = csv.writer(database, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, email, phone, message, localtime])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')		#call html page
		except:
			return 'Did not send'	
	else:
		return 'something went wrong. try again.!!!'