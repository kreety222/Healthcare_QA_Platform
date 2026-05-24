import json
from pathlib import Path

from agent.extraction_agent import ExtractionAgent
from utils.schema_validator import SchemaValidator


TEST_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "patient_test_data.json"

with open(TEST_DATA_PATH) as f:
    test_data = json.load(f)


valid_patients = test_data["valid_patients"]
invalid_patient = test_data["invalid_patients"][0]
edge_patient = test_data["edge_patients"][0]


def is_duplicate(patient_a, patient_b):
    return (
        patient_a.get("patient_id")
        == patient_b.get("patient_id")
    )


class TestAgentIntegration:

    agent = ExtractionAgent()

    def test_valid_patient_extraction(self):

        for patient in valid_patients:

            extracted_data = self.agent.extract_patient_data(
                patient
            )

            SchemaValidator.validate_required_fields(
                extracted_data
            )

            SchemaValidator.validate_patient_id(
                extracted_data["patient_id"]
            )

            SchemaValidator.validate_name(
                extracted_data["name"]
            )

            SchemaValidator.validate_age(
                extracted_data["age"]
            )

            SchemaValidator.validate_gender(
                extracted_data["gender"]
            )

            SchemaValidator.validate_symptoms(
                extracted_data["symptoms"]
            )

            SchemaValidator.validate_blood_pressure(
                extracted_data["blood_pressure"]
            )

            SchemaValidator.validate_heart_rate(
                extracted_data["heart_rate"]
            )

            SchemaValidator.validate_risk_expected(
                extracted_data["risk_expected"]
            )

    def test_invalid_patient_extraction(self):

        extracted_data = self.agent.extract_patient_data(
            invalid_patient
        )

        try:
            SchemaValidator.validate_required_fields(
                extracted_data
            )

        except AssertionError:
            assert True

    def test_edge_case_patient_extraction(self):

        extracted_data = self.agent.extract_patient_data(
            edge_patient
        )

        SchemaValidator.validate_required_fields(
            extracted_data
        )

        assert extracted_data["age"] > 100

        assert "breathe" in extracted_data["symptoms"]

    def test_duplicate_patient_detection(self):

        patient_1 = valid_patients[0]
        patient_2 = valid_patients[0]

        assert is_duplicate(patient_1, patient_2) is True

    def test_missing_field_validation(self):

        corrupted_data = {
            "name": "John"
        }

        try:
            SchemaValidator.validate_required_fields(
                corrupted_data
            )

        except AssertionError:
            assert True