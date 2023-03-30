"""
Customer 클래스 제작
Customer는 이름, 잔고(입력 없는 경우 기본값은 0) 입력받아 생성

1) 속성에는 name(이름), balance(잔고)
2) Customer 객체 출력하면 형식에 맞게 속성 출력
3) withdraw() method 파라메터로 주어진 amount를 잔고에서 차감하되, balance보다 amount가 큰 경우 잔고 그대로, 최종적으로 balance 반환
4) deposit() method는 주어진 amount를 잔고에 더하여 최종적으로 balance 반환
"""

class Customer: #Customer 클래스 정의
    def __init__(self, name, balance=0): #속성으로 name(이름), balance(잔고) 생성
        self.name = name #이름을 받아서 self의 name에 저장
        self.balance = balance #잔고 balance를 받아서 self의 balance에 저장

    def __repr__(self): 
        return self.name + '(' + str(self.balance) + '원)' 

    def deposit(self, amount):
        self.balance += amount #amount를 받고, 잔고에 더해줌
        return self.balance #최종적으로 balance 반환

    def withdraw(self, amount): 
        if amount > self.balance: #amount가 balance보다 큰 경우
            return self.balance #원래 잔고를 반환
        else: #amount가 balance보다 작은 경우
            self.balance -= amount #amount를 잔고에서 빼줌
            return self.balance #balance에서 amount를 뺀 값을 반환
        
if __name__ == '__main__': #아래 코드는 교재에 참고 프로그램 코드로 주어짐
    c1 = Customer('Bill')
    c2 = Customer('Steve', 50000)
    c3 = Customer('Tim', 100000)
    print(c1, c2, c3)

    c1.deposit(50000)
    c2.deposit(30000)
    c3.withdraw(100000)
    print(c1, c2, c3)

    c2.withdraw( 1000000 )
    print(c1, c2, c3)

    print( c3.withdraw(10000), c2.deposit(10000))
    print(c1, c2, c3)

    