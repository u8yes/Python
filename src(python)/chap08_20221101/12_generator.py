

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
#print(iterator.__next__()) # error