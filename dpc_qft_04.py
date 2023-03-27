from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
from numpy import pi
num_qubits = 4

def qft_04(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)

    qc.h(0)
    qc.measure(0,0)
    qc.p(pi/2,1).c_if(1)
    qc.p(pi/4,2).c_if(1)
    qc.p(pi/8,3).c_if(1)
    qc.h(1)
    qc.measure(1,1)
    qc.p(pi/2,2).c_if(1)
    qc.p(pi/4,3).c_if(1)
    qc.h(2)
    qc.measure(2,2)
    qc.p(pi/2,3).c_if(1)
    qc.h(3)
    qc.measure(3,3)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 100000).result().get_counts(qc)
    return job