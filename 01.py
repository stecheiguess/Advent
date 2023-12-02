
FILE = "inputs/01.txt"

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

keys = list(numbers.keys())


'''with open(FILE, "r") as file:
    lines = file.readlines()
    num = 0
    for line in lines:
        for i in line:
            if i.isnumeric():
                num += int(i) * 10
                break

        for i in reversed(line):
            if i.isnumeric():
                num += int(i)
                break


print(num) '''

# ======================


def check(string):
    if string[0].isnumeric():
        return int(string[0])

    for i in keys:
        if string.startswith(i):
            return numbers[i]

    return


# ====================== P1

with open(FILE, "r") as file:
    lines = file.readlines()
    num = 0
    for line in lines:
        digits = []

        for i in range(len(line)):
            if line[i].isnumeric():
                digits.append(int(line[i]))

        num += digits[0]*10 + digits[-1]

print(num)

# ---------------------- P2: convert words to digits

with open(FILE, "r") as file:
    lines = file.readlines()
    num = 0
    for line in lines:
        digits = []

        for i in range(len(line)):
            x = check(line[i:])
            if x:
                digits.append(x)

        num += digits[0]*10 + digits[-1]


print(num)
