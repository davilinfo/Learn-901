from azure.ai.contentunderstanding import ContentUnderstandingClient
import azure.ai.contentunderstanding.models as models
from azure.core.credentials import AzureKeyCredential
import os

client = ContentUnderstandingClient(
    endpoint=os.getenv("AZURE_CONTENT_UNDERSTANDING_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("AZURE_CONTENT_UNDERSTANDING_KEY"))
)

analyzer_id = "prebuilt-audioSearch"


try:
    acmodels = models.AnalysisInput(
        source=models.FileSource(
            source_url="https://learn901.blob.core.windows.net/ai-speech-resource/audio/AudioSample.mp3"
        )
    )
    audioing = client.begin_analyze(
        analyzer_id=analyzer_id,
        inputs=[
            acmodels
        ]
    )
    result = audioing.result()
except Exception as e:
    print(f"Error: {e}")

for content in result.contents:
    print(f"Content ID: {content.id}")
    print(getattr(content, "text", "No text available"))
    for segment in content.segments:
        print(f"Segment ID: {segment.id}")
        print(f"Start Time: {segment.start_time}")
        print(f"End Time: {segment.end_time}")
        print(f"Text: {segment.text}")
        print(f"Confidence Score: {segment.confidence_score}")

