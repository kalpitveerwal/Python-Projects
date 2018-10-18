import inc
import sys
import numpy as np
if sys.argv[3] == "0" :
    for line in sys.argv[1]:
        inp = np.loadtxt(sys.argv[1],delimiter=",")
        np.savetxt(sys.argv[2],inc.ang_to_vec(inp),delimiter=",")
if sys.argv[3] == "1" :
    for line in sys.argv[1]:	
        inp = np.loadtxt(sys.argv[1],delimiter=",")
        np.savetxt(sys.argv[2],inc.vec_to_ang(inp),delimiter=",")
