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
        gp = gc * (self.anchor.mass)
        
        return gp


    def getVel(self):
                
        velocity = sqrt(self.getGravParamOrbit()/self.dist)

        velocity = round(velocity.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        #something wrong with velocity calculations

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

    def getTimeTaken(self):
        #can use orbital period but i feel that angular velocity is better
        #in units time
        tt = 2*pi
        ttd = tt/self.getAngVel()

        ttd = round(ttd.real, 10)
        #getting real value because will always result in 0i being passed since complex number

        return ttd

    def statPrint(self,time):
        x = 1
        full = 2*pi
        fullo = 360/full
        if type(time) != type(x):
            raise ValueError("Parameter 'time' of statPrint function needs to be of type integer.")
        
        radians = self.getAngVel() * time
        print("Raw Radians, including full revolutions: " + str(round(radians, 10)))
        if radians > full:
            while radians > full:
                radians -= full

        smpl = round(radians/pi, 10)
        y = radians/2*pi

        print("Radians simplified and rounded to 10 significant digits: " + str(round(radians,10)))
        print("Percentage of orbit completed rounded to 1 significant digit: " + str(round(y,1)))

        print("Degrees rounded to 10 significant digits: " + str(round(radians*fullo, 10)))

        dista = self.getVel() * time

        print("Total distance traveled in meters (rounded to 10 significant digits): " + str(round(dista,10)))

        cir = pi * (self.dist * 2)
        
        print("Length of orbit rounded to 10 sigdigits: " + str(round(cir, 10)))

        orb = self.getOrbPeriod()
        if dista > cir:
            while dista > cir:
                dista -= cir

        print("Amount of seconds needed to finish orbit (rounded to 10 significant digits): " + str(self.getOrbPeriod()))









