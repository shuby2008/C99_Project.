import os
import shutil

source = input("enter source folder name:- ")
destination = input('enter destination folder name:- ')

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)