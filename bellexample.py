from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, Aer, execute

def bell_state():
    q = QuantumRegister(2)
    c = ClassicalRegister(2)
    qc = QuantumCircuit(q, c)

    qc.h(q[0])
    # qc.cx(q[0], q[1])
    __qmutpy_qgi_func__(qc, q[0], q[1])
    qc.measure(q, c)
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1000)
    return job.result().get_counts(qc)
def __qmutpy_qgi_func__(circ, arg1, arg2):
    circ.cx(arg1, arg2)
    circ.u1(arg1, arg2)

bell_state()