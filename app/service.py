from flask import Flask, render_template, make_response, jsonify, request, url_for
from flask_restful import Resource, Api
from json import *
from passlib.hash import sha256_crypt


class register(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        users_datum = {'form_name': request.form['name'],
                       'form_surname': request.form['surname'],

                       'form_mail': request.form['email'],
                       'form_password': str(sha256_crypt.encrypt(request.form['password'])),
                       }

        from Helpers.databasehelpers import register_record
        return jsonify(register_record(users_datum))

    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("register-get")



class event_delete(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        event_id=request.form['event_id']
        from Helpers.databasehelpers import event_delete
        return jsonify(event_delete(event_id))

    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("event-get")

class event_record(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        users_datum = {'users_id': request.form['users_id'],
                       'form_date': request.form['date'],
                       'form_event_text': request.form['event_text'],

                       }

        from Helpers.databasehelpers import event_record
        return jsonify(event_record(users_datum))

    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("event-get")


class get_event_record(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        event_id = request.form['event_id']

        from Helpers.databasehelpers import get_event
        return jsonify(get_event(event_id))

    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("event-get")


class get_events(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        user_id = request.form['user_id']

        from Helpers.databasehelpers import get_events
        return jsonify(get_events(user_id))

    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("event-get")


class login(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        users_datum = {
            'form_mail': request.form['email'],
            'form_password': request.form['password']
        }

        from Helpers.databasehelpers import record_control
        return jsonify(record_control(users_datum))

    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("login-get")
