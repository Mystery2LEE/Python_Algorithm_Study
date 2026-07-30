T = int(input())

for test_case in range(1, T + 1):
    s_arr = list(input().strip())
    
    if s_arr == s_arr[::-1]:
        num = 1
    else:
        num = 0
    print(f"# {test_case} {num}")