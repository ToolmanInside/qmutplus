from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
num_qubits = 4

def bv_04(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)

    qc = mqc.compose(qc)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.x(3)
    qc.h(3)
    qc.cx(0,3)
    qc.cx(1,3)
    qc.cx(2,3)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)

    for i in range(num_qubits):
        qc.measure(i, i)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 10000).result().get_counts(qc)
    return job