print("Hello")
a = 5
a = 1.5
a = "asd"
a = 'a'
a = True


# comment


def increment(number):
    return number + 1


def apply_operation(start, operation):
    return operation(start)


b = 5
print(apply_operation(b, increment))
assert (6 == increment(5))

# structural
# conditional
if b == 5:
    print("Yay")
else:
    print("Naaaah")

if b == 3:
    print("Yes")
elif b == 5:
    print("nope")
else:
    print("Haha")

numbers = [1, 3, 45, 1828, 11]

counter = 0
while counter < len(numbers):
    print(numbers[counter])
    counter += 1

for number in numbers:
    print(number)


# fp
def decrement(a):
    return a - 1


operations = [increment, decrement]
a = 17

for operation in operations:
    print(operation(a))


class Car:
    def __init__(self, name, top_speed, acceleration):
        self.name = name
        self.top_speed = top_speed
        self._speed = 0
        self.acceleration = 0

    def accelerate(self):
        pass


class ColoredCar(Car):
    def __init__(self, name, top_speed, color, acceleration):
        super().__init__(name, top_speed, acceleration)
        self.color = color

    def accelerate(self):
        if self._speed < self.top_speed - self.acceleration:
            self._speed += self.acceleration
        else:
            self._speed = self.top_speed


class SportsCar(ColoredCar):
    def __init__(self, name, top_speed, color):
        super().__init__(name, top_speed, color, 200)

    def accelerate(self):
        self.accelerate()
        print("Sporty accelaration")



class FamilyCar(ColoredCar):
    def __init__(self, name, top_speed, color):
        super().__init__(name, top_speed, color, 10)

    def accelerate(self):
        self.accelerate()
        print("Family accelaration")

    def carry_children(self):
        pass


# Car("Subaru Impreza", 170)
cars = [
    SportsCar("Ferrari", 500, "red"),
    FamilyCar("Passat", 100, "gray")
]

for car in cars:
    car.accelerate()
    print(car._speed)
    print(car.name)

cars.append(SportsCar("Lamborgini", 400, "black"))
cars.append(FamilyCar("Batmobil", 700, "Bat Black"))
cars.remove(cars[0])
print(cars)

'''
    Homework: Write a shopping list. Shopping list should have positions which can be added and removed. 
    Each position has a category. List should have a method that prints it.
    Some useful articles of mine: https://medium.com/@kacper.roszczyna
'''
