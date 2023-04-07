from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
num_qubits = 4

def adder_04(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    for i in range(num_qubits):
        qc.h(i)
    qc = mqc.compose(qc)
    qc.ccx(1,2,3)
    qc.cx(1,2)
    qc.ccx(0,2,3)
    qc.cx(0,2)
    for i in range(num_qubits):
        qc.measure(i, i)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 10000).result().get_counts(qc)
    return job