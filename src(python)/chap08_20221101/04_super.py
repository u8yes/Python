class A:
    def __init__(self):
        print("A.__init__()")
        self.message = "Heavenly"

class B(A):
    def __init__(self):
        super().__init__()
        print("B.__init__()")

        print("self.message is " + self.message)

if __name__ == '__main__':
    obj = B()

    print("__main__"+obj.message)


##########################################################################################

class Base:
    def __init__(self):
        print("Base")

class Derived(Base):
    pass
    # def __init__(self):
    #    super().__init__()

print("=============")

d = Derived()