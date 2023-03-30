"""
menu_choice/menu/select.py 구조의 패키지로 구성되어 식사 메뉴 골라주는 프로그램
항목 선택은 사용자가 종료할 때까지 반복하며, 메뉴는 추가 가능
메뉴 리스트 비어있을 경우 추가하라는 메시지 출력
오늘의 메뉴는 현재 메뉴 리스트에서 무작위로 선택
초기 메뉴 리스트는 ['김치찌개', '된장찌개', '설렁탕', '백반']
"""

import random

def showmenu(menulist):
    if len(menulist) < 1:
        print('메뉴를 추가하세요.')
        addmenu(menulist)
    else:
        return print(menulist)

def addmenu(menulist):
    addmenu = input('추가할 식사 메뉴를 입력하세요: ')
    menulist.append(addmenu)
    return print(menulist)

def randommenu(menulist):
    n = random.randint(0, len(menulist)-1)
    return print('오늘 식사는 *', menulist[n], '* 어때요?')

def choicemenu(menulist):
    while True:
        print('(1)현재 메뉴 보기, (2)메뉴 추가, (3)무작위 메뉴 선택, (9)종료')
        choice = int(input('번호를 선택하세요: '))

        if choice == 1:
            showmenu(menulist)
            continue
        elif choice == 2:
            addmenu(menulist)
            continue
        elif choice == 3:
            randommenu(menulist)
            continue
        elif choice == 9:
            break
        else:
            print('잘못 입력하셨습니다.')
            continue