for tc in range(1, 11):
    n = int(input())
    str = input().split()
    m = int(input())
    cmd = input().split()
    idx = 0
    while idx < len(cmd):
        if cmd[idx] == "I":
            x = int(cmd[idx+1])
            y = int(cmd[idx+2])
            data = cmd[idx+3:idx+3+y]
            str[x:x] = data
            idx += 3+y
        elif cmd[idx] == "D":
            x = int(cmd[idx+1])
            y = int(cmd[idx+2])
            del str[x:x + y]
            idx += 3
        elif cmd[idx] == "A":
            y = int(cmd[idx+1])
            s = cmd[idx+2:idx+2+y]
            str.extend(s)
            idx += 2+y
    print(f'#{tc}', *str[:10])
