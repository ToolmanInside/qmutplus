from qiskit import QuantumCircuit, execute, Aer, QuantumRegister, ClassicalRegister

def adder(mqc):
    q = QuantumRegister(4)
    c = ClassicalRegister(4)
    qc = QuantumCircuit(q, c)

    for i in range(4):
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

    # qc = mqc.compose(qc)
    for i in range(4):
        qc.measure(i, i)
    # print(qc)

    backend = Aer.get_backend("aer_simulator")
    job = execute(qc, backend, shots = 1000).result().get_counts(qc)
    # print(job)
    # counts = job.result().get_counts(qc)
    return job