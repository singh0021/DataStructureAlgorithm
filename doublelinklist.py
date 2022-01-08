class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList():

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1

    def print_list(self):
        temp = self.head
        while (temp is not None):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = temp.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head= new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1

    def pop_first(self):
        if self.length == 0:
            return True
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return True

    def get(self, index):
        if self.length < 0 or index >= self.length:
            return None
        temp = self.head
        if index < (self.length)/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp


    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        before = self.get(index -1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        after.prev = new_node
        new_node.next = after
        self.length +=1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length -1:
            self.pop()
        temp = self.get(index)


        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp.value

ld = DoubleLinkedList(5)
ld.append(10)
ld.append(1)

ld.prepend(12)
ld.prepend(24)
ld.print_list()
print("\n")


ld.remove(2)
ld.print_list()