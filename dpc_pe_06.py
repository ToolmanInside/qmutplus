from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
from numpy import pi
num_qubits = 6

def dpc_pe_06(mqc):
    q = QuantumRegister(num_qubits, 'q')
    c = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)

    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)
    qc.cp(pi/512,4,5)
    qc.cp(pi/256,3,5)
    qc.cp(pi/128,2,5)
    qc.cp(pi/64,1,5)
    qc.cp(pi/32,0,5)
    qc.h(0)
    qc.measure(0,0)
    qc.p(-pi/2,1).c_if(c,1)
    qc.p(-pi/4,2).c_if(c,1)
    qc.p(-pi/8,3).c_if(c,1)
    qc.p(-pi/16,4).c_if(c,1)
    qc.h(1)
    qc.measure(1,0)
    qc.p(-pi/2,2).c_if(c,1)
    qc.p(-pi/4,3).c_if(c,1)
    qc.p(-pi/8,4).c_if(c,1)
    qc.h(2)
    qc.measure(2,0)
    qc.p(-pi/2,3).c_if(c,1)
    qc.p(-pi/4,4).c_if(c,1)
    qc.h(3)
    qc.measure(3,0)
    qc.p(-pi/2,4).c_if(c,1)
    qc.h(4)
    qc.measure(4,0)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 100000).result().get_counts(qc)
    return job