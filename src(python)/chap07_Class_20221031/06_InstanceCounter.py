class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def print_instance_count(cls): # self는 new로써 만들어지기 때문에 지움
        print(cls.count)

if __name__ == '__main__':
    x = InstanceCounter()
    x.print_instance_count()

    InstanceCounter.print_instance_count()

    y = InstanceCounter()
    y.print_instance_count()

    InstanceCounter.print_instance_count()

    InstanceCounter.count = 10
    InstanceCounter.print_instance_count()
