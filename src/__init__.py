import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

from flask import Flask

app = Flask(__name__)
# app.config.from_object('config')

import routes
