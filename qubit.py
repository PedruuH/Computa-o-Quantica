import matplotlib.ticker as ticker
import numpy as np
import matplotlib.pyplot as plt

#video aula 7  33:31

class Qugate:
    @property
    def X(self):
        return np.array[[0,1],[1,0]]
    def Y(self):
        return np.array[[0,-1j],[1j,0]]
    def Z(self):
        return np.array[[1,0],[0,-1]]

class Qubit:
    @property
    def theta(self):
        return 2*np.arccos(self.a)
    @property
    def phi(self):
        return np.arctan2(self.b.imag,self.b.real)
    @property
    def x(self):
        return np.sin(self.theta)*np.cos(self.phi)
    @property
    def y(self):
        return np.sin(self.theta)*np.sin(self.phi)
    @property
    def z(self):
        return np.cos(self.theta)
    def __init__(self):
        self.a = 1.0
        self.b = 0.0+0.0j
       
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
        self.a = np.sqrt(abs(a)**2/aux)
        self.b = np.sqrt(abs(b)**2/aux)*(b/np.abs(b))*(np.abs(a)/a)
        
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
    @staticmethod
    def plot(*args, **kwargs):
        def repel_from_center(x, y, z, m=0.1):
            return x + (-m if x < 0 else m), \
                    y + (-m if y < 0 else m), \
                    z + (-m if z < 0 else m)
        def bloch_sphere():
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            u = np.linspace(0, 2*np.pi, 30)
            v = np.linspace(0, np.pi, 20)
            x = 1 * np.outer(np.cos(u), np.sin(v))
            y = 1 * np.outer(np.sin(u), np.sin(v))
            z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
            ax.plot_wireframe(x, y, z, color='gray', linestyle=':')
            ax.plot3D([-1, 1], [0, 0], [0, 0], color='k', linestyle='--')
            ax.text(-1.1, 0, 0, '$|-\\rangle$', 'x', horizontalalignment='right', \
                fontweight='bold', fontsize=11)
            ax.text(1.1, 0, 0, '$|+\\rangle$', 'x', horizontalalignment='left', \
                fontweight='bold', fontsize=11)
            ax.plot3D([0, 0], [-1, 1], [0, 0], color='k', linestyle='--')
            ax.text(0, -1.1, 0, '$|-i\\rangle$', 'y', horizontalalignment='right', \
                fontweight='bold', fontsize=11)
            ax.text(0, 1.1, 0, '$|i\\rangle$', 'y', horizontalalignment='left', \
                fontweight='bold', fontsize=11)
            ax.plot3D([0, 0], [0, 0], [-1, 1], color='k', linestyle='--')
            ax.text(0, 0, -1.1, '$|1\\rangle$', 'x', horizontalalignment='center', \
                fontweight='bold', fontsize=11)
            ax.text(0, 0, 1.1, '$|0\\rangle$', 'x', horizontalalignment='center', \
                fontweight='bold', fontsize=11)
            limits = np.array([getattr(ax, f'get_{axis}lim')() \
                for axis in 'xyz'])
            ax.set_box_aspect(np.ptp(limits, axis = 1))
            ax._axis3don = False
            return ax
        if kwargs.get('title', False):
            title = kwargs['title']
        else:
            title = ''
        ax = bloch_sphere()
        for arg in args:
            label, color = '| ', 'r'
            if type(arg) == tuple:
                if len(arg) == 3: color = arg[2]
                label = '$|' + arg[1] + '\\rangle$'
                arg = arg[0]
            ax.quiver(0, 0, 0, arg.x, arg.y, arg.z, color=color)
            ax.text(*repel_from_center(arg.x, arg.y, arg.z), label, 'x', \
                horizontalalignment='center', fontweight='bold', fontsize=11, \
                color=color)
        plt.title(title)
        plt.show()
    
    def measurement(self):
        if random() <= (np.abs(self.a)**2):
            return 0 
        else:
            return 1
    def simulate(self, times=1000):
        data = list (self.measurement() for _ in range(times))
        plt.hist(data, bins=[-0.1,0.1,0.9,1.1], weight = np.ones(len(data)) / len(data))
        plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(1))
        plt.show()

        
if __name__ == "__main__":
    q = Qubit()
    print(q)
    q.set_pa(1/np.sqrt(2), 1/np.sqrt(2))
    print(q.a,q.b)
    Qubit.plot((q, '\Psi', 'b'), title = 'Meu Qubit')
    q.simulate(times=100000)