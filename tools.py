# 👉 tools.py

from llm import call_llm   # ✅ always at top


def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        return "File not found"


def summarize_text(text):
    try:
        return call_llm([
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text clearly."
            },
            {
                "role": "user",
                "content": f"Summarize this:\n{text}"
            }
        ])
    except:
        return "Error in summarizing"