from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class RiskClassifier:

    def __init__(self):

        self.vectorizer = CountVectorizer()

        self.model = MultinomialNB()

        self.train_model()

    def train_model(self):

        training_symptoms = [

            "chest pain breathing difficulty",
            "severe chest pressure sweating",
            "cannot breathe properly",

            "dizziness high blood pressure",
            "chest pain dizziness",

            "mild headache",

            "normal tiredness"
        ]

        training_labels = [

            "Critical",
            "Critical",
            "Critical",

            "High",
            "High",

            "Low",

            "Medium"
        ]

        x_train = self.vectorizer.fit_transform(
            training_symptoms
        )

        self.model.fit(
            x_train,
            training_labels
        )

    def predict(self, symptoms):

        transformed_input = self.vectorizer.transform(
            [symptoms]
        )

        predicted_risk = self.model.predict(
            transformed_input
        )[0]

        recommendation = (
            self.generate_recommendation(
                predicted_risk
            )
        )

        return {
            "risk": predicted_risk,
            "recommendation": recommendation
        }

    def predict_risk(self, symptoms):

        transformed_input = self.vectorizer.transform(
            [symptoms]
        )

        return self.model.predict(
            transformed_input
        )[0]

    def generate_recommendation(self, risk):

        recommendations = {

            "Critical":
                "Immediate ER escalation required",

            "High":
                "Urgent doctor consultation required",

            "Medium":
                "Monitor symptoms closely",

            "Low":
                "Home care recommended"
        }

        return recommendations[risk]