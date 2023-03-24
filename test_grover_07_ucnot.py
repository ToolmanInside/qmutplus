from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from grover_07 import grover_07

designated_mutator = UCNOTMutator()

class Test_grover_07(TestCase):
    def test_grover_07_prob_0_percent(self):
        new_circuit = Circuit(7)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = grover_07(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['0000000'] >= 1500)