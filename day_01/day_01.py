def main():
    frequency   = 0
    variations  = []
    match_found = False

    with open("input.txt") as f:
        while not match_found:
            for line in f:
                change = int(line.strip())
                frequency += change
                # print(frequency)
                if frequency not in variations:
                    variations.append(frequency)
                else:
                    match_found = True
                    print("Answer to part 2: " + str(frequency))
                    break
            print(frequency)

    print("Answer to part 1: " + str(frequency))

main()
