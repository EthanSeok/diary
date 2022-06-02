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


def main():
    diary = ""
    while True:
        print("일기장 프로그램")
        print("1. 일기장 입력 2. 일기장 수정 3. 일기 삭제 4. 일기 출력 5. 종료")
        select = int(input())

        if (select == 1):
            diary = add()
        elif (select == 2):
            diary = modify(diary)
        elif (select == 3):
            diary = delete(diary)
        elif (select == 4):
            print(diary)
        else:
            break

if __name__=='__main__':
    main()
