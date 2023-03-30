#이메일 주소를 입력 받아 아이디 출력하는 프로그램
#모르는 호스트의 이메일 주소일 경우 이메일 호스트부분을 있는 그대로 출력
#잘못된 형식일 경우 오류 메시지 출력되며, 'done' 입력되거나 입력 값이 없으면 종료

while True:
    str = input("이메일을 입력하세요: ")

    if '@' in str:
        email = str.split("@")

        if email[1] == "gmail.com":
            print("*구글 아이디: ", email[0])
        elif email[1] == "daum.net":
            print("*다음 아이디: ", email[0])
        elif email[1] == "naver.com":
            print("*네이버 아이디: ", email[0])
        else:
            print(email[1], "아이디: ", email[0])
    elif str == "done" or str == "":
        print("--Bye")
        break
    else:
        print("잘못된 형식입니다.")
        continue