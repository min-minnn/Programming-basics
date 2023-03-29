#섭씨 온도를 입력 받아, 화씨 온도로 변환해 주는 프로그램

def F_temp(c): #화씨 온도로 변환해 주는 함수
    return float(c) * (9/5) + 32 #섭씨 온도를 화씨 온도로 변환하는 공식

temp = input('섭씨 온도(℃)를 입력하세요. > ')
f = F_temp(temp)
print(f, '℉')
