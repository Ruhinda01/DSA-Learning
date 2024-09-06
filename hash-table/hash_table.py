#!/usr/bin/python3

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            # ord() returns ASCII value
            h += ord(char)
        
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            # key already exists and we just update the value
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            # key doesn't exist in the linked list
            self.arr[h].append((key, val))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        # self.arr[h] is the list that contains key-value pairs
        # Remember
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 140
    t['march 6'] = 200
    t['march 8'] = 76
    t['march 9'] = 23
    t['march 17'] = 459
    print(t.arr)
    print(t['march 8'])
    t['march 8'] = 45
    print(t['march 8'])
    print(t.arr)