def generator():
    yield 0
    yield 1
    yield 2
    yield 3

iterator = generator()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) # error

################################################################

def yourRange(start, end):
    current = start

    while current < end:
        yield current
        current += 1

if __name__ == '__main__':
    print("============================")
    for i in yourRange(0, 4):
        print(i)

