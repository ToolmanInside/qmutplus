from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from adder_test import adder

designated = True
designated_mutator = QFTMutator()

class TestAdder_01(TestCase):
    def test_0000_prob_0_percent(self):
        new_circuit = Circuit(4)
        if designated == True:
            mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        else:
            mutate_circuit = new_circuit
        result = adder(mutate_circuit.code)
        # result = adder(new_circuit.code)
        self.assertTrue(result['0000'] >= 50)