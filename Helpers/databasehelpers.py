from flask import flash, redirect, url_for
from main import *
from passlib.handlers.sha2_crypt import sha256_crypt

class kartaca_users(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    surname = db.Column(db.String(250))
    mail = db.Column(db.Text)
    password = db.Column(db.Text)


def record_control(users_datum):

    users = db.session.query(kartaca_users).filter(
        (kartaca_users.mail == str(users_datum.get('form_mail')))).first()

    try:

        if users:

            users_data = {
                    'id': users.id,
                    'name': users.name,
                    'surname': users.surname,
                    'mail': users.mail,
                    'password': users.password

                }

            if sha256_crypt.verify(str(users_datum.get('form_password')), str(users_data.get('password'))):
                msg = {'status': True,
                           'message': "Kullanıcı bulundu",
                           'users': users_data}
            else:
                msg = {'status': False,
                           'message': "Yanlış şifre girişi"}
            return msg

        else:
            msg = {'status': False,
                   'error': '204',
                   'message': 'Kullanıcı bulunamadı'}
            return msg



    except ValueError:
        msg = {'status': False,
               'error': '400'}
        return msg


def register_record(users_datum):
    users = db.session.query(kartaca_users).filter(kartaca_users.mail == users_datum.get('form_mail')).count()

    if users > 0:

        msg = {'status': False,
               'error': '501',
               'message': "Böyle bir kullanıcı mevcuttur!"}
        return msg
    else:
        try:

            users_data = kartaca_users(name=users_datum.get('form_name'), surname=users_datum.get('form_surname'),
                                       mail=users_datum.get('form_mail'),
                                       password=users_datum.get('form_password'))

            db.session.add(users_data)
            db.session.commit()
            msg = {'status': True,
                   'message': "Kullanıcı Kaydedildi",
                   'users': users_datum}

            return msg
        except ValueError:
            msg = {'status': False,
                   'error': '400'}
            return msg
