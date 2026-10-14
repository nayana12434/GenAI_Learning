import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a model instance with config
model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 150
    },
    system_instruction="You are a concise AI tutor. Answer in 2-3 sentences."
)

# Call the model
result = model.generate_content("What is a vector database?")

print(result.text)
print(f"Token: {result.usage_metadata}")