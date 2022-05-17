import orbitor as o
import Anchor as a

# anch = a.Anch(10000)

# sat = o.orbitor(5000, 1000, anch)

sun = a.Anch(1988920000000000000000000000000)
earth = o.orbitor(5973600000000000000000000,149508058000,sun)

#print(str(sat.getVel()))
#print(str(sat.getTimeTaken()))

#sat.statPrint(10000)
#sat.statPrint(10000000000)
print(str(earth.getAngVel()))
earth.statPrint(31536000)