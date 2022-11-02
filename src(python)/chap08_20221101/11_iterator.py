# Iterator와 순회 가능한 객체

for i in range(5): # range(0, 5) # 0,1,2,3,4
    print(i)

print("--------------------------------")

iterator = range(3).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# print(iterator.__next__()) # error

class MyRange: # range() 함수와 같은 일을 하는 클래스 정의.
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self): # 한번만 반환해주고 for문에 포함안 됨.
        print("iter")
        return self

    def __next__(self): # 계속 반복해서 for문이 거치게 됨.
        print("next")
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration # raise는 자바에서의 throw기능과 같다, 예외를 던져주는 것.

if __name__ == '__main__':
    print("--------------------------------")
    for i in MyRange(0, 5):
        print(i)