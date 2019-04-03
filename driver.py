from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from txt_read_write_functions import read_in_names, edit_text
from image_info import image_info
from PIL import Image
import random
import ast

app = Flask(__name__, static_url_path = "/static", static_folder = "static")
bootstrap = Bootstrap(app)

def assert_no_repeating(array1, array2):
    current = random.choice(image_info)
    while (current["title"] in array1 or current["title"] in array2):
        current = random.choice(image_info)
    return current

@app.route('/')
def main_page():
    past_images = read_in_names()
    current_images = []
    current_image_titles = []
    for i in range(3):
        current_images.append(assert_no_repeating(past_images, current_image_titles))
        current_image_titles.append(current_images[i]["title"])
    edit_text(current_image_titles)
    return render_template('home.html', first=current_images[0], second=current_images[1], third=current_images[2])

@app.route('/image_info/<var>')
def image_page(var):
    new_var = ast.literal_eval(var)
    current_image = Image.open("static/" + new_var["id"] + ".jpg")
    dimensions_w, dimensions_h = current_image.size
    return render_template('image_info.html', pic=new_var, w=dimensions_w, h=dimensions_h)

if __name__ == '__main__':
    app.run(debug=True)
