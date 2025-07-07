import sys


def normalize_whitespace(text: str) -> str:
    return " ".join(text.lower().split())


def main():
    lines = [line.rstrip('\n') for line in sys.stdin]

    if not lines:
        print("404. Not Found")
        return

    raw_query = lines[0]
    query = normalize_whitespace(raw_query)

    filenames = lines[1:]

    found_files = []

    for fname in filenames:
        try:
            with open(fname, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            continue

        norm_content = normalize_whitespace(content)

        if query in norm_content:
            found_files.append(fname)

    if found_files:
        print("\n".join(found_files))
    else:
        print("404. Not Found")

if __name__ == "__main__":
    main()
