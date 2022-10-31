import sys

print(sys.builtin_module_names) # 파이썬 인터프리터 내장 모듈

for path in sys.path:
    print(path)