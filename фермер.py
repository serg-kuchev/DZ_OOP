class Cow:
    def __init__(self, name, animal, weight, voice, milk=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.milk = milk
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def tomilk(self, milkk):
        self.milk -= milkk

    def voice1(self):
        print('Муму')


class Goat:
    def __init__(self, name, animal, weight, voice, milk=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.milk = milk
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def tomilk(self, milkk):
        self.milk -= milkk

    def voice1(self):
        print('Мее')


class Sheep:
    def __init__(self, name, animal, weight, voice, hair=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.hair = hair
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def cut(self, long):
        if self.animal == 'Овца':
            self.hair -= long

    def voice1(self):
       print('Бее')


class Goose:
    def __init__(self, name, animal, weight, voice, eggs=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.eggs = eggs
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def geteggs(self, get):
        self.eggs -= get

    def voice1(self):
        print('Гага')


class Hen:
    def __init__(self, name, animal, weight, voice, eggs=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.eggs = eggs
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def geteggs(self, get):
        self.eggs -= get

    def voice1(self):
        print('Коко')


class Duck:
    def __init__(self, name, animal, weight, voice, eggs=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.eggs = eggs
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def geteggs(self, get):
        self.eggs -= get

    def voice1(self):
        print('Крякря')


goose1 = Goose('Серый', 'Гусь', 3, 'Гага', 4)
goose2 = Goose('Белый', 'Гусь', 3, 'Гага', 4)
hen1 = Hen('Ко-Ко', 'Курица', 3, 'Коко', 4)
hen2 = Hen('Кукареку', 'Курица', 3, 'Коко', 4)
duck = Duck('Кряква', 'Утка', 3, 'Крякря', 4)
cow = Cow('Манька', 'Корова', 100, 'Муму', 4)
goat1 = Goat('Рога', 'Коза', 35, 'Мее', 1)
goat2 = Goat('Копыта', 'Коза', 25, 'Мее', 2)
sheep1 = Sheep('Барашек', 'Овца', 25, 'Бее', 2)
sheep2 = Sheep('Кудрявый', 'Овца', 25, 'Бее', 2)

animals_dic = {goose1.name: goose1.weight, goose2.name: goose2.weight,
               hen1.name: hen1.weight, hen2.name: hen2.weight,
               duck.name: duck.weight, cow.name: cow.weight,
               goat1.name: goat1.weight, goat2.name: goat2.weight,
               sheep1.name: sheep1.weight, sheep2.name: sheep2.weight
               }
genweight = 0
for animal_weight in animals_dic.values():
    genweight += animal_weight
print(f'Общий вес всех животных {genweight} килограмоов')

maxweight = 0
animal_name = 0
for i, j in animals_dic.items():
    if maxweight < j:
        maxweight = j
        animal_name = i
print(f'{animal_name} самое тяжелое животное')
