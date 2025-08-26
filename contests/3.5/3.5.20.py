def main():
    with open('numbers.num', 'rb') as f:
        data = f.read()

    limit = len(data) - (len(data) % 2)
    total = 0
    for i in range(0, limit, 2):
        val = int.from_bytes(data[i:i+2], 'big', signed=False)
        total = (total + val) & 0xFFFF

    print(total)


if __name__ == '__main__':
    main()