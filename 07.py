FILE = "inputs/07.txt"


def check(dict):
    k = len(dict.keys())
    v = max(dict.values())
    if k == 5:
        return 0  # high card, nothing is the same
    elif k == 4:
        return 1  # one pair, has to have 1 value that occurs twice
    elif k == 3:
        if v == 3:
            return 3  # 3 values, one that occurs thrice, 3 of a kind
        return 2  # 3 values, two occur twice, two pair
    elif k == 2:
        if v == 3:
            return 4  # 2 values, 1 that occurs thrice and twice for other, full house
        return 5  # 2 values, 1 that occurs 4 times, 4 of a kind
    else:
        return 6  # all the same, five of a kind

# =================================


RANKING = "23456789TJQKA"

with open(FILE, "r") as file:

    lines = [l.split() for l in file.readlines()]
    total = 0
    hands = {}
    rank = 1

    for l in lines:
        dic = {}
        for c in l[0]:
            dic[c] = dic.get(c, 0) + 1

        hands.setdefault(check(dic), []).append((l[0], l[1]))

    for i in range(len(hands)):
        byRank = sorted(hands[i], key=lambda word: [RANKING.index(c)
                                                    for c in word[0]])

        for j in byRank:
            total += int(j[1])*rank
            rank += 1

    print(total)


# ------------------------------------

RANKING = "J23456789TQKA"

with open(FILE, "r") as file:
    lines = [l.split() for l in file.readlines()]
    total = 0
    hands = {}
    rank = 1

    for l in lines:
        dic = {}
        for c in l[0]:
            dic[c] = dic.get(c, 0) + 1

        if "J" in dic and dic["J"] != 5:
            ans = dic.pop("J")
            dic[max(dic, key=dic.get)] += ans

        hands.setdefault(check(dic), []).append((l[0], l[1]))

    for i in range(len(hands)):
        byRank = sorted(hands[i], key=lambda word: [RANKING.index(c)
                                                    for c in word[0]])
        for j in byRank:
            total += int(j[1])*rank
            rank += 1

    print(total)
