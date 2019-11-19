import os
import sys
import  flask

from os import environ
from flask import flask

app = flask(__name__)
app.run(environ.get('PORT'))