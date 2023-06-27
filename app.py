import os
import random
from flask import Flask, render_template, send_file

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/image')
def serve_image():
    return render_template('image.html')

@app.route('/random')
def serve_random_image():
    img_list = os.listdir(IMG_DIR)
    img_path = os.path.join(IMG_DIR, random.choice(img_list))
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='localhost', port=8081)
