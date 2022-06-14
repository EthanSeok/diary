from tkinter import *
from tkinter import messagebox

def clearlistbox():
    listb.delete(0, "end")

def deleteall():
    message = messagebox.askquestion(
        '삭제 경고', '정말로 리스트를 비우겠습니까?')
    print(message)
    if message.upper() == "YES":
        global day_list, time_list, place_list, people_list, task_list, sunny_list, rain_list, hazy_list, snow_list, wind_list, thun_list, verysati_list, sati_list, neither_list, dissati_list, verydissati_list,felt_list
        day_list= []
        time_list = []
        place_list = []
        people_list = []
        task_list = []
        sunny_list = []
        rain_list = []
        hazy_list = []
        snow_list = []
        wind_list = []
        thun_list = []
        verysati_list = []
        sati_list = []
        neither_list = []
        dissati_list = []
        verydissati_list = []
        felt_list = []
        update()
    else:
        pass

def update():
    clearlistbox()
    for date in day_list:
        listb.insert("end", date)

    for times in time_list:
        listb.insert("end", times)

    for sunny in sunny_list:
        listb.insert("end", sunny)

    for rain in rain_list:
        listb.insert("end", rain)

    for hazy in hazy_list:
        listb.insert("end", hazy)

    for snow in snow_list:
        listb.insert("end", snow)

    for wind in wind_list:
        listb.insert("end", wind)

    for thun in thun_list:
        listb.insert("end", thun)

    for places in place_list:
        listb.insert("end", places)

    for peoples in people_list:
        listb.insert("end", peoples)

    for tasks in task_list:
        listb.insert("end", tasks)

    for verysati in verysati_list:
        listb.insert("end", verysati)

    for sati in sati_list:
        listb.insert("end", sati)

    for neither in neither_list:
        listb.insert("end", neither)

    for dissati in dissati_list:
        listb.insert("end", dissati)

    for verydissati in verydissati_list:
        listb.insert("end", verydissati)

    for felt in felt_list:
        listb.insert("end", felt)

    return

def deleteone():
    delt = listb.get("active")
    if delt in day_list:
        day_list.remove(delt)
    update()

    if delt in sunny_list:
        sunny_list.remove(delt)
    update()

    if delt in rain_list:
        rain_list.remove(delt)
    update()

    if delt in hazy_list:
        hazy_list.remove(delt)
    update()

    if delt in snow_list:
        snow_list.remove(delt)
    update()

    if delt in wind_list:
        wind_list.remove(delt)
    update()

    if delt in thun_list:
        thun_list.remove(delt)
    update()

    if delt in time_list:
        time_list.remove(delt)
    update()

    if delt in place_list:
        place_list.remove(delt)
    update()

    if delt in people_list:
        people_list.remove(delt)
    update()

    if delt in task_list:
        task_list.remove(delt)
    update()

    if delt in verysati_list:
        verysati_list.remove(delt)
    update()

    if delt in sati_list:
        sati_list.remove(delt)
    update()

    if delt in neither_list:
        neither_list.remove(delt)
    update()

    if delt in dissati_list:
        dissati_list.remove(delt)
    update()

    if delt in verydissati_list:
        verydissati_list.remove(delt)
    update()

    if delt in felt_list:
        felt_list.remove(delt)
    update()

    return

def day_in():
    lbl_1_display["text"] = ""
    day = entry_1_text.get()
    if day != "":
        day_list.append(day)
        update()
    else:
        lbl_1_display["text"] = "날짜를 빼먹으면 일기를 못쓰지?"
    entry_1_text.delete(0, 'end')

    return

def sunny_in():
    lbl_2_display['text'] = ''
    sunny = '맑았다.'
    if sunny_list != "":
        sunny_list.append(sunny)
        update()
    return sunny

def rain_in():
    lbl_2_display['text'] = ''
    rain = '비가 왔다.'
    if rain_list != "":
        sunny_list.append(rain)
        update()
    return rain

def hazy_in():
    lbl_2_display['text'] = ''
    hazy = '날이 흐렸다.'
    if hazy_list != "":
        sunny_list.append(hazy)
        update()
    return hazy

def snow_in():
    lbl_2_display['text'] = ''
    snow = '눈이 왔다.'
    if snow_list != "":
        snow_list.append(snow)
        update()
    return snow

def wind_in():
    lbl_2_display['text'] = ''
    wind = '바람이 많이 불었다.'
    if wind_list != "":
        wind_list.append(wind)
        update()
    return wind

def thun_in():
    lbl_2_display['text'] = ''
    thun = '번개가 많이 쳤다.'
    if thun_list != "":
        thun_list.append(thun)
        update()
    return thun

def time_in():
    lbl_3_display["text"] = ""
    time = entry_3_text.get()
    if time != "":
        time_list.append(time)
        update()
    else:
        lbl_3_display["text"] = "시간 빼먹으면 일기를 못쓰지?"
    entry_3_text.delete(0, 'end')

    return

def place_in():
    lbl_4_display["text"] = ""
    place = entry_4_text.get()
    if place != "":
        place_list.append(place)
        update()
    else:
        lbl_4_display["text"] = "장소를 빼먹으면 일기를 못쓰지?"
    entry_4_text.delete(0, 'end')

    return

def people_in():
    lbl_5_display["text"] = ""
    people = entry_5_text.get()
    if people != "":
        people_list.append(people)
        update()
    else:
        lbl_5_display["text"] = "인원을 빼먹으면 일기를 못쓰지?"
    entry_5_text.delete(0, 'end')

    return

def task_in():
    lbl_6_display["text"] = ""
    task = entry_6_text.get()
    if task != "":
        task_list.append(task)
        update()
    else:
        lbl_6_display["text"] = "할 일이 없어? 게으르게 살거야?"
    entry_6_text.delete(0, 'end')

    return

def verysati_in():
    lbl_satisfaction_display['text'] = ''
    verysati = '매우 만족스러웠다.'
    if verysati_list != "":
        verysati_list.append(verysati)
        update()
    return verysati

def sati_in():
    lbl_satisfaction_display['text'] = ''
    sati = '만족스러웠다.'
    if sati_list != "":
        sati_list.append(sati)
        update()
    return sati

def neither_in():
    lbl_satisfaction_display['text'] = ''
    neither = '그저그랬다.'
    if neither_list != "":
        neither_list.append(neither)
        update()
    return neither

def dissati_in():
    lbl_satisfaction_display['text'] = ''
    dissati = '별로였다.'
    if dissati_list != "":
        dissati_list.append(dissati)
        update()
    return dissati

def verydissati_in():
    lbl_satisfaction_display['text'] = ''
    verydissati = '매우 별로였다.'
    if verydissati_list != "":
        verydissati_list.append(verydissati)
        update()
    return verydissati

def felt_in():
    lbl_felt["text"] = ""
    felt = felt_input.get()
    if felt != "":
        felt_list.append(felt)
        update()
    else:
        lbl_felt_display["text"] = "느낀게 없어? 귀찮아도 생각해봐.."
    felt_input.delete(0, 'end')

def add():
    day = ''.join(day_list) + '' + "\n"
    sunny = ''.join(sunny_list)
    rain = ''.join(rain_list)
    hazy = ''.join(hazy_list)
    snow = ''.join(snow_list)
    wind = ''.join(wind_list)
    thun = ''.join(thun_list)
    time = ''.join(time_list)
    place = ''.join(place_list)
    people = ''.join(people_list)
    task = ''.join(task_list)
    verysati = ''.join(verysati_list)
    sati = ''.join(sati_list)
    neither = ''.join(neither_list)
    dissati = ''.join(dissati_list)
    verydissati = ''.join(verydissati_list)
    felt = ''.join(felt_list)


    weather = sunny + rain + hazy + snow + wind + thun
    sati = verysati + sati + neither + dissati + verydissati
    diary_text = "오늘의 일기 {}\n " \
                 "오늘은 날씨가 {}\n " \
                 "{}에 {}명이랑 만났다.\n " \
                 "{}명이랑 {}에서 만나서 {}을(를) 했다.\n" \
                 "오늘 하루는 {}\n" \
                 "\n" \
                 "느낀점\n" \
                 "\n" \
                 "{}\n" \
                 "---------------------------------------------------------------\n" \
                 " ".format(day,weather,time,people, people, place, task, sati, felt)

    if people == '0':
        diary_text = "오늘의 일기 {}\n " \
                 "오늘은 날씨가 {}\n " \
                 "{}에 나 혼자 있었다.\n " \
                 "{}에서 나 혼자 {}을(를) 했다.\n" \
                 "오늘 하루는 {}\n" \
                 "\n" \
                 "느낀점\n" \
                 "\n" \
                 "{} \n" \
                 "---------------------------------------------------------------\n" \
                "".format(day,weather,time, place, task, sati, felt)

    elif people != (1, 100000):
        diary_text = "오늘의 일기 {}\n " \
                     "오늘은 날씨가 {}\n " \
                     "{}에 {}이랑 만났다.\n " \
                     "{}명이랑 {}에서 만나서 {}을(를) 했다.\n" \
                     "오늘 하루는 {}\n" \
                     "\n" \
                     "느낀점\n" \
                     "\n" \
                     "{} \n" \
                     "---------------------------------------------------------------\n" \
                     "".format(day, weather, time, people, people, place, task, sati, felt)

    message = messagebox.askquestion(
        '일기 쓰기', '리스트를 확정하여 일기를 불러오시겠습니까?')
    print(message)
    if message.upper() == "YES":
        lbl_diary_2['text'] = ''
        if diary_text != "":
            lbl_diary_2['text'] = diary_text
            update()

    f = open('diary_text.txt', 'a')
    f.write(diary_text)

    return

def clear_default(event):
    event.widget.delete(0, 'end')
    event.widget.unbind('<FocusIn>')

window = Tk()
window.title("일기를 써주세요")
window.configure(bg='white')
window.geometry("1000x600+100+100")
window.resizable(True, True)

day_list = []
sunny_list = []
rain_list = []
hazy_list = []
snow_list = []
wind_list = []
thun_list = []
time_list = []
place_list = []
people_list = []
task_list = []
verysati_list = []
sati_list = []
neither_list = []
dissati_list = []
verydissati_list = []
felt_list = []


# 날짜
lbl_1 = Label(window, text='날짜', bg="white")
entry_1_text = Entry(window, width=20)
entry_1_text.insert(0, 'ex) 2022.06.14')
entry_1_text.bind('<FocusIn>', clear_default)
lbl_1.place(x=30, y=0)
entry_1_text.place(x=70, y=0)
btn_day = Button(window, text='추가', bg="white", width=5, command=day_in)
btn_day.place(x=240, y=0)
lbl_1_display = Label(window, text="", bg="white")
lbl_1_display.place(x=290, y=0)

# 시간
lbl_3 = Label(window, text='시간', bg="white")
entry_3_text = Entry(window, width=20)
entry_3_text.insert(0, 'ex) 아침(오전) 9시')
entry_3_text.bind('<FocusIn>', clear_default)
lbl_3.place(x=30, y=30)
entry_3_text.place(x=70, y=30)
btn_time = Button(window, text='추가', bg="white", width=5, command=time_in)
btn_time.place(x=240, y=30)
lbl_3_display = Label(window, text="", bg="white")
lbl_3_display.place(x=290, y=30)

# 날씨
lbl_2 = Label(window, text="날씨", bg="white")
lbl_2.place(x=30, y=60)
entry_2_text = Entry(window, width=10, takefocus=True, bg='white')

photo_sunny = PhotoImage(file="../final_project/image/sunny.png")
photo_rain = PhotoImage(file="../final_project/image/rain.png")
photo_hazy = PhotoImage(file="../final_project/image/hazy.png")
photo_snow = PhotoImage(file="../final_project/image/snow.png")
photo_wind = PhotoImage(file="../final_project/image/wind.png")
photo_thun = PhotoImage(file="../final_project/image/thunderbolt.png")

btn_sunny = Button(master=window, image=photo_sunny, width=20, height=20, command=sunny_in)
btn_rain = Button(master=window, image=photo_rain, width=20, height=20, command=rain_in)
btn_hazy = Button(master=window, image=photo_hazy, width=20, height=20, command=hazy_in)
btn_snow = Button(master=window, image=photo_snow, width=20, height=20, command=snow_in)
btn_wind = Button(master=window, image=photo_wind, width=20, height=20, command=wind_in)
btn_thun = Button(master=window, image=photo_thun, width=20, height=20, command=thun_in)

btn_sunny.place(x=70, y=60)
btn_rain.place(x=120, y=60)
btn_hazy.place(x=170, y=60)
btn_snow.place(x=220, y=60)
btn_wind.place(x=270, y=60)
btn_thun.place(x=320, y=60)

lbl_2_display = Label(window, text="", bg="white")
lbl_2_display.place(x=350, y=60)


# 장소
lbl_4 = Label(window, text="장소", bg="white")
entry_4_text = Entry(window, width=20)
lbl_4.place(x=30, y=90)
entry_4_text.place(x=70, y=90)
btn_place = Button(window, text='추가', bg="white", width=5, command=place_in)
btn_place.place(x=240, y=90)
lbl_4_display = Label(window, text="", bg="white")
lbl_4_display.place(x=290, y=90)

# 인원
lbl_5 = Label(window, text="인원", bg="white")
entry_5_text = Entry(window, width=20)
entry_5_text.insert(0, 'ex) 혼자일 경우 0')
entry_5_text.bind('<FocusIn>', clear_default)
lbl_5.place(x=30, y=120)
entry_5_text.place(x=70, y=120)
btn_people = Button(window, text='추가', bg="white", width=5, command=people_in)
btn_people.place(x=240, y=120)
lbl_5_display = Label(window, text="", bg="white")
lbl_5_display.place(x=290, y=120)

# 할 일
lbl_6 = Label(window, text="할 일", bg="white")
entry_6_text = Entry(window, width=20)
lbl_6.place(x=30, y=150)
entry_6_text.place(x=70, y=150)
btn_task = Button(window, text='추가', bg="white", width=5, command=task_in)
btn_task.place(x=240, y=150)
lbl_6_display = Label(window, text="", bg="white")
lbl_6_display.place(x=290, y=150)

# 만족도
lbl_satisfaction = Label(window, text="만족도", bg="white", width=5)
lbl_satisfaction.place(x=30, y=180)

btn_verysati = Button(master=window, text="매우만족", width=7, command=verysati_in)
btn_verysati.place(x=80, y=180)

btn_sati = Button(master=window, text="만족", width=7, command=sati_in)
btn_sati.place(x=145, y=180)

btn_neither = Button(master=window, text="보통", width=7, command=neither_in)
btn_neither.place(x=210, y=180)

btn_dissati = Button(master=window, text="나쁨", width=7, command=dissati_in)
btn_dissati.place(x=275, y=180)

btn_verydissati = Button(master=window, text="매우나쁨", width=7, command=verydissati_in)
btn_verydissati.place(x=340, y=180)

lbl_satisfaction_display = Label(window, text="", bg="white")
lbl_satisfaction_display.place(x=400, y=180)

#느낀점
lbl_felt = Label(window, text="느낀점", bg="white", width=5)
lbl_felt.place(x=30, y=215)

felt_input = Entry(window, width=45)
felt_input.place(x=80, y=215, height=130)

btn_add = Button(window, text="추가", bg="white", width=5, command=felt_in)
btn_add.place(x=353, y=215)

lbl_felt_display = Label(window, text="", bg="white")
lbl_felt_display.place(x=80, y=355)

# 저장
btn_update = Button(window, text="완료", width=5, command=add)
btn_update.place(x=335, y=380, height=50)

btn_del = Button(window, text="삭제", width=5, command=deleteone)
btn_del.place(x=335, y=445, height=35)

btn_diary = Button(window, text="clear", width=5, command=deleteall)
btn_diary.place(x=335, y=495, height=35)

listb = Listbox()
listb.place(x=30, y=380, width=300, height=150)

# 일기
lbl_diary = Label(window, text="일기", bg="white", width=5)
lbl_diary.place(x=500, y=0)
lbl_diary_2 = Label(window, bg="white", relief="solid")
lbl_diary_2.place(x=500, y=30, width=480, height=500)

window.mainloop()
