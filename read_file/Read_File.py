"""
'범내려온다.txt' 파일 읽어들인 후 모든 단어들의 개수 세어서 단어와 등장 횟수 딕셔너리로 저장
단어가 노래 가사에 4번 이상 등장한 경우만 출력
"""
file = open('범내려온다.txt', "r")
text = file.read()
wordList = text.split()

wordCount = {}

for word in wordList:
    wordCount[word] = wordCount.get(word, 0) + 1
    keys = wordCount.keys()

for word in keys:
    if wordCount[word]>=4:
        print(word + ':' + str(wordCount[word])+",",end=" ")