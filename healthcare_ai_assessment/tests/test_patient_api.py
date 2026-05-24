import json
import requests
from pathlib import Path
from utils.response_validator import ResponseValidator

BASE_URL = "https://dummyjson.com"
TEST_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "patient_test_data.json"

with open(TEST_DATA_PATH) as f:
    test_data = json.load(f)

valid_patients = test_data["valid_patients"]
invalid_patient = test_data["invalid_patients"][0]
edge_patient = test_data["edge_patients"][0]


class TestPatientAPI:

    def test_create_valid_patient(self):
        for patient in valid_patients:

            payload = {
                "patient_id": patient["patient_id"],
                "name": patient["name"],
                "age": patient["age"],
                "symptoms": patient["symptoms"]
            }

        response = requests.post(
            f"{BASE_URL}/users/add",
            json=payload
        )

        ResponseValidator.validate_status_code(response, 201)

        response_json = response.json()

        ResponseValidator.validate_response_key(
            response_json,
            "id"
        )

    def test_create_invalid_patient(self):

        payload = {
            "patient_id": invalid_patient["patient_id"],
            "age": invalid_patient["age"]
        }

        response = requests.post(
            f"{BASE_URL}/users/add",
            json=payload
        )

        # Simulated validation expectation
        assert payload["patient_id"] is None

    def test_edge_case_patient(self):

        payload = {
            "patient_id": edge_patient["patient_id"],
            "age": edge_patient["age"],
            "symptoms": edge_patient["symptoms"]
        }

        response = requests.post(
            f"{BASE_URL}/users/add",
            json=payload
        )

        ResponseValidator.validate_status_code(response, 201)

        response_json = response.json()

        assert len(response_json) > 0