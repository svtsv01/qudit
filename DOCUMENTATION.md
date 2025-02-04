# Qudit Cirq Library Documentation

This library extends Google's Cirq framework to support **qudits**.

---

## Introduction

Quantum computing relies on the concept of **qubits**, which are two-dimensional quantum systems. However, **qudits** generalise this concept to $d$-dimensional quantum systems, providing a richer computational space and potential advantages in quantum algorithms.

This qudit Cirq library enhances [Google's Cirq](https://quantumai.google/cirq) by including:

- Common qudit gates for arbitrary dimensions $d$.
- Utilities for creating and manipulating qudit circuits.
- Simulation and measurement of qudit-based quantum circuits.

---

## Features

- **Qudit Support**: Work with qudits of any dimension.
- **Generalized Qudit Gates**: Implementations of qudit versions of common quantum gates:
  - Pauli-X Gate
  - Pauli-Z Gate
  - Hadamard Gate
  - Controlled-NOT Gate
  - Pi-Over-Eight Gate (or T Gate)
  - Phase Gate
  - Controlled-Z Gate
- **Circuit Utilities**: Functions to build and manipulate circuits with qudits, including a versatile `create_circuit` function.
- **Measurement and Simulation**: Support for measuring qudits and simulating qudit circuits using Cirq's simulator.

---

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have a compatible Python version installed.
- **pip**: The Python package installer.
- **cirq**
- **numpy**

### Installing Cirq

<h3> Option 1: </h3>

1.1 **Install Cirq via pip**:

```bash
pip install cirq
```

1.2. **Verify the installation**

```
python -c "import cirq; print('Cirq version:', cirq.__version__)"
```

Ensure the version is 0.10.0 or higher for qudit support.

1.3 **Clone the Qudit Library Repository**

Clone the repository from GitHub:

```git
git clone https://github.com/svtsv01/qudit.git
```

1.4 Now the new notebook can be created.

If you have any issues go to <strong> step 2 </strong> and try to set up everything using Anaconda Navigator.

<h3> Option 2: </h3>

2. **Installing the Qudit Cirq Library via Anaconda**

#### Prerequisites

- **Anaconda** or **Miniconda** installed on your system.
- **Git** installed for cloning repositories.

---

2.1. **Create a New Anaconda Environment**

It's recommended to create a new environment to avoid conflicts with existing packages.

```bash
conda create -n qudit-env python=3.8
```

Replace 3.8 with your preferred Python version (3.7 or higher).

This creates an environment named qudit-env.

2.2 **Activate the Environment**

Activate the newly created environment:

```bash
conda activate qudit-env
```

On Windows, you might need to use:

```bash
activate qudit-env
```

2.3. **Install Cirq**

Install Cirq and other dependencies within the environment:

```bash
conda install -c conda-forge cirq numpy matplotlib
```

Alternatively, you can use pip: see step 1.1.

2.4. **Verify the Installation**

```bash
python -c "import cirq; print('Cirq version:', cirq.__version__)"
```

Ensure the version is 0.10.0 or higher for qudit support.

2.5. **Clone the Qudit Library Repository**

Clone the repository from GitHub:

```git
git clone https://github.com/svtsv01/qudit.git
```

2.6. **Navigate to the Library Directory**

Change to the library directory:

```
cd qudit
```

2.7. **Install the Qudit Library**

```
pip install -e .
```

---

## Dependencies

The Qudit Cirq Library depends on:

<ol>
<li>Cirq (>=0.10.0) </li>
<li>NumPy </li>
<li> Matplotlib (optional) </li>
</ol>
These dependencies should have been installed in step 3. If you encounter issues, ensure they are installed:

```
pip install cirq numpy matplotlib
```

## Fixing Common Dependency Issues

<strong> Version Conflicts </strong> </br>

Use the Anaconda environment (qudit-env) to manage dependencies and avoid conflicts with other Python packages.
</br>

Activate the environment:

```
conda activate qudit-env
```

List environments:

```
conda info --envs
```

<strong> Upgrading Packages </strong> </br>

If you have older versions of the packages, upgrade them:

```
pip install --upgrade cirq numpy matplotlib
```

## Constraints and limitations

While there are no hard-coded limits on the number of qudits, their dimensions, or the number of gates used, practical constraints arise from computational resources. Higher dimensions and larger numbers of qudits or operations significantly increase memory usage and simulation time. It’s generally advisable to keep the system size and gate count as small as possible for efficient simulations. For certain specialized gate the dimension must be prime, and parameters must be chosen carefully to ensure well-defined modular arithmetic.

## Cloud-Computing Services

For qudit-based quantum simulations and library usage, leveraging cloud computing services can help ensure scalability, cost-effectiveness, and ease of collaboration. Services like <strong> Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure </strong> can provide high-performance compute instances to run complex simulations efficiently.
