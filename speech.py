import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set the endpoint and key
endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")
key = os.getenv("TEXT_ANALYTICS_KEY")

# Create the TextAnalyticsClient
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def recognize_pii_entities(texts):
    """
    Recognize Personally Identifiable Information (PII) entities in the given texts.

    :param texts: A list of strings to analyze for PII entities.
    :return: The response from the Text Analytics service.
    """
    response = client.recognize_pii_entities(texts)
    return response

result = recognize_pii_entities(["My name is John Doe and my email is john.doe@example.com"])
print(result)
print("Recognized PII entities:")
for entity in result[0].entities:
    print(f"Text: {entity.text}, Category: {entity.category}, Subcategory: {entity.subcategory}, Confidence Score: {entity.confidence_score}")