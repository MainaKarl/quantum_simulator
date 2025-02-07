import numpy as np
import random

# Qubit states
ket_0 = np.array([1, 0], dtype=complex)  # |0⟩
ket_1 = np.array([0, 1], dtype=complex)  # |1⟩

# Define basic gates
HADAMARD = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)  # Hadamard gate
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)  # Pauli-X gate

def apply_gate(qubit, gate):
    """
    Apply a quantum gate to a qubit.
    """
    return np.dot(gate, qubit)

def measure(qubit):
    """
    Simulate measurement of a qubit.
    Returns 0 or 1 with probabilities |a|^2 and |b|^2.
    """
    probabilities = np.abs(qubit) ** 2
    return 0 if random.random() < probabilities[0] else 1

def print_qubit_state(qubit):
    """
    Display the qubit's state vector and probabilities.
    """
    print(f"State vector: {qubit}")
    probabilities = np.abs(qubit) ** 2
    print(f"Probabilities: |0⟩ = {probabilities[0]:.2f}, |1⟩ = {probabilities[1]:.2f}")

# Initialize the qubit in state |0⟩
qubit = ket_0
print("Initial Qubit State:")
print_qubit_state(qubit)

# Apply the Hadamard gate to create superposition
qubit = apply_gate(qubit, HADAMARD)
print("\nAfter Applying Hadamard Gate:")
print_qubit_state(qubit)

# Measure the qubit
result = measure(qubit)
print(f"\nMeasurement Result: {result}")
