from basic_state_machines import *

class Switch(SM):
    def __init__(self, condition, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.condition = condition
        self.startState = (sm1.startState, sm2.startState)

    def start(self):
        self.m1.start()
        self.m2.start()
        self.state = self.startState
        return self

    def getNextValues(self, state, inp):
        (s1, s2) = state
        if(self.condition(inp)):
            (ns1, o) = self.m1.getNextValues(s1, inp)
            return ((ns1, s2), o)
        else:
            (ns2, o) = self.m2.getNextValues(s2, inp)
            return ((s1, ns2), o)

class Multiplex(Switch):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ns1, o1) = self.m1.getNextValues(s1, inp)
        (ns2, o2) = self.m2.getNextValues(s2, inp)

        if(self.condition(inp)):
            return ((ns1, ns2), o1)
        else:
            return ((ns1, ns2), o2)

m1 = Switch(lambda inp: inp > 100,
        Accumulator(0),
        Accumulator(0))

m2 = Multiplex(lambda inp: inp > 100,
        Accumulator(0),
        Accumulator(0))

conditionalsInput = [2, 3, 4, 200, 300, 400, 1, 2, 3]
#import pudb; pu.db
print 'switch: ', m1.start().transduce(conditionalsInput)
print 'multiplex: ', m2.start().transduce(conditionalsInput)
