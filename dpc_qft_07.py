from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
from numpy import pi
num_qubits = 7

def dpc_qft_07(mqc):
    q = QuantumRegister(num_qubits, 'q')
    c = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)

    qc.h(0)
    qc.measure(0,0)
    qc.p(pi/2,1).c_if(c,1)
    qc.p(pi/4,2).c_if(c,1)
    qc.p(pi/8,3).c_if(c,1)
    qc.p(pi/16,4).c_if(c,1)
    qc.p(pi/32,5).c_if(c,1)
    qc.p(pi/64,6).c_if(c,1)
    qc.h(1)
    qc.measure(1,1)
    qc.p(pi/2,2).c_if(c,1)
    qc.p(pi/4,3).c_if(c,1)
    qc.p(pi/8,4).c_if(c,1)
    qc.p(pi/16,5).c_if(c,1)
    qc.p(pi/32,6).c_if(c,1)
    qc.h(2)
    qc.measure(2,2)
    qc.p(pi/2,3).c_if(c,1)
    qc.p(pi/4,4).c_if(c,1)
    qc.p(pi/8,5).c_if(c,1)
    qc.p(pi/16,6).c_if(c,1)
    qc.h(3)
    qc.measure(3,3)
    qc.p(pi/2,4).c_if(c,1)
    qc.p(pi/4,5).c_if(c,1)
    qc.p(pi/8,6).c_if(c,1)
    qc.h(4)
    qc.measure(4,4)
    qc.p(pi/2,5).c_if(c,1)
    qc.p(pi/4,6).c_if(c,1)
    qc.h(5)
    qc.measure(5,5)
    qc.p(pi/2,6).c_if(c,1)
    qc.h(6)
    qc.measure(6,6)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 100000).result().get_counts(qc)
    return job