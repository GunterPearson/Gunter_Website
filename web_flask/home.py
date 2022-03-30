#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, session, request, jsonify
from flask import redirect, flash, url_for
from flask_simple_geoip import SimpleGeoIP
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"": {"origins": "*"}})

app.config["GEOIPIFY_API_KEY"] = "at_Odn3yiaerwjP1EPcvdotCZyrNitvL"

simple_geoip = SimpleGeoIP(app)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def home():
    """home route for html file"""
    geoip_data = simple_geoip.get_geoip_data()
    # print(type(geoip_data))
    location = geoip_data["location"]
    location["IP"] = request.remote_addr
    location["ip_address"] = geoip_data.get("ip")
    return location
    # session["user"] = request.remote_addr
    # return render_template("index.html")
