class Hoofs:
    def __init__(self, name, animal, weight, voice, milk=0, hair=0):
        self.name = name
        self.animal = animal
        self.weight = weight
        self.milk = milk
        self.hair = hair
        self.voice = voice

    def eat(self, food):
        self.weight += food

    def tomilk(self, milkk):
        if self.animal != 'Овца':
            self.milk -= milkk
        else:
            print('Овцы не доятся')

    def cut(self, long):
        if self.animal == 'Овца':
            self.hair -= long

    def voice1(self):
        if self.animal == 'Корова':
            print('Муму')
        elif self.animal == 'Коза':
            print('Мее')
        elif self.animal == 'Овца':
            print('Бее')


class Birds:
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
        if self.animal == 'Гусь':
            print('Гага')
        elif self.animal == 'Курица':
            print('Коко')
        elif self.animal == 'Утка':
            print('Крякря')


goose1 = Birds('Серый', 'Гусь', 3, 'Гага', 4)
goose2 = Birds('Белый', 'Гусь', 3, 'Гага', 4)
hen1 = Birds('Ко-Ко', 'Курица', 3, 'Коко', 4)
hen2 = Birds('Кукареку', 'Курица', 3, 'Коко', 4)
duck = Birds('Кряква', 'Утка', 3, 'Крякря', 4)
cow = Hoofs('Манька', 'Корова', 100, 'Муму', 4, 0)
goat1 = Hoofs('Рога', 'Коза', 35, 'Мее', 1, 0)
goat2 = Hoofs('Копыта', 'Коза', 25, 'Мее', 2, 0,)
sheep1 = Hoofs('Барашек', 'Овца', 25, 'Бее', 0, 2,)
sheep2 = Hoofs('Кудрявый', 'Овца', 25, 'Бее', 0, 2,)

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
