class Car: # DB 데이터를 관리하는 자바의 V0같은 역할을 하는 클래스
    def __init__(self): # 생성자를 정의함. # self는 시작 주소값을 가지고 있다.
        self.color = 0xFF0000 # 필드 선언 # self는 생략불가능(필드라는 표시의 의도) # 차량 색상(빨간색)
        # 생성자는 초기화를 해줌
        self.wheel_size = 16 # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량

    def forward(self):          # 전진
        pass                    # 기능은 보류(pass)

    def backward(self):         # 후진
        pass

    def turn_left(self):        # 좌회전
        pass

    def turn_right(self):       # 우회전
        pass

if __name__ == '__main__':
    my_car = Car()           # new 메모리 할당하는 것과 같음 # 1)자료형 찾고 크기 계산해서 메모리 할당
    # 2)self 키워드에 주소값 저장 # 3)생성자 호출 # 4)주소값을 리턴해줌 # my_car. 으로 접근할 수 있게 만들어줌.
