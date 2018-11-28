class Counter:
    def __init__(self, persistance):
        self.__persistance = persistance
        self.__count = self.__persistance.load()

    def increment(self):
        self.__count += 1
        self.__persistance.persist(self.__count)
        return self.__count

    def decrement(self):
        self.__count -= 1
        self.__persistance.persist(self.__count)
        return self.__count

    def get_count(self):
        return self.__count
