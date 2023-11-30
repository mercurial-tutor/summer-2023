import os
import random
from flask import Flask, render_template, request, redirect
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

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

@app.route('/start')
def start_of_story():
    return render_template('start_of_story.html')

@app.route('/path1', methods = ['POST'])
def path_1():
    if request.method == 'POST':
        return render_template('path_1.html')
    
@app.route('/path2', methods = ['POST'])
def path_2():
    if request.method == 'POST':
        return render_template('path_2.html')

@app.route('/path22', methods = ['POST'])
def path_22():
    if request.method == 'POST':
        return render_template('path_22.html')

@app.route('/path221', methods = ['POST'])
def path_221():
    if request.method == 'POST':
        return render_template('path_221.html')
    
@app.route('/path222', methods = ['POST'])
def path_222():
    if request.method == 'POST':
        return render_template('path_222.html')

@app.route('/path11', methods = ['POST'])
def path_11():
    if request.method == 'POST':
        return render_template('path_11.html')

@app.route('/path112', methods = ['POST'])
def path_112():
    if request.method == 'POST':
        return render_template('path_112.html')

@app.route('/path111', methods = ['POST'])
def path_111():
    if request.method == 'POST':
        return render_template('path_111.html')

@app.route('/path12', methods = ['POST'])
def path_12():
    if request.method == 'POST':
        return render_template('path_12.html')

@app.route('/pathc12', methods = ['POST'])
def path_c12():
    if request.method == 'POST':
        return render_template('path_c12.html')

@app.route('/pathdeath', methods = ['POST'])
def path_death():
    if request.method == 'POST':
        return render_template('path_death.html')

@app.route('/pathcave', methods = ['POST'])
def path_cave():
    if request.method == 'POST':
        return render_template('path_cave.html')

@app.route('/path121', methods = ['POST'])
def path_121():
    if request.method == 'POST':
        return render_template('path_121.html')

@app.route('/path1211', methods = ['POST'])
def path_1211():
    if request.method == 'POST':
        return render_template('path_1211.html')

@app.route('/path1212', methods = ['POST'])
def path_1212():
    if request.method == 'POST':
        return render_template('path_1212.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8081)

