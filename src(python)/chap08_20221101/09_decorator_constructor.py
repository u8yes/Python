# 데코레이터 사용 용도(생성자=constructor)

class MyDecorator:
    def __init__(self, f):
        print("initializing MyDecorator...")
        self.func = f # func라는 field 정의

    def __call__(self):
        print(f"Begin:{self.func.__name__}")

if __name__ == "__main__":
    