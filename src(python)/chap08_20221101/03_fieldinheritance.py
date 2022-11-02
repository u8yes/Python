# 데이터 속성(field) 상속

"""
class A:
    def __init__(self): # '__init__'는 필드값을 초기화하라고 정의해준 것.
        print("A.__init()__() 생성자 호출")
        self.message = "Heavenly"

class B(A):
    def __init__(self):
        print("B.__init__() 생성자 호출")

if __name__ == '__main__':
    obj = B() # B를 호출하면서 A의 생성자를 호출하면 필드를 초기화할 의무를 가지고 있다.(상속)

    print(obj.message) # AttributeError: 'B' object has no attribute 'message'

"""

class A:
    def __init__(self): # '__init__'는 필드값을 초기화하라고 정의해준 것.
        print("A.__init()__() 생성자 호출")
        self.message = "Heavenly"

class B(A):
    def __init__(self):
        A.__init__((self))                  # 생성자 호출을 명시적으로 표현.
        print("B.__init__() 생성자 호출")

if __name__ == '__main__':
    obj = B() # B를 호출하면서 A의 생성자를 호출하면 필드를 초기화할 의무를 가지고 있다.(상속)

    print(obj.message)