n = input()
arr = map(int, input().split())
count_arr = {}
for a in arr:
    if a in count_arr:
        count_arr[a] += 1
    else:
        count_arr[a] = 1
    
print(f"#{n} {max(count_arr, key=count_arr.get)}")