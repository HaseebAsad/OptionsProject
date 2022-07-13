import numpy as np
from scipy.stats import norm as N
import math
from BlackScholesFormulae import Call, Put
import opstrat as op


"""
These strategies are all taken from "Trading strategies involving options", Ch11 - Hull.
"""
"""
First strategy attempt to program is a Bull Spread. The inputs will be the usual for finding an option, but also the other two strikes.
The call with the higher strike price is shorted, whilst the call with the lower strike price is held long.
"""
# An idea is to also create payoff diagrams? Will need classes for this. Can use the opstrat module above.

"""
BULL SPREAD (can create  a bear spread by shorting the lower strike and longing the higher strike)
A bull spread can also be created by
"""

def BullSpread(S0,k1,k2,r,vol,T):
    K1, K2 = k1, k2
    if k2<k1:
        K1, K2 = k2, k1 #this ensures that K2 is always the greater strike price. Probably inefficient, check.
    c1 = Call(S0,K1,r,vol,T) #long a call with the lower strike
    c2 = Call(S0,K2,r,vol,T) #short a call with the higher strike
    cost = c1-c2
    print("This Bull spread strategy consists of going long a call of strike",K1, "at a cost of",c1, \
          "and going short a call of strike",K2,"with return",c2, "for a total cost of", cost)
    return cost

S0 = 40
k1, k2 = 38 , 42
r = 0.1
vol = 0.2
T = 0.5

BullSpread(S0, k1, k2, r, vol, T)

"""
The following is a plot of the above Bull spread
"""

op_1 = {'op_type':'c','strike':k2,'tr_type':'s','op_pr':Call(S0,k2, r, vol, T)}
op_2 = {'op_type':'c','strike':k1,'tr_type':'b','op_pr':Call(S0,k1, r, vol, T)}
op.multi_plotter(spot=S0, op_list=[op_1,op_2])