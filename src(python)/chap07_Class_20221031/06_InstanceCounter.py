class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def print_instance_count(cls): # self는 new로써 만들어지기 때문에 지움
        print(cls.count)




