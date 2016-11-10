class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    def transduce(self, inputs):
        return [self.step(inp) for inp in inputs]


class Accumulator(SM):
    startState = 0
    def __init__(self, startValue):
        self.startState = startValue

    def getNextValues(self, state, inp):
        # returns the new state and the output
        return (state + inp, state + inp)





c = Accumulator(100)
c.start()
print(c.step(20))
