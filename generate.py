import os
import google.generativeai as genai

# Gemini API key lena (GitHub secret se)
api_key = os.getenv("GEMINIAPIKEY")
genai.configure(api_key=api_key)

# Model initialize
model = genai.GenerativeModel("gemini-1.5-flash")

# Simple test run
prompt = "Hello Gemini! Is integration working?"
response = model.generate_content(prompt)

print(response.text)
