from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from pe_06 import pe_06

designated_mutator = RandomMutator()

class Test_pe_06(TestCase):
    def test_pe_06_prob_0_percent(self):
        new_circuit = Circuit(6)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = pe_06(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['000000'] >= 1200)