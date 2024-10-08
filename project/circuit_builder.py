#creating the circuit:
import cirq

def create_circuit(*args):
    circuit = cirq.Circuit()
    qudits = {}

    dimension = None

    for arg in args:
        if isinstance(arg, int):
            dimension = arg
            continue

        if not isinstance(arg, tuple):
            raise ValueError(f"Invalid argument format: {arg}")

        if len(arg) == 3:
            # Tuple like (dimension, gate_type, qudit_names)
            dim, gate_type, qudit_names = arg
            dimension = dim  
        elif len(arg) == 2:
            if dimension is None:
                raise ValueError("Dimension must be specified before gate tuples without dimension")
            gate_type, qudit_names = arg
        else:
            raise ValueError(f"Invalid tuple length: {len(arg)}")

        if isinstance(qudit_names, str):
            qudit_names = [qudit_names]

        qudit_objects = []
        for name in qudit_names:
            if name not in qudits:
                qudits[name] = cirq.NamedQid(name, dimension=dimension)
            qudit_objects.append(qudits[name])

        if issubclass(gate_type, cirq.Gate):
            gate = gate_type(dimension)
            circuit.append(gate(*qudit_objects))
        else:
            raise ValueError(f"Invalid gate type: {gate_type}")

    return circuit