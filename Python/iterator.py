class Test:
    def __init__(self, limit):
        self._limit = limit

    def __iter__(self):
        self._x = 10
        return self

    def __next__(self):
        x = self._x

        if x>self._limit:
            raise StopIteration
        
        self._x = x+1

        return x
    

for i in Test(120):
    print(i)

