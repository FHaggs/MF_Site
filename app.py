#!/usr/bin/python3
import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

from form_contact import ContactForm, csrf

mail = Mail()

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mfconsultit.contato@gmail.com'
app.config['MAIL_PASSWORD'] = 'M&F_site'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

@app.route('/')
def index():
    return render_template('views/home/index.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        return redirect('/success')    

    return render_template('views/contacts/contact.html', form=form)

@app.route('/success')
def success():
    return render_template('views/home/successe.html')

@app.route('/servicos')
def servicos():
    return render_template('views/home/servicos.html')

@app.route('/consultor')
def consultor():
    return render_template('views/home/consultor.html')

@app.route('/projetos-executados')
def projetos():
    return render_template('views/home/projetos-executados.html')


def send_message(message):
    print(message.get('name'))

    msg = Message((message.get('subject'), message.get('email')), sender = message.get('email'),
            recipients = ['mfconsultit.contato@gmail.com'],
            body= message.get('message')
    )  
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug = False)
