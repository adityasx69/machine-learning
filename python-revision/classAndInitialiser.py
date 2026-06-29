class Car:
    def __init__(self,color: str, horsePower: int):
        self.color = color
        self.horsePower = horsePower
        
volvo: Car = Car('Red',120)
print(volvo.color)
print(volvo.horsePower)

bmw: Car = Car('Blue',600)
print(bmw.color)
print(bmw.horsePower)