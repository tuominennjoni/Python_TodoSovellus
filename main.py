import tkinter
from tkinter import *

root = Tk() # luodaan ikkuna
root.title("To-Do-Lista") # nimi
root.geometry("400x650+400+100") # koko
root.resizable(False, False) # ei voi muuttaa ikkunan kokoa

task_list = [] # list


def addTask(): # lisätään taski funktio
    task = task_entry.get() # lisäys
    task_entry.delete(0, END) # lisäysboksi tyhjäksi

    if task:
        with open("tasklist.txt", "a") as taskfile: # avataan tasklist tekstitiedosto
            taskfile.write(f"\n{task}") # kirjoitetaan 
        task_list.append(task) # lisätään taski listaan
        listbox.insert(END, task) # insert
  
def deleteTask(): # taskin poisto
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open('tasklist.txt', 'w')
        file.close()


# vaihdetaan iconi
Image_icon = PhotoImage(file="image/task.png")
root.iconphoto(False, Image_icon)

# ylä bar
TopImage = PhotoImage(file="image/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="image/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="Kaikki tehtävät", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# maini
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
button = Button(frame, text="LISÄÄ", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# list boksit

frame1 = Frame(root, bd=3, width=700, height=250, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="#fff", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# poisto
Delete_icon = PhotoImage(file="image/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)
root.mainloop()
