# Tutorial

This tutorial provides a guide on how to use the Qudit Cirq Library, including creating qudits, applying qudit gates, building circuits, and simulating quantum computations with qudits.

Qudits are $d$-level quantum systems which serve as the generalization of qubit systems ($d =2$). Theoretically, we assume that they lie in the $d$-dimensional complex Hilbert space $\mathbb{C}^d$. Assume that we have the computational basis $\{\ket{s} : s \in \mathbb{Z}_d\}$ of $\mathbb{C}^d$, where $\ket{s}$ is a column vector of $d$ dimensions with zeros everywhere except at position $s$, where it is $1$. The general form of a qudit $\ket{\psi}$ is:

$$
\ket{\psi} = \sum_{j = 0}^{d-1} \alpha_j \ket{j},
$$

with the condition that $\sum_{j = 0}^{d - 1} |\alpha_j|^2 = 1$, and $\alpha_j \in \mathbb{C}$. For an introduction to qudit systems, see for example Asghar, Mukherjee and Brennen [2024] (https://doi.org/10.48550/arXiv.2409.04026), and the reference there in.

---

## Creating Qudits

Qudits are created using Cirq's `LineQid` class with a specified dimension. Here's how you can create a qudit of dimension $d$:

The following code creates the qudit $\ket{0}$ of dimension $𝑑 = 10$

```python
import cirq

# Create a qudit of dimension 𝑑 = 10
qudit = cirq.LineQid(0, dimension=10)
```

To create a state vector representing $\ket{S}$ you can use the next:

```python
s = 3
initial_state = np.zeros(d, dtype=complex)
initial_state[s] = 1
```

## Qudit Gates

The Qudit Cirq Library provides implementations of common quantum gates.

### Qudit Pauli-$X$ Gate (`quditXGate`):

The qudit Pauli-$X$ gate generalizes the bit-flip operation to
$𝑑$ dimensions. Its operation on the computational basis state $\ket{s}$ is defined as:

$$
X\ket{s} = \ket{s + 1}
$$

```python
from qudit_cirq.qudit import quditXGate

# Create a qudit X gate for dimension d=3
x_gate = quditXGate(d=3)
```

This can be applied on a qudit using `.on()`.

### Qudit Pauli-$Z$ Gate (`quditZGate`):

The qudit Pauli-$Z$ gate generalizes the phase-flip operation. Its operation on the computational basis state $\ket{s}$ is defined as:

$$
Z \ket{s} = \omega^s \ket{s}
$$

```python

from qudit_cirq.qudit import quditZGate

# Create a qudit Z gate for dimension d=3
z_gate = quditZGate(d=3)
```

This can be applied on a qudit using `.on()`.

### Qudit Hadamard Gate (`quditHGate`):

The qudit Hadamard gate sends computational basis states into equal superpositions in
$d$ dimensions. Its operation on the computational basis state $\ket{s}$ is defined as:

$$
H\ket{s} = \frac{1}{\sqrt{d}}\sum_{j = 0}^{d-1} \omega^{js} \ket{j}
$$

See for example Yang et al. [2020] (https://doi.org/10.3389/fphy.2020.589504).

```python

from qudit_cirq.qudit import quditHGate

# Create a qudit Hadamard gate for dimension d=5
h_gate = quditHGate(d=5)
```

This can be applied on a qudit using `.on()`.

### Qudit Controlled-NOT Gate (`quditCNOTGate`):

The qudit Controlled-NOT gate generalises the CNOT operation. This is a two qudit operation with two inputs, a control qudit and a target qudit. Given two computational basis states its action is defined as:

$$
\ket{r}\ket{s} \rightarrow \ket{r}\ket{r + s} = \ket{r} X^r \ket{s}
$$

```python
from qudit_cirq.qudit import quditCNOTGate

# Create a qudit CNOT gate for dimension d=4
cnot_gate = quditCNOTGate(d=4)
```

This can be applied on on a qudit using `.on()`. In this case two qudits need to be specified, target and control, respectively.

### Qudit $S$ Gate (`quditPhaseGate`):

The qudit S gate generalizes the phase gate to dimension $d$. Its operation on the computational basis state $\ket{s}$ is defined as:

$$
S\ket{s} = \omega^{s(s+p_d)/2} \ket{s},
$$

where $p_d = 1$ if $d$ is odd, and $0$ otherwise. This is one of the generators of the qudit Clifford group, alongwith the Pauli-$Z$ gate, the qudit Hadamard gate and the controlled-$Z$ gate. See for example Jafarzadeh et al [2019] (https://doi.org/10.48550/arXiv.1911.08162).

```python
from qudit_cirq.qudit import quditPhaseGate

# Create a qudit Phase gate for dimension d=5 (prime and odd)
phase_gate = quditPhaseGate(d=5)
```

This can be applied on a qudit using `.on()`.

### Qudit Controlled-$Z$ Gate (`quditCZGate`):

The qudit Controlled-$Z$ gate generalises the same operation on qubits. This is a two qudit operation with two inputs, a control qudit and a target qudit. Given two computational basis states its action is defined as:

$$
\ket{r}\ket{s} \rightarrow \omega^{rs}\ket{r}\ket{s} = \ket{r}Z^r \ket{s}
$$

This is one of the generators of the qudit Clifford group, alongwith the Pauli-$Z$ gate, the qudit Hadamard gate and the controlled-$Z$ gate. See for example Jafarzadeh et al [2019] (https://doi.org/10.48550/arXiv.1911.08162).

```python
from qudit_cirq.qudit import quditPhaseGate

# Create a qudit Phase gate for dimension d=5 (prime and odd)
phase_gate = quditCZGate(d=5)
```

This can be applied on a qudit using `.on()`.

### Qudit $U_{\pi/8}$ Gate (`quditU8Gate`):

The $U_{\pi/8}$ gate generalizes the qubit $\pi/8$ gate to qudits (called the $T$ gate in the classic text from Chuang and Nielsen [2010]). The extension to qudits is defined for a prime dimension $d$. The general form of the gate is defined as:

$$
U = \sum_{j = 0}^{d-1} \omega^{v_j} \ket{j}\bra{j}
$$

The exact values of the $v_j$'s depends on the dimension $d$. Explicit formula to compuate these values for $d = 3$ and $d \geq 5$ (remember $d$ should be a prime) are given in Howard and Vala [2012] (
https://doi.org/10.48550/arXiv.1206.1598). Our implementation of this gate follows their construction.

```python
from qudit_cirq.qudit import quditU8Gate

# Create a qudit U_{π/8} gate for dimension d=7
u8_gate = quditU8Gate(d=7)
```

This can be applied on a qudit using `.on()`.

## Building Circuits with Qudits

There are two primary methods for building circuits with qudits:

### Method 1: Manual Construction

Manually create circuits by explicitly defining qudits and appending gates. Gates are appended to the circuit using the `.append()` method.

```python
import cirq
from qudit_cirq.qudit import quditXGate, quditHGate, quditCNOTGate

# Create qudits
qudit1 = cirq.LineQid(0, dimension=3)
qudit2 = cirq.LineQid(1, dimension=3)

# Build a circuit
circuit = cirq.Circuit()
circuit.append(quditHGate(d=3).on(qudit1))
circuit.append(quditCNOTGate(d=3).on(qudit1, qudit2))
```

You can view the circuit using the `print` command.

```python
print(circuit)
```

This outputs the following:

```
0 (d=3): ───H(d=3)───C(d=3)───
                     │
1 (d=3): ────────────X(d=3)───
```

### Method 2: Using the `create_circuit` Function

Use the `create_circuit` function for a more concise syntax when building circuits.

```python
from qudit_cirq.circuit_builder import create_circuit
from qudit_cirq.qudit import quditHGate, quditCNOTGate, qudit_measure

# Build the circuit using create_circuit
circuit, qudits, qudit_order = create_circuit(
    3,  # Set dimension d=3
    (quditHGate, 'q0'),
    (quditCNOTGate, ['q0', 'q1']),
    (qudit_measure, 'q0'),
    (qudit_measure, 'q1')
)

print(circuit)
```

This yields:

```
q0 (d=3): ───H(d=3)───C(d=3)───M('m_q0')───
                      │
q1 (d=3): ────────────X(d=3)───M('m_q1')───
```

- <strong> Arguments: </strong>

1.  The function accepts a variable number of arguments: `\*args`.
2.  Dimension is set by passing an integer.
3.  Gates are specified as tuples with the gate type and qudit names.

- <strong> Returns:</strong>

1.  circuit: The constructed `cirq.Circuit`.
2.  qudits: A dictionary mapping qudit names to `cirq.Qid` objects.
3.  qudit_order: A list of qudits in the order they were added.

### Extended Usage of the `create_circuit` Function:

If needed, the dimensions for each qudit can be specified explicitly in the `create_circuit` function:

```python
circuit, qudits, qudit_order = create_circuit(
    (3, quditHGate, 'q0'),
    (4, quditHGate, 'q1'),
    (5, quditTGate, 'q3'),
    (6, quditTGate, 'q4')
)
```

## Measurement and Simulation

Once you have created a circuit, you can measure qudits and simulate the circuit.

### Measuring Qudits

For manual circuits use `.append()` and `cirq.measure()` to add measurements to specified qudits. For instance, add the following to the manually constructed circuit above:

```python
circuit.append(cirq.measure(qudit1, key='q1'))
circuit.append(cirq.measure(qudit2, key='q2'))

print(circuit)
```

This yields:

```
0 (d=3): ───H(d=3)───C(d=3)───M('q1')───
                     │
1 (d=3): ────────────X(d=3)───M('q2')───
```

For circuits built with create_circuit, measurements are included during construction as shown above.

### Simulating the Circuit

Use Cirq's simulator to run the circuit and obtain measurement results.

```python
# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=10)

# Print the results
print(result)
```

For the circuit above, this yields:

```
q1=2200102011
q2=2200102011
```

- Note:

1. `repetitions=10` specifies the number of times the circuit is run.
2. result contains the measurement outcomes from all runs.

## Utility Functions

The Qudit Cirq Library provides multiple utility functions to assist with formatting outputs, printing state vectors, and computing tensor products.

### Formatting Output `(format_out)`

The `format_out` function formats a NumPy matrix or vector for display, allowing you to specify the output type for better readability.

<strong> Function definition: </strong>

```python
def format_out(matrix, output_type='float'):
    # Function implementation
```

- Parameters

1. matrix: The NumPy array (matrix or vector) to format.
2. output_type (optional): The type of formatting to apply to the elements. Options are `float`, `int`, or `str`. Default is `float`.

Example:

```python
import numpy as np
from qudit_cirq.utils import format_out

# Define a matrix with complex elements
matrix = np.array([[1+0j, 0+0j], [0+0j, -1+0j]])

# Format the matrix as integers
formatted_matrix = format_out(matrix, output_type='int')
print(formatted_matrix)
```

Output:

```
[['1' '0']
 ['0' '-1']]
```

### Printing the State Vector (`printVector`)

The `printVector` function prints the final state vector of a quantum circuit.

<strong> Function definition: </strong>

```python
def printVector(final_state, dimensions, qudits=None, threshold=1e-6):
    # Function implementation
```

- Parameters

1. `final_state`: The state vector, e.g., `result.final_state_vector`.
2. `dimensions`: An integer or list of integers representing the dimensions of the qudits.
3. `qudits` (optional): A list of qudit objects to label the qudits in the output.
4. `threshold` (optional): A float specifying the minimum amplitude magnitude to display. Default is `1e-6`.

Example:

```python
import cirq
from qudit_cirq.utils import printVector

d = 3
qudit1 = cirq.NamedQid('q0', dimension=d)
qudit2 = cirq.NamedQid('q1', dimension=d)

circuit = cirq.Circuit()
circuit.append(quditHGate(d).on(qudit1))
circuit.append(quditHGate(d).on(qudit2))


simulator = cirq.Simulator()
result = simulator.simulate(circuit)

final_state = result.final_state_vector

# List of qudits in order
qudit_order = [qudit1, qudit2]

# Print the state vector using printVector
printVector(final_state, dimensions=[d, d], qudits=qudit_order)
```

This should produce the state

$$
\frac{1}{3}\sum_{j = 1}^3 \sum_{k = 1}^3 \ket{jk},
$$

as can be seen from the output:

```
Final state vector:
|00⟩: (0.3333333432674408+0j)
|01⟩: (0.3333333432674408+0j)
|02⟩: (0.3333333432674408+0j)
|10⟩: (0.3333333432674408+0j)
|11⟩: (0.3333333432674408+0j)
|12⟩: (0.3333333432674408+0j)
|20⟩: (0.3333333432674408+0j)
|21⟩: (0.3333333432674408+0j)
|22⟩: (0.3333333432674408+0j)
```

### Tensor Product of Matrices (`tensor_product`)

The `tensor_product` function computes the tensor product of multiple matrices or vectors.

<strong> Function definition: </strong>

```python
def tensor_product(*arrays):
    # Function implementation
```

- Parameters

1. `*arrays`: A variable number of NumPy arrays to compute their tensor product.

Example:

```python
import cirq
import numpy as np
from qudit_cirq.utils import tensor_product

# Define single-qudit states
state0 = np.array([1, 0, 0])  # |0⟩ in dimension 3
state1 = np.array([0, 1, 0])  # |1⟩ in dimension 3

# Compute the tensor product to create a two-qudit state
combined_state = tensor_product(state0, state1)

print(combined_state)
```

Output:

```
[0 1 0 0 0 0 0 0 0]
```

## Examples

We provide a couple of end-to-end examples. These examples create the Greenberger–Horne–Zeilinger (GHZ) state for qudits. The GHZ state for an $n$-qudit system in $d$ dimensions is defined as:

$$
\frac{1}{\sqrt{d}} \sum_{j = 0}^{d-1} \ket{j}^{\otimes n}
$$

The examples below construct this GHZ state using the circuit shown in Asghar, Mukherjee and Brennen [2024] (https://doi.org/10.48550/arXiv.2409.04026).

### Example 1: Qudit GHZ State Preparation (Manual Construction)

Prepare a GHZ state of $n = 3$ qudits of dimension $d = 3$.

```python
import cirq
from qudit_cirq.qudit import quditHGate, quditCNOTGate

# Parameters
d = 3  # Qudit dimension
n_qudits = 3  # Number of qudits

# Create qudits
qudits = [cirq.LineQid(i, dimension=d) for i in range(n_qudits)]

# Build the circuit
circuit = cirq.Circuit()
circuit.append(quditHGate(d).on(qudits[0]))
for i in range(1, n_qudits):
    circuit.append(quditCNOTGate(d).on(qudits[i - 1], qudits[i]))

# Measure
circuit.append(cirq.measure(*qudits, key='result'))

# Simulate
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=10)
print(result)
```

Output:

```
result=2201011100, 2201011100, 2201011100
```

If instead, we want to print the state vector, then we can replace the measurement and simulation code with:

```python
simulator = cirq.Simulator()
result = simulator.simulate(circuit)
final_state = result.final_state_vector

printVector(final_state, dimensions=[d, d, d])
```

This gives the output:

```
Final state vector:
|000⟩: (0.5773502588272095+0j)
|111⟩: (0.5773502588272095+0j)
|222⟩: (0.5773502588272095+0j)
```

as expected. We can also print this circuit:

```
0 (d=3): ───H(d=3)───C(d=3)────────────
                     │
1 (d=3): ────────────X(d=3)───C(d=3)───
                              │
2 (d=3): ─────────────────────X(d=3)───
```

### Example 2: Qudit GHZ State Preparation (`Using create_circuit Function`)

Prepare the same GHZ state using the `create_circuit` function.

```python
import cirq
from qudit_cirq.qudit import quditHGate, quditCNOTGate, qudit_measure

# Build the circuit using create_circuit
circuit, qudits, qudit_order = create_circuit(
    3,  # Set dimension d=3
    (quditHGate, 'q0'),
    (quditCNOTGate, ['q0', 'q1']),
    (quditCNOTGate, ['q1', 'q2']),
    (qudit_measure, 'q0'),
    (qudit_measure, 'q1'),
    (qudit_measure, 'q2')
)

# Simulate
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=10)
print(result)
```

Output:

```
m_q0=2002211000
m_q1=2002211000
m_q2=2002211000
```

## Computantional Constraintes
