from flask import Flask, render_template
from image_info import image_info
import random

app = Flask(__name__, static_url_path = "/static", static_folder = "static")

@app.route('/')
def main_page():
    randoms = []
    img1 = random.choice(image_info)
    img2 = random.choice(image_info)
    img3 = random.choice(image_info)
    return render_template('home.html', first=img1, second=img2, third=img3)

if __name__ == '__main__':
    app.run(debug=True)
