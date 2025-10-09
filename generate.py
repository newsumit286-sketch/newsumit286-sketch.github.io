import os
import google.generativeai as genai
from datetime import datetime

# Gemini API Key (GitHub Secrets se)
api_key = os.getenv("GEMINIAPIKEY")
genai.configure(api_key=api_key)

# ✅ Gemini model (latest working one)
model = genai.GenerativeModel("models/gemini-2.5-flash-lite")

# -------------------------------
# 🧠 Prompt: automatic article generation
# -------------------------------
prompt = """
Generate a trending, SEO-optimized blog article for today.
The article should:
- Have a catchy title
- Include an engaging 500-800 word body
- Include 5 relevant hashtags
- Include a 150-character SEO meta description
- Be written in simple, human-sounding English
- Be about trending or viral topics (tech, movies, AI, finance, or entertainment)
- At the end, add my social links in HTML:
  <p>Follow me on:
     <a href='https://instagram.com/sumit_official'>Instagram</a> |
     <a href='https://x.com/sumit_official'>Twitter</a> |
     <a href='https://youtube.com/@sumit_official'>YouTube</a>
  </p>
"""

# -------------------------------
# ✨ Generate article content
# -------------------------------
response = model.generate_content(prompt)
article = response.text.strip()

# -------------------------------
# 🕒 File save (timestamped)
# -------------------------------
today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"posts/article_{today}.html"

os.makedirs("posts", exist_ok=True)

# -------------------------------
# 🖋️ Save as HTML page
# -------------------------------
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Auto-generated trending article by AI. Stay updated with the latest trends.">
  <title>Auto-Generated Blog | Gemini AI</title>
</head>
<body style="font-family: Arial; margin: 40px;">
  {article}
  <hr>
  <p style="font-size: 14px; color: gray;">Published automatically by Gemini 2.5 Flash Lite AI</p>
</body>
</html>
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Article generated and saved as {filename}")
