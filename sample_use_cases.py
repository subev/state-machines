from basic_state_machines import *

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

delayInstance = Delay(6)
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

parking = SimpleParkingGate()
parkingInput = [
    ('bottom', True, False),
    ('bottom', True, False),
    ('bottom', True, False),
    ('bottom', True, False),
    ('top', True, False),
    ('top', True, False),
    ('top', True, False),
    ('top', True, False),
    ('top', False, False),
    ('top', False, False),
    ('top', False, False),
    ('top', False, False),
    ('top', False, True),
    ('top', False, True),
    ('top', False, True),
    ('top', False, True),
    ('middle', False, True),
    ('middle', False, True),
    ('middle', False, True),
    ('middle', False, False),
    ('middle', False, False),
    ('middle', False, False),
    ('middle', False, False),
    ('middle', False, False),
    ('middle', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', False, False),
    ('bottom', True, False),
    ('bottom', True, False),
    ('bottom', True, False),
    ('bottom', True, False),
]
print parkingInput
parking.start()
print parking.transduce(parkingInput)

#use cascade machine
cascade = Cascade(Delay(100), Increment(5))
cascade.start()
cascadeInputs = [22, 33, 44, 55, 66]
print 'cascadeInputs', cascadeInputs
print 'cascadeOutputs', cascade.transduce(cascadeInputs)

# use counter, (a feedback machine)
counter = makeCounter(3, 5)
counter.start()
print 'counter output', counter.run()

fib = makeFibonaci()
fib.start();
print fib.run()

