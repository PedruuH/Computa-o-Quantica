import numpy as np
import matplotlib as plt


class Qubit:
    def __init__(self):
        self.theta = 0.0
        self.phi = 0.0
        self.a = 1.0
        self.b = 0.0+0.0j
        self.x = 0
        self.y = 0
        self.z = 1
    def wf(self):
        return np.array([[self.a],[self.b]])
    def set_bs(self,theta,phi):
        if not(0.0 <= theta <= np.pi ):
            theta = np.pi - theta%np.pi
        if not(-np.pi >= phi <= np.pi):
            phi = phi%(2*np.pi) - 2*np.pi
        self.theta = theta
        self.phi = phi
    def set_pa(self,a,b):
        aux = np.abs(a)**2 + np.abs(b)**2
        a = np.sqrt(abs(a)**2/aux)
        b = np.sqrt(abs(b)**2/aux)*(b/np.abs(b))*(np.abs(a)/a)
        
    def __repr__(self):
        return str(self.wf())
    
    def validate(self):
        self.theta = 2*np.arccos(self.a)
        self.phi = np.arctan2(self.b.imag, self.b.real)
        self.x = np.sin(self.theta)*np.cos(self.phi)
        self.y = np.sin(self.theta)*np.sin(self.phi)
        self.z = np.cos(self.theta)
    
    def set_wf(self, colvec):
        a = colvec[0,0]
        b = colvec[1,0]
        self.set_pa(a,b)
        
if __name__ == "__main__":
    q = Qubit()
    print(q)