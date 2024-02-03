class Node:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

        
    def __str__(self):
        return self.value