class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    # default implementation
    def getNextValues(self, state, inp):
        # the method bellow should be implemented by the descendents
        nextState = self.getNextState(state, inp)
        return (nextState, nextState)

    def transduce(self, inputs):
        return [self.step(inp) for inp in inputs]


class Accumulator(SM):
    def __init__(self, initialValue):
        self.startState = initialValue

    def getNextState(self, state, inp):
        # returns the new state and the output
        return (state + inp)

    def run(self, n = 10):
        return self.transduce([None]*n)


class Gain(SM):
    def __init__(self, k):
        self.startState = k

    def getNextState(self, state, inp):
        return inp * self.state

class LanguageAcceptor(SM):
    def __init__(self):
        self.startState = 0

    def getNextValues(self, state, inp):
        if (state == 0 and inp == 'a'):
            return (1, True)
        elif (state == 1 and inp == 'b'):
            return (2, True)
        elif (state == 2 and inp == 'c'):
            return (0, True)
        else:
            return (state, False)

# ---------------------------------------
a = Accumulator(100)
a.start()
print('a', a.step(20))
print('a transduce', a.transduce([1,2,3,4,5]))
print('a', a.step(4))

a2 = Accumulator(50)
a2.start()
print('a2', a2.step(-20))

g = Gain(5)
g.start()
print('Gain transduce', g.transduce([3, 6, 5, 3, 2, 3.1, 4.6, 0.33]))
print('Gain sttep', g.step(4))

language = LanguageAcceptor()
language.start()
print('language acceptor', language.transduce(['a', 'b', 'c', 'c', 'a', 'd', 'a', 'b']));
