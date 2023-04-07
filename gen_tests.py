import os
import sys
from line import Circuit
from mutator import RandomMutator, UCNOTMutator, QFTMutator
from logzero import logger
from copy import deepcopy

RUN_TIME = 10
# SAVE_DIR = "exp-01-09"
# if os.path.exists(SAVE_DIR) == False:
#     os.mkdir(SAVE_DIR)
NUM_QUBITS = 11
mutators = [
    RandomMutator, 
    UCNOTMutator, 
    QFTMutator
    ]

def main(num_qubits):
    for run_idx in range(RUN_TIME):
        logger.debug(run_idx)
        save_dir = 'inputs_' + str(num_qubits).zfill(2)
        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)
        # exp_path = os.path.join(save_dir, "run_" + str(run_idx).zfill(2))
        # if os.path.exists(exp_path) == False:
        #     os.mkdir(exp_path)
        random = Circuit(num_qubits)
        ucnot = Circuit(num_qubits)
        qft = Circuit(num_qubits)
        random_circuit = RandomMutator().generate_circuit(random)
        ucnot_circuit = UCNOTMutator().generate_circuit(ucnot)
        qft_circuit = QFTMutator().generate_circuit(qft)
        save_path_1 = os.path.join(save_dir, "random" + "_" + str(run_idx).zfill(2))
        save_path_2 = os.path.join(save_dir, "ucnot" + "_" + str(run_idx).zfill(2))
        save_path_3 = os.path.join(save_dir, "qft" + "_" + str(run_idx).zfill(2))
        with open(save_path_1, 'w') as f:
            print(random_circuit.code.qasm(), file = f)
        with open(save_path_2, 'w') as f:
            print(ucnot_circuit.code.qasm(), file = f)
        with open(save_path_3, 'w') as f:
            print(qft_circuit.code.qasm(), file = f)

        # handler_1 = open(save_path_1, 'w')
        # handler_2 = open(save_path_2, 'w')
        # handler_3 = open(save_path_3, 'w')
        # print(random_circuit.code.qasm(), file = handler_1)
        # print(ucnot_circuit.code.qasm(), file = handler_2)
        # print(qft_circuit.code.qasm(), file = handler_3)


        # for m in mutators:
        #     # load mutator
        #     mutator = m()
        #     mutator_name = mutator.__class__.__name__
        #     logger.debug(mutator_name)
        #     circuit = Circuit(num_qubits)
        #     circuit_2 = 
        #     new_circuit = mutator.generate_circuit(circuit)
        #     save_path = os.path.join(save_dir, mutator_name + "_" + str(run_idx).zfill(2))
        #     handler = open(save_path, 'w')
        #     print(new_circuit.code.qasm(), file = handler)


            # new_circuit.run_code()
            # target_path = os.path.join(exp_path, mutator_name)
            # if os.path.exists(target_path) == False:
            #     os.mkdir(target_path)

            # hanlder1 = open(os.path.join(target_path, 'circuit'), 'w')
            # print(new_circuit.code.qasm(), file = hanlder1)
            # hanlder2 = open(os.path.join(target_path, 'results'), 'w')
            # results = new_circuit.results
            # print(results, file = hanlder2)

if __name__ == "__main__":
    for i in range(4, 8):
        main(i)