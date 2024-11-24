# This file contains the implemenation of the qudit gates.

from typing import Dict, List
import cirq
import numpy as np
from typing import Tuple

# Implementation of X gate for qudit
# Modified quditXGate
class quditXGate(cirq.Gate):
    def __init__(self, d, exponent=1):
        super().__init__()
        self.d = int(d)
        self.exponent = int(exponent % d)

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        x_matrix = np.zeros((self.d, self.d), dtype=complex)
        for i in range(self.d):
            row = int((i + self.exponent) % self.d)
            x_matrix[row][i] = 1
        return x_matrix

    def _circuit_diagram_info_(self, args):
        return f"X^{self.exponent}(d={self.d})"

    def __pow__(self, power):
        power = int(power)
        new_exponent = (self.exponent * power) % self.d
        return quditXGate(self.d, exponent=new_exponent)


# Modified quditZGate
class quditZGate(cirq.Gate):
    def __init__(self, d, exponent=1):
        super().__init__()
        self.d = int(d)
        self.exponent = int(exponent % d)

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        z_matrix = np.zeros((self.d, self.d), dtype=complex)
        omega = np.exp(2j * np.pi / self.d)
        for i in range(self.d):
            z_matrix[i][i] = omega ** ((i * self.exponent) % self.d)
        return z_matrix

    def _circuit_diagram_info_(self, args):
        return f"Z^{self.exponent}(d={self.d})"

    def __pow__(self, power):
        power = int(power)
        new_exponent = (self.exponent * power) % self.d
        return quditZGate(self.d, exponent=new_exponent)

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
    def __init__(self, d: int):
        super().__init__()
        self.d = d
    
    def _qid_shape_(self) -> Tuple[int, ...]:
        return (self.d, self.d)

    def _unitary_(self) -> np.ndarray:
        size = self.d ** 2
        CNOT = np.zeros((size, size), dtype=complex)
        for a in range(self.d):
            for b in range(self.d):
                control = a
                target = (b + a) % self.d
                row = a * self.d + b
                col = a * self.d + target
                CNOT[row, col] = 1
        return CNOT

    def _circuit_diagram_info_(self, args):
        return cirq.CircuitDiagramInfo(wire_symbols=(f"C(d={self.d})", f"X(d={self.d})"))
    

# Implementation of Measurement Gate for qudit
def qudit_measure(qudit: cirq.Qid, key: str) -> cirq.Operation:
    return cirq.measure(qudit, key=key)
    
def state_vector(dimension, index):

    if not (0 <= index < dimension):
        raise ValueError(f"Index {index} is out of bounds for dimension {dimension}.")
    state = np.zeros(dimension, dtype=complex)
    state[index] = 1
    return state

def measure_qudits(state_vector: np.ndarray, qudit_order: List[cirq.Qid]) -> Dict[str, int]:
    d = qudit_order[0].dimension  
    num_qudits = len(qudit_order)
    total_dim = d ** num_qudits

    if len(state_vector) != total_dim:
        raise ValueError("State vector size does not match the total qudit dimensions.")

    probabilities = np.abs(state_vector) ** 2
    probabilities /= probabilities.sum() 

    
    sampled_index = np.random.choice(total_dim, p=probabilities)

    measurement_results = {}
    for qudit in reversed(qudit_order):
        outcome = sampled_index % d
        measurement_results[qudit.name] = outcome
        sampled_index = sampled_index // d

    return measurement_results