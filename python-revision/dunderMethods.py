class Car:
    def __init__(self,brand: str, horsePower: int):
        self.brand = brand
        self.horsePower = horsePower
        
    def drive(self)->None:
        print(f'{self.brand} is driving')
        
    def getInfo(self)->None:
        print(f'{self.brand} is driving with {self.horsePower} horsepower')
        
    def __str__(self):
        return f'{self.brand},{self.horsePower}hp'
    
    def __add__(self, other: self)->str:
        return f'{self.brand} & {other.brand}'
        
volvo: Car = Car('Volvo',120)
bmw: Car = Car('BMW',140)
print(volvo+bmw)