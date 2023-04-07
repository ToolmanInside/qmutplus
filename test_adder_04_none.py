from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from adder_04 import adder_04

designated_mutator = QFTMutator()
num_qubits = 4

class Test_adder_04(TestCase):
    def test_adder_04_0000_prob_0_percent(self):
        input_folder = "inputs_" + str(num_qubits).zfill(2)
        new_circuit = Circuit(num_qubits)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = adder_04(new_circuit.code)
        # result = bv_04(mutate_circuit.code)
        self.assertTrue(result['0000'] >= 4000)