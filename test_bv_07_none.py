from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from bv_07 import bv_07

designated_mutator = RandomMutator()

class Test_bv_07(TestCase):
    def test_bv_07_prob_0_percent(self):
        new_circuit = Circuit(7)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = bv_07(new_circuit.code)
        self.assertTrue(result['0000000'] >= 500)