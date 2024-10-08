# This file contains the implemenation of the qudit gates.

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
        return (self.d, self.d)  # It acts on two qudits of dimension d

    def _unitary_(self):
        d = self.d
        dim = d * d
        unitary_matrix = np.zeros((dim, dim), dtype=complex)
        for i in range(d):
            for j in range(d):
                # Compute the input and output indices
                input_index = i * d + j
                output_index = i * d + ((i + j) % d)
                unitary_matrix[output_index, input_index] = 1
        return unitary_matrix

    def _circuit_diagram_info_(self, args):
        return [f"", f"CNOT(d={self.d})"] 