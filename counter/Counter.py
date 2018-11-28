class Counter:
    def __init__(self, initial):
        self.__count = initial

    def increment(self):
        self.__count += 1
        return self.__count

    def decrement(self):
        self.__count -= 1
        return self.__count
