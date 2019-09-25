#Sept 25#

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":

    node = Node('root')
    print(node)


    #node = Node('root', Node('left', Node('left.left')), Node('right'))
    #assert deserialize(serialize(node)).left.left.val == 'left.left'    