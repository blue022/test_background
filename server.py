from flask import Flask, render_template, request,url_for, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("./index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
	with open ("./static/database.txt", "a") as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]

		file = database.write(f"\n {email} \n {subject} \n {message}")


def write_to_csv(data):
	with open ("./static/database.csv", mode="a", newline="",) as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]

		csv_writter = csv.writer(database2, delimiter=",",quotechar="\"",  quoting=csv.QUOTE_MINIMAL)
		csv_writter.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			data= request.form.to_dict()
			write_to_csv(data)
			return redirect("/thank_you.html")
		except:
			return "did not save to database"
	else:
		return "something went wrong, please try again"
    
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return "form submitet hooray!!"



# @app.route('/index.html')
# def home2():
#     return render_template("./index.html")

# @app.route('/works.html')
# def works():
#     return render_template("./works.html")


# # @app.route('/works.html')
# # def works():
# #     return render_template("./works.html")


# @app.route('/about.html')
# def about():
#     return render_template("./about.html")

# @app.route('/contact.html')
# def contact():
#     return render_template("./contact.html")

# @app.route('/components.html')
# def components():
#     return render_template("./components.html")






