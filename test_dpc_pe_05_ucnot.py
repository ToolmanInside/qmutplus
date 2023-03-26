from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from line import Circuit
from qiskit import QuantumCircuit, execute, Aer
from dpc_pe_05 import dpc_pe_05

designated_mutator = UCNOTMutator()

class Test_dpc_pe_05(TestCase):
    def test_dpc_pe_05_prob_0_percent(self):
        new_circuit = Circuit(5)
        mutate_circuit = designated_mutator.generate_circuit(new_circuit)
        result = dpc_pe_05(mutate_circuit.code)
        # result = bv_04(mutate_circuit.code)
        # print(result)
        self.assertTrue(abs(result['00000'] - result['00001']) <= 30000)