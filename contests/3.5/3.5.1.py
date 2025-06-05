def parse_numbers_from_stdin():
    import sys
    for line in sys.stdin:
        parts = line.strip().split()
        for token in parts:
            yield int(token)

print(sum(parse_numbers_from_stdin()))
