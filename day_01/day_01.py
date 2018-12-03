def main():
    frequency   = 0
    variations  = []
    match_found = False

    # while not match_found:
    with open("input.txt") as f:
        for line in f:
            change = int(line.strip())
            frequency += change
            variations.append(frequency)
            print(frequency)
            # if frequency not in variations:
            #     variations.append(frequency)
            # else:
            #     match_found = True
            #     print("Answer to part 2: " + str(frequency))
            #     break

    print("Answer to part 1: " + str(frequency))

main()
