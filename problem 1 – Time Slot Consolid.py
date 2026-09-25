#### problem 1 – Time Slot Consolidation


n = int(input())

ranges = []
for i in range(n):
    start, end = map(int, input().split())
    ranges.append([start, end])
ranges.sort()

merged = []

for current in ranges:
    if not merged or current[0] > merged[-1][1]:
        merged.append(current)
    else:
        if current[1] > merged[-1][1]:
            merged[-1][1] = current[1]

for start, end in merged:
    print(start, end)


