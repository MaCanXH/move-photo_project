import os
import platform
import re
import datetime
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Photo Mover")
root.geometry('640x240')

EXTS = ('jpg', 'png', 'jpeg', 'mov', 'mp4')
DATE_PATTERN = r'.*(20\d\d)-?([01]\d)-?([0123]\d).*'

def getFolder(year, monthNumber):
  if (monthNumber == "01"):
    monthFolder = "01 January"
  elif (monthNumber == "02"):
    monthFolder = "02 February"
  elif (monthNumber == "03"):
    monthFolder = "03 March"
  elif (monthNumber == "04"):
    monthFolder = "04 April"
  elif (monthNumber == "05"):
    monthFolder = "05 May"
  elif (monthNumber == "06"):
    monthFolder = "06 June"
  elif (monthNumber == "07"):
    monthFolder = "07 July"
  elif (monthNumber == "08"):
    monthFolder = "08 August"
  elif (monthNumber == "09"):
    monthFolder = "09 September"
  elif (monthNumber == "10"):
    monthFolder = "10 October"
  elif (monthNumber == "11"):
    monthFolder = "11 November"
  elif (monthNumber == "12"):
    monthFolder = "12 December"
  
  return year + "\\" + monthFolder

def creation_date(path_to_file):
    if platform.system() == 'Windows':
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_date(folder, file):
    dateCreated = creation_date(folder + '\\' + file)
    matchObj = re.match(DATE_PATTERN, dateCreated)
    if(matchObj):
        year = matchObj.group(1)
        month = matchObj.group(2)
    else:
        year = "0"
        month = "0"
        print("unable to get file date")
    return {"year": year, "month": month}


def move_photo(source, target):
    try:
        files = os.listdir(source)
        duplicate = []

        for file in files:
            if(file.lower().endswith(EXTS)):
                date = get_date(source, file)
                year = date["year"]
                month = date["month"]

                if(year == "0" or month == "0"):
                    continue
                
                folder = getFolder(year, month)
                
                targetFolder = target + "\\" + folder
                if(not os.path.exists(targetFolder)):
                    os.makedirs(targetFolder)
                
                sourceFile = source + "\\" + file
                targetFile = targetFolder + "\\" + file
                if(not os.path.exists(targetFile)):
                    shutil.move(sourceFile, targetFolder)

                else:
                # If it already exists and is exactly the same size then delete it.
                    if os.stat(sourceFile).st_size == os.stat(targetFile).st_size:
                        print("Duplicate file, deleting: " + file)
                        os.remove(sourceFile)
                        duplicate.append(file)
                    else:
                        # Might want to rename and move here
                        print("Duplicate file, different size: " + file)
        if (len(duplicate) == 0):
            messagebox.showinfo('Success', 'Photos successfully sorted')
        elif (len(duplicate) > 0):
            msg = 'Photos successfully sorted, duplicates files are: \n'
            for file in duplicate:
               msg += file + '\n'
            messagebox.showinfo('Success', msg)
    except:
        messagebox.showerror('Error', 'Incorrect paths, please try again')

def select_path(entry, choice):
    path = filedialog.askdirectory()
    if choice == 'source':
        global source_path
        source_path = path
    else:
        global target_path
        target_path = path
    
    entry.configure(text = path)

def path_frame(frameLabel, choice):
    fra = LabelFrame(root, text = frameLabel, height = 200, width = 500, padx=10, pady=10)
    fra.pack(pady=10)

    entry = Label(fra, text = "(choose a path)")
    entry.grid(column=0, row=0,)

    Btn = Button(fra, text = 'Select', command = lambda: select_path(entry, choice))
    Btn.grid(column=1, row=0, padx=10)

source_path = ''
target_path = ''

path_frame('Select a Path:', 'source')
path_frame('Select a Destination:', 'target')

confirmBtn = Button(root, text = 'Move', command= lambda: move_photo(source_path, target_path))
confirmBtn.pack(pady=10)

root.mainloop()