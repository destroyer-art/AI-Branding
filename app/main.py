import os
import requests
import argparse
from pydantic import BaseModel, Field


def main():
    print("Running AI Branding...")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User Input: {user_input}")
    branding = generate_content(prompt=user_input)
    keywords = generate_keywords(prompt=user_input)
    print(branding, end="\n\n")
    print(keywords)


def generate_content(prompt: str) -> str:
    API_TOKEN = os.environ.get("HF_API_TOKEN")
    API_URL = f"https://api-inference.huggingface.co/models/google/flan-t5-xxl"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    new_prompt = f"Generate upbeat branding snippet for '{prompt}'"
    params = {
        "max_length": 30,  # The maximum number of tokens to generate
        "num_return_sequences": 5,  # The number of different texts to generate
        "temperature": 0.7,  # The randomness of the text generation
    }
    response = requests.post(
        url=API_URL, headers=headers, json={"inputs": new_prompt, "parameters": params}
    )
    result:str = response.json()[0]["generated_text"]
    result = result.strip()
    return result

def generate_keywords(prompt: str) -> str:
    API_TOKEN = os.environ.get("HF_API_TOKEN")
    API_URL = f"https://api-inference.huggingface.co/models/google/flan-t5-xxl"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    new_prompt = f"Generate cool branding keywords for '{prompt}'"
    params = {
        "max_length": 50,  # The maximum number of tokens to generate
        "num_return_sequences": 5,  # The number of different texts to generate
        "temperature": 0.6,  # The randomness of the text generation
    }
    response = requests.post(
        url=API_URL, headers=headers, json={"inputs": new_prompt, "parameters": params}
    )
    result:str = response.json()[0]["generated_text"]
    return result


if __name__ == "__main__":
    main()
