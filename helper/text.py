# Formats date suffix 
def ordinal(n): 
    if 11 <= n % 100 <= 13: 
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")