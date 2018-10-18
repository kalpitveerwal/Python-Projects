import numpy as np
def ang_to_vec(ang):
        rad = np.radians(ang)
        a1=np.cos(rad)
        a2=np.sin(rad)
        ans=np.insert(a2,np.arange(len(a1)),a1)
        return ans.reshape(ang.shape[0],2)
def vec_to_ang(vec):
    rd=np.arctan2(vec[:,1],vec[:,0])
    ang=np.degrees(rd)
    return ang
