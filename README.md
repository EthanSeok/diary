
# Python을 활용하여 **Diary**를 작성해 보자.

---

<p align="center">
<img src = "https://user-images.githubusercontent.com/102236107/173296132-d20e82d4-2db1-43ee-9109-510085cf58dd.png" width="500" height="300"/>

---

## 프로젝트 배경 및 목표
이 프로젝트는 바쁜 일상에 지쳐 일기를 쓸 겨를도 없는 현대인들이 하루의 일상을 놓치지 않고 기록할 수 있으면 좋겠다는 생각에 진행하게 되었습니다.<br>
하루동안 기억에 남는 하나의 일과에 대한 간단한 정보만 입력하면 자동으로 일기를 구현해 줍니다.<br>
일기는 느낀점이 중요한거 아니냐고요? --> 맞습니다! 그래서 느낀점 또한 추가하여 일기의 질을 높일 수 있도록 구현하였습니다.<br>
<br>
파이썬 모듈인 **tkinter**을 활용하여 자동 일기쓰기를 **GUI**로 구현하였습니다.


---

## 구현 방법

tkinter 모듈을 이용하여 gui로 구연했기 때문에 평소에 보던 검정 화면에서 벗어나 클릭할 수 있는 버튼과 직접 타이핑을 할 수 있는 텍스트 박스를 활용하여 보다 쉽게 활용할 수 있습니다.<br>
<br>
  
<p align="center">
<img src = "https://user-images.githubusercontent.com/102236107/173298980-2a2ed9e6-98b4-4948-bf26-4fa92191dfa5.png" width="500" height="300"/><br>
  
<br>
다음 사진과 같은 양식으로 텍스트 박스 안에 그날 한 일에 대한 간단한 정보를 입력합니다.<br>
<br>
  
<p align="center">  
<img src = "https://user-images.githubusercontent.com/102236107/173299395-818e0dab-0259-4ec9-aeb0-60bed2728a97.png" width="500" height="300"/><br>
  
<br>
텍스트를 입력한 후 텍스트 박스 옆에 있는 '추가' 버튼을 클릭하고 확인 리스트 박스에 입력 값이 잘 들어갔는지 확인합니다.
<br>
<br>
<br>
날씨의 경우 모든 선택지가 버튼으로 구현되어 있습니다. 날씨는 차례대로 '맑음', '비', '구름', '눈', '바람', '번개'입니다.
당시 날씨에 맞는 버튼을 클릭하면 리스트 박스 안에 해당 날씨가 자동으로 입력됩니다. <br>
만족도도 날씨와 마찬가지로 모든 선택지가 버튼으로 구현되어 있기 때문에 당일 한 일에 대한 만족도를 스스로 평가하여 입력하면 됩니다.<br>
<br>  
  
<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/173333711-f8a002ed-ee9f-433d-b0c7-7a42064387ca.png" width="500" height="300"/><br>
<br>
<p align="center">  
다음과 같이 모든 항목을 채웠으나 마음에 들지 않아 수정하고 싶을 경우에는  

<br>  
<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/173334333-5380b1f8-0a4c-47ca-b9cb-7dd940f6737e.png" width="500" height="300"/><br>
<br>
지우고 싶은 항목을 클릭한 뒤에 삭제 버튼을 누르면 다음과 같이 삭제 됩니다.<br>

<br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/93086581/173334641-17e5a582-798d-4100-8583-968e67665292.png" width="500" height="300"/><br>
<br>
다음과 같이 항목이 삭제 된것을 확인할 수 있습니다.<br>
    
<br>
<br>
이후 리스트 박스 안에 원하는 값이 모두 들어간 것을 확인했다면, 이후 '입력' 버튼을 클릭하면 일기가 자동으로 써서 출력됩니다.<br>
<br>

<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/173331961-40cee848-6c5d-4074-932c-a9bbb2a8fec8.png" width="400" height="200"/><br>  
<br>
다음 안내창이 뜨면 일기를 불러오려면 '예' 다시 수정하려면 '아니요'를 클릭합니다.
  
<br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/93086581/172658242-c931c8c3-a209-4bbf-b54b-9f742721846f.png" width="400" height="400"/><br> 
다음과 같이 일기가 자동으로 출력됩니다!

---
## 사용한 기술
**GUI** 에 대한 표준 **Python 인터페이스**인 **tkinter** 모듈을 사용하여 window 창을 활용하여 프로그램을 구현.
<br>
<br>
<br>

<h3> tkinter 사용하기 </h3>

```
from tkinter import *
```

```
window = Tk()
window.title("일기를 써주세요")
window.configure(bg='white')
window.geometry("1000x600+100+100")
window.resizable(True, True)

window.mainloop()
```

기본적인 window 틀을 만들어 줍니다. 순서대로 배경색, 사이즈, 창사이즈 조절 가능 여부를 의미합니다.<br>
<br>
마지막 **window.mainloop()** 는 창을 임의로 종료할때 까지 실행되도록 합니다.<br>

<h3> 프로그램 설계 </h3>
---

자동으로 일기쓰기 프로그램은 날짜, 시간, 날씨, 장소, 인원, 할 일, 만족도, 느낀점을 각각 따로 입력 받아 <br>
이미 짜여진 일기 스크립트에 적용되어 자동으로 일기가 작성되는 방법을 베이스로 합니다.<br>
<br>
이를 위해서는 각각 입력 받은 요소를 각각의 리스트에 집어 넣어 필요할때 꺼낼 수 있도록 설계했습니다.
<br>

```
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
```
<br>
다음과 같이 각각을 리스트에 저장합니다. 날씨와 만족도의 경우 버튼 클릭으로 구현하고 싶었습니다.<br>
고민 끝에 각각의 요소를 모두 리스트로 만들어 리스트 안에 텍스트가 들어가도록 설계했습니다.<br>
<br>

```
def sunny_in():
    lbl_2_display['text'] = ''
    sunny = '맑았다.'
    if sunny_list != "":
        sunny_list.append(sunny)
        update()
    return sunny
```
<br>
다음 날씨 예시 코드와 같이 '맑았다'를 sunny_list 리스트 안에 고정으로 넣어 버튼을 클릭시'맑았다'가 출력되도록<br>
설계했습니다.<br>
<br>
<br>

```
def day_in():
    lbl_1_display["text"] = ""
    day = entry_1_text.get()
    if day != "":
        day_list.append(day)
        update()
    else:
        lbl_1_display["text"] = "날짜를 빼먹으면 일기를 못쓰지?"
    entry_1_text.delete(0, 'end')
```
<br>
다음 날짜 예시 코드는 사용자가 날씨 예시 코드와는 다르게 정해진 텍스트가 아닌 사용자가 입력한 텍스트가 <br>
리스트 안에 들어가도록 설계했습니다. 만약에 사용자가 아무것도 입력을 하지 않고 '추가'를 클릭했을 시<br>
"날짜를 빼먹으면 일기를 못쓰지?"와 같은 반응이 나오도록 설계했습니다.<br>
<br>

<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/173354480-d9151ca4-13f7-472c-9eae-c3b10b3dd9ef.png" width="500" height="300"/><br>
<br>
<br>

```
listb = Listbox()
listb.place(x=30, y=380, width=300, height=150)
```
<br>
사용자가 어떠한 값을 입력했는지 확인하기 위해서 리스트 박스를 만들어 입력한 값을 확인하고 수정할 수 있도록 설계했습니다.<br>

<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/173359111-ed051ac7-4160-4316-adc6-981ccb946f3d.png" width="400" height="200"/><br>
<br>
다음과 같이 입력한 값이 리스트 박스 안에 들어가고, 수정 작업을 할 수 있습니다.<br>
<br>

```
def clearlistbox():
    listb.delete(0, "end")
```
<br>
다음 코드는 리스트 박스 안에 입력된 값을 지우는 코드입니다.
<br>
<br>

```
def update():
    clearlistbox()
    for date in day_list:
        listb.insert("end", date)
```
<br>
다음 날짜 예시 코드는 리스트 박스 안에 입력 받은 값을 넣어주는 코드입니다. 위에서 만든 clearlistbox()를<br>
이용하여 선행 입력 값을 삭제하여 같은 값이 중복되어 들어가는 것을 방지합니다. for 반복문을 사용하여 <br>
날짜 뿐만 아니라 다른 값들 또한 입력 받을 수 있도록 설계했습니다.
<br>
<br>

```
def deleteone():
    delt = listb.get("active")
    if delt in day_list:
        day_list.remove(delt)
    update()
```
<br>
다음 날짜 예시 코드는 리스트 박스 안에 입력 받은 값을 제거하는 코드입니다. if 문을 사용하여 날짜 리스트<br>
안에 들어 있는 입력 받은 값을 제거하고, update()을 다시 실행하여 리스트 박스 안에 들어간 값을 제거합니다.
<br>
<br>

```
from tkinter import messagebox
```
<br>
messagebox 모듈을 이용하여 새로운 윈도우 창이 실행 되어 메세지를 전달 할 수 있도록 설계했습니다.
<br>
<br>

```
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
```
<br>
다음 코드는 리스트 박스 안에 입력 받은 값을 모두 지우는 코드입니다. messagebox 모듈을 이용하여<br>
메세지 창을 띄우고, 사용자가 '예'를 클릭하면 모두 삭제 되도록 설계했습니다. global을 통해 전역 변수인 <br>
리스트 들을 불러와 공백으로 만들고, update()를 실행하여 리스트 박스 내에 입력 받은 값들을 제거합니다.
<br>
<br>

```
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
                 "{} ".format(day,weather,time,people, people, place, task, sati, felt)

    message = messagebox.askquestion(
        '일기 쓰기', '리스트를 확정하여 일기를 불러오시겠습니까?')
    print(message)
    if message.upper() == "YES":
        lbl_diary_2['text'] = ''
        if diary_text != "":
            lbl_diary_2['text'] = diary_text
            update()
```
<br>
다음 코드는 사용자로 부토 입력 받아 리스트안에 들어간 정보를 기반으로 일기를 쓰는 코드입니다.<br>
''.join()을 이용하여 리스트 내의 텍스트를 추출하여 미리 작성한 일기 스크립트 내에 지정한 위치에 <br>
대입합니다. 이 또한 마찬가지로 messagebox룰 이용하여 최종적으로 일기를 작성할 것인지 물어봅니다.
<br>
<br>

```
lbl_1 = Label(window, text='날짜', bg="white")
entry_1_text = Entry(window, width=20)
lbl_1.place(x=30, y=0)
entry_1_text.place(x=70, y=0)
btn_day = Button(window, text='추가', bg="white", width=5, command=day_in)
btn_day.place(x=240, y=0)
lbl_1_display = Label(window, text="", bg="white")
lbl_1_display.place(x=290, y=0)
```
<br>
마지막으로 다음 날짜 예제 코드는 tkinter의 GUI 위젯을 세팅하는 코드입니다.<br>
각각 Label(라벨), Entry(입력 칸), Button(버튼) 위젯의 크기를 조절하고<br>
place()를 이용하여 위젯의 위치를 지정했습니다. command를 통해 위에서 본 day_in 코드를 <br>
버튼을 누르면 실행 되도록 설계했습니다. 
<br>
<br>


---
## 참고 문헌
Python tkinter 강좌 - https://076923.github.io/posts/Python-tkinter-1/ <br>
to do list - https://pythonguides.com/python-tkinter-todo-list/
