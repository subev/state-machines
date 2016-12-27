from basic_state_machines import *

k = -1.5
dDesired = 1.0

class WallController(SM):
    def getNextState(self, state, inp):
        return safeMul(k, safeAdd(dDesired, safeMul(-1, inp)))


deltaT = 0.1

class WallWorld(SM):
    startState = 5
    def getNextValues(self, state, inp):
        return (state - deltaT * inp, state)


def coupledMachine(m1, m2):
    return Feedback(Cascade(m1, m2)).start()

wallSim = coupledMachine(WallController(), WallWorld())
print 'wallSim run:', wallSim.run(30)
