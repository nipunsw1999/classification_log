from sentence_transformers import SentenceTransformer
import joblib

# Load the saved model
classifier_model = joblib.load("models/log_classifier.joblib")

# Load the SentenceTransformer model to generate embeddings
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

def classify_with_bert(log_message):
    # Generate the log message embedding
    message_embedding = transformer_model.encode(log_message)

    # Predict the classification label
    predicted_class = classifier_model.predict(message_embedding)[0]
    return predicted_class


if __name__ == "__main__":
    log_message = [
        "User User1 logged in."
        "Backup started at 12:00."
        "Backup completed successfully."
        "System updated to version 1.0."
    ]

    for log in log_message:
        label = classify_with_bert(log)
        print(log, "->", label)