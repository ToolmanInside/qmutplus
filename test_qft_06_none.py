from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from qft_06 import qft_06

designated_mutator = RandomMutator()

class Test_qft_06(TestCase):
    def test_qft_06_prob_0_percent(self):
        new_circuit = Circuit(6)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = qft_06(new_circuit.code)
        self.assertTrue(result['000000'] >= 500)