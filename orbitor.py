from cmath import *
import Anchor as a
import os


class orbitor:

    def __init__(self, mass, dist, anchor):
        if not type(anchor) == a.Anch:
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

    # assume satellite is sphere
    def getAngMom(self):
        am = 0.667 * self.mass * self.dist * self.dist * self.getAngVel()

        return am

    def getOrbPeriod(self):
        full = 2 * pi * self.dist
        op = full/self.getVel()

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

    #def printInfo(self):







    
