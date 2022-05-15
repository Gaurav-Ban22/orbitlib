from cmath import *
import Anchor
import os


class orbitor:

    def __init__(self, mass, dist, anchor):
        if not type(anchor) == Anchor:
            raise ValueError("Parameter 'anchor' in orbitor must be of type Anchor.")

        self.mass = mass
        #in kilograms
        self.dist = dist
        #in km
        self.anchor = anchor
        #object of Anchor class

    def getGravParamOrbit(self):
        gc = .00000000006674
        gp = gc * (self.anchor.mass + self.mass)
        
        return gp


    def getVel(self):
                
        semi = self.getGravParamOrbit()/self.dist
        velocity = sqrt(semi)

        return velocity

    def getAngMom(self):
        am = self.mass * self.dist * self.getVel()

        return am

    def getOrbPeriod(self):
        fullRev = 2 * pi
        rCubed = self.dist ** 3
        op = fullRev * sqrt(rCubed/self.getGravParamOrbit())

        return op

    def getLength(self):
        round = 2 * pi * self.dist
        
        return round

    def getAngVel(self):
        final = self.getVel() / self.dist
        #in radians

        return final

    def __clearTerm(self):
        command = "clear"
        if os.name in ('nt','dos'):
            command = "cls"
        os.system(command)

    







    
