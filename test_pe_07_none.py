from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from pe_07 import pe_07

designated_mutator = RandomMutator()

class Test_pe_07(TestCase):
    def test_pe_07_prob_0_percent(self):
        new_circuit = Circuit(7)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = pe_07(new_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['0000000'] >= 500)