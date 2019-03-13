#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: html_render
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, started assignment, 03/03/2019
# ----------------------------------------------------------------------- #

'''
The purpose of this assignment is to create a nifty Circle class that will
demonstrate properties and Python's magic methods
'''

from math import pi

##########
# STEP 1 #
##########

class Circle(object):
    '''
    This is a simple class utilzed to represent a circle
    '''

    def __init__(self, radius):
        self.radius = float(radius)

    ##########
    # STEP 2 #
    ##########

    @property
    def diameter(self):
        return self.radius * 2

    ##########
    # STEP 3 #
    ##########

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    ##########
    # STEP 4 #
    ##########

    @property
    def area(self):
        return self.radius ** 2 * pi

    ##########
    # STEP 5 #
    ##########

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    ##########
    # STEP 6 #
    ##########

    def __str__(self):
        return f'Circle with radius: {self.radius:6f}'

    def __repr__(self):
        return f'Circle({self.radius})'

c = Circle(4)
d = eval(repr(c))

print(d)


