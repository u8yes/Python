# 데이터 속성(field) 상속

class A:
    def __init__(self):
        print("A.__init()__() 생성자 호출")
        self.message = "Heavenly"

class B(A):
    def __init__(self):
        print("B.__init__() 생성자 호출")

if __name__ == '__main__':
    obj = B()

    print(obj.message) # AttributeError: 'B' object has no attribute 'message'