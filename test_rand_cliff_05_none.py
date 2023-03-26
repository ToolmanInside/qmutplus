from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from rand_cliff_05 import rand_cliff_05

designated_mutator = RandomMutator()

class Test_rand_cliff_05(TestCase):
    def test_rand_cliff_05_prob_0_percent(self):
        new_circuit = Circuit(5)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = rand_cliff_05(new_circuit.code)
        self.assertTrue(result['00000'] >= 2000)