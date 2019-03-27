class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animals):
    def __init__(self, name, age, legs):
        super().__init__(name, age)
        self.legs = legs

    def produce_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished \
                sound! Bau Bau."

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, \
                 Number Of Legs: {self.legs}"


class Cat(Animals):
    def __init__(self, name, age, intelligence):
        super().__init__(name, age)
        self.intelligence = intelligence

    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! \
                Myau Myau."

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence}"


class Snake(Animals):
    def __init__(self, name, age, cruelty):
        super().__init__(name, age)
        self.cruelty = cruelty

    def produce_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated \
                sound! Honey, I'm home."

    def __str__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}"


data = input()
animal_storage = {}
animal_talk = []

animal_dogs = []
animal_cats = []
animal_snake = []

while data != "I'm your Huckleberry":
    data = data.split()

    if len(data) == 4:
        animal = data[0]

        if animal == 'Dog':
            curr_animal = Dog(data[1], data[2], data[3])
            animal_dogs.append(str(curr_animal))
        elif animal == 'Cat':
            curr_animal = Cat(data[1], data[2], data[3])
            animal_cats.append(str(curr_animal))
        else:
            curr_animal = Snake(data[1], data[2], data[3])
            animal_snake.append(str(curr_animal))

        animal_storage[curr_animal.name] = curr_animal

    else:
        animal_talk.append(animal_storage[data[1]].produce_sound())

    data = input()


def loop_animals(lst):
    for x in lst:
        print(x)

loop_animals(animal_talk)
loop_animals(animal_dogs)
loop_animals(animal_cats)
loop_animals(animal_snake)
