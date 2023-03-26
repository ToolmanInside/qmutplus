from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
num_qubits = 4

def rand_cliff_04(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)

    qc.h(0)
    qc.h(2)
    qc.s(2)
    qc.s(3)
    qc.h(3)
    qc.swap(1,0)
    qc.cx(1,0)
    qc.cx(3,2)
    qc.cx(2,1)
    qc.cx(1,3)
    qc.s(0)
    qc.h(0)
    qc.swap(2,0)
    qc.s(0)
    qc.h(0)
    qc.s(0)
    qc.cx(0,3)
    qc.h(3)
    qc.cx(3,0)
    qc.z(0)
    qc.z(1)
    qc.y(2)
    qc.y(3)

    for i in range(num_qubits):
        qc.measure(i, i)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 100000).result().get_counts(qc)
    return job