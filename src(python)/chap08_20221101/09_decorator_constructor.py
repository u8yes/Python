# 데코레이터 사용 용도(생성자=constructor)

class MyDecorator:
    def __init__(self, f):  # self에 주소값을 넣을 것이다.
        print("initializing MyDecorator...")
        self.func = f # func라는 field 정의

    def __call__(self):
        print(f"Begin:{self.func.__name__}")

        self.func()     # __call__() 메서드가 호출되면 생성자에서 저장해둔 함수(데이터 속성)를 호출

        print(f"End:{self.func.__name__}")

def print_hello():
    print("Hello.")

if __name__ == "__main__":
    hello = MyDecorator(print_hello) # f에 print_hello주소값을 저장
            # MyDecorator의 인스턴스가 만들어지며, __init__() 메서드가 호출
            # print_hello 식별자는 앞에서 정의한 함수가 아닌 MyDecorator의 객체.
    hello() # __call__(self) 메서드 덕에 MyDecorator 객체를 호출하듯 사용할 수 있음.