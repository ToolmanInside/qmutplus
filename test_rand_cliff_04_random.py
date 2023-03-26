from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from rand_cliff_04 import rand_cliff_04

designated_mutator = RandomMutator()

class Test_rand_cliff_04(TestCase):
    def test_rand_cliff_04_0000_prob_0_percent(self):
        new_circuit = Circuit(4)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = rand_cliff_04(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['0000'] >= 4000)