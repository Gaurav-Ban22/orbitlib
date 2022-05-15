import orbitor as o
import Anchor as a

anch = a.Anch(2500)

sat = o.orbitor(1000, 1000, anch)

print(str(sat.getVel()))