#!/usr/bin/python3

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_forward(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr = self.head
        # illustrate the linked list
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next
        print(dllstr)
    
    def print_backward(self):
        if self.head is None:
            print('Linked List is empty')
            return
    
        itr = self.head
        while itr.next:
            itr = itr.next
        
        tail = itr
        dllstr = ''
        while tail:
            dllstr += '-->' + str(tail.data)
            tail = tail.prev
        print(dllstr)
    
    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
        

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_values(["banana","mango","grapes","orange"])
    dll.print_forward()
    dll.print_backward()