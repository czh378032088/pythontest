
"""Module that contains the Normalization class."""

import numpy as np


class NormalizationClass(object):
    minValue = 0
    maxValue = 1
    def __init__(self):
        pass

    def recvalue111(self,b):
        b = np.dot(b,( self.maxValue - self.minValue)) + self.minValue
        return b    

    def norma(self,a):
        self.minValue = np.min(a)
        self.maxValue = np.max(a)
        if self.minValue == self.maxValue:
            if self.minValue != 0:
                a = a / self.minValue
        else:
            a = (a - self.minValue) / (self.maxValue - self.minValue)
        return a




