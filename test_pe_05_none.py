from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from pe_05 import pe_05

designated_mutator = RandomMutator()

class Test_pe_05(TestCase):
    def test_pe_05_prob_0_percent(self):
        new_circuit = Circuit(5)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = pe_05(new_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['00000'] >= 2500)