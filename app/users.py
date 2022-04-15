from flask import Flask, render_template, make_response, jsonify, request, url_for
from flask_restful import Resource, Api
from json import*
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
