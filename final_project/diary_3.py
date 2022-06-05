import tkinter as tk
from tkinter import messagebox

def update():
    clearlistbox()
    for utask in tasks:
        lbl_task.insert('end', utask)

def clearlistbox():
    lbl_task.delete(0, 'end')

def addtask():
    lbl_display['text'] = ""
    new_date = dateinput.get()
    new_time = timeinput.get()
    new_weather = weatherinput.get()
    new_place = placeinput.get()
    new_people = peopleinput.get()
    new_task = taskinput.get()

    if {
        (new_date != ""),
        (new_time != ""),
        (new_weather != ""),
        (new_place != ""),
        (new_people != ""),
        (new_task != "")
    }:
        dates.append(new_date)
        times.append(new_time)
        weathers.append(new_weather)
        places.append(new_place)
        people.append(new_people)
        tasks.append(new_task)
        update()

    elif new_date == "":
        lbl_display["text"] = "날짜를 입력하세요."
    dateinput.delete(0, "end")

    elif new_weather == "":
        lbl_display["text"] = "날씨를 입력하세요."
        weatherinput.delete(0, "end")

    elif new_task == "":
        lbl_display["text"] = "할 일을 입력하세요."
        taskinput.delete(0, "end")

    else:
        pass
    timeinput.delete(0, "end")
    placeinput.delete(0, "end")
    peopleinput.delete(0, "end")
    # if new_date != "":
    #     dates.append(new_date)
    #     update()
    # else:
    #     lbl_display['text'] = "날짜를 입력하세요."
    # dateinput.delete(0, 'end')
    #
    # if new_time != "":
    #     times.append(new_time)
    #     update()
    # timeinput.delete(0, 'end')
    #
    # else:
    #     pass
    #
    # if new_weather != "":
    #     weathers.append(new_weather)
    #     update()
    #
    # else:
    #     lbl_display['text'] = "날씨를 입력하세요."
    # weatherinput.delete(0, 'end')
    #
    # if new_place != "":
    #     places.append(new_place)
    #     update()
    # else:
    #     pass
    # placeinput.delete(0, 'end')
    #
    # if new_people != "":
    #     people.append(new_people)
    #     update()
    #
    # else:
    #     pass
    # peopleinput.delete(0, 'end')
    #
    # if new_task != "":
    #     tasks.append(new_task)
    #     update()
    # else:
    #     lbl_display['text'] = "할 일을 입력하세요."
    # taskinput.delete(0, 'end')

def delete():
    delt = lbl_task.get('active')
    if delt in tasks:
        tasks.remove(delt)
    update()

def save():
    savecon = messagebox.askquestion(
        'Save confirmation', '저장하시겠습니까?'
    )
    if savecon.upper() == "yes":
        with open("savefile.txt", "w") as filehandle:
            for listitem in tasks:
                filehandle.write('%s\n' % listitem)
    else:
        pass

def load():
    loadcon = messagebox.askquestion(
        'Load confirmation', '저장된 데이터를 불러오시겠습니까?'
    )
    if loadcon.upper() == "yes":
        tasks.clear()

        with open('savefile.txt', 'r') as filereader:
            for line in filereader:
                currentask = line
                tasks.append(currentask)
            update()
    else:
        pass

def exit():
    exitcon = messagebox.askquestion(
        'Quit confirmation', '나가시겠습니까?'
    )
    if exitcon.upper() == 'yes':
        window.destroy()
    else:
        pass





window = tk.Tk()
window.title("TO DO LIST")
window.configure(bg='white')
window.geometry("1000x600+100+100")
window.resizable(True, True)

dates = []
times = []
weathers = []
places = []
people = []
tasks = []

#label
lbl_title = tk.Label(window, text='TO DO LIST', bg="white")
lbl_title.grid(row=0, column=0)

lbl_date = tk.Label(window, text="날짜", bg="white")
lbl_date.grid(row=1, column=0)
dateinput = tk.Entry(window, width=15)
dateinput.grid(row=1, column=1)

lbl_time = tk.Label(window, text="시간", bg="white")
lbl_time.grid(row=2, column=0)
timeinput = tk.Entry(window, width=15)
timeinput.grid(row=2, column=1)

lbl_weather = tk.Label(window, text="날씨", bg="white")
lbl_weather.grid(row=3, column=0)
weatherinput = tk.Entry(window, width=15)
weatherinput.grid(row=3, column=1)

lbl_place = tk.Label(window, text="장소", bg="white")
lbl_place.grid(row=4, column=0)
placeinput = tk.Entry(window, width=15)
placeinput.grid(row=4, column=1)

lbl_people = tk.Label(window, text="인원", bg="white")
lbl_people.grid(row=5, column=0)
peopleinput = tk.Entry(window, width=15)
peopleinput.grid(row=5, column=1)

lbl_task = tk.Label(window, text="할 일", bg="white")
lbl_task.grid(row=6, column=0)
taskinput = tk.Entry(window, width=15)
taskinput.grid(row=6, column=1)

lbl_display = tk.Label(window, text="", bg="white")
lbl_display.grid(row=7, columnspan=7)
