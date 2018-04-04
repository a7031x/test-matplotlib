from scipy.signal import lti,step2,impulse2
import matplotlib.pyplot as plt
import numpy as np

def continuous():
    k2 = 3
    k1 = 5

    Ds = lti([k2, k1, 0], [1, k2, k1])
    Fs = lti([k2, k1], [1, k2, k1])

    timeFs, stepFs = step2(Fs)
    f, ax = plt.subplots(1, 1, sharex='col', sharey='row')
    ax.plot(timeFs, stepFs, 'b')
    plt.show()


X = [
    -267414,-849729,-972797,-731674,-857230,-2375513,-2131863,-1843964,-1949364,-2016107,-2072753,
-2057888,-1928186,-2048304,-2035917,-2030861,-2034251,-1877662,-1740215,-1910897,-2030785,
-1906154,-2010053,-745431,-1011578,-861927,-755155,-841082,-2009074,-870806,-2019886,-2000770,
-1993168,-1745021,-2061268,-2059142,-1976525,-2043387,-1980734,-2115240,-2086700,-2067485,-2094287,
-1948204,-1871015,-1859875,-1949220,-1925913,-1984551,-1860617,-609256,-837095,-37697,-512846,
-523970,-14012,-1217725,-2224543,-2244236,
-469594,-26778,-2728184,-2704446,-2368748,
-2396297,-2695093,-2431761,-2363982,-2376266,
-2357668,-2577660,-2785666,-2275030,-2763599,
-2736172,-2326798,-2707329,-2250895,-2254920,
-876340,-968872,-868693,-965284,-1133738,-2408320,
-2235177,-2113388,-2225767,-2237005,-2253291,
-2249920,-2232281,-2267364,-2294318,-2384293,
-2288848,-2302481,-2668125,-2263546,-2255746
]

class Integral:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def input(self, v):
        self.v += self.k * v

    def value(self):
        return self.v


def discrete():
    k1 = 0.05
    k2 = 0.3

    k1Int = Integral(k1, 0)
    fsInt = Integral(0.3, X[0])
    Y = []
    for x in X:
        diff = x - fsInt.value()
        k1Int.input(diff)
        delta = k1Int.value() + k2 * diff
        fsInt.input(delta)
        Y.append(fsInt.value())
    timeFs = range(len(X))
    f, ax1 = plt.subplots(1, 1, sharex='col', sharey='row')
    ax2 = ax1.twinx()
    ax1.plot(timeFs, X, 'b')
    ax2.plot(timeFs, Y, 'g')
    plt.show()


discrete()