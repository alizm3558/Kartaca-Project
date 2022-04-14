from cmath import log
from flask import Flask, Blueprint, redirect, render_template, url_for, request, flash, session


#from passlib.handlers.sha2_crypt import sha256_crypt

index = Blueprint('index', __name__, template_folder='templates')




@index.route('/', methods=["GET", "POST"])
def login():
    return "index"





