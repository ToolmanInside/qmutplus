from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from line import Circuit
from qiskit import QuantumCircuit, execute, Aer
from dpc_pe_06 import dpc_pe_06

designated_mutator = RandomMutator()

class Test_dpc_pe_06(TestCase):
    def test_dpc_pe_06_prob_0_percent(self):
        new_circuit = Circuit(6)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = dpc_pe_06(new_circuit.code)
        self.assertTrue(abs(result['000000'] - result['000001']) <= 5000)