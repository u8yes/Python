# @Decorator

class MyDecorator:
    def __init__(self, f):  # self에 주소값을 넣을 것이다.
        print("initializing MyDecorator...")
        self.func = f # func라는 field 정의

    def __call__(self):
        print(f"Begin:{self.func.__name__}")

        self.func()     # __call__() 메서드가 호출되면 생성자에서 저장해둔 함수(데이터 속성)를 호출
        
        print(f"End:{self.func.__name__}")

if __name__ == "__main__":

    @MyDecorator  # 데코레이터가 __call__(self)가 호출되게 만들어줌.
    def print_hello():
        print("Hello.")

    print_hello()