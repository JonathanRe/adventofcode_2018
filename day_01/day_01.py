def main():
    frequency = 0

    with open("input.txt") as f:
        for line in f:
            num = int(line.strip())
            frequency += num

    print(frequency)

main()
