from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_txt(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        txt = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Did not save to databse'
    else:
        return 'Something went wrong. Try again!'


# @app.route("/index.html")
# def index():
#     return render_template("index.html")


# @app.route("/components.html")
# def components():
#     return render_template("components.html")


# @app.route("/about.html")
# def about_me():
#     return render_template("about.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


# @app.route("/works.html")
# def works():
#     return render_template("works.html")


# @app.route("/work.html")
# def work():
#     return render_template("work.html")


# @app.route("/work2.html")
# def work002():
#     return render_template("work002.html")


# @app.route("/work3.html")
# def work003():
#     return render_template("work003.html")


# @app.route("/thank_you.html")
# def thankyou_note():
#     return render_template("thank_you.html")
