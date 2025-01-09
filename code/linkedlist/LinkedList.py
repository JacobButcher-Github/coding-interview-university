class Node:
    def __init__(self, n: int) -> None:
        self.data: int = n
        self.next: "Node" = None

    def setNext(self, node: "Node") -> None:
        self.next = node


class LinkedList:
    def __init__(self, n: int) -> None:
        self.head: Node = Node(n)
        self.len: int = 1

    def size(self) -> int:
        return self.len

    def empty(self) -> bool:
        if self.len:
            return True
        return False

    def value_at(self, index: int) -> int:
        start: Node = self.head
        for i in range(index):
            if not start.next:
                return -1
            start = start.next
        return start.data

    def push_front(self, value: int) -> None:
        """adds an item to the front of the list"""
        ...

    def pop_front(self) -> int:
        """remove the front item and return its value"""
        ...

    def push_back(self, value: int) -> None:
        """adds an item at the end"""
        ...

    def pop_back(self) -> int:
        """removes end item and returns its value"""
        ...

    def front(self) -> int:
        """get the value of the front item"""
        ...

    def back(self) -> int:
        """get the value of the end item"""
        ...

    def insert(self, index: int, value: int) -> None:
        """insert value at index, so the current item at that index is pointed to by the new item at the index"""
        ...

    def erase(self, index: int) -> None:
        """removes node at given index"""
        ...

    def value_n_from_end(self, n: int) -> int:
        """returns the value of the node at the nth position from the end of the list"""
        ...

    def reverse(self) -> None:
        """reverses the list"""
        ...

    def remove_value(self, value: int) -> None:
        """removes the first item in the list with this value"""
        ...
