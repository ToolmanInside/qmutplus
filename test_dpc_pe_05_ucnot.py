from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from line import Circuit
from qiskit import QuantumCircuit, execute, Aer
from dpc_pe_05 import dpc_pe_05

import os
from util import JSDivergence 

program = dpc_pe_05
designated_mutator = UCNOTMutator()
sample_times = 10000
num_qubits = 5
input_folder = "inputs_" + str(num_qubits).zfill(2)
test_case_list = list()
dist_list = list()
for idx in range(10):
    file_name_path = designated_mutator.__class__.__name__ + "_" + str(idx).zfill(2)
    quantum_circuit = QuantumCircuit.from_qasm_file(os.path.join(input_folder, file_name_path))
    test_case_list.append(quantum_circuit)
    dist = program(quantum_circuit)
    dist_list.append(dist)

class Test_case_00(TestCase):
    def test(self):
        result = program(test_case_list[0])
        self.assertTrue(JSDivergence(dist_list[0], result, sample_times) < 0.1)

class Test_case_01(TestCase):
    def test(self):
        result = program(test_case_list[1])
        self.assertTrue(JSDivergence(dist_list[1], result, sample_times) < 0.1)

class Test_case_02(TestCase):
    def test(self):
        result = program(test_case_list[2])
        self.assertTrue(JSDivergence(dist_list[2], result, sample_times) < 0.1)

class Test_case_03(TestCase):
    def test(self):
        result = program(test_case_list[3])
        self.assertTrue(JSDivergence(dist_list[3], result, sample_times) < 0.1)

class Test_case_04(TestCase):
    def test(self):
        result = program(test_case_list[4])
        self.assertTrue(JSDivergence(dist_list[4], result, sample_times) < 0.1)

class Test_case_05(TestCase):
    def test(self):
        result = program(test_case_list[5])
        self.assertTrue(JSDivergence(dist_list[5], result, sample_times) < 0.1)

class Test_case_06(TestCase):
    def test(self):
        result = program(test_case_list[6])
        self.assertTrue(JSDivergence(dist_list[6], result, sample_times) < 0.1)

class Test_case_07(TestCase):
    def test(self):
        result = program(test_case_list[7])
        self.assertTrue(JSDivergence(dist_list[7], result, sample_times) < 0.1)

class Test_case_08(TestCase):
    def test(self):
        result = program(test_case_list[8])
        self.assertTrue(JSDivergence(dist_list[8], result, sample_times) < 0.1)

class Test_case_09(TestCase):
    def test(self):
        result = program(test_case_list[9])
        self.assertTrue(JSDivergence(dist_list[9], result, sample_times) < 0.1)