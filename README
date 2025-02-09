# Quantum Circuit Simulation

This project is a simple quantum computing simulator written in Python. It demonstrates the fundamental principles of quantum mechanics, including quantum states, gates, and measurements.

## Features

- Simulates single-qubit states: |0⟩ and |1⟩.
- Implements basic quantum gates:
  - **Hadamard (H)**: Creates superposition.
  - **Pauli-X (X)**: Acts as a NOT gate, flipping |0⟩ to |1⟩ and vice versa.
- Simulates quantum measurement with probabilities based on the qubit state.
- Displays state vectors and measurement probabilities.

## Prerequisites

To run this project, you need:

- Python 3.6 or later
- `numpy` library

You can install `numpy` using pip:

```bash
pip install numpy
```

## How It Works

1. **Initialize the Qubit:**
   - The qubit starts in the |0⟩ state.

2. **Apply Quantum Gates:**
   - Use the Hadamard gate to create a superposition state.

3. **Measure the Qubit:**
   - Simulates the probabilistic collapse of the qubit into either |0⟩ or |1⟩ based on its state.

## Code Structure

### Qubit States
- `ket_0`: Represents the |0⟩ state.
- `ket_1`: Represents the |1⟩ state.

### Quantum Gates
- `HADAMARD`: The Hadamard gate for creating superposition.
- `PAULI_X`: The Pauli-X gate for flipping qubit states.

### Functions
- `apply_gate(qubit, gate)`: Applies a quantum gate to a given qubit.
- `measure(qubit)`: Simulates measurement of a qubit, returning 0 or 1 based on probabilities.
- `print_qubit_state(qubit)`: Displays the state vector and measurement probabilities of a qubit.

## Example Usage

```python
# Initialize the qubit in |0⟩ state
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
```

### Sample Output

```
Initial Qubit State:
State vector: [1.+0.j 0.+0.j]
Probabilities: |0⟩ = 1.00, |1⟩ = 0.00

After Applying Hadamard Gate:
State vector: [0.70710678+0.j 0.70710678+0.j]
Probabilities: |0⟩ = 0.50, |1⟩ = 0.50

Measurement Result: 0
```

## Potential Enhancements

- Add support for multi-qubit systems and tensor products.
- Implement additional gates like Pauli-Y, Pauli-Z, and phase gates.
- Simulate quantum entanglement and correlations.
- Visualize qubit states on the Bloch sphere.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Contributing

Contributions are welcome! If you have ideas to improve this project, feel free to fork the repository and submit a pull request.

