# This file contains the implemenation of the qudit gates.

from typing import Dict, List
import cirq
import numpy as np

# Implementation of X gate for qudit
class quditXGate(cirq.Gate):
    def __init__(self, d):
        super(quditXGate, self)
        self.d = d

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        x_matrix = np.zeros((self.d, self.d), dtype=complex)
        for i in range(self.d):
            x_matrix[i][(i + 1) % self.d] = 1
        transposed_matrix = x_matrix.T
        return transposed_matrix

    def _circuit_diagram_info_(self, args):
        return f"X(d={self.d})"
    
# Implementation of Z gate for qudit
class quditZGate(cirq.Gate):

    def __init__(self, d):
        super(quditZGate, self)
        self.d = d

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        z_matrix = np.zeros((self.d, self.d), dtype=complex)
        for i in range(self.d):
            z_matrix[i][i] = np.exp(2j * np.pi * i / self.d)
        transposed_matrix = z_matrix.T
        return transposed_matrix

    def _circuit_diagram_info_(self, args):
        return f"Z(d={self.d})"

# Implementation of H gate for qudit
class quditHGate(cirq.Gate):

    def __init__(self, d):
        super(quditHGate, self)
        self.d = d 

    def _qid_shape_(self):
        return (self.d,) 

    def _unitary_(self):
        h_matrix = np.zeros((self.d, self.d), dtype=complex)
        omega = np.exp(2j * np.pi / self.d)  
        for i in range(self.d):
            for j in range(self.d):
                h_matrix[i, j] = omega ** (i * j) / np.sqrt(self.d) 
        transposed_matrix = h_matrix.T
        return transposed_matrix

    def _circuit_diagram_info_(self, args):
        return f"H(d={self.d})"
        
class quditCNOTGate(cirq.Gate):
    def __init__(self, d):
        super(quditCNOTGate, self).__init__()
        self.d = d

    def _qid_shape_(self):
        return (self.d, self.d) 

    def _unitary_(self):
        d = self.d
        dim = d * d
        unitary_matrix = np.zeros((dim, dim), dtype=complex)
        for i in range(d):
            for j in range(d):
                input_index = i * d + j
                output_index = i * d + ((i + j) % d)
                unitary_matrix[output_index, input_index] = 1
        return unitary_matrix

    def _circuit_diagram_info_(self, args):
        return [f"", f"CNOT(d={self.d})"] 

# Implementation of Measurement Gate for qudit
class quditMeasurementGate(cirq.Gate):
    def __init__(self, d: int, key: str = 'm'):
        super().__init__()
        self.d = d
        self.key = key

    def _qid_shape_(self):
        return (self.d,)

    def _circuit_diagram_info_(self, args):
        return f"M(d={self.d})"
    
def state_vector(dimension, index):

    if not (0 <= index < dimension):
        raise ValueError(f"Index {index} is out of bounds for dimension {dimension}.")
    state = np.zeros(dimension, dtype=complex)
    state[index] = 1
    return state

def measure_qudits(state_vector: np.ndarray, qudit_order: List[cirq.Qid]) -> Dict[str, int]:

    d = qudit_order[0].dimension  # Assuming all qudits have the same dimension
    num_qudits = len(qudit_order)
    total_dim = d ** num_qudits

    if len(state_vector) != total_dim:
        raise ValueError("State vector size does not match the total qudit dimensions.")

    probabilities = np.abs(state_vector) ** 2
    probabilities /= probabilities.sum()  # Normalize

    # Sample a basis state based on the probabilities
    sampled_index = np.random.choice(total_dim, p=probabilities)

    # Decode the sampled index into individual qudit outcomes
    measurement_results = {}
    for qudit in reversed(qudit_order):
        outcome = sampled_index % d
        measurement_results[qudit.name] = outcome
        sampled_index = sampled_index // d

    return measurement_results