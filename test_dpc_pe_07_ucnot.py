from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from line import Circuit
from qiskit import QuantumCircuit, execute, Aer
from dpc_pe_07 import dpc_pe_07

designated_mutator = UCNOTMutator()

class Test_dpc_pe_07(TestCase):
    def test_dpc_pe_07_prob_0_percent(self):
        new_circuit = Circuit(7)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = dpc_pe_07(mutate_circuit.code)
        self.assertTrue(abs(result['0000000'] - result['0000001']) <= 5000)