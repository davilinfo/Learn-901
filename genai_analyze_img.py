from openai import OpenAI
from dotenv import load_dotenv
import base64
import os
from pathlib import Path

load_dotenv()

endpoint = os.getenv("OPENAI_API_BASE_URL")
deployment_name = "gpt-5-mini"
api_key = os.getenv("OPENAI_API_KEY")
"""foi necessário pegar uma imagem e colocar localmente"""
image_path = Path(__file__).with_name("Itaparicadrone.jpg")
image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "tell me about the image in the file itaparicadrone.jpg"},
            {"type": "input_image", "image_url": f"data:image/jpeg;base64,{image_data}"}
        ],
    }],
)

print(f"answer: {response.output_text}")