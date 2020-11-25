import os, shutil, ctypes, tkinter
from subprocess import check_output


rootpath = "C:/Users/" + os.getlogin()+ "/Downloads"

#Paths
imagespath = "C:/Users/" + os.getlogin()+ "/Pictures"
docspath = "C:/Users/" + os.getlogin()+ "/Documents"
destinationpath = "D:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/csgo/demo_pvpro"

#demo array extensions
#listExtensions = [".ext", ".ext2"]
# if file.endswith(tuple(listExtensions)):

imageExtensions = [".jpg", ".png"]

#this are the extensions to ask to delete, it will not auto delete them!
deleteExtensions = [".exe", ".zip"]

def ask(text, title):
	return ctypes.windll.user32.MessageBoxW(0, text, title, 1)
	pass

checkfiles = 0

if ask("Do you want to run the file checker?", "Filemanager") == 1:
	checkfiles = 1

for file in os.listdir(rootpath):

	#The following statements will always move automatically, use with care
    if file.endswith(".dem.gz"):
        shutil.move(os.path.join(rootpath, file),os.path.join(destinationpath, file))

    if file.endswith(tuple(imageExtensions)):
        shutil.move(os.path.join(rootpath, file),os.path.join(imagespath, file))

    if file.endswith(".doc"):
        shutil.move(os.path.join(rootpath, file),os.path.join(docspath, file))

    if checkfiles == 1:
	    if file.endswith(tuple(deleteExtensions)):
	    	if ask(file, "Remove file?") == 1:
	    		os.remove(os.path.join(rootpath, file))