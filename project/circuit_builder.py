#creating the circuit:
import cirq

def create_circuit(*args):
    circuit = cirq.Circuit()
    qudits = {}
    qudit_order = []
    current_dimension = None

    for arg in args:
        if isinstance(arg, int):
            current_dimension = arg
            continue

        if not isinstance(arg, tuple):
            raise ValueError(f"Invalid argument format: {arg}")

        if len(arg) == 3 and isinstance(arg[0], int):
            # Tuple like (dimension, gate_type, qudit_names)
            gate_dimension, gate_type, qudit_names = arg
            current_dimension = gate_dimension 
        elif len(arg) == 2:
            # Tuple like (gate_type, qudit_names)
            if current_dimension is None:
                raise ValueError("Dimension must be specified before gate tuples without dimension")
            gate_dimension = current_dimension
            gate_type, qudit_names = arg
        else:
            raise ValueError(f"Invalid tuple format: {arg}")

        if isinstance(qudit_names, str):
            qudit_names = [qudit_names]

        qudit_objects = []
        for name in qudit_names:
            if name not in qudits:
                qudit = cirq.NamedQid(name, dimension=gate_dimension)
                qudits[name] = qudit
                qudit_order.append(qudit)
            else:
                qudit = qudits[name]
                if qudit.dimension != gate_dimension:
                    raise ValueError(f"Qudit '{name}' was previously defined with dimension {qudit.dimension}, but now is used with dimension {gate_dimension}")
            qudit_objects.append(qudits[name])

        if issubclass(gate_type, cirq.Gate):
            gate = gate_type(gate_dimension)
            circuit.append(gate(*qudit_objects))
        else:
            raise ValueError(f"Invalid gate type: {gate_type}")

    return circuit, qudits, qudit_order