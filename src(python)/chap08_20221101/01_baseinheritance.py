class Base: # 부모 클래스 # 상위 클래스
    def __init__(self):
        print(self) # 16진수 # 인스턴스 생성 요청할 때 시작 주소값을 알려줌
        # <__main__.Base object at 0x00000199CC224588>

        self.message = "Heaven World"

    def print_message(self):
        print(self.message)

class Derived(Base): # 상속의 관계 정의 해줌. # 자식 클래스 # 하위 클래스
    pass

if __name__ == '__main__':
    base = Base()
    base.print_message() # <__main__.Base object at 0x000001C086D24608>

    derived = Derived() # 부모를 상속받은 자식의 메서드 # 시작 주소값이 저장돼있기 때문에 부모로 바로 실행 가능
    derived.print_message()    # <__main__.Derived object at 0x000001C086D24648>

    