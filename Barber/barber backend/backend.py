from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user # type: ignore
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barber.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for Flask-Login

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Model for Appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

# Model for Services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Model for Pricing
class Pricing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Model for Users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_appointment():
    name = request.form['name']
    phone = request.form['phone']
    service = request.form['service']
    date = datetime.strptime(request.form['date'], '%Y-%m-%dT%H:%M')

    new_appointment = Appointment(name=name, phone=phone, service=service, date=date)
    db.session.add(new_appointment)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/services')
def services():
    all_services = Service.query.all()
    return render_template('services.html', services=all_services)

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{
        'id': appt.id,
        'name': appt.name,
        'phone': appt.phone,
        'service': appt.service,
        'date': appt.date.isoformat()
    } for appt in appointments])

if __name__ == '__main__':
    app.run(debug=True)






from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barber.db'
db = SQLAlchemy(app)

# Model for Appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

@app.route('/book', methods=['POST'])
def book_appointment():
    name = request.form['name']
    phone = request.form['phone']
    service = request.form['service']
    date = datetime.strptime(request.form['date'], '%Y-%m-%dT%H:%M')

    new_appointment = Appointment(name=name, phone=phone, service=service, date=date)
    db.session.add(new_appointment)
    db.session.commit()

    return redirect(url_for('index'))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Pricing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)


@app.route('/services')
def services():
    all_services = Service.query.all()
    return render_template('services.html', services=all_services)


from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user # type: ignore

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from flask import jsonify

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{
        'id': appt.id,
        'name': appt.name,
        'phone': appt.phone,
        'service': appt.service,
        'date': appt.date.isoformat()
    } for appt in appointments])
