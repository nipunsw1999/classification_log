from sentence_transformers import SentenceTransformer
import joblib


def classify_with_bert(log_message):
    # Load the saved model
    classifier_model = joblib.load("models/log_classifier.joblib")

    # Load the SentenceTransformer model to generate embeddings
    transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

    # Generate the log message embedding
    message_embedding = transformer_model.encode(log_message)

    # Predict the classification label
    predicted_class = classifier_model.predict(message_embedding)[0]
    return predicted_class
