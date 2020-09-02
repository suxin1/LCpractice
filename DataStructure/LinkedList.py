"""
设计链表的实现。您可以选择使用单链表或双链表。
    单链表中的节点应该具有两个属性：val 和 next。
    val 是当前节点的值，next 是指向下一个节点的指针/引用。
    如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。
    假设链表中的所有节点都是 0-index 的。
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    """
    双链表
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        if index < self.size / 2:
            cur = self.head
            for i in range(index + 1):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size - index):
                cur = cur.prev

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        if index > self.size:
            return

        new_node = ListNode(val)
        if index <= self.size / 2:
            cur = self.head
            for i in range(index + 1):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size - index):
                cur = cur.prev

        before = cur.prev

        before.next = new_node
        new_node.prev = before

        new_node.next = cur
        cur.prev = new_node
        self.size += 1



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        if index < self.size / 2:
            cur = self.head
            for i in range(index + 1):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size - index):
                cur = cur.prev
        before = cur.prev
        after = cur.next
        before.next = after
        after.prev = before
        self.size -= 1

    def __str__(self):
        s = "[ "
        cur = self.head
        for i in range(self.size):
            cur = cur.next
            s += "{}, ".format(cur.val)
        s += "]"
        return s


ll = LinkedList()
ll.addAtHead(2)
ll.deleteAtIndex(1)
ll.addAtHead(2)
ll.addAtHead(7)
ll.addAtHead(3)
ll.addAtHead(2)
ll.addAtTail(5)
print(ll)
ll.deleteAtIndex(3)
print(ll)