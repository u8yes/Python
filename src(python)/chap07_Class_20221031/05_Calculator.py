class Calculator:

    @staticmethod # java의 어노테이션 같이 정의 # @는 데코레이터이라고 부름 # static 정의 데코
    def plus(x1, x2):       # self(자신의 주소값을 만들 때 생김)가 사라짐
        return x1 + x2

    @staticmethod
    def minus(x1, x2):
        return x1 - x2

    @staticmethod
    def multiply(x1, x2):
        return x1 * x2

    @staticmethod
    def divide(x1, x2):
        return x1 / x2

if __name__ == '__main__':
    print(f'{7} + {4} = {Calculator.plus(7,4)}')
    print(f'{7} - {4} = {Calculator.minus(7, 4)}')
    print(f'{7} * {4} = {Calculator.multiply(7, 4)}')
    print(f'{7} / {4} = {Calculator.divide(7, 4)}')
