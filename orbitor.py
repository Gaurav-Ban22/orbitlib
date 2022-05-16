from cmath import *
import Anchor as a
import os


class orbitor:

    def __init__(self, mass, dist, anchor):
        if not type(anchor) == a.Anch:
            raise ValueError("Parameter 'anchor' in orbitor must be of type Anch from Anchor class; please create a new Anch object.")

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

        velocity = round(velocity.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        return velocity

    # assume satellite is sphere
    def getAngMom(self):
        am = 0.667 * self.mass * self.dist * self.dist * self.getAngVel()

        am = round(am.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        return am

    def getOrbPeriod(self):
        full = 2 * pi * self.dist
        op = full/self.getVel()

        op = round(op.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        return op

    def getLength(self):
        roundo = 2 * pi * self.dist

        roundo = round(roundo.real, 10)
        #getting real value because will always result in 0i being passed since complex number
        
        return roundo

    def getAngVel(self):
        final = self.getVel() / self.dist
        #in radians

        final = round(final.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        return final

    def __clearTerm(self):
        command = "clear"
        if os.name in ('nt','dos'):
            command = "cls"
        os.system(command)

    def printTimeTaken(self):
        #can use orbital period but i feel that angular velocity is better
        #in units time
        tt = 2*pi
        ttd = tt/self.getAngVel()

        ttd = round(ttd.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        return ttd








    
