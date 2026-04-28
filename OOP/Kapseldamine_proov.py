class Quiz:

    def __init__(self):
        self.__count = 1

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count

if __name__ == '__main__':
    q = Quiz()
    q.increment()
    q.increment()
    q.__count = 5

    print(q.get_count())