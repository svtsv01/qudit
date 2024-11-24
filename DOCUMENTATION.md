# Qudit Cirq Library Documentation

This library extends Google's Cirq framework to support **qudits**.

---

## Introduction

Quantum computing relies on the concept of **qubits**, which are two-dimensional quantum systems. However, **qudits** generalise this concept to d-dimensional quantum systems, providing a richer computational space and potential advantages in quantum algorithms.

The qudit Cirq library enhances Cirq by:

- Qudit gates for arbitrary dimensions - d .
- Utilities for creating and manipulating qudit circuits.
- Simulation and measurement of qudit-based quantum circuits.

---

## Features

- **Qudit Support**: Work with qudits of any dimension.
- **Generalized Gates**: Implementations of qudit versions of common quantum gates:
  - Pauli-X Gate
  - Pauli-Z Gate
  - Hadamard Gate
  - Controlled-NOT Gate
- **Circuit Utilities**: Functions to build and manipulate circuits with qudits, including a versatile `create_circuit` function.
- **Measurement and Simulation**: Support for measuring qudits and simulating qudit circuits using Cirq's simulator.

---

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have a compatible Python version installed.
- **pip**: The Python package installer.

### Installing Cirq
