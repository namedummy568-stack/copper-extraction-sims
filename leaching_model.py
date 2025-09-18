
import numpy as np

def simulate_leaching(ore_grade, acid_concentration, time_hours, temperature_celsius):
    """
    Simulates the copper leaching process.

    Args:
        ore_grade (float): Percentage of copper in the ore.
        acid_concentration (float): Concentration of leaching acid (e.g., H2SO4) in mol/L.
        time_hours (float): Duration of the leaching process in hours.
        temperature_celsius (float): Temperature of the leaching process in Celsius.

    Returns:
        float: Percentage of copper extracted.
    """
    # Simple linear model for demonstration purposes
    # In a real scenario, this would be a complex kinetic model
    base_extraction = 0.1 * ore_grade
    acid_effect = 0.05 * acid_concentration
    time_effect = 0.02 * time_hours
    temp_effect = 0.01 * (temperature_celsius - 25) # Assuming 25C as baseline

    extraction_rate = base_extraction + acid_effect + time_effect + temp_effect

    # Ensure extraction doesn't exceed ore grade
    extracted_copper = min(extraction_rate, ore_grade)

    return extracted_copper

if __name__ == "__main__":
    # Example usage
    ore = 1.5 # 1.5% copper ore
    acid = 0.5 # 0.5 mol/L acid
    time = 48 # 48 hours
    temp = 35 # 35 degrees Celsius

    extracted = simulate_leaching(ore, acid, time, temp)
    print(f"Simulated copper extraction: {extracted:.2f}%")

    ore = 2.0
    acid = 1.0
    time = 72
    temp = 50
    extracted = simulate_leaching(ore, acid, time, temp)
    print(f"Simulated copper extraction: {extracted:.2f}%")
