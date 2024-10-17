#!/usr/bin/python3

import time
import threading
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if len(self.buffer) == 0:
            print('Queue is empty')
            return
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)
    
    def isEmpty(self):
        return len(self.buffer) == 0
    
    def __repr__(self):
        return str(self.buffer)
    
    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    number_queue = Queue()
    number_queue.enqueue("1")

    for _ in range(n):
        front = number_queue.front()
        print("   ",front)
        number_queue.enqueue(front + "0")
        number_queue.enqueue(front + "1")

        number_queue.dequeue()

# food_order_queue = Queue()

# def place_order(orders):
#     if len(orders) == 0:
#         print('No orders to place')
#         return
#     for order in orders:
#         print("Placing order: ", order)
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)
        
    
# def serve_order():
#     time.sleep(1.0)
#     while True:
#         print("Serving order: ", food_order_queue.dequeue())
#         time.sleep(2.0)
    
    


if __name__ == '__main__':

    produce_binary_numbers(10)
    # orders = ['pizza','samosa','pasta','biryani','burger']

    # t1 = threading.Thread(target=place_order, args=(orders,))
    # t2 = threading.Thread(target=serve_order)

    # t1.start()
    # t2.start()

    # q.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15:30',
    #     'price': 123.45
    # })

    # q.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15:31',
    #     'price': 124.97
    # })

    # q.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15:32',
    #     'price': 121.30
    # })

    # q.enqueue({
    #     'company': 'Wall Mart',
    #     'timestamp': '15:33',
    #     'price': 125.65
    # })

    # print(q.buffer)

    # print(q.dequeue())

    # print(q.size())