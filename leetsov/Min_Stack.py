class MinStack:
    # @param x, an integer
    # @return an integer

    def __init__(self):
        self._stack = [];
        self._min = []

    def push(self, x):
        if self._min == [] or x <= self._min[-1] :
            self._min.append(x)
        self._stack.append(x)


    # @return nothing
    def pop(self):
        if self._stack[-1] == self._min[-1]:
            self._min.pop()
        self._stack.pop()


    # @return an integer
    def top(self):
        return self._stack[-1]


    # @return an integer
    def getMin(self):
        return self._min[-1]
