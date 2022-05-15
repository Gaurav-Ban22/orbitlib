from cmath import *


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

    def getGravPara(self):
        gc = .00000000006674
        gp = gc * self.mass
        
        return gp


    def getVel(self):
                
        semi = self.getGravPara()/self.dist
        velocity = sqrt(semi)

        return velocity

    def getAngMom(self):
        am = self.mass * self.dist * self.getVel()

        return am

    def getOrbPeriod(self):
        fullRev = 2 * pi
        rCubed = self.dist ** 3
        op = fullRev * sqrt(rCubed/self.getGravPara())

        return op


    
