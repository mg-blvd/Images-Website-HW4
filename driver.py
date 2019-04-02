from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from image_info import image_info
import random

app = Flask(__name__, static_url_path = "/static", static_folder = "static")
bootstrap = Bootstrap(app)

def assert_no_repeating(array1):
    current = random.choice(image_info)
    while(current["title"] in array1):
        current = random.choice(image_info)
    return current

@app.route('/')
def main_page():
    past_images = []
    current_images = [0,0,0]
    for i in range(len(current_images)):
        current_images[i] = assert_no_repeating(past_images)
        past_images.append(current_images[i]["title"])
    return render_template('home.html', first=current_images[0], second=current_images[1], third=current_images[2])

@app.route('/image_info/')
def image_page():
    return render_template('image_info.html')

if __name__ == '__main__':
    app.run(debug=True)
