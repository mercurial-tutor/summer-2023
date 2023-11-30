import os
import random
from flask import Flask, render_template
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

IMG_DIR = './static'

@app.route('/')
def hello_world():
    return 'i like to eat chicken wings!'

@app.route("/start")
def start():
    return render_template('start.html')

@app.route("/page1")
def page_1():
    return render_template('page1.html')

@app.route("/page2")
def page_2():
    return render_template('page2.html')

@app.route("/page3")
def page_3():
    return render_template('page3.html')

@app.route("/page4")
def page_4():
    return render_template('page4.html')

@app.route("/page5a")
def page_5a():
    return render_template('page5a.html')

@app.route("/page5b")
def page_5b():
    return render_template('page5b.html')

@app.route("/page6")
def page_6():
    return render_template('page6.html')

@app.route("/page7")
def page_7():
    return render_template('page7.html')

@app.route("/page8")
def page_8():
    return render_template('page8.html')

@app.route("/page9")
def page_9():
    return render_template('page9.html')

@app.route("/page10")
def page_10():
    return render_template('page10.html')

@app.route("/page11")
def page_11():
    return render_template('page11.html')

@app.route("/page12")
def page_12():
    return render_template('page12.html')

@app.route("/page13")
def page_13():
    return render_template('page13.html')

@app.route("/page14")
def page_14():
    return render_template('page14.html')

@app.route("/page15")
def page_15():
    return render_template('page15.html')

@app.route("/page16")
def page_16():
    return render_template('page16.html')

@app.route("/page17")
def page_17():
    return render_template('page17.html')

@app.route("/page18")
def page_18():
    return render_template('page18.html')

@app.route("/page19")
def page_19():
    return render_template('page19.html')

@app.route("/page20")
def page_20():
    return render_template('page20.html')

@app.route("/page21")
def page_21():
    return render_template('page21.html')

@app.route("/page22")
def page_22():
    return render_template('page22.html')

@app.route("/page23")
def page_23():
    return render_template('page23.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8081)
