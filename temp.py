from helper.text import loadPrompt

from json import load

# Load Data for Document
with open("data.json", "r", encoding="utf-8") as f:
    data = load(f)