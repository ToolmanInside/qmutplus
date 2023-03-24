from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from bv_05 import bv_05

designated_mutator = QFTMutator()

class Test_bv_05(TestCase):
    def test_bv_05_prob_0_percent(self):
        new_circuit = Circuit(5)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = bv_05(new_circuit.code)
        self.assertTrue(result['00000'] >= 2400)