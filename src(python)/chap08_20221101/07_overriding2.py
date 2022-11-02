class Car:
    def ride(self):
        print("Run")

class FlyingCar(Car):
    def ride(self):
        super().ride()
        # 부모의 생성자를 호출할 때는 super() 괄호를 붙어줘야한다. super(x) / super()(o)
        print("FLY")

if __name__ == "__main__":
    # car = Car()
    # car.ride()

    my_car = FlyingCar()
    my_car.ride()

