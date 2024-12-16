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
- **Circuit Utilities**: Functions to build and manipulate circuits with qudits, including a versatile `create_circuit` function.
- **Measurement and Simulation**: Support for measuring qudits and simulating qudit circuits using Cirq's simulator.

---

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have a compatible Python version installed.
- **pip**: The Python package installer.

### Installing Cirq

1.1 **Install Cirq via pip**:

```bash
pip install cirq
```

1.2. **Verify the installation**

```
python -c "import cirq; print('Cirq version:', cirq.__version__)"
```

<!-- In my case this command, the above command did not work. Instead this one worked:

python3 -c "import cirq; print('Cirq version:', cirq.__version__)"

-->

Ensure the version is 0.10.0 or higher for qudit support.

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

<!-- My installation is stuck at this step. Also, if I have already installed cirq, numpy, matplotlib, why do I have to install them again?
At this point it is also a good idea to have a "hello world" example to check if the environment is running correctly
-->

Alternatively, you can use pip: see step 1.1.

<!--
- I think this is a bit confusing. You can make it into two ways to install and number them separately: install via anaconda, or install via pip
- Also, the install cirq part is duplicate
-->

4. **Verify the Installation**

```bash
python -c "import cirq; print('Cirq version:', cirq.__version__)"
```

Ensure the version is 0.10.0 or higher for qudit support.

5. **Clone the Qudit Library Repository**

Clone the repository from GitHub:

```git
git clone link
```

<!--
Make sure to update the link
-->

6. **Navigate to the Library Directory**

Change to the library directory:

```
cd qudit-cirq-library
```

7. **Install the Qudit Library**

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

## <!-- again this is a repitition of the above. These things have been installed. -->

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

//to do

## Cloud-Computing Services

//to do

For qudit-based quantum simulations and library usage, leveraging cloud computing services can help ensure scalability, cost-effectiveness, and ease of collaboration. Services like <strong> Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure </strong> can provide high-performance compute instances to run complex simulations efficiently.

## References

-
-
-
