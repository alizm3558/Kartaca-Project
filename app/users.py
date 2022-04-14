from flask import Flask, render_template, make_response, jsonify, request, url_for
from flask_restful import Resource, Api
from json import*
class register(Resource):
    def post(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("register-post")
    def get(self):  # post ile veri alıyoruz, çalışıyor
        return jsonify("register-get")
