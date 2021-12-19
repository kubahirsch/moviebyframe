from random import randrange

class Changing:
        random_number = randrange(124)
        score = 0


        def change_random_number(self):
            self.random_number = randrange(124)
            return

        def add_point(self):
            self.score+=1
            return

        def zero_score(self):
            self.score = 0
            return