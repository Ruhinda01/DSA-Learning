#!/usr/bin/python3

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def __repr__(self):
        return repr(self.container)
    
    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self, s):
        for char in s:
            self.push(char)
        
        string = ''
        while not self.isEmpty():
            string += str(self.pop())
        
        return string
    
    def is_balanced(self, s):
        match_dict = {')': '(', '}': '{', ']': '['}
        # match_dict[neg_character] = pos_character

        for char in s:
            if char == '(' or char == '{' or char == '[':
                self.push(char)
            if char == ')' or char == '}' or char == ']':
                if self.isEmpty():
                    return False
                if self.pop() != match_dict[char]:
                    return False
        
        return self.size() == 0
        
        # This is wrong and needed correction
        # count = 0
        # while not self.isEmpty():
        #     char = self.pop()
        #     if char == '(' or char == '{' or char == '[':
        #         count += 1
        #     elif char == ')' or char == '}' or char == ']':
        #         count -= 1
        
        # if count < 0 or count > 0:
        #     return False
        # return count == 0
        


    

if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.peek())

    print(stack)

    stack.pop()
    stack.pop()

    print(stack)
    print(stack.size())

    print(stack.reverse_string("We will conquer COVID-19"))

    print(stack.is_balanced("({a+b})"))
    print(stack.is_balanced("))((a+b}{"))
    print(stack.is_balanced("((a+b))"))
    print(stack.is_balanced("))"))
    print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    

# stack = deque()

# stack.append('1')
# stack.append('2')
# stack.append('3')
# stack.append('4')

# print(stack)

# stack.pop()
# stack.pop()

# print(stack)