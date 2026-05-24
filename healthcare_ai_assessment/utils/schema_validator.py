class SchemaValidator:

    @staticmethod
    def validate_required_fields(data):

        required_fields = [
            "patient_id",
            "name",
            "age",
            "gender",
            "symptoms",
            "blood_pressure",
            "heart_rate",
            "risk_expected"
        ]

        for field in required_fields:
            assert field in data
            assert data[field] is not None
            assert data[field] != ""

    @staticmethod
    def validate_patient_id(patient_id):

        assert patient_id.startswith("P")

    @staticmethod
    def validate_name(name):

        assert isinstance(name, str)
        assert len(name) > 2

    @staticmethod
    def validate_age(age):

        assert isinstance(age, int)
        assert age > 0
        assert age < 120

    @staticmethod
    def validate_gender(gender):

        valid_genders = [
            "Male",
            "Female",
            "Other"
        ]

        assert gender in valid_genders

    @staticmethod
    def validate_symptoms(symptoms):

        assert isinstance(symptoms, str)
        assert len(symptoms) > 3

    @staticmethod
    def validate_blood_pressure(bp):

        assert "/" in bp

        systolic, diastolic = bp.split("/")

        assert systolic.isdigit()
        assert diastolic.isdigit()

    @staticmethod
    def validate_heart_rate(hr):

        assert isinstance(hr, int)

        assert hr > 30
        assert hr < 220

    @staticmethod
    def validate_risk_expected(risk):

        valid_risks = [
            "Low",
            "Medium",
            "High",
            "Critical",
            "Validation Error"
        ]

        assert risk in valid_risks