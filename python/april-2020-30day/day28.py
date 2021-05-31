from collections import OrderedDict
from typing import List
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()
        self.all = set()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if not self.unique:
            return -1
        key, value = next(iter(self.unique.items()))
        return key

    def add(self, value: int) -> None:
        # If we've seen this before, then don't bother adding.
        # Remove from unique since it's not unique anymore.
        if value in self.all:
            if value in self.unique:
                del self.unique[value]
        else:
            self.all.add(value)
            self.unique[value] = None


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

s = FirstUnique([7,7,7,7,7,7])
print(s.showFirstUnique())
s.add(7)
s.add(3)
s.add(4)
print(s.showFirstUnique())
s.add(3)
print(s.showFirstUnique())