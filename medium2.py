arr = input().split(" ")
max = 0
ans = 0
for i in range (0, len(arr)):
    if len(arr[i]) > max:
        max = len(arr[i])
        ans = i
print(arr[ans])