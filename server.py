from flask import Flask, render_template, send_file, url_for, request, redirect
import csv

import io
app = Flask(__name__)

print(__name__)



# @app.route("/index.html")
# def hello_world():
#     return render_template("index.html")

@app.route("/")
def index():
    return render_template("index.html")




# @app.route("/about.html")
# def about():
#     return render_template("./about.html")


# @app.route("/works.html")
# def works():
#     return render_template("works.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name)


# @app.route("/favicon.ico")
# def logo():
#     try:
#         with open("images/logo.png", "rb") as img:
#             return send_file(io.BytesIO(img.read()), mimetype= 'image/x-icon")
#     except Exception as e:
#         return "Did not work", 404


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>Dogs 2020>"


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to DB"
        
    
    else:
        return "There is an error"


def write_to_db(data):
    with open("database.txt",mode = "a") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"] 
        file = db.write(f"\nThe email is {email}\n the subject is {subject}\n the message is {message}")

        

def write_to_csv(data):
    with open("db.csv",mode = "a", newline='') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"] 
        csv_writer = csv.writer(db2,delimiter= ',', lineterminator='\n', quotechar = '|')
        csv_writer.writerow([email,subject,message])