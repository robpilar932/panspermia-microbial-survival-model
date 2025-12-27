import math

def calculate_survival(uv_dose, decay_constant):
    """
    Calculate the survival fraction of Deinococcus radiodurans under UV radiation.
    
    Uses an exponential decay model: S(d) = exp(-k * d)
    where S is survival fraction (0 to 1), d is UV dose, k is decay constant.
    
    Parameters
    ----------
    uv_dose : float
        UV radiation dose (in arbitrary units, e.g., J/m^2).
    decay_constant : float
        Decay constant representing microbial sensitivity to UV (unit: 1/(dose unit)).
        Typical values for D. radiodurans range from ~0.001 to 0.05 per J/m^2
        based on experimental data (example range).
        
    Returns
    -------
    float
        Survival fraction between 0 and 1.
    """
    survival = math.exp(-decay_constant * uv_dose)
    return survival


if __name__ == "__main__":
    # Example usage
    dose = 100.0  # Example UV dose
    k = 0.01      # Example decay constant (typical value for D. radiodurans)
    fraction = calculate_survival(dose, k)
    print(f"UV dose: {dose}, survival fraction: {fraction:.4f}")