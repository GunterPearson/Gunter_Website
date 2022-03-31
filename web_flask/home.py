#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, session, request, jsonify
from flask import redirect, flash, url_for
import os
from dotenv import load_dotenv
from web_flask.forms import EmailForm
from flask_simple_geoip import SimpleGeoIP
from flask_mail import Message, Mail
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"": {"origins": "*"}})


load_dotenv()
SECRET_KEY = os.urandom(32)
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
GEOIPIFY_API_KEY = os.getenv('GEOIPIFY_API_KEY')

app.config['SECRET_KEY'] = SECRET_KEY
app.config["GEOIPIFY_API_KEY"] = GEOIPIFY_API_KEY
# app.config["DEBUG"] = True
# app.config["TESTING"] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_SEND'] = None
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTATCHMENTS'] = False
mail = Mail(app)

simple_geoip = SimpleGeoIP(app)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def home():
    """home route for html file"""
    form = EmailForm()
    geoip_data = simple_geoip.get_geoip_data()
    # print(type(geoip_data))
    location = geoip_data["location"]
    location["ip_address"] = geoip_data.get("ip")
    session["user"] = location
    if request.method == "POST":
        msg = Message(form.subject.data, sender=form.email.data, recipients=['gunterjpearson@gmail.com'])
        msg.body = form.name.data + "\n" + form.message.data + "\n\n" + form.email.data
        mail.send(msg)
    # return location
    return render_template("index.html", form=form)

# @app.route('/mail', strict_slashes=False, methods=['GET', 'POST'])
# def mail():
#     """Email route for sending me emails"""
#     form = ContactForm()
#     if request.method == "POST":
        