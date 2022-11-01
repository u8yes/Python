class HasPrivate:
    def __init__(self):
        self.public1 = "public1"
        self.__private1 = "private1" # '__' 변수 이름앞에 언더바2개를 붙이면 바로 private 특성을 가지게 된다.
        self.__private2_ = "private2"
        self.__public2__ = "public2" # 이름으로 public, private 참고

    def print_from_internal(self):
        print(self.public1)
        print(self.__private1)
        print(self.__private2_)
        print(self.__public2__)

if __name__ == '__main__':
    obj = HasPrivate()
    obj.print_from_internal()

    print("====================")
    print(obj.public1)
    # print(obj.__private1) # error - private 속성이기 때문에
    # print(obj.__private2_) # error - private 속성이기 때문에
    print(obj.__public2__)

