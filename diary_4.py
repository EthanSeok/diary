import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("TO DO LIST")
window.configure(bg='white')
window.geometry("1000x600+100+100")
window.resizable(True, True)


lbl_date = tk.Label(window, text='날짜', bg="white")
lbl_date.place(x=30, y=0)
date_input = tk.Entry(window, width=20)
date_input.place(x=70, y=0)


lbl_time = tk.Label(window, text='시간', bg="white")
lbl_time.place(x=30, y=30)
time_input = tk.Entry(window, width=20)
time_input.place(x=70, y=30)


lbl_weather = tk.Label(window, text="날씨", bg="white")
lbl_weather.place(x=30, y=60)
# weather_input = tk.Entry(window, width=20)
# weather_input.place(x=70, y=60)


lbl_place = tk.Label(window, text="장소", bg="white")
lbl_place.place(x=30, y=90)
place_input = tk.Entry(window, width=20)
place_input.place(x=70, y=90)


lbl_people = tk.Label(window, text="인원", bg="white")
lbl_people.place(x=30, y=120)
people_input = tk.Entry(window, width=20)
people_input.place(x=70, y=120)


lbl_task = tk.Label(window, text="할 일", bg="white")
lbl_task.place(x=30, y=150)
task_input = tk.Entry(window, width=20)
task_input.place(x=70, y=150)


lbl_listbox = tk.Listbox(window)
lbl_listbox.place(x=0, y=200, width=300, height=150)


# lbl_display = tk.Label(window, text="할 일을 입력하세요.", bg="white")
# lbl_display.place(x=100, y=200)


# button
btn_date = tk.Button(
    window, text='추가', bg="white", width=5)
btn_date.place(x=240, y=0)

btn_time = tk.Button(
    window, text='추가', bg="white", width=5)
btn_time.place(x=240, y=30)

# btn_weather = tk.Button(
#     window, text='추가', bg="white", width=5)
# btn_weather.place(x=240, y=60)

btn_place = tk.Button(
    window, text='추가', bg="white", width=5)
btn_place.place(x=240, y=90)

btn_people = tk.Button(
    window, text='추가', bg="white", width=5)
btn_people.place(x=240, y=120)

btn_task = tk.Button(
    window, text='추가', bg="white", width=5)
btn_task.place(x=240, y=150)

btn_clear = tk.Button(window, text="완료", width=5)
btn_clear.place(x=305, y=200)

btn_del = tk.Button(window, text="삭제", width=5)
btn_del.place(x=305, y=230)

btn_load = tk.Button(window, text="load", width=5)
btn_load.place(x=305, y=260)

btn_save = tk.Button(window, text="저장", width=5)
btn_save.place(x=305, y=290)

btn_diary = tk.Button(window, text="일기", width=5)
btn_diary.place(x=305, y=320)

# weather button
btn_sunny = tk.Button(master=window, text="맑음", width=5)
btn_sunny.place(x=70, y=60)

btn_rain = tk.Button(master=window, text="비", width=5)
btn_rain.place(x=120, y=60)

btn_hazy = tk.Button(master=window, text="흐림", width=5)
btn_hazy.place(x=170, y=60)

btn_snow = tk.Button(master=window, text="눈", width=5)
btn_snow.place(x=220, y=60)

btn_wind = tk.Button(master=window, text="바람", width=5)
btn_wind.place(x=270, y=60)

btn_thun = tk.Button(master=window, text="번개", width=5)
btn_thun.place(x=320, y=60)

btn_typ = tk.Button(master=window, text="태풍", width=5)
btn_typ.place(x=370, y=60)



window.mainloop()