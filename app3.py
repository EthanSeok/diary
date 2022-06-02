import tkinter as tk
from tkinter import *


def add():
    day = input("날짜 (ex 2018. 1. 1.) : ")
    weather = input("날씨: ")
    time = input('시간:')
    place = input('장소:')
    people = input('인원:')
    task = input('할 일:')

    day = day + ''
    weather = weather + "\n"
    time = time + "\n"
    place = place + "\n"
    people = people + "\n"
    task = task + "\n"
    day = day + "\n"

    text = day + weather + time + place + people + task
    diary_text = input("일기 쓰기 : ")
    text = text+diary_text

    f = open('diary_text.txt', 'w')
    f.write(diary_text)

    return text

def modify(text):
    print("저장한 일기")
    print(text)
    print("일기를 다시 입력하세요 \n")
    modify_diary = add()
    return modify_diary


def delete(text):
    print("작성한 일기")
    print(text)
    print("")
    print("작성한 일기를 삭제 하려면 1번, 다시 돌아가려면 2번을 선택하시오.:")
    select = int(input(""))

    if (select==1):
        text = ""
        return text
    else:
        return text


# def main():
#     diary = ""
#     while True:
#         print("일기장 프로그램")
#         print("1. 일기장 입력 2. 일기장 수정 3. 일기 삭제 4. 일기 출력 5. 종료")
#         select = int(input())
#
#         if (select == 1):
#             diary = add()
#         elif (select == 2):
#             diary = modify(diary)
#         elif (select == 3):
#             diary = delete(diary)
#         elif (select == 4):
#             print(diary)
#         else:
#             break


window = tk.Tk()
window.title("TO DO LIST")
window.geometry("1000x600+100+100")
window.resizable(True, True)

# title
lbl_title = tk.Label(window, text="TO DO LIST", bg='white')
lbl_title.grid(row=0, column=0)

# lbl_display = tk.Label(window, text="", bg="white")
# lbl_display.grid(row=0, column=1)


# 날짜
lbl_1 = tk.Label(window, text='날짜')
entry_1_text = tk.Entry(window, width=10, takefocus=True, bg='white')
lbl_1.grid(row=1, column=0)
entry_1_text.grid(row=1, column=1)


# 날씨
lbl_2 = tk.Label(window, text='날씨')
entry_2_text = tk.Entry(window, width=10, takefocus=True, bg='white')

# photo_sunny = PhotoImage(file="../final_project/image/sunny.png")
# photo_rain = PhotoImage(file="../final_project/image/rain.png")
# photo_hazy = PhotoImage(file="../final_project/image/hazy.png")
# photo_snow = PhotoImage(file="../final_project/image/snow.png")
# photo_wind = PhotoImage(file="../final_project/image/wind.png")
# photo_thun = PhotoImage(file="../final_project/image/thunderbolt.png")
# photo_typ = PhotoImage(file="../final_project/image/typhoon.png")
#
# btn_sunny = tk.Button(master=window, image=photo_sunny, width=20, height=20)
# btn_rain = tk.Button(master=window, image=photo_rain, width=20, height=20)
# btn_hazy = tk.Button(master=window, image=photo_hazy, width=20, height=20)
# btn_snow = tk.Button(master=window, image=photo_snow, width=20, height=20)
# btn_wind = tk.Button(master=window, image=photo_wind, width=20, height=20)
# btn_thun = tk.Button(master=window, image=photo_thun, width=20, height=20)
# btn_typ = tk.Button(master=window, image=photo_typ, width=20, height=20)

btn_sunny = tk.Button(master=window, text="맑음", width=10)
btn_rain = tk.Button(master=window, text="비", width=10)
btn_hazy = tk.Button(master=window, text="흐림", width=10)
btn_snow = tk.Button(master=window, text="눈", width=10)
btn_wind = tk.Button(master=window, text="바람", width=10)
btn_thun = tk.Button(master=window, text="번개", width=10)
btn_typ = tk.Button(master=window, text="태풍", width=10)

lbl_2.grid(row=2, column=0)
btn_sunny.grid(row=2, column=1, padx=10)
btn_rain.grid(row=2, column=2, padx=10)
btn_hazy.grid(row=2, column=3, padx=10)
btn_snow.grid(row=2, column=4, padx=10)
btn_wind.grid(row=2, column=5, padx=10)
btn_thun.grid(row=2, column=6, padx=10)
btn_typ.grid(row=2, column=7, padx=10)


# 시간
lbl_3 = tk.Label(window, text='시간')
entry_3_text = tk.Entry(window, width=10, takefocus=True, bg='white')

lbl_3.grid(row=3, column=0)
entry_3_text.grid(row=3, column=1)


# 장소
lbl_4 = tk.Label(window, text='장소')
entry_4_text = tk.Entry(window, width=10, takefocus=True, bg='white')

lbl_4.grid(row=4, column=0)
entry_4_text.grid(row=4, column=1)


# 인원
lbl_5 = tk.Label(window, text='인원')
entry_5_text = tk.Entry(window, width=10, takefocus=True, bg='white')

lbl_5.grid(row=5, column=0)
entry_5_text.grid(row=5, column=1)


# 할 일
lbl_6 = tk.Label(window, text='할 일')
entry_6_text = tk.Entry(window, width=10, takefocus=True, bg='white', justify='left')

lbl_6.grid(row=6, column=0)
entry_6_text.grid(row=6, column=1)

# 저장
btn_update = tk.Button(window, text='저장', width=10)
btn_update.grid(row=7, column=0)



# if __name__=='__main__':
#     main()


window.mainloop()
