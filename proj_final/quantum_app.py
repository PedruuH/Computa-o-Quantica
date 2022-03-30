from cv2 import Algorithm
import matplotlib.pyplot as plt
import qiskit as qk
import qiskit.aqua.algorithms as qkal
import qiskit.aqua.components.oracles as LEO
from qiskit.tools.visualization import plot_histogram
from apitoken import apitoken 

expression = '((Pedro & Fabio) | (Carlos & Alex)) & ~(Fabio & Alex)'
algorith = qkal.Grover(LEO.LogicalExpressionOracle(expression))
                  
simulator = qk.Aer.get_backend('qasm_simulator')
result = algorith.run(simulator)
plot_histogram(result['measurement'])
plt.show()