# Overriding

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

# ---- 여기까지는 다중상속이 아니다. -----

