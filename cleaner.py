import platform
import getpass
import os
import shutil
import tkinter as tk
from tkinter import messagebox as mb

import yaml

if "macOS" in platform.platform():
    username = getpass.getuser()
else:
    username = os.getlogin()

a_yaml_file = open("config.yaml")
data = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

rootpath = data['downloads'][0].replace('{osuser}', username)

for item in data['paths']:
    for extension in data['paths'][item]:
        pathing = data['paths'][item][extension][0].replace('{osuser}', username)

        for file in os.listdir(rootpath):

            if file.endswith(extension):
                shutil.move(os.path.join(rootpath, file), os.path.join(pathing, file))


def call():
    res = mb.askquestion('Delete files', 'Do you want to delete the leftover files?')

    if res == 'yes':
        root.destroy()
        for extension in data['delete']:
            for file in os.listdir(rootpath):
                if file.endswith(extension):
                    os.remove(os.path.join(rootpath, file))

    else:
        root.destroy()


root = tk.Tk()

call()
