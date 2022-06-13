
# Python을 활용하여 **Diary**를 작성해 보자.

---

<p align="center">
<img src = "https://user-images.githubusercontent.com/102236107/173296132-d20e82d4-2db1-43ee-9109-510085cf58dd.png" width="500" height="300"/>

---

## 개요
이 프로젝트는 바쁜 일상에 지쳐 일기를 쓸 겨를도 없는 현대인들이 하루의 일상을 놓치지 않고 기록할 수 있으면 좋겠다는 생각에 진행하게 되었습니다.<br>
하루동안 기억에 남는 하나의 일과에 대한 간단한 정보만 입력하면 자동으로 일기를 구현해 줍니다.<br>
일기는 느낀점이 중요한거 아니냐고요? --> 맞습니다! 그래서 느낀점 또한 추가하여 일기의 질을 높일 수 있도록 구현하였습니다.<br>
<br>
파이썬 모듈인 tkinter을 활용하여 자동 일기쓰기를 gui로 구현하였습니다.


---

## 사용법

tkinter 모듈을 이용하여 gui로 구연했기 때문에 평소에 보던 검정 화면에서 벗어나 클릭할 수 있는 버튼과 직접 타이핑을 할 수 있는 텍스트 박스를 활용하여 보다 쉽게 활용할 수 있습니다.<br>
<br>
  
<p align="center">
<img src = "https://user-images.githubusercontent.com/102236107/173296630-8b8521f7-3aa4-4e9f-99a4-1376bb35aa03.png" width="500" height="300"/><br>
  
<br>
다음 사진과 같은 양식으로 텍스트 박스 안에 그날 한 일에 대한 간단한 정보를 입력합니다.<br>
<br>
  
<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/172655590-bb819d1a-7c99-40e6-8f8b-c9a50311a7b9.png" width="500" height="300"/><br>
  
<br>
텍스트를 입력한 후 텍스트 박스 옆에 있는 '추가' 버튼을 클릭하고 확인 리스트 박스에 입력 값이 잘 들어갔는지 확인합니다.
<br>
  
날씨의 경우 모든 선택지가 버튼으로 구현되어 있습니다. 날씨는 차례대로 '맑음', '비', '구름', '눈', '바람', '번개'입니다.
당시 날씨에 맞는 버튼을 클릭하면 리스트 박스 안에 해당 날씨가 자동으로 입력됩니다. <br>
<br>
  
만족도도 날씨와 마찬가지로 모든 선택지가 버튼으로 구현되어 있기 때문에 당일 한 일에 대한 만족도를 스스로 평가하여 입력하면 됩니다.<br>
  
<p align="center">  
<img src = "https://user-images.githubusercontent.com/93086581/172657485-3119ea25-ce4c-47c9-8a4e-275c13e72b15.png" width="500" height="300"/><br>
  
<br>
리스트 박스 안에 원하는 값이 모두 들어간 것을 확인했다면, 이후 '입력' 버튼을 클릭하면 일기가 자동으로 써서 출력됩니다.<br>
  
<br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/93086581/172658242-c931c8c3-a209-4bbf-b54b-9f742721846f.png" width="300" height="300"/><br>
  
<br>
다음과 같이 일기가 자동으로 출력됩니다.
