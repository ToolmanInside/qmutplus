from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from pe_04 import pe_04

designated_mutator = QFTMutator()

class Test_pe_04(TestCase):
    def test_pe_04_prob_0_percent(self):
        new_circuit = Circuit(4)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = pe_04(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['0000'] >= 4000)