from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from line import Circuit
from qiskit import QuantumCircuit, execute, Aer
from dpc_pe_04 import dpc_pe_04

designated_mutator = QFTMutator()

class Test_dpc_pe_04(TestCase):
    def test_dpc_pe_04_prob_0_percent(self):
        new_circuit = Circuit(4)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = dpc_pe_04(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        # print(result)
        self.assertTrue(abs(result['0000'] - result['0001']) <= 5000)