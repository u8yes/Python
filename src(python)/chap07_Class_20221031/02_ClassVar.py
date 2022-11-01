class ClassVar: # static 과 같다. # 생성자가 쓰지 않아도 정상 구동됨. # 클래스 변수, 클래스 메서드
    # 전역변수로 사용 가능함.
    # static은 호출하면 할당했다가 끝나면 할당된 것을 삭제함.
    text_list = []          # 클래스 변수

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == '__main__':
    ClassVar.text_list.append('a')
    print(ClassVar.text_list)

    x = ClassVar()
    x.add('b')
    x.print_list()

    print(ClassVar.text_list)

    y = ClassVar()
    y.add('c')
    y.print_list()

    print(ClassVar.text_list)