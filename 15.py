from pathlib import Path


def count_words(path):
    try:
        content = path.read_text(encoding="utf-8")
        print(content)
    except FileNotFoundError:
        print("File not found")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file contains {num_words} words.")


path = Path("alice.txt")
count_words(path)
