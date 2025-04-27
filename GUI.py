from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Photo Mover")
root.geometry('640x240')

def clicked():
    messagebox.showinfo('success', source_path + target_path)

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

path_frame('Select a Path:', 'source')
path_frame('Select a Destination:', 'target')

confirmBtn = Button(root, text = 'Move', command= lambda: clicked())
confirmBtn.pack(pady=10)

root.mainloop()