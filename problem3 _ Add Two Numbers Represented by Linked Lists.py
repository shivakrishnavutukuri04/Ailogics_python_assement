n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

ans = []
carry = 0

i = 0
j = 0

while i < n or j < m or carry > 0:
    x = a[i] if i < n else 0
    y = b[j] if j < m else 0

    total = x + y + carry

    digit = total % 10
    carry = total

    ans.append(digit)

    i += 1
    j += 1

print(*ans)
