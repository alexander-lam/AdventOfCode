input = open('input1.txt', 'r').read().splitlines()
num = 50
count1 = 0
count2 = 0

for line in input:
    if line[0] == 'R':
        for _ in range(int(line[1:])):
            num += 1
            if num % 100 == 0:
                count2 += 1
    elif line[0] == 'L':
        for _ in range(int(line[1:])):
            num -= 1
            if num % 100 == 0:
                count2 += 1
    if num % 100 == 0:
        count1 += 1
print(count1)
print(count2)