def export_prompt(prompt: str, filename: str) :

    if not filename.endswith(".txt"):
        raise ValueError("Only .txt file are supported")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(prompt)

    return f"Prompt exported successfully to '{filename}"