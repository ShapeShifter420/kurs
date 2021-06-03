import json
import os

from flask import Flask, session, render_template, send_file, request, send_from_directory, redirect, url_for

app = Flask(__name__)
app.debug = False
app.secret_key = b'\xcbt\x0f\xbfAQd\x16\x91\xa4\x1f\x8b\xa2j\xc8k\x19^\xf19\xf4Bq\xe1'

load_keys = {}


def init_keys():
    with (open("../keys.json")) as keys:
        global load_keys
        load_keys = json.load(keys)

@app.route('/')
def hello():
    return render_template('/views/index.html')

def new_color_space():


def start(self):
    app.run(host='0.0.0.0')


def start80(self):
    app.run(host='0.0.0.0', port=80)


def create_new_json(**kwargs):
    return json.dumps(kwargs)


if __name__ == '__main__':
    init_keys()

