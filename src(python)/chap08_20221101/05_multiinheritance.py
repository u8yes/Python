# 다중 상속 # UML이라는 단어는 상속 모양을 만들 수 있다는 것.

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B,C):
    pass

if __name__ == '__main__':
    obj = D()
    obj.method() # B가 호출됨.

