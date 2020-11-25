import platform, getpass, os, shutil
from ruamel import yaml
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

if "macOS" in platform.platform():
    username = getpass.getuser()
else:
    username = os.getlogin()

data = yaml.safe_load(open('config.yaml'))

rootpath = data['downloads'][0]

for item in data['paths']:
    for extension in data['paths'][item]:
        pathing = data['paths'][item][extension][0].replace("{osuser}", username)

        for file in os.listdir(rootpath):

        	#The following statements will always move automatically, use with care
            if file.endswith(extension):
                shutil.move(os.path.join(rootpath, file),os.path.join(pathing, file))

def call():
    res=mb.askquestion('Delete files', 'Do you want to delete left over files?')
    if res == 'yes' :
        root.destroy()
        for file in os.listdir(rootpath):
            for extension in data['delete']:
                for file in os.listdir(rootpath):
                    if file.endswith(extension):
                        os.remove(os.path.join(rootpath, file))
    else :
        root.destroy()

root = tk.Tk()

call()


