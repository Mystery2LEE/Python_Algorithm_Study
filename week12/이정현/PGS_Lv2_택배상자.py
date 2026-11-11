def solution(order):
    sub = []
    main = 1       
    count = 0      

    for q in order:
        if q >= main:
            sub.extend(range(main, q))
            main = q+1
            count += 1
        elif sub and sub[-1] == q:
            sub.pop()
            count += 1
        else:
            break

    return count