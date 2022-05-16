import orbitor as o
import Anchor as a

anch = a.Anch(10000)

sat = o.orbitor(5000, 1000, anch)

print(str(sat.getVel()))
print(str(sat.getTimeTaken()))

sat.statPrint(10000)