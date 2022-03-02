"""A simple flask web app"""
import jo as jo
from flask import Flask, render_template
from controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication
jo
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return get()
