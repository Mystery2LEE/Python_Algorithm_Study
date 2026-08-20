n = int(input())
arr_list = list(map(int, input().split()))

arr_list.sort()
print(arr_list[n//2])