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
        if index > self.__current_index:
            sys.exit("Array index out of bounds")
        return self.arr[index]

    # def push(self, item: int) -> int:
