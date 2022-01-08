class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value ==  temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                     temp.right = new_node
                     return True
                temp = temp.right


    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False

    def BFS(self):
        queue = []
        results = []
        temp = self.root
        queue.append(temp)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)


        traverse(self.root)
        return results


tb = BinaryTree()
tb.insert(42)
tb.insert(21)
tb.insert(76)
tb.insert(18)
tb.insert(27)
tb.insert(56)
print(tb.root.value)
print(tb.contains(21))
print(tb.BFS())
print(tb.dfs_pre_order())
print(tb.dfs_post_order())
print(tb.dfs_in_order())
