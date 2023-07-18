import os
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@app.route('/riddle', methods = ['GET', 'POST'])
def riddle():
    if request.method == 'GET':
        return render_template('riddle.html')
    if request.method == 'POST':
        form_data = request.form
        if form_data['answer'] != 'nothing':
            return redirect('/lose', code = 307)
        return redirect('/win', code = 307)

@app.route('/win', methods = ['POST'])
def win():
    if request.method == 'POST':
        return 'You win!'

@app.route('/lose', methods = ['POST'])
def lose():
    if request.method == 'POST':
        return 'You lose!'

if __name__ == '__main__':
    app.run(host='localhost', port=8081)
