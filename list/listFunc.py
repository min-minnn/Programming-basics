"""
listFunc.py: 리스트에 적용할 수 있는 다양한 기능을 제공하는 모듈
list_reverse(myList): myList의 원소를 역순으로 바꿔 반환
list_clear(myList): 리스트의 원소를 모두 삭제하고 빈 리스트 반환
list_filter(myList, n): 리스트 원소 중 n보다 작은 원소만 반환
"""

def list_reverse(myList):
    return myList.reverse()

def list_clear(myList):
    return myList.clear()

def list_filter(myList, n):
    for i in myList:
        if i>= n:
            myList.remove(i)