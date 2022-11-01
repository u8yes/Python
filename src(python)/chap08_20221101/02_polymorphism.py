# 다형성(Polymorphism)
# 상속의 조건하에서 자식의 인스턴스를 생성했을 때 1)자식의 자료형으로 바라볼 수 있고
# 2)부모의 자료형으로도 바라볼 수 있는 것.

class Suite:
    pass

class ArmorSuite:
    def armor(self):
        print("armored")

class IronMan(ArmorSuite):
    pass

def get_armored(suite):
    suite.armor()

if __name__ == '__main__':
    suite = ArmorSuite() # 참조 변수를 통해서 접근을 할 수 있다.
    get_armored(suite)

    iron_main = IronMan()
    get_armored(iron_main)

    # suite = Suite()
    # get_armored(suite) # error # AttributeError: 'Suite' object has no attribute 'armor'

    