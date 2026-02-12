

from google import genai

client = genai.Client(api_key="AIzaSyCCtoihMAXdfZBdwXJb-mlW8ZiPJUWW628")

for model in client.models.list():
    print(model.name)
