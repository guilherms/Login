from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  password = db.Column(db.String(30))
  created_at = db.Column(db.String(50))
  updated_at = db.Column(db.String(50))

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(50))
  image = db.Column(db.String(100))
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))

contatos = [
  {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16) 99922-1122' },
  {'name': 'Maria Souza', 'email': 'maria1@gmail.com', 'phone': '(16) 99922-3333' },

]

@app.route('/')
def index():
  new_contacts = Contacts.query.all()
  return render_template('index.html', contatos=contatos, new_contacts=new_contacts)
  new_contacts.append(contatos)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  new_contacts = Contacts(
    name=name,
    email=email,
    phone=phone,
)

  db.session.add(new_contacts)
  db.session.commit()
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  new_contacts = Contacts.query.filter_by(id=id).first()
  db.session.delete(new_contacts)
  db.session.commit()
  return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
  new_contacts = Contacts.query.filter_by(id=id).first()
  new_contacts.complete = True
  db.session.commit()
  return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  new_contacts = Contacts.query.filter_by(id=id).first()
  new_contacts.name = name
  new_contacts.email = email
  new_contacts.phone = phone
  db.session.commit()
  return redirect('/')


if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0')