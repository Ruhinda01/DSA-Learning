#!/usr/bin/python3

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        # checks if the data is the same as the node (if so, no need to add it)
        if data == self.data:
            return
        
        if data < self.data:
            # check if self.left already has data
            if self.left:
                # recursive call
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # check if self.right already has data ( this case data > self.data)
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # checks the left subtree first and then adds list to the elements list
        if self.left:
            elements += self.left.in_order_traversal() # my original error had self.in_order_traversal() which creates a recursion error.
            # it exceeds the maximum depth for recursion
        
        # appends the node
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        # to find the minimum value in the tree I need to traverse the left subtree
        if self.left:
            return self.left.find_min()
        return self.data
    
    def find_max(self):
        # find the max value in the tree which is normally the last leaf on the right side
        if self.right:
            return self.right.find_max()
        return self.data
    
    def calculate_sum(self):
        # calculates sum of all the elements
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # if the value to be deleted is the root
            if self.left is None and self.right is None:
                return None
            # this means you have right but do not have left child
            if self.left is None:
                return self.right
            # this means you have left but do not have right child
            if self.right is None:
                return self.left
            # if you have both left and right children
            # what about using the maximum value in the left subtree
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
            # find the minimum value in the right subtree
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
        # issue was that i was not returning self yet changes had been made after delete
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    # Should print sorted array: [1,4,9,17,18,23,34]
    print("In-order traversal:", numbers_tree.in_order_traversal())
    
    numbers_tree.delete(4)
    print("After deleting 20:", numbers_tree.in_order_traversal())
    # print(numbers_tree.search(20))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    # print('------------------------------')

    # print(numbers_tree.in_order_traversal())

    # print('------------------------------')

    # print(numbers_tree.pre_order_traversal())

    # print('------------------------------')
    
    # print(numbers_tree.post_order_traversal())
    
