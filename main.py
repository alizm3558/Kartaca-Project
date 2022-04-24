import json
import os

from flask import Flask, render_template, make_response, jsonify, request, url_for
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from app.service import *
app = Flask(__name__)
api = Api(app)
app.secret_key="Kartaca"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWD']}@{os.environ['MYSQL_HOST']}/{os.environ['MYSQL_DATABASE']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# pass in the app into SQLAlchemy to create a db session.
db = SQLAlchemy(app)

#restful
api.add_resource(register, '/register')
api.add_resource(login, '/login')
api.add_resource(event_record, '/event-record')
api.add_resource(get_event_record, '/get-event')
api.add_resource(get_events,'/get-events')
api.add_resource(event_delete,'/event-delete')


if __name__ == "__main__":
    app.run(debug=True)
