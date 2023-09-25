from qiskit import qasm3 
from qiskit import *


 
qc=QuantumCircuit(2,2) 

qc.h(0)
qc.cx(0,1)
qc.z(0)


qc.draw(output='mpl')

