import random
from settings import *

class Tiger:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.mod = "Выследить добычу"
    def update_pozition(self, hares):
        if self.mod == "Выследить добычу":
            print("Тигр выслеживает добычу!")
            self.x += random.randint(-1,1)
            self.y += random.randint(-1,1)
            self.x = max(0, min(4,self.x))
            self.y = max(0, min(4,self.y))
            for hare in hares:
                if self.is_near_hare(hare):
                    self.mod = "Атаковать добычу!"
        elif self.mod =="Атаковать добычу!":
            print("Тигр атакует добычу!")
            if random.random() < 0.5:
                print("Заяц повержен!")
                for hare in hares:
                    if self.is_near_hare(hare):
                        hare.change_condition()

            else:
                print("Заяц убежал!")
            self.mod = "Бежать домой"


        elif self.mod == "Бежать домой":
            print("Тигр бежит домой.")
            self.x = 0
            self.y = 0
    def is_near_hare(self, hare):
        return abs(self.x -hare.x) <= 1 and abs(self.y - hare.y) <= 1

class Hare:
    def __init__(self):
        self.x = random.randint(1, 4)
        self.y = random.randint(1,4)
        self.mod = False
    def change_condition(self):
        self.mod = True


class Field:
    def __init__(self,  tiger, hares):
        self.wides = WIDES
        self.heights = HEIGTS
        self.tiger = tiger
        self.hares = hares



    def field_display(self):
        f= []
        for i in range(5):
            row = []
            for j in range(5):
                row.append('.')
            f.append(row)
        f[self.tiger.y][self.tiger.x] = "T"
        for hare in self.hares:
            if  not hare.mod:
                f[hare.y][hare.x] = "Z"
            else:
                f[hare.y][hare.x] = "X"
        for row in f:
            print(*row)


class Game:
    def __init__(self):
        self.tiger = Tiger()
        self.hares = []
        self.__add_hares()
        self.field = Field(self.tiger, self.hares)

        self.run()

    def __add_hares(self):
        for i in range(2):
            while True:
                hare = Hare()
                if hare.y == 1 and hare.x == 1:
                    continue
                flag = True
                for hare2 in self.hares:
                    if hare2.x == hare.x and hare2.y == hare.y:
                        flag = False
                if flag:
                    self.hares.append(hare)
                    break

    def run(self):
        while True:
            self.field.field_display()
            self.tiger.update_pozition(self.hares)
            print()
            if self.tiger.mod ==  "Бежать домой":
                self.tiger.x = 0
                self.tiger.y = 0
                break
        self.field.field_display()


if __name__ == '__main__':
    Game()