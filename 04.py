FILE = "inputs/04.txt"

with open(FILE, "r") as file:
    lines = file.readlines()

    grandtotal = 0

    for l in range(len(lines)):
        line = lines[l].split(" | ")
        nums = line[0].split(": ")[1].split()
        winning = line[1].split()

        total = 0
        for i in nums:
            if i in winning:
                total += 1

        grandtotal += int(2**(total-1))

    print(grandtotal)


# --------------------------- P2: total scratchcards

with open(FILE, "r") as file:
    lines = file.readlines()

    cards = {}

    for i in range(len(lines)):
        cards[i] = 1

    for l in range(len(lines)):
        line = lines[l].split(" | ")
        nums = line[0].split(": ")[1].split()
        winning = line[1].split()

        total = 0
        for i in nums:
            if i in winning:
                total += 1

        for x in range(total):
            cards[l+x+1] += 1 * cards[l]

    print(sum(cards.values()))
