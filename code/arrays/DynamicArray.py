import sys
import math
from array import array


class DynamicArray:
    def __init__(self, n: int) -> None:
        self.arr: array[int] = array("i", [0])
        self.__current_index: int = 0
        self.__current_capacity: int = 16
        if n < 0:
            sys.exit("Array cannot be initialized as less than 0")
        elif n <= 16:
            self.arr = array("i", [0] * n)
        else:
            array_size: int = 2 ** math.ceil(math.log2(n))
            self.arr = array("i", [0] * array_size)
            self.__current_capacity = array_size

    def size(self) -> int:
        return self.__current_index

    def capacity(self) -> int:
        return self.__current_capacity

    def isempty(self) -> bool:
        return bool(self.__current_index)

    def at(self, index: int) -> int:
        if index < 0 or index > self.__current_index:
            sys.exit("Array index out of bounds")
        return self.arr[index]

    def push(self, item: int) -> None:
        self.__resize()
        self.__current_index += 1
        self.arr[self.__current_index] = item

    def insert(self, index: int, item: int) -> None:
        self.__resize()
        self.__current_index += 1
        for i in range(len(self.arr) - 1, index + 1, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = item

    def prepend(self, item: int) -> None:
        self.__resize()
        self.__current_index += 1
        for i in range(len(self.arr) - 1, 1, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[0] = item

    def pop(self) -> int:
        self.__current_index -= 1
        return self.arr[self.__current_index]

    def delete(self, index: int) -> None:
        for i in range(index, len(self.arr)):
            self.arr[i] = self.arr[i + 1]
        self.__current_index -= 1
        self.__resize()

    def remove(self, item: int) -> None:
        for i in range(self.__current_index):
            if self.arr[i] == item:
                self.delete(i)

    def find(self, item: int) -> int:
        for i in range(self.__current_index):
            if self.arr[i] == item:
                return i
        return -1

    def __resize(self) -> None:
        new_size: int
        new_arr: array[int]
        if self.__current_index + 1 >= self.__current_capacity:
            new_size = self.__current_capacity * 2
            new_arr = array("i", [0] * new_size)
            for i in range(len(self.arr)):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.__current_capacity = new_size
        # Handle case of current size being less than 1/4 of max
        elif self.__current_index < self.__current_capacity / 4:
            new_size = self.__current_capacity // 4
            new_arr = array("i", [0] * new_size)
            for i in range(new_size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.__current_capacity = new_size
