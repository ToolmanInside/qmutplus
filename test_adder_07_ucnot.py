from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from adder_07 import adder_07

import os
from util import JSDivergence

program = adder_07
designated_mutator = UCNOTMutator()
num_qubits = 7
input_folder = "inputs_" + str(num_qubits).zfill(2)
test_case_list = list()
dist_list = list()
for idx in range(10):
    file_name_path = designated_mutator.__class__.__name__ + "_" + str(idx).zfill(2)
    quantum_circuit = QuantumCircuit.from_qasm_file(os.path.join(input_folder, file_name_path))
    test_case_list.append(quantum_circuit)
    dist = adder_07(quantum_circuit)
    dist_list.append(dist)

class Test_case_00(TestCase):
    def test(self):
        result = program(test_case_list[0])
        self.assertTrue(JSDivergence(dist_list[0], result, 100000) < 0.3)

class Test_case_01(TestCase):
    def test(self):
        result = program(test_case_list[1])
        self.assertTrue(JSDivergence(dist_list[1], result, 100000) < 0.3)

class Test_case_02(TestCase):
    def test(self):
        result = program(test_case_list[2])
        self.assertTrue(JSDivergence(dist_list[2], result, 100000) < 0.3)

class Test_case_03(TestCase):
    def test(self):
        result = program(test_case_list[3])
        self.assertTrue(JSDivergence(dist_list[3], result, 100000) < 0.3)

class Test_case_04(TestCase):
    def test(self):
        result = program(test_case_list[4])
        self.assertTrue(JSDivergence(dist_list[4], result, 100000) < 0.3)

class Test_case_05(TestCase):
    def test(self):
        result = program(test_case_list[5])
        self.assertTrue(JSDivergence(dist_list[5], result, 100000) < 0.3)

class Test_case_06(TestCase):
    def test(self):
        result = program(test_case_list[6])
        self.assertTrue(JSDivergence(dist_list[6], result, 100000) < 0.3)

class Test_case_07(TestCase):
    def test(self):
        result = program(test_case_list[7])
        self.assertTrue(JSDivergence(dist_list[7], result, 100000) < 0.3)

class Test_case_08(TestCase):
    def test(self):
        result = program(test_case_list[8])
        self.assertTrue(JSDivergence(dist_list[8], result, 100000) < 0.3)

class Test_case_09(TestCase):
    def test(self):
        result = program(test_case_list[9])
        self.assertTrue(JSDivergence(dist_list[9], result, 100000) < 0.3)
