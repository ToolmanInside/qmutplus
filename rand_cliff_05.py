from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
num_qubits = 5

def rand_cliff_05(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)

    qc.s(0)
    qc.h(0)
    qc.s(0)
    qc.s(1)
    qc.s(2)
    qc.s(4)
    qc.swap(3,0)
    qc.cx(3,4)
    qc.cx(2,1)
    qc.cx(1,3)
    qc.cx(3,2)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.s(2)
    qc.cx(0,4)
    qc.cx(2,1)
    qc.cx(1,0)
    qc.cx(0,2)
    qc.s(1)
    qc.h(1)
    qc.h(2)
    qc.swap(2,1)
    qc.cx(2,1)
    qc.h(1)
    qc.cx(1,2)
    qc.h(1)
    qc.s(1)
    qc.swap(4,1)
    qc.cx(4,1)
    qc.s(1)
    qc.y(0)
    qc.y(1)
    qc.y(2)
    qc.y(3)
    qc.z(4)

    for i in range(num_qubits):
        qc.measure(i, i)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 100000).result().get_counts(qc)
    return job