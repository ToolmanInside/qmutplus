from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from bv_06 import bv_06

designated_mutator = UCNOTMutator()

class Test_bv_06(TestCase):
    def test_bv_06_prob_0_percent(self):
        new_circuit = Circuit(6)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = bv_06(mutate_circuit.code)
        self.assertTrue(result['000000'] >= 1200)