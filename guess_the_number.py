from flask import Flask, render_template, request
from random import choice
from replit import db

app = Flask(__name__)

if 'guesses' not in db:
  db['guesses'] = []

if 'computer_number' not in db:
  db['computer_number'] = choice(range(1, 101))


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    guess = request.form['number_guess']
    guessed_number = int(guess)
    db['guesses'].append(check_number_show_message(
        guessed_number, db['computer_number']))

  return render_template('index.html', guesses=reversed(db['guesses']))


def check_number_show_message(guessed_number, computer_number):
  if guessed_number < computer_number:
    return f'{guessed_number} is too low'

  elif guessed_number > computer_number:
    return f'{guessed_number} is too high'

  else:

    return f'{guessed_number} is correct'


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    db['guesses'] = []
    db['computer_number'] = choice(range(1, 101))
    return render_template('index.html', guesses=reversed(db['guesses']))


app.run(host='0.0.0.0', port=81)
