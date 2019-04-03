from flask import Flask, render_template
from flask_bootstrap import Bootstrap
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
    f = open("former_images.txt", "r")
    past_images = f.read().split('\n')
    f.close()
    current_images = []
    current_image_titles = []
    print(past_images)
    for i in range(3):
        current_images.append(assert_no_repeating(past_images, current_image_titles))
        current_image_titles.append(current_images[i]["title"])
        print(current_images)
        print(current_image_titles)
    f = open("former_images.txt", 'w')
    for i in range(3):
        f.write(current_image_titles[i] + '\n')
    f.close()
    return render_template('home.html', first=current_images[0], second=current_images[1], third=current_images[2])

@app.route('/image_info/<var>')
def image_page(var):
    new_var = ast.literal_eval(var)
    current_image = Image.open("static/" + new_var["id"] + ".jpg")
    dimensions_w, dimensions_h = current_image.size
    return render_template('image_info.html', pic=new_var, w=dimensions_w, h=dimensions_h)

if __name__ == '__main__':
    app.run(debug=True)
