# ListFunc.py 생성하고 모듈 import하여 함수 사용하기
import listFunc
scoreList = [1, 2, 3, 4, 5, 6]

listFunc.list_reverse(scoreList)
print('reverse: ', scoreList)

listFunc.list_filter(scoreList, 4)
print('filter: ', scoreList)

listFunc.list_clear(scoreList)
print('clear: ', scoreList)