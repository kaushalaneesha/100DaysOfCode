"""
Design a data structure that supports all following operations in average O(1) time.



insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        # Position of the last element
        self.last_elem = -1
        self.arr_hash = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # print("INSERT VAL {}".format(val))
        next_elem = self.last_elem + 1
        if self.arr_hash.get(val) is not None:
            return False
        if next_elem < len(self.arr):
            self.arr[next_elem] = val
        else:
            self.arr.append(val)
        self.last_elem = next_elem
        self.arr_hash[val] = next_elem

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # print("Remove VAL {}".format(val))
        pos = self.arr_hash.get(val)
        if pos is None:
            return False
        if pos != self.last_elem:
            self.arr[pos] = self.arr[self.last_elem]
            self.arr_hash[self.arr[pos]] = pos
        self.last_elem -= 1
        self.arr_hash[val] = None
        # print("last_elem {}".format(self.last_elem))
        # print("arr_hash {}".format(self.arr_hash))
        # print("arr  {}".format(self.arr))
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # print("arr  {}".format(self.arr))
        return self.arr[random.randint(0, self.last_elem)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()