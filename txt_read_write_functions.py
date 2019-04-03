def read_in_names():
    f = open("former_images.txt", "r")
    read_names = f.read().split('\n')
    f.close()
    return read_names

def edit_text(name_list):
    f = open("former_images.txt", 'w')
    for i in range(3):
        f.write(name_list[i] + '\n')
    f.close()
