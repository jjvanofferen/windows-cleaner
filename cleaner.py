import platform
import getpass
import os
import shutil
import PySimpleGUI as sg
import yaml


if "macOS" in platform.platform():
    username = getpass.getuser()
else:
    username = os.getlogin()

a_yaml_file = open("config.yaml")
data = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

rootpath = data['downloads'][0].replace('{osuser}', username)


file_list_column = [
    [
        sg.Text("Select folder to clean"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Review files on the left before running the cleaner:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("Run cleaner", enable_events=True, key="cleanup")]
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("PC cleaner", layout)


# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "cleanup":

        for item in data['paths']:
            for extension in data['paths'][item]:
                pathing = data['paths'][item][extension][0].replace('{osuser}', username)

                for file in os.listdir(values["-FOLDER-"]):

                    if file.endswith(extension):
                        shutil.move(os.path.join(values["-FOLDER-"], file), os.path.join(pathing, file))

        print("Finished cleaning folder")

        folder = values["-FOLDER-"]
        file_list = os.listdir()
        extensions = list()

        for item in data['paths']:
            for extension in data['paths'][item]:
                extensions.append(extension)

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(tuple(extensions))
        ]
        window["-FILE LIST-"].update(fnames)

    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)

        except:
            file_list = []

        extensions = list()

        for item in data['paths']:
            for extension in data['paths'][item]:
                extensions.append(extension)

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(tuple(extensions))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()
