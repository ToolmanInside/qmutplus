from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from grover_05 import grover_05

designated_mutator = RandomMutator()

class Test_grover_05(TestCase):
    def test_grover_05_0000_prob_0_percent(self):
        new_circuit = Circuit(5)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = grover_05(new_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['00000'] >= 3000)