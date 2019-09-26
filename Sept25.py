#Sept 25#

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    # init empty string
    serialStr = []
    looplst = [node.val, node.left, node.right]
    for i in looplst:
        serialStr.append(i)
    return serialStr


def deserialize(serialStr):
    #for i in serialStr:
    node = Node(serialStr[0],serialStr[1],serialStr[2])
    return node


if __name__ == "__main__":

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    #print(node.val)
    #print(node.left.left.val)
    #print(node.right.val)
    #print(serialize(node))
    #print(deserialize(serialize(node)).left.val)




    #node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'    