# import random module from Python standard library

# define a dictionary with image urls and number of flucks

# set the served img variable to be a random element from imgs
# hints: 
#	to put dict keys in a list: list(dict.keys())
#	to choose a random item from a list: random.choice(lst)

# keep asking user if they want to fluck the image until
# they say either 'yes' or 'no'

# if they say 'yes', output a message and increment the flucks
# if they say 'no', serve another image?

# repeat process for another image...
# hint: group blocks of task-specific code into functions?

import random

imgs = {"img_1":1,"img_2":2,"img_3":3,"img_4":4}
img = imgs.keys()
random.choice(imgs)
served_img = imgs[random.randrange(0,len(imgs)-1)]

print(served_img)

input = raw_input("Would you like to fluck it?!")

if input == "yes":
    print("YOU FLUCKED IT")
    
elif input == "no":
    print("WHAT ARE YOU???..")
        
