class SM:
    startState = None

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
    startState = 0

    def getNextValues(self, state, inp):
        if (state == 0 and inp == 'a'):
            return (1, True)
        elif (state == 1 and inp == 'b'):
            return (2, True)
        elif (state == 2 and inp == 'c'):
            return (0, True)
        else:
            return (state, False)

class UpDown(SM):
    startState = 0

    def getNextState(self, state, inp):
        if (inp == 'u'):
            return state + 1
        elif (inp == 'd'):
            return state - 1
        else:
            return state

class R(SM): # DELAY MACHINE
    def __init__(self, initial):
        self.startState  = initial

    def getNextValues(self, state, inp):
        return (inp, state)

class Average(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (inp, (state + inp) / 2.0)

class SumLast3(SM):
    startState = (0, 0)

    def getNextValues(self, state, inp):
        (previousPreviousInput, previousInput) = state
        newState = (previousInput, inp)
        output = previousPreviousInput + previousInput + inp
        return (newState, output)

class Selector(SM):
    def __init__(self, pickAtIndex):
        self.pickAtIndex = pickAtIndex

    def getNextState(self, state, inp):
        return inp[self.pickAtIndex]

class SimpleParkingGate(SM):
    startState = 'waiting'

    def generateOutput(self, state):
        if state == 'lowering':
            return 'lower'
        elif state == 'raising':
            return 'raise'
        else:
            return 'nop'

    def getNextValues(self, state, inp):
        (gatePosition, carAtGate, carExited) = inp

        if state == 'waiting' and carAtGate:
            nextState = 'raising'
        elif state == 'raising' and gatePosition == 'top':
            nextState = 'top'
        elif state == 'top' and carExited:
            nextState = 'lowering'
        elif state == 'lowering' and gatePosition == 'bottom':
            nextState = 'waiting'
        else:
            nextState = state

        return (nextState, self.generateOutput(nextState))
