from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()
api_key = os.environ.get("MY_API_KEY")

client = genai.Client(api_key=api_key)


def giving_hint(images):
    prompt = "read the images and give hints to solve the bugs with proper explanation make use to use markdown the important parts in at max 100 words"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents = [prompt, images]
    )

    return response.text

def solve_with_code(images):
    prompt = "give me the full corrected code with proper color and markdown in a structured way"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [prompt, images]
    )
    return response.text