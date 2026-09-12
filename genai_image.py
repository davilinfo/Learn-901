from openai import OpenAI
import os
import base64

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), 
                base_url=os.getenv("OPENAI_API_BASE_URL") )

prompt = "Generate an image of a bridge linking the Itaparica island Salvador Bahia with a beautiful ship sailing upon baía de todos os santos, with a beautiful sunset in the background.   "

result = client.images.generate(
    prompt=prompt, 
    size="1024x1024",
    model="gpt-image-2")

base64_image = base64.b64decode(result.data[0].b64_json)
print("Image Base64:", base64_image)

