import os


FOLDER_PATH = r"C:\temp"


SEARCH_PHRASES = [
    "test",
]

CONTEXT_SIZE = 10


def search_in_file(file_path: str, phrases: list[str]) -> list[tuple[str, int]]:
    results = []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    content_lower = content.lower()

    for phrase in phrases:
        phrase_lower = phrase.lower()

        start = 0
        while True:
            index = content_lower.find(phrase_lower, start)
            if index == -1:
                break

            results.append((phrase, index))
            start = index + len(phrase_lower)

    return results, content


def get_context(content: str, index: int, size: int) -> str:
    start = max(0, index - size)
    end = index + size
    return content[start:end].replace("\n", " ")


def main():
    total_found = 0

    for filename in os.listdir(FOLDER_PATH):
        if not filename.endswith(".html"):
            continue

        file_path = os.path.join(FOLDER_PATH, filename)

        matches, content = search_in_file(file_path, SEARCH_PHRASES)

        if matches:
            print(f"\n=== {filename} ===")

            for phrase, index in matches:
                context = get_context(content, index, CONTEXT_SIZE)
                print(f"[{phrase}] -> ...{context}...")

                total_found += 1

    print(f"\n Total found text : {total_found}")


if __name__ == "__main__":
    main()