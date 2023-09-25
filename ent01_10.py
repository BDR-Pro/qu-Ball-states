from qiskit import qasm3 
from qiskit import *


 
qc=QuantumCircuit(2,2) 

qc.h(0)
qc.x(1)
qc.cx(0,1)
qc.z(1)

qc.draw(output='mpl')

