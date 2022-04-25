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


class kartaca_events(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.String(250))
    date = db.Column(db.String(250))
    event_text = db.Column(db.Text)
    status = db.Column(db.Boolean)



def event_delete(event_id):
    try:
        update = kartaca_events.query.filter_by(id=event_id).first()
        # status=True: silindi
        update.status = True
        db.session.commit()
        msg = {'status': True,
               'message': "Etkinlik silindi!"}

        return msg
    except ValueError:
        msg = {'status': False,
               'error': '400'}
        return msg

def get_events(user_id):  # category id ye göre developer geliyor, mobilde çalışanlar gibi

    datum = db.session.query(kartaca_events).filter(
        (kartaca_events.users_id == user_id) & (
                kartaca_events.status != True))

    events = []
    for row in datum:
        event_data = {
            'id': str(row.id),
            'users_id': str(row.users_id),
            'date': str(row.date),

            'event_text': str(row.event_text)
        }
        events.append(event_data)
    return events


def event_record(users_datum):
    try:

        event_data = kartaca_events(users_id=str(users_datum.get('users_id')), date=str(users_datum.get('form_date')),
                                    status=False,
                                    event_text=str(users_datum.get('form_event_text')))

        db.session.add(event_data)
        db.session.commit()
        msg = {'status': True,
               'message': "Etkinlik kaydedildi"}

        return msg
    except ValueError:
        msg = {'status': False,
               'error': '400'}
        return msg


def get_event(id):
    event = db.session.query(kartaca_events).filter(
        (kartaca_events.id == str(id))).first()

    try:

        if event:

            event_data = {
                'id': event.id,
                'users_id': event.users_id,
                'date': event.date,
                'event_text': event.event_text,

            }

            return event_data

        else:
            msg = {'status': False,
                   'error': '204',
                   'message': 'Etkinlik bulunamadı'}
            return msg
    except ValueError:
        msg = {'status': False,
               'error': '400'}
        return msg


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
                   'message': "Kullanıcı kaydedildi",
                   'users': users_datum}

            return msg
        except ValueError:
            msg = {'status': False,
                   'error': '400'}
            return msg
