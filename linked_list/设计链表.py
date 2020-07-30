class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    # 链表的索引是从0开始的！

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        if self.isEmpty():
            return -1
        pos = self.head
        while index > 0 and pos.next:
            pos = pos.next
            index -= 1
        if index > 0:
            return -1
        return pos.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.isEmpty():
            self.head = Node(val)
            return
        pos = self.head
        while pos and pos.next:
            pos = pos.next
        pos.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            return
        node = Node(val)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        if self.isEmpty():
            return
        pos = self.head
        while index > 1 and pos.next:
            index -= 1
            pos = pos.next
        if pos:
            temp = pos.next
            pos.next = node
            node.next = temp

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
        if self.isEmpty():
            return
        if index == 0:
            self.head = self.head.next
            return
        pos = self.head
        while pos and index > 1:
            index -= 1
            pos = pos.next
        if not pos or not pos.next:
            return
        pos.next = pos.next.next

    def isEmpty(self):
        return not self.head


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(7)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtIndex(3, 0)
    obj.deleteAtIndex(2)
    obj.addAtHead(6)
    obj.addAtTail(4)
    print(obj.get(4))
    obj.addAtHead(4)
    obj.addAtIndex(5, 0)
    obj.addAtHead(6)

