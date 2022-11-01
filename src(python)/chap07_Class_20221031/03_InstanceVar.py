class InstanceVar:
    def __init__(self):
        self.text_list = []         # 멤버변수(field)

    def add(self, text):            # 멤버 메서드
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == '__main__':
    # InstanceVar.text_list.append('a') # error

    x = InstanceVar()
    x.add('a')
    x.print_list()      # ['a']
    print(x.text_list)  # ['a']

    y = InstanceVar()
    y.add('b')
    y.print_list()      # ['b']


