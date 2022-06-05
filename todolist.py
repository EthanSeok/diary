from tkinter import *
import tkinter
import random
from tkinter import messagebox


def updatetask():
    clearlistbox()
    for utask in tasks:
        lbltask.insert("end", utask)
    numtask = len(tasks)
    lbldsp_count['text'] = numtask


def clearlistbox():
    lbltask.delete(0, "end")


def addtask():
    lbldisplay["text"] = ""
    Ntask = txtinput.get()
    if Ntask != "":
        tasks.append(Ntask)
        updatetask()
    else:
        lbldisplay["text"] = "please enter the text"
    txtinput.delete(0, 'end')


def deleteall():
    conf = messagebox.askquestion(
        'delet all??', 'are you sure to delete all task?')
    print(conf)
    if conf.upper() == "YES":
        global tasks
        tasks = []
        updatetask()
    else:
        pass


def deleteone():
    delt = lbltask.get("active")
    if delt in tasks:
        tasks.remove(delt)
    updatetask()


def sortasc():
    tasks.sort()
    updatetask()


def sortdsc():
    tasks.sort(reverse=True)
    updatetask()


def randomtsk():
    randtask = random.choice(tasks)
    lbldisplay["text"] = randtask


def numbertsk():
    numtask = len(tasks)
    lbldisplay["text"] = numtask


def saveact():
    savecon = messagebox.askquestion(
        'Save confirmation', 'Save Your Progress?')
    if savecon.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for listitem in tasks:
                filehandle.write('%s\n' % listitem)
    else:
        pass


def loadinfo():
    messagebox.showinfo(
        "info", "This is Todolist  \n created by Pythontpoint ",)


def loadact():
    loadcon = messagebox.askquestion(
        'Save Confirmation', 'save your progress?')
    if loadcon.upper() == "YES":
        tasks.clear()

        with open('SaveFile.txt', 'r') as filereader:
            for line in filereader:
                currentask = line
                tasks.append(currentask)
            updatetask()

    else:
        pass


def exitapp():
    confex = messagebox.askquestion(
        'Quit confirmation', 'Are you sue you want to quit?')
    if confex.upper() == "YES":
        wd.destroy()
    else:
        pass


wd = tkinter.Tk()
# change wd background col and ect
wd.configure(bg="white")
wd.title("Pythontpoint")
wd.geometry("260x300")
# database
tasks = []
# tasks = ['tes 1', 'best2', 'dest3']


# GUI (graphical user interface)
# main wd app


lbltitle = tkinter.Label(wd, text="Todo List", bg="white")
lbltitle.grid(row=0, column=0)

lbldisplay = tkinter.Label(wd, text="", bg="white")
lbldisplay.grid(row=0, column=1)

lbldsp_count = tkinter.Label(wd, text="", bg="white")
lbldsp_count.grid(row=0, column=3)

txtinput = tkinter.Entry(wd, width=15)
txtinput.grid(row=1, column=1)

# button section
txtadd_button = tkinter.Button(
    wd, text="add todo", bg="white", fg="cyan", width=15, command=addtask)
txtadd_button.grid(row=1, column=0)

delonebutton = tkinter.Button(
    wd, text="Done Task", bg="white", width=15, command=deleteone)
delonebutton.grid(row=2, column=0)

delallbutton = tkinter.Button(
    wd, text="Delete all", bg="white", width=15, command=deleteall)
delallbutton.grid(row=3, column=0)

sortasc = tkinter.Button(wd, text="sort (ASC)",
                          bg="White", width=15, command=sortasc)
sortasc.grid(row=4, column=0)

sortdsc = tkinter.Button(wd, text="sort (DSC)",
                          bg="White", width=15, command=sortdsc)
sortdsc.grid(row=5, column=0)

randombutton = tkinter.Button(
    wd, text="random task", bg="White", width=15, command=randomtsk)
randombutton.grid(row=6, column=0)

numbertsk = tkinter.Button(
    wd, text="Number of Task", bg="white", width=15, command=numbertsk)
numbertsk.grid(row=7, column=0)

exitbutton = tkinter.Button(wd, text="exit app",
                           bg="white", width=15, command=exitapp)
exitbutton.grid(row=8, column=0)

savebutton = tkinter.Button(
    wd, text="save TodoList", bg="white", width=15, command=saveact)
savebutton.grid(row=10, column=1)

loadbutton = tkinter.Button(
    wd, text="Load LastTodolist", bg="white", width=15, command=loadact)
loadbutton.grid(row=10, column=0)

infobutton = tkinter.Button(
    wd, text="info", bg="white", width=15, command=loadinfo)
infobutton.grid(row=11, column=0, columnspan=2)

lbltask = tkinter.Listbox(wd)
lbltask.grid(row=2, column=1, rowspan=7)


# main loop
wd.mainloop()