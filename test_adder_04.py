from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
# import importlib
# program = importlib.import_module("/Users/think/qmutplus/benchmark/adder_04.py", "adder_04")
from adder_04 import adder_04

designated = True
designated_mutator = QFTMutator()

class Test_adder_04(TestCase):
    def test_adder_04_0000_prob_0_percent(self):
        new_circuit = Circuit(4)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = adder_04(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['0000'] >= 4000)