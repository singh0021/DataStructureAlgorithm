class HashTable:
    def __init__(self, size):

        self.data_map = [None]*size

    def print_table(self):
        for key, value in enumerate(self.data_map):
            print(key, ":", value)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash

    def set_table(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
           for i in range(len(self.data_map[index])):
               if self.data_map[index][i][0] == key:
                   return self.data_map[index][i][1]
        return None

    def get_keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys

HT = HashTable(5)
HT.set_table('mine', 10)
HT.set_table('anubha', 10)
HT.set_table('singh', 10)
HT.set_table('DD', 10)
print(HT.print_table())
print(HT.get('anubha'))
print(HT.get_keys())