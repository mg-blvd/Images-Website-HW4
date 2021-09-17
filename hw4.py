'''Authors: Misael Guijarro && Jose Alfaro
Date: 04/02/2019
Class: CST 205
Teacher: Wes Modes
Description: The home page displays three randoms images. Once clicked they take you to
a separate page with the picture and a description of it.'''
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from txt_read_write_functions import read_in_names, edit_text
from image_info import image_info
from PIL import Image
import random
import ast

app = Flask(__name__, static_url_path = "/static", static_folder = "static")
bootstrap = Bootstrap(app)

#this function is so that the picture does not get repeated on the home page
def assert_no_repeating(array1, array2):
    current = random.choice(image_info)
    while (current["title"] in array1 or current["title"] in array2):
        current = random.choice(image_info)
    return current

#this will route the function to be our home page
#this function allows the images to be displayed onto the page
# Function: inside of the for loop it is making sure that the images will not be repeated or reuse images from the last refresh
# by passing in the assert_no_repeating function and the read_in_names with the past_images variable.
# after completion it will use the edit_text function to pass in the names of the images that
# will be posted onto the home page to our text file. This will assure that different
#images are used after each refresh.
@app.route('/')
def main_page():
    past_images = read_in_names()
    current_images = []
    current_image_titles = []
    for i in range(3):
        current_images.append(assert_no_repeating(past_images, current_image_titles))
        current_image_titles.append(current_images[i]["title"])
    edit_text(current_image_titles)
    return render_template('home.html', image_list=current_images)

#this will route the function to be the pages where the individual image description is on after clicking on it
#this function will display the image resized onto another page with some description of it
# Function: it is passing in var so it could be later used in the home.html to make print out the random images with
# their respective 'locations' in the array in the previous function.
# The .literal_eval(var) makes a dictionary out of string output from html code.
# Images are being resized once clicked on and taken to new page.
# We get the dimensions od the image using PIL.
@app.route('/image_info/<var>')
def image_page(var):
    new_var = ast.literal_eval(var)
    current_image = Image.open("static/" + new_var["id"] + ".jpg")
    dimensions_w, dimensions_h = current_image.size
    return render_template('image_info.html', pic=new_var, w=dimensions_w, h=dimensions_h)

if __name__ == '__main__':
    print("Working!")
    app.run(debug=True)
