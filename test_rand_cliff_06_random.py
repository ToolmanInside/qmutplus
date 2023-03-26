from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from rand_cliff_06 import rand_cliff_06

designated_mutator = RandomMutator()

class Test_rand_cliff_06(TestCase):
    def test_rand_cliff_06_prob_0_percent(self):
        new_circuit = Circuit(6)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = rand_cliff_06(mutate_circuit.code)
        print(result)
        # first_idx = list(result.keys())[0]
        # self.assertTrue(len(result.keys()) <= 32)
        self.assertTrue(result['000000'] > 500)