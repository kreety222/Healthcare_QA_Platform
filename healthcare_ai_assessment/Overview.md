
# Healthcare AI Platform 

## Objective
Explain the repository structure, folder responsibilities, and QA validation strategy for UI, API, Agent, and Model integration.

## Architecture Summary
This project is organized as a QA assessment suite for a healthcare AI pipeline.
It includes raw data, an extraction agent, validation helpers, an AI risk classifier, API integration tests, and UI automation.

## Folder Breakdown

### `data/`
- Stores patient scenario files used by the tests.
- Includes `patient_test_data.json` with valid, invalid, and edge-case records.
- Also supports UI upload test fixtures such as invalid and large files.

### `agent/`
- Contains `extraction_agent.py`.
- The agent reads raw patient input and extracts the canonical fields.
- It normalizes patient data into the expected schema.
- This layer is tested by agent integration tests.

### `utils/`
- Contains `schema_validator.py` and `response_validator.py`.
- `schema_validator.py` validates patient records for required fields and field formats.
- `response_validator.py` checks API responses for correct status codes and expected JSON keys.
- This folder supports validation logic used across tests.

### `model/`
- Contains `risk_classifier.py`.
- Trains a simple text classifier on symptom strings and risk labels.
- Provides `predict_risk(symptoms)` for label prediction and `predict(symptoms)` for full risk + recommendation output.
- This layer is verified by model integration tests.

### `tests/`
- Contains integration tests for API, agent, and model components.
- `test_patient_api.py` validates REST behavior and response structure.
- `test_agent_integration.py` validates extraction and schema compliance.
- `test_model_integration.py` validates risk prediction and recommendation safety.

### `ui_tests/`
- Contains Playwright-based UI automation.
- `test_medical_upload_ui.py` verifies the document upload UI for invalid files, large uploads, and empty submissions.

## Validation Strategy

### UI Validation
- Simulates user interaction with file upload UI.
- Confirms unsupported file types are rejected.
- Confirms file size validation and empty upload handling.
- Ensures the UI shows the correct validation messages.

### API Validation
- Sends patient create requests to the API endpoint.
- Checks successful creation for valid payloads.
- Validates failure handling for invalid payloads.
- Uses response validators for status code and response key assertions.

### Agent Validation
- Ensures the extraction agent correctly maps raw patient records into the canonical model.
- Validates each extracted field using schema rules.
- Tests invalid payload handling and edge-case extraction.
- Includes duplicate detection and missing field failure tests.

### Model Integration Validation
- Verifies that symptom descriptions map to expected risk labels.
- Confirms edge-case risk predictions like critical breathing issues.
- Ensures no unsafe medical advice is produced.
- Validates the model does not leak PHI via recommendations.

## How to use this repository
1. Install dependencies: `py -m pip install -r requirements.txt`
2. Run the test suite: `py -m pytest -q`
3. Run UI tests separately: `py -m pytest -v ui_tests/test_medical_upload_ui.py`
4. Add new patient scenarios in `data/patient_test_data.json`.
5. Add model or agent validations by extending the `tests/` files.

