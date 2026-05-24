class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected_code):
        assert response.status_code == expected_code

    @staticmethod
    def validate_response_key(response_json, key):
        assert key in response_json