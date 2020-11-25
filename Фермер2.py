class Animal:
    def __init__(self, name, animal, voice, weight=0, milk=0, hair=0, eggs=0):
        self.name = name
        self.animal = animal
        self.voice = voice
        self.weight = weight
        self.milk = milk
        self.hair = hair
        self.eggs = eggs

    def eat(self, food):
        self.weight += food
        return self.weight


class Birds(Animal):
    def __init__(self, name, animal, voice, weight, milk, hair, eggs):
        super().__init__(name, animal, voice, weight, milk, hair, eggs)

    def geteggs(self, get):
        self.eggs -= get

    def voice(self):
        print(self.voice)


class Hoofs(Animal):
    def __init__(self, name, animal, voice, weight, milk, hair):
        super().__init__(name, animal, voice, weight, milk, hair)

    def tomilk(self, milkk):
        if (self.animal == 'Корова') or (self.animal == 'Коза'):
            self.milk -= milkk
        else:
            return 'Не доится'

    def cut(self, long):
        if self.animal == 'Овца':
            self.hair -= long
        else:
            return 'Не стрижется'

    def voice1(self):
        return self.voice


duck = Birds('Кряква', 'Утка', 'Крякря', 3, 0, 0, 4)
goose1 = Birds('Серый', 'Гусь', 'Гага', 5, 0, 0, 4)
goose2 = Birds('Белый', 'Гусь', 'Гага', 6, 0, 0, 4)
hen1 = Birds('Ко-Ко', 'Курица', 'Коко', 3, 0, 0, 4)
hen2 = Birds('Кукареку', 'Курица', 'Коко', 4, 0, 0, 4)
cow = Hoofs('Манька', 'Корова', 'Муму', 100, 6, 0)
goat1 = Hoofs('Рога', 'Коза', 'Мее', 20, 6, 0)
goat2 = Hoofs('Копыта', 'Коза', 'Мее', 32, 6, 0)
sheep1 = Hoofs('Барашек', 'Овца', 'Бее', 45, 0, 2)
sheep2 = Hoofs('Кудрявый', 'Овца', 'Бее', 34, 0, 4)

birds_list = [duck, goose1, goose2, hen1, hen2]
for bird in birds_list:
    print(f'{bird} голос {bird.voice}')
    print(f'{bird} кушает {bird.eat(1)}')
    print(f'осталось собрать {bird.geteggs(2)} яиц')

animal_list = [cow, goat1, goat2, sheep1, sheep2]
for animal in animal_list:
    print(f'Молоко {animal.tomilk(2)}')
    print(f'Шерсть {animal.cut(1)}')
    print(f'{animal} голос {animal.voice1()}')
