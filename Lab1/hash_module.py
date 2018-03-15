import random


class HashTable:
    """Implementation of Hash table"""
    def __init__(self, capacity=864): #288 possible combinations * 3 = 864 cells
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
        self.random_num = [random.randrange(0, capacity - 1)] * capacity

    def _hash_func(self, value):
        return (ord(value[0])-32) + (ord(value[1])-32) + (ord(value[-1])-32)


    def put_element(self, value):
        key = self._hash_func(value)
        coll_count = 0
        found = False
        if self.table[key] is None:
            self.table[key] = value
            self.size += 1
            found = True
        else:
            coll_count += 1
            i = 0
            while (i < len(self.random_num)) and (not found):
                p = self.random_num[i]
                new_key = (key + p) % self.capacity
                if self.table[new_key] is None:
                    self.table[key] = value
                    self.size += 1
                    found = True
                else:
                    coll_count += 1
                    i += 1
        if found:
            return coll_count
        else:
            return -1

    def find_element(self, value):
        key = self._hash_func(value)
        comp_count = 1
        found = False
        result = -1
        if self.table[key] == value:
            result = key
            found = True
        else:
            i = 0
            while (i < len(self.random_num)) and (not found):
                p = self.random_num[i]
                new_key = (key + p) % self.capacity
                if self.table[new_key] == value:
                    result = new_key
                    found = True
                else:
                    i += 1
                comp_count += 1
        if found:
            return comp_count, result
        else:
            return -1, -1

    def print_table(self):
        print("Current table:")
        print(70 * "-")
        for i, p in enumerate(self.table):
            if not (p is None):
                print ("Key: ", i, "; Value: ", p)
        print(70 * "-")
        print("Current table size: ", self.size)
