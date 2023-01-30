# provide a list of imported modules here
import random as rd
import os
import math

def gen_random_numbers(n):
    """
    This function generates "n" random integers within (0, 1000),
    and write these integers into a file. Each line has only one integer.
    It returns the file name.
    """
    i = 0
    while os.path.exists("randomNumbers%s.txt" % i):
        i += 1
    
    file = open("randomNumbers%s.txt" % i, "w")
    for num in range(n):
        file.write(str(rd.randint(0,1000)) + "\n")
    
    filename = file.name
    file.close()
    
    return filename


def mergesort(filename):
    """
    Read into a file name, which has the random integers.
    Use merge sort algorithm to sort these integers.
    Print the sorting result.
    """
    
    def ms(list):
        if len(list) == 1:
            return list
        else:
            center = int(len(list) / 2)
            half1 = ms(list[0:center])
            half2 = ms(list[center:])
            
            h1 = 0
            h2 = 0
            for i in range(len(list)):             
                if h1 == len(half1) or (h2 != len(half2) and half1[h1] > half2[h2]):
                    list[i] = half2[h2]
                    h2 += 1
                else:
                    list[i] = half1[h1]
                    h1 += 1
            return list
                
            
            
    file = open(filename, "r")
    
    numbers = file.readlines()
    for i in range(len(numbers)):
        numbers[i] = eval(numbers[i])
    #print("Numbers read: " + str(numbers))
    print("Numbers sorted: " + str(ms(numbers)))
    
    file.close()
    
    pass


def quicksort(filename):
    """
    Read into a file name, which has the random integers.
    Use quick sort algorithm to sort these integers.
    Print the sorting result.
    """
    def sort(arr):
        if len(arr) <= 1:
            return arr
        half1, half2, center = partition(arr)
        half1 = sort(half1)
        half2 = sort(half2)
        
        return half1 + [center] + half2
    
    def partition(arr):
        less = []
        greater = []
        pivot = arr[int(len(arr) / 2)]
        for element in arr:
            if element < pivot:
                less.append(element)
            elif element > pivot:
                greater.append(element)
        
        
        return (less, greater, pivot)
        
    
    file = open(filename, "r")
    
    numbers = file.readlines()
    for i in range(len(numbers)):
        numbers[i] = eval(numbers[i])
    #print("Numbers read: " + str(numbers))
    print("Numbers sorted: " + str(sort(numbers)))
    
    file.close()
    
    pass

# In this example, value is integer type.
class BinarySearchTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        

    def insert(self, value):
        """
        Insert a new value.
        If this value exists, tell the user.
        If not, insert it.
        """
        if value > self.value:
            if self.right == None:
                self.right = BinarySearchTreeNode(value)
            else:
                return self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTreeNode(value)
            else:
                return self.left.insert(value)
        else:
            return False
            
        return True

    def search(self, value):
        """
        Search a value.
        Tell the user the result.
        """
        
        if self.value == value:
            return True
        else:
            leftResult = False
            rightResult = False
            if self.left != None:
                leftResult = self.left.search(value)
            if self.right != None:
                rightResult = self.left.search(value)
            return leftResult or rightResult
                

    def inorder(self):
        """
        Print the tree starting from this node with in-order traversal
        """
        def ioTraversal(node):
            if node.left != None:
                ioTraversal(node.left)
            print (node.value)
            if node.right != None:
                ioTraversal(node.right)
            pass
        
        print("In-order Traversal:")
        ioTraversal(self)
        pass
            


if __name__ == '__main__':

    # Do not change the following part.

    filename = gen_random_numbers(30)
    mergesort(filename)
    quicksort(filename)

    # Init a binary search tree
    root = BinarySearchTreeNode(34)
    root.insert(23)
    root.insert(56)
    root.insert(90)
    root.insert(28)
    root.insert(10)
    root.insert(7)
    root.insert(25)
    root.insert(7)
    root.search(90)
    root.inorder()

    pass

# Output
# --------------------
# 
# Numbers sorted: [62, 65, 77, 90, 94, 95, 120, 124, 126, 160, 161, 187, 187, 215, 218, 236, 239, 412, 453, 471, 477, 481, 525, 609, 619, 658, 701, 735, 853, 915]
# Numbers sorted: [62, 65, 77, 90, 94, 95, 120, 124, 126, 160, 161, 187, 215, 218, 236, 239, 412, 453, 471, 477, 481, 525, 609, 619, 658, 701, 735, 853, 915]
# In-order Traversal:
# 7
# 10
# 23
# 25
# 28
# 34
# 56
# 90