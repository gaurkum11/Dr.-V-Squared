# step1: setup GROQ API key
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# step2: convert image to required format

#image_path = "burn.jpg"
import base64  #it convert bits/byte to string

def encode_image(image_path):
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


# step3: setup Multimodal LLM
from groq import Groq
# completion = client.chat.completions.create(
#     model="llama-3.2-90b-vision-preview",
#     messages=[],
#     temperature=1,
#     max_completion_tokens=1024,
#     top_p=1,
#     stream=False,
#     stop=None,
# )

query="Is there something wrong my hand?"
model="llama-3.2-90b-vision-preview"
def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages=[
        {
            "role" : "user",
            "content": [
                {
                    "type" : "text",
                    "text" : query
                },
                {
                    "type": "image_url",
                    "image_url" : {
                        "url" : f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content
    #print(completion.choices[0].message)


