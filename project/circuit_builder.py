#creating the circuit:
import cirq

def create_circuit(*args):
    circuit = cirq.Circuit()

    if isinstance(args[0], tuple):
        # Handling tuples like (d1, x), (d2, x), (d3, y)
        for dimension, gate_type in args:
            qudit = cirq.NamedQid(f"qudit_d{dimension}", dimension=dimension)
            gate = gate_type(dimension) 
            circuit.append(gate(qudit))
    else:
        # Handling dimension followed by gates, e.g., (d, x, y, z, z)
        dimension = args[0] 
        gates = args[1:]   
        qudit = cirq.NamedQid(f"qudit_d{dimension}", dimension=dimension)
        for gate_type in gates:
            gate = gate_type(dimension)
            circuit.append(gate(qudit))

    return circuit