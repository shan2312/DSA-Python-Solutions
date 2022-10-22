import random

class RandomizedSet:

    def __init__(self) -> None:
        self.random_set = set()
        self.random_list = []

    def insert(self, val):
        if val in self.random_set:
            return False

        self.random_set.add(val)
        self.random_list.append(val)
        return True

    def remove(self, val):
        if val not in self.random_set:
            return False

        self.random_set.remove(val)
        self.random_list.remove(val)
        return True

    def getRandom(self):
        random_num = random.choice(self.random_list)
        return random_num

