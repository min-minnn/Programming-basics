"""
식당 메뉴 관리 프로그램을 딕셔너리 이용하여 작성하기
식당의 초기 메뉴는 {'김치찌개': 6000, '된장찌개': 6000, '제육볶음': 8000}
프로그램은 전체 메뉴 보기, 단일 항목의 가격 조회, 메뉴 추가 혹은 수정, 삭제 가능
"""
menu = {'김치찌개': 6000, '된장찌개': 6000, '제육볶음': 8000}

while True:
    print('(1)전체 메뉴 보기, (2)메뉴 가격 보기, (3)메뉴 추가/수정 (4)메뉴 삭제, (9)종료')
    num = int(input('> 번호를 선택하세요: '))

    if num == 1:
        print('* ', menu)
        continue
    elif num == 2:
        choice = input('가격을 확인하고 싶은 메뉴를 입력하세요: ')

        if choice in menu:
            print('* ', choice, '의 가격은 ', menu[choice], '원 입니다.')
            continue
        else:
            print('메뉴에 없습니다. 다시 선택하세요.')
            continue
    elif num == 3:
        newmenu = input('>> 추가할 식사 메뉴를 입력하세요: ')
        newmenuprice = int(input('>> 새로운 식사 메뉴의 가격을 입력하세요: '))
        menu[newmenu] = newmenuprice
        print('* 메뉴 수정 완료')
        continue
    elif num == 4:
        delmenu = input('삭제할 식사 메뉴를 입력하세요: ')
        if delmenu in menu:
            del(menu[delmenu])
            print('* 현재 메뉴에서 ', delmenu, '가 삭제되었습니다.')
            continue
        else:
            print('해당 메뉴가 없습니다.')
    elif num == 9:
        break
    else:
        print('잘못 입력하셨습니다.')
        continue