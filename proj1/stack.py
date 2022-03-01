class Stack:
    __storage = []

    def __init__(self, *arg) -> None:
        self.__storage += list(arg)

    def length(self) -> int:
        return len(self.__storage)

    def pop(self, index=-1):
        if self.length():
            return self.__storage.pop(index)
        else:
            raise Exception('EmptyStack')
    
    def append(self, *arg):
        self.__storage += list(arg)

    def get_top(self):
        return self.__storage[-1]

    def set_top(self, val):
        self.__storage[-1] = val