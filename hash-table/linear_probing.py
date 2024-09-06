#!/usr/bin/python3

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        initial_h = h
        # checks if a slot is empty or occupied
        while self.arr[h] != [] and self.arr[h][0] != key:
            # if the slot is not empty, then we increment the hash value
            h = (h + 1) % self.MAX
            # if we reach the initial hash value, then we raise an exception
            if h == initial_h:
                raise Exception("Hash table is full!")
        
        self.arr[h] = (key, val)  

    def __getitem__(self, key):
        h = self.get_hash(key)
        initial_h = h
        # checks if a slot is empty or occupied
        while self.arr[h] is not None:
            # if the slot is not empty, then we check the key
            if self.arr[h] and self.arr[h][0] == key:
                # if the key is found, then we return the value
                return self.arr[h][1]
            # if the slot is not empty, then we increment the hash value
            h = (h + 1) % self.MAX
            # if we reach the initial hash value, then we break the loop
            if h == initial_h:
                break
        raise Exception("Key not found!")
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        initial_h = h
        while self.arr[h] is not None:
            if self.arr[h] and self.arr[h][0] == key:
                self.arr[h] = []
                return
            h = (h + 1) % self.MAX
            if h == initial_h:
                break
        
        raise Exception("Key not found!")
    
if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 200
    t['march 8'] = 76
    t['march 9'] = 23
    t['march 17'] = 459
    t['march 10'] = 20
    t['march 1'] = 57
    t['april 18'] = 97
    t['april 6'] = 200
    t['may 23'] = 21
    t['may 2'] = 90
    print(t.arr)
    print(t.get_hash('march 9'))
    print(t.get_hash('march 17'))
    print(t.get_hash('march 6'))