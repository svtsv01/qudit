# This file contains the implemenation of the qudit gates.

from typing import Dict, List
from sympy import Mod, mod_inverse
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
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(n**0.5)
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

class quditU8Gate(cirq.Gate):
    def __init__(self, d, gamma=2, z=1, eps=0):
        super().__init__()
        if not is_prime(d):
            raise ValueError(f"Dimension d={d} is not prime. U_{pi/8} gate requires a prime dimension.")
        if gamma == 0:
            raise ValueError("gamma must not be zero.")

        self.d = d
        self.gamma = gamma
        self.z = z
        self.eps = eps

        self.vks = [0]*d

        if d == 3:
            self.vks = [0, 1, 8]
        else:
            try:
                inv_12 = mod_inverse(12, d)
            except ValueError:
                raise ValueError(f"Inverse of 12 mod {d} does not exist. Choose a prime d that does not divide 12.")

            for i in range(1, d):
                a = inv_12 * i * (self.gamma + i*(6*self.z + (2*i - 3)*self.gamma)) + self.eps*i
                self.vks[i] = Mod(a, d)
        print(self.vks)   
        sum_vks = Mod(sum(self.vks), d)
        if sum_vks != 0:
            raise ValueError(f"Sum of v_k's is not 0 mod {d}. Got {sum_vks}. Check parameters.")

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        omega = np.exp(2j * np.pi / self.d)
        u_matrix = np.zeros((self.d, self.d), dtype=complex)
        for j in range(self.d):
            u_matrix[j, j] = omega ** self.vks[j]
        return u_matrix

    def _circuit_diagram_info_(self, args):
        return f"U8(d={self.d})"


class quditPhaseGate(cirq.Gate):
    def __init__(self, d):
        super().__init__()
        if not is_prime(d):
            raise ValueError(f"d={d} is not prime. Phase gate requires a prime dimension.")
        if d == 2:
            raise ValueError("Phase gate is defined for odd prime d >= 3.")
        self.d = d

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        omega = np.exp(2j * np.pi / self.d)
        p_matrix = np.zeros((self.d, self.d), dtype=complex)
        for s in range(self.d):
            phase_exp = (s*(s-1))//2
            p_matrix[s, s] = omega**phase_exp
        return p_matrix

    def _circuit_diagram_info_(self, args):
        return f"P(d={self.d})"