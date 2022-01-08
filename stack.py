class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.height = 1

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1

    def pull(self):
        if self.height ==0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp


s = Stack(6)
s.push(10)
s.push(8)
s.push(12)
s.pull()
s.pull()
s.print_stack()