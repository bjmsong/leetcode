"""
using linked list to implement bag structure
"""


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Bag():

    def __init__(self):
        self.first = None
        self.n = 0

    def add(self, item):
        if not self.first:
            self.first = Node(item)
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

    def __len__(self):
        return self.n

    def __iter__(self):
        cur = self.first
        while cur.next:
            yield cur.data
            cur = cur.next


if __name__ == '__main__':
    bag = Bag()
    bag.add(1)
    bag.add(3)
    bag.add(5)
    print(len(bag))
    for i in bag:
        print(i)
