# Tutorial

This tutorial will provide you a clear guidline on how to use the Qudit Cirq Library, including creating qudits, applying qudit gates, building circuits, and simulating quantum computations with qudits.

---

## Creating Qudits

Qudits are created using Cirq's `LineQid` class with a specified dimension. Here's how you can create a qudit of dimension - 𝑑:

```python
import cirq

# Create a qudit of dimension 𝑑 = 10
qudit = cirq.LineQid(0, dimension=10)
```

## Qudit Gates

The Qudit Cirq Library provides implementations of common quantum gates.

### Qudit Pauli-X Gate (quditXGate):

The qudit Pauli-X gate generalizes the bit-flip operation to
𝑑 dimensions.

```python
from qudit_cirq.qudit import quditXGate

# Create a qudit X gate for dimension d=3
x_gate = quditXGate(d=3)
```

Note: Apply .on() for the qudits.

### Qudit Pauli-Z Gate (quditZGate):

The qudit Pauli-Z gate generalizes the phase-flip operation.

```python

from qudit_cirq.qudit import quditZGate

# Create a qudit Z gate for dimension d=3
z_gate = quditZGate(d=3)
```

Note: Apply .on() for the qudits.

### Qudit Hadamard Gate (quditHGate):

The qudit Hadamard gate creates superpositions in
𝑑 dimensions.

```python

from qudit_cirq.qudit import quditHGate

# Create a qudit Hadamard gate for dimension d=3
h_gate = quditHGate(d=3)
```

Note: Apply .on() for the qudits.

### Qudit Controlled-NOT Gate (quditCNOTGate):

The qudit Controlled-NOT gate generalises the CNOT operation.

```python
from qudit_cirq.qudit import quditCNOTGate

# Create a qudit CNOT gate for dimension d=3
cnot_gate = quditCNOTGate(d=3)
```

Note: The qudit CNOT gate acts on two qudits — a control and a target.

## Building Circuits with Qudits

There are two primary methods for building circuits with qudits:

### Method 1: Manual Construction

Manually create circuits by explicitly defining qudits and appending gates.

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

Gates are appended to the circuit using the .append() method.

### Method 2: Using `create_circuit` Function

Use the `create_circuit` function for a more concise syntax when building circuits.

```python
from qudit_cirq.qudit import quditHGate, quditCNOTGate, qudit_measure

# Build the circuit using create_circuit
circuit, qudits, qudit_order = create_circuit(
    3,  # Set dimension d=3
    (quditHGate, 'q0'),
    (quditCNOTGate, ['q0', 'q1']),
    (qudit_measure, 'q0'),
    (qudit_measure, 'q1')
)
```

- <strong> Arguments: </strong>

1.  The function accepts a variable number of arguments (\*args).
2.  Dimension is set by passing an integer.
3.  Gates are specified as tuples with the gate type and qudit names.

- <strong> Returns:</strong>

1.  circuit: The constructed cirq.Circuit.
2.  qudits: A dictionary mapping qudit names to cirq.Qid objects.
3.  qudit_order: A list of qudits in the order they were added.

### Extended Usage of `create_circuit` Function:

Also, dimensions for each qudit can be specified explicitly in `create_circuit` function:

```python
circuit, qudits, qudit_order = create_circuit(
    (3, quditHGate, 'q0'),
    (4, quditHGate, 'q1')
)
```

## Measurement and Simulation

You can measure the qudits and simulate the circuit.

### Measuring Qudits

For manual circuits:

```python
circuit.append(cirq.measure(qudit1, key='q1'))
circuit.append(cirq.measure(qudit2, key='q2'))
```

For circuits built with create_circuit, measurements are included during construction.

### Simulating the Circuit

Use Cirq's simulator to run the circuit and obtain measurement results.

```python
# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=10)

# Print the results
print(result)
```

- Note:

1. `repetitions=10` specifies the number of times the circuit is run.
2. result contains the measurement outcomes from all runs.

## Examples

### Example 1: Qudit GHZ State Preparation (Manual Construction)

Prepare a GHZ state using qudits of dimension 3.

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

### Example 2: Qudit GHZ State Preparation (`Using create_circuit Function`)

Prepare the same GHZ state using the `create_circuit` function.

```python
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

## Utility Functions

The Qudit Cirq Library provides multiple utility functions to assist with formatting outputs, printing state vectors, performing tensor products.

### Formatting Output `(format_out)`

The `format_out` function formats a NumPy matrix or vector for display, allowing you to specify the output type for better readability.

<strong> Function definition: </strong>

```python
def format_out(matrix, output_type='float'):
    # Function implementation
```

- Parameters

1. matrix: The NumPy array (matrix or vector) to format.
2. output_type (optional): The type of formatting to apply to the elements. Options are 'float', 'int', or 'str'. <strong>Default is 'float' </strong>.

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

1. final_state: The state vector (e.g., result.final_state_vector).
2. dimensions: An integer or list of integers representing the dimensions of the qudits.
3. qudits (optional): A list of qudit objects to label the qudits in the output.
4. threshold (optional): A float specifying the minimum amplitude magnitude to display. Default is 1e-6.

Example:

```python
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

Output:

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

1. \*arrays: A variable number of NumPy arrays to compute the tensor product of.

Example:

```python
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
