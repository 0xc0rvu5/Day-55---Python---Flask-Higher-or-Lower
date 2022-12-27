import random
from flask import Flask
from flask import render_template


#initialize global variables
#create flask APP global variable and direct it to the templates/static folders
APP = Flask(__name__, template_folder='templates', static_folder='static')
RANDOM_NUMBER = random.randint(0,9)


#create main page based on the index.html file in templates
@APP.route('/')
def hello_world():
    return render_template('index.html')


#endpoint that prints 'Hey {{ name }} how are you doing? You are {{ number }} years old!'
#example endpoint: /username/0xc0rvu5/100
@APP.route('/username/<name>/<int:number>')
def greet(name,number):
    return render_template('username.html', name=name, number=number)


#guess a number, if too high send to 'too_high.html', if too low send to 'too_low.html' else send to 'correct.html'
@APP.route('/<int:num>')
def guess_the_num(num):
    if num > RANDOM_NUMBER:
        return render_template('too_high.html', num=num)
    if num < RANDOM_NUMBER:
        return render_template('too_low.html', num=num)
    else:
        return render_template('correct.html', num=num)


#turn on debugging to allow for `some` dynamic updates
if __name__ == '__main__':
    APP.run(debug=True)


#to start run
#export FLASK_APP=name_of_flask_file
#flask run