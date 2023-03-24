from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from grover_03 import grover_03

designated_mutator = QFTMutator()

class Test_grover_03(TestCase):
    def test_grover_03_0000_prob_0_percent(self):
        new_circuit = Circuit(3)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = grover_03(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['000'] >= 4000)