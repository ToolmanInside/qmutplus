from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister
num_qubits = 5

def grover_05(mqc):
    q = QuantumRegister(num_qubits)
    c = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(q, c)

    # for i in range(num_qubits):
    #     qc.h(i)

    qc = mqc.compose(qc)

    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(4)
    qc.ccx(0,1,3)
    qc.ccx(2,3,4)
    qc.ccx(0,1,3)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.x(0)
    qc.x(1)
    qc.x(2)
    qc.h(2)
    qc.ccx(0,1,2)
    qc.h(2)
    qc.x(0)
    qc.x(1)
    qc.x(2)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(4)

    for i in range(num_qubits):
        qc.measure(i, i)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 10000).result().get_counts(qc)
    return job