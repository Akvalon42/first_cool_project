import random
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
        elif self.mod =="Атаковать добычу":
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



