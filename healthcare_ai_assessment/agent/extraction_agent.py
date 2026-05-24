class ExtractionAgent:

    REQUIRED_FIELDS = [
        "patient_id",
        "name",
        "age",
        "gender",
        "symptoms",
        "blood_pressure",
        "heart_rate",
        "risk_expected"
    ]

    def extract_patient_data(self, raw_data):

        extracted_data = {
            "patient_id": raw_data.get("patient_id"),
            "name": raw_data.get("name"),
            "age": raw_data.get("age"),
            "gender": raw_data.get("gender"),
            "symptoms": raw_data.get("symptoms"),
            "blood_pressure": raw_data.get("blood_pressure"),
            "heart_rate": raw_data.get("heart_rate"),
            "risk_expected": raw_data.get("risk_expected")
        }

        return extracted_data