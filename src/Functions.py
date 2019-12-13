import os


def change_name_file(mushroom_name):
    i = 1
    path = f"Input/Mushroom-images/{mushroom_name}/"
    for filename in os.listdir(path): 
        print(filename)
        dst =f"{mushroom_name}" + str(i) + ".jpeg"
        src = path + filename 
        dst = path + dst      
        os.rename(src, dst) 
        i += 1