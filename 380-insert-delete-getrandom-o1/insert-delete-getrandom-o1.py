import random
class RandomizedSet:

    def __init__(self):
        self.randoms = dict()


    def insert(self, val: int) -> bool:
        if val in self.randoms:
            return False
        self.randoms[val] = val

    def remove(self, val: int) -> bool:
        if val in self.randoms:
            del self.randoms[val]
            return True

        return False

    def getRandom(self) -> int:
       return random.choice(list(self.randoms.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()