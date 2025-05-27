# Patient Record Management

class patients:
    def __init__(self, name, age, latest_admission, medical_history):
        self.name = name
        self.age = age
        self.latest_admission = latest_admission
        self.medical_history = medical_history

    def print_details(self):
        print(f"Patient name: {self.name}, Age: {self.age}, Date of latest admission: {self.latest_admission}, Medical history: {self.medical_history}")


# Example usage
if __name__ == "__main__":
    # Create a patient record
    patient1 = patients(
        name="San Zhang",
        age=30,
        latest_admission="2025-01-15",
        medical_history="Asthma since childhood, no recent hospitalizations."
    )

    # Print patient information
    patient1.print_details()