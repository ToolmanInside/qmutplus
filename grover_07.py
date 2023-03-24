from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
num_qubits = 7

def grover_07(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)

    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(6)
    qc.ccx(0,1,4)
    qc.ccx(2,4,5)
    qc.ccx(3,5,6)
    qc.ccx(2,4,5)
    qc.ccx(0,1,4)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.x(0)
    qc.x(1)
    qc.x(2)
    qc.x(3)
    qc.h(3)
    qc.ccx(0,1,4)
    qc.ccx(2,4,3)
    qc.ccx(0,1,4)
    qc.h(3)
    qc.x(0)
    qc.x(1)
    qc.x(2)
    qc.x(3)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(6)

    for i in range(num_qubits):
        qc.measure(i, i)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 100000).result().get_counts(qc)
    return job