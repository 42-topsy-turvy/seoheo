N = int(input())
people = []

for i in range(N):
    people.append(int(input()))

people.sort(reverse=True)

total = 0
for i in range(N):
    tip = people[i] - i
    if tip < 0:
        break
    total += tip

print(total)