# Synthetic Patient Data
## NIW Evidence - Healthcare Data Pipeline

### Purpose
- MVP testing without real patient data
- HIPAA-compliant development
- AI model training and validation

### Data Specifications
- **Volume**: 1,000 synthetic patient records
- **Features**: Age, BMI, HbA1c, Blood Pressure, Cholesterol
- **Compliance**: No real patient data used
- **Status**: Active development for NIW petition

### Usage
```python
from generate_data import SyntheticDataGenerator
patients = SyntheticDataGenerator().generate_patients()
