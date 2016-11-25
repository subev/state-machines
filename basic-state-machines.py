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

# ---------------------------------------

a = Accumulator(100)
a.start()
print'a', a.step(20)
print'a transduce', a.transduce([1,2,3,4,5])
print'a', a.step(4)

a2 = Accumulator(50)
a2.start()
print'a2', a2.step(-20)

g = Gain(5)
g.start()
gainInputs = [3, 6, 5, 3, 2, 3.1, 4.6, 0.33]
print'Gain inputs:', gainInputs
print'Gain output:', g.transduce(gainInputs)
print'Gain sttep', g.step(4)

language = LanguageAcceptor()
language.start()
acceptorInput = ['a', 'b', 'c', 'c', 'a', 'd', 'a', 'b']
print'language acceptor inputs:', acceptorInput;
print'language acceptor output:', language.transduce(acceptorInput);

ud = UpDown()
ud.start()
updownInput = ['r', 'e', 'u', 'd', 'u', 'u', 'u', 'd']
print'up-down inputs:', updownInput;
print'up-down output:', ud.transduce(updownInput);

delayInstance = R(6)
delayInstance.start()
delayInputs = [4,3,5,5,9,1]
print 'delay inputs:', delayInputs
print 'delay outputs:', delayInstance.transduce(delayInputs)

average = Average()
average.start()
averageInputs = [5,10,15,5,23,44,12,38]
print 'average inputs:', averageInputs
print 'average output:', average.transduce(averageInputs)

prev3 = SumLast3()
prev3.start()
prev3Inputs = [1,4,7,3,5,7,1,2,3]
print 'prev3 inputs:', prev3Inputs
print 'prev3 outputs:', prev3.transduce(prev3Inputs)

selector = Selector(2)
selector.start()
selectorInputs = [[1,2,3], [5,6,7], [7,8,9,8,3]]
print 'selector inputs:', selectorInputs
print 'selector output:', selector.transduce(selectorInputs)
selectorInputs = [(1,2,3), [5,6,7], [7,8,9,8,3]]
print 'selector inputs:', selectorInputs
print 'selector output:', selector.transduce(selectorInputs)
selectorInputs = ((1,2,3), [5,6,7], [7,8,9,8,3])
print 'selector inputs:', selectorInputs
print 'selector output:', selector.transduce(selectorInputs)
