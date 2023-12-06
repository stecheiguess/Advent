FILE = "inputs/05.txt"


def translate(n, Map):

    for i in range(len(Map)):
        if n >= Map[i][1] and n <= Map[i][1]+Map[i][2]:
            n += Map[i][0]-Map[i][1]
            return n

    return n


with open(FILE, "r") as file:
    seeds2 = []
    lines = file.read().split("\n\n")
    seeds = [int(x) for x in lines[0].split()[1:]]

    for n in seeds:
        for i in range(1, 8):
            n = translate(n, [[int(y) for y in x] for x in [x.split()
                          for x in lines[i].split("\n")[1:]]])
        seeds2.append(n)

    print(min(seeds2))

# -----------

with open(FILE, "r") as file:
    seeds2 = []
    lines = file.read().split("\n\n")
    seeds = [int(x) for x in lines[0].split()[1:]]

    soil = [[int(y) for y in x] for x in [x.split()
                                          for x in lines[1].split("\n")[1:]]]
    fert = [[int(y) for y in x] for x in [x.split()
                                          for x in lines[2].split("\n")[1:]]]
    water = [[int(y) for y in x] for x in [x.split()
                                           for x in lines[3].split("\n")[1:]]]
    light = [[int(y) for y in x] for x in [x.split()
                                           for x in lines[4].split("\n")[1:]]]
    temp = [[int(y) for y in x] for x in [x.split()
                                          for x in lines[5].split("\n")[1:]]]
    humid = [[int(y) for y in x] for x in [x.split()
                                           for x in lines[6].split("\n")[1:]]]
    loc = [[int(y) for y in x] for x in [x.split()
                                         for x in lines[7].split("\n")[1:]]]

    for i in range(1, len(seeds), 2):
        limit = seeds[i] + seeds[i-1]
        base = seeds[i-1]
        diff = 0
        while base + diff < limit:
            ans = base + diff

            ans = translate(ans, soil)
            ans = translate(ans, fert)
            ans = translate(ans, water)
            ans = translate(ans, light)
            ans = translate(ans, temp)
            ans = translate(ans, humid)
            ans = translate(ans, loc)

            seeds2.append(ans)
            diff += 1
            if diff % 100 == 0:
                seeds2 = [min(seeds2)]

        print(min(seeds2))
