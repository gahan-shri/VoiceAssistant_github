import base64
import os
from google import genai
from google.genai import types
def generate(x):
    client = genai.Client(api_key= "AIzaSyC4k2PaJ03DraIvTahCMiu-cXgsdrANzbw")

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=x),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Give response in a single paragraph at most 5 to 100 words. And name your self as zero"""),
        ],
    )
    ans = ''
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        # print(chunk.text, end="")
        ans += chunk.text
    return ans

# if __name__ == "__main__":
#     a=generate("hi")
#     print(a)