class Car:
    def __init__(self,brand: str, horsePower: int):
        self.brand = brand
        self.horsePower = horsePower
        
    def drive(self)->None:
        print(f'{self.brand} is driving')
        
    def getInfo(self)->None:
        print(f'{self.brand} is driving with {self.horsePower} horsepower')
        
volvo: Car = Car('Volvo',120)
volvo.drive()
volvo.getInfo()

bmw: Car = Car('BMW',600)
bmw.drive()
bmw.getInfo()