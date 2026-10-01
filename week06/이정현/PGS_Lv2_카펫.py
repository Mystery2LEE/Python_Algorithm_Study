def solution(brown, yellow):
    # yellow 개수 만큼 반복
    for i in range(1,yellow+1):
        # 만약 yellow 나눠지는 값이면
        if yellow % i == 0:
            # 갈색 대각선 개수를 제외한 것이 가로, 세로 2배해서 더한 것과 같으면
            if (brown-4) == 2*i + (yellow//i)*2:
                # 가로 세로 값 리턴
                return [(yellow//i)+2, i+2]