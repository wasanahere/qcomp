# Class for a state
import numpy as np

class State:
    def init(self, a=None, b=None):
        # if a and b are none then initialize to a random valid state
        # if only one is given initliaze the other one using the normalization constraint
        # if a and b are given, then initialize the state
        self = np.array([[a], [b]])

    def normalization_constraint(self):
        pass

zero = State(1, 0)
print(zero)
