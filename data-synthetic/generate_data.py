"""
Synthetic Patient Data Generator
NIW Evidence - HIPAA-compliant data pipeline
"""

import pandas as pd
import numpy as np

class SyntheticDataGenerator:
    def __init__(self, patient_count=1000):
        self.patient_count = patient_count
        print("✅ SyntheticDataGenerator initialized - NIW Evidence")
        
    def generate_patients(self):
        """Generate synthetic patient data for MVP testing"""
        np.random.seed(42)
        
        data = {
            'patient_id': range(1, self.patient_count + 1),
            'age': np.random.randint(30, 80, self.patient_count),
            'bmi': np.round(np.random.uniform(18.5, 45, self.patient_count), 1),
            'hba1c': np.round(np.random.uniform(5.0, 12.0, self.patient_count), 1),
            'blood_pressure': np.random.randint(90, 180, self.patient_count),
            'cholesterol': np.random.randint(150, 300, self.patient_count),
        }
        
        df = pd.DataFrame(data)
        print(f"✅ Generated {len(df)} synthetic patient records - NIW Evidence")
        return df

# NIW Proof - Working code
if __name__ == "__main__":
    generator = SyntheticDataGenerator()
    patients = generator.generate_patients()
