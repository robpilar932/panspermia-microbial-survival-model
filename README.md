# Panspermia Microbial Survival Model

A simple computational model for microbial survival under space conditions, simulating aspects of the Japanese Tanpopo experiment that tests the panspermia hypothesis.

## Mathematical Model

The model uses an exponential decay function to estimate the survival fraction of *Deinococcus radiodurans* under UV radiation:

```
S(d) = e^(-k * d)
```

Where:
- `S` is the survival fraction (0 to 1)
- `d` is the UV radiation dose (e.g., in J/m²)
- `k` is a decay constant representing the microbe's sensitivity to UV

## Usage

Import the `calculate_survival` function from `survival_model.py`:

```python
from survival_model import calculate_survival

# Example parameters
uv_dose = 150.0          # UV dose in J/m²
decay_constant = 0.015   # Approximate sensitivity for D. radiodurans

survival = calculate_survival(uv_dose, decay_constant)
print(f"Survival fraction: {survival:.4f}")
```

## Project Context

This model is a simplified representation of the kind of analysis performed in astrobiology to assess the feasibility of interplanetary transfer of life (panspermia). The Tanpopo experiment, conducted on the International Space Station, exposes microbial samples to space to study their survival. This code provides a starting point for simulating one of the key environmental stressors: ultraviolet radiation.

## License

This project is open source under the MIT License.