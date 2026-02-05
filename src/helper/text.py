# Formats date suffix 
def ordinal(n): 
    if 11 <= n % 100 <= 13: 
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

# Loads a given prompt
def loadPrompt(file, data):
    with open(file) as file:
        template = file.read()
    text = template.format(data=data)

    return text