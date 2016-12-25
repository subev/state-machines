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

    def run(self, n = 10):
        return self.transduce([None] * n)


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

class Delay(SM): # DELAY MACHINE
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

#----------------------------------------
class Cascade(SM):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.startState = (m1.startState, m2.startState)

    def getNextValues(self, state, inp):
        (state1, state2) = state
        (newS1, o1) = self.m1.getNextValues(state1, inp)
        (newS2, o2) = self.m2.getNextValues(state2, o1)
        return ((newS1, newS2), o2)

class Increment(SM):
    def __init__(self, incr):
        self.incr = incr
    def getNextState(self, state, inp):
        return safeAdd(inp, self.incr)

# COMBINING STATE MACHINES
class Parallel(SM):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.startState = (m1.startState, m2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, out1) = self.m1.getNextValues(s1, inp)
        (newS2, out2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (out1, out2))

# Well known Variation of the Parallel class 
class Parallel2(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = splitValue(inp)
        (newS1, out1) = self.m1.getNextValues(s1, i1)
        (newS2, out2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (out1, out2))

# helper function
def splitValue(v):
    if v == 'undefined':
        return ('undefined', 'undefined')
    else:
        return v

def safeAdd(v1, v2):
    if v1 != 'undefined' and v2 != 'undefined':
        return v1 + v2
    else:
        return 'undefined'

def safeMul(v1, v2):
    if v1 != 'undefined' and v2 != 'undefined':
        return v1 * v2
    else:
        return 'undefined'

class ParallelAdd(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        newS1, o1 = self.m1.getNextValues(s1, inp)
        newS2, o2 = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), o1 + o2)


class Feedback(SM):
    def __init__(self, sm):
        self.m = sm
        self.startState = self.m.startState

    def getNextValues(self, state, inp):
        (ingore, o) = self.m.getNextValues(state, 'undefined')
        (newState, ingore) = self.m.getNextValues(state, o)
        return (newState, o)

# make COUNTER machine without direct depending on state

def makeCounter(init, step):
    return Feedback(Cascade(Increment(step), Delay(init)))

class Adder(SM):
    def getNextState(self, state, inp):
        (i1, i2) = splitValue(inp)
        return safeAdd(i1, i2)

def makeFibonaci():
    return Feedback(Cascade(
    Parallel(
        Delay(0),
        Cascade(
            Delay(1),Delay(0)
        )
    ), Adder()))


