from unittest import TestCase
from mutator import RandomMutator, QFTMutator, UCNOTMutator
from qiskit import QuantumCircuit, execute, Aer
from line import Circuit
from rand_cliff_05 import rand_cliff_05

import os
from util import JSDivergence 

program = rand_cliff_05
designated_mutator = QFTMutator()
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

# class Test_case_00(TestCase):
#     def test(self):
#         result = program(test_case_list[0])
#         output_dist = JSDivergence(dist_list[0], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[0], dist_list[0], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         # print(distance)
#         self.assertTrue(distance < 2)

# class Test_case_01(TestCase):
#     def test(self):
#         result = program(test_case_list[1])
#         output_dist = JSDivergence(dist_list[1], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[1], dist_list[1], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_02(TestCase):
#     def test(self):
#         result = program(test_case_list[2])
#         output_dist = JSDivergence(dist_list[2], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[2], dist_list[2], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_03(TestCase):
#     def test(self):
#         result = program(test_case_list[3])
#         output_dist = JSDivergence(dist_list[3], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[3], dist_list[3], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_04(TestCase):
#     def test(self):
#         result = program(test_case_list[4])
#         output_dist = JSDivergence(dist_list[4], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[4], dist_list[4], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_05(TestCase):
#     def test(self):
#         result = program(test_case_list[5])
#         output_dist = JSDivergence(dist_list[5], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[5], dist_list[5], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_06(TestCase):
#     def test(self):
#         result = program(test_case_list[6])
#         output_dist = JSDivergence(dist_list[6], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[6], dist_list[6], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_07(TestCase):
#     def test(self):
#         result = program(test_case_list[7])
#         output_dist = JSDivergence(dist_list[7], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[7], dist_list[7], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_08(TestCase):
#     def test(self):
#         result = program(test_case_list[8])
#         output_dist = JSDivergence(dist_list[8], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[8], dist_list[8], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)

# class Test_case_09(TestCase):
#     def test(self):
#         result = program(test_case_list[9])
#         output_dist = JSDivergence(dist_list[9], result, sample_times)
#         oringal_dist = JSDivergence(dist_list[9], dist_list[9], sample_times)
#         distance = abs(output_dist - oringal_dist)
#         self.assertTrue(distance < 2)