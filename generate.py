import os
import datetime
import google.generativeai as genai

# Gemini API key
genai.configure(api_key=os.getenv("GEMINIAPIKEY"))

# Get current time for dynamic prompt
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a dynamic prompt so each run gives a new article
prompt = f"""
Write a brand-new, SEO-optimized trending blog article in HTML format.
Topic should be based on the most current global or tech trends as of {today}.
Include a catchy title, engaging intro, subheadings, and a short meta description.
At the end, add: "Published automatically by Gemini 2.5 Flash Lite AI".
"""

# Generate content using Gemini
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)

# Save the response in /posts folder with unique name
os.makedirs("posts", exist_ok=True)
filename = f"posts/article_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"✅ New article generated: {filename}")
