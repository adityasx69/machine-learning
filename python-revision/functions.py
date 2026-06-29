from datetime import datetime

def showDate() -> None:
    print("This is the current date and time")
    print(datetime.now())
    
showDate()
showDate()

def greet(name: str) -> None:
    print(f'Hello {name}!')
    

greet('A')
greet('B')

def addFloat(a: float,b: float)-> float:
    return a+b

print(addFloat(1,2))