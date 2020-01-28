#5. Реализация бинарного дерева. Операции: вставка, поиск, печать дерева


class Node:
    def __init__(self, data_to_set):
        self.data=data_to_set
        self.left=None
        self.right=None


class bynary_tree:
    def __init__(self):
        self.size=0
        self.head=None

    def getHead(self):
        return self.head

    def addNode(self, data, lastnode):
        if(lastnode == None):
            self.head=Node(data)
        elif(lastnode.left == None):
            lastnode.left=Node(data)
        elif(lastnode.right == None):
            lastnode.right = Node(data)
        elif(lastnode.data<data):
            self.addNode(data, lastnode.right)
        else:
            self.addNode(data, lastnode.left)

    def print_tree(self, lastnode):
        if(lastnode==None):
            lastnode=self.getHead()
        if(lastnode.data != None):
            print(lastnode.data)
        if(lastnode.left !=None):
            self.print_tree(lastnode.left)
        if(lastnode.right !=None):
            self.print_tree(lastnode.right)

    def findNode(self, data_to_find, lastnode):
        if (lastnode == None):
            return
        if (lastnode.data == data_to_find):
            print(lastnode.data)
            return
        if (lastnode.left != None):
            self.findNode(data_to_find, lastnode.left)
        if (lastnode.right != None):
            self.findNode(data_to_find, lastnode.right)


bt = bynary_tree()
for i in range(5):
    bt.addNode(i, bt.getHead())
bt.print_tree(bt.getHead())
for i in range(5):
    bt.findNode(i, bt.getHead())

