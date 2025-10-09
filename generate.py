import os
import google.generativeai as genai
from datetime import datetime

# Gemini API key from GitHub Secrets
api_key = os.getenv("GEMINIAPIKEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

def generate_article(topic, region):
    prompt = f"""
    Write a detailed, human-like, SEO-optimized blog article in English about the trending topic '{topic}'.
    The article should be written for {region} readers. Use storytelling tone, deep insights, and natural flow.
    Include headers, short paragraphs, and an SEO meta description at the end.
    """
    response = model.generate_content(prompt)
    return response.text

def save_article(content, region):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"posts/{region.lower()}_article_{now}.html"
    os.makedirs("posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{region} | Auto AI Blog</title>
</head>
<body style="font-family: Arial; margin: 40px;">
{content}
<hr>
<p style="font-size:14px;color:gray;">Published automatically by Gemini 2.5 Flash Lite AI</p>
</body>
</html>""")
    print(f"✅ Saved: {filename}")

def main():
    topics = ["latest AI trends", "emerging tech innovations"]
    regions = ["India", "Global"]
    for topic, region in zip(topics, regions):
        print(f"📰 Generating {region} article...")
        content = generate_article(topic, region)
        save_article(content, region)
    print("✨ All articles generated successfully!")

if __name__ == "__main__":
    main()
# --- Append this at the end of generate.py ---

import os

posts_dir = "posts"
index_file = "index.html"

# Get all post files
posts = sorted(os.listdir(posts_dir), reverse=True)

# Generate list of links
links_html = "\n".join([
    f'<li><a href="posts/{p}">{p.replace("_", " ").replace(".html", "")}</a></li>'
    for p in posts if p.endswith(".html")
])

# Create or update index.html
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI Auto Blog</title>
  <meta name="description" content="Automatically updated AI-generated blog using Gemini 2.5 Flash Lite">
</head>
<body style="font-family: Arial; margin: 40px;">
  <h1>📰 Latest AI-Generated Articles</h1>
  <ul>{links_html}</ul>
  <hr>
  <p style="font-size: 14px; color: gray;">Updated automatically by Gemini AI — {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC</p>
</body>
</html>
"""

with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_content)

print("✅ index.html updated with latest blog post links.")
