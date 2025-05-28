def calculate_paracetamol_volume(weight_kg, strength_mg_per_5ml):  # Function to calculate the volume of paracetamol needed
    # Safety check 1: Validate weight
    if not (10 <= weight_kg <= 100):
        return "Error: Weight must be between 10 and 100 kg."

    # Safety check 2: Validate strength input
    if strength_mg_per_5ml not in [120, 250]:
        return "Error: Strength must be either 120 mg/5ml or 250 mg/5ml."

    # Calculate dose in mg
    dose_mg = 15 * weight_kg

    # Calculate required volume (in ml) = total dose ÷ (strength in mg/ml)
    mg_per_ml = strength_mg_per_5ml / 5
    volume_ml = dose_mg / mg_per_ml

    # Return volume rounded to 2 decimal places
    return round(volume_ml, 2)


# Drug Dosage Calculator for Paracetamol
if __name__ == "__main__":
    weight = float(input("Enter the patient's weight in kg (10–100): "))  # Input weight in kg
    strength = int(input("Enter paracetamol strength (120 or 250): "))    # Input strength in mg/5ml

    result = calculate_paracetamol_volume(weight, strength)  # Calculate the required volume of paracetamol
    print(result if isinstance(result, str) else f"Volume to give is: {result} ml")


# Example usage
print("\n--- Test Examples ---")
print("Example 1 (weight: 20 kg, strength: 120):", calculate_paracetamol_volume(20, 120))  # Expected: 12.5 ml
print("Example 2 (weight: 9 kg, strength: 120):", calculate_paracetamol_volume(9, 120))    # Expected: error message (too light)
print("Example 3 (weight: 30 kg, strength: 200):", calculate_paracetamol_volume(30, 200))  # Expected: error message (invalid strength)
print("Example 4 (weight: 35 kg, strength: 250):", calculate_paracetamol_volume(35, 250))  # Expected: 10.5 ml