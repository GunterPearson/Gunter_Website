#!/usr/bin/python3
""" run app"""
from web_flask.home import app


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', debug=True)
