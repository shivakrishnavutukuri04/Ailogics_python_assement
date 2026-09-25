## probelm 2  Longest Stable Signal Window

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_len = 0
start_pos = 1

for i in range(n):
    min_val = arr[i]
    max_val = arr[i]

    for j in range(i, n):
        if arr[j] < min_val:
            min_val = arr[j]
        if arr[j] > max_val:
            max_val = arr[j]

        if max_val - min_val <= k:
            length = j - i + 1
            if length > max_len:
                max_len = length
                start_pos = i + 1
        else:
            break

print(max_len, start_pos)
