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

def override(overriding):
    overriding.method()

if __name__ == '__main__':
    a = A()
    # a.method()

    b = B()
    # b.method()

    c = C()
    # c.method()

    override(a)
    override(b)
    override(c)

    # override("ABC") # .method가 없다고 반응해줌 # AttributeError: 'str' object has no attribute 'method'

