'''Authors: Misael Guijarro && Jose Alfaro
Date: 04/02/2019
Class: CST 205
Teacher: Wes Modes
Description: Holds thst function that will write to the text file that keeps track
             of the images we used in the last refresh.'''
# this function literally reads the names that are in former_images.txt
# it then 'splits' the strings after the new line
def read_in_names():
    f = open("former_images.txt", "r")
    read_names = f.read().split('\n')
    f.close()
    return read_names

#this function passes in name_list which is used to 'write' the name of the images
# this we are using in the current page. We will call these names back at the
#next refresh.
# Writes out the name of image followed by a new line.
def edit_text(name_list):
    f = open("former_images.txt", 'w')
    for i in range(3):
        f.write(name_list[i] + '\n')
    f.close()
