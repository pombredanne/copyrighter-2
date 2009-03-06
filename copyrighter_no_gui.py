#!/usr/local/bin/python


import os
import time
import sys
from iptcinfo import IPTCInfo
import string

time= time.gmtime()
year = str(time[0])
copyright_name = ""


def get_choice(x):
    """Get choice from user and process file or directory"""
    if x == 'i':
        print "You chose to process 1 image"
        print "Please enter the path of an image: "
        i_path = raw_input()
        choose_image(i_path)
    elif x == 'd':
        print "You chose to process a directory"
        print "Please enter the path to a directory: "
        d_path = raw_input()
        # ------
        # insert function
        # ------
    elif x == 'q':
        print "Thanks for playing!"
        sys.exit()
    else:
        print "Please choose either (i) or (d)"
        y = raw_input()
        get_choice(y)


class imageFile(object):
    """get name of file out of it's path and provide function \
        to save with new copyright info"""
    def __init__(self, path, cr_text):
        self.path = path
        self.split_image_path = path.split('/')
        self.image_name= self.split_image_path[-1]
        self.split_image_name = self.image_name.split('.')
        self.orig_name = self.split_image_name[0]
        self.folder = (string.join(self.split_image_path[0:-1], "/") + "/")
        self.info= IPTCInfo(str(path), force= True)
        self.copyright = self.info.data['copyright notice']
        self.info.data['copyright notice']= (year + " " + cr_text)

    def save_new(self):
        file_copy = (str(self.orig_name) + '_cr' + '.' + \
            str(self.split_image_name[-1]))
        if os.path.exists(self.folder + '/' + file_copy):
            print "Sorry! The file " + file_copy + " already exists!"
            return
        else:
            try:
                #print self.folder + file_copy
                #print self.path
                self.info.saveAs(self.folder + file_copy)
            except:
                print 'error'
    

def choose_image(image_path):
    if image_path == "":
    	return
    my_image = imageFile(image_path, copyright_name)
    my_image.save_new()


def choose_folder(image_dir):
    image_list = os.walk(image_dir, True)
    for x in image_list:
        for y in x[2]:
            w = imageFile(x[0] + '/' + y, copyright_name)
            w.save_new()


print "Welcome to CoPyrighter. Press (q) at a prompt to quit."
 
copyright_name = raw_input("Please enter the name \
to use for the copyright: ")

if copyright_name == "q":
    print "Thanks for playing!"
    sys.exit()


choice_file = raw_input("Would you like to copyright an\
(i)mage or a (d)irectory of images?")

get_choice(choice_file)