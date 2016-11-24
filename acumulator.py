class SM:
    def start(self):
        self.state = self.startState

    def getNextValues(self, state, inp):
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        return [self.step(inp) for inp in inputs]


class Accumulator(SM):
    def __init__(self, initialValue):
        self.startState = initialValue

    def getNextValues(self, state, inp):
        # returns the new state and the output
        return (state + inp, state + inp)

    def run(self, n = 10):
        return self.transduce([None]*n)


class Gain(SM):
    def __init__(self, k):
        self.startState = k

    def getNextValues(self, state, inp):
        return (inp * self.state, inp * self.state)


# ---------------------------------------
a = Accumulator(100)
a.start()
print('a', a.step(20))
print('a transduce', a.transduce([1,2,3,4,5]))
print('a', a.step(4))

a2 = Accumulator(50)
a2.start()
print('b', a2.step(-20))

g = Gain(5)
g.start()
print('Gain transduce', g.transduce([3,6,5,3,2]))
print('Gain sttep', g.step(4))
