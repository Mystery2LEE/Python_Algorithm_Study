def solution(clothes):
    answer = 1
    
    closet = {}
    for Kind, Type in clothes:
        # 딕셔너리에 key가 없을 때 새로 만들기 value는 배열로
        if Type not in closet.keys():
            closet[Type] = [Kind]
        else:
            # key 존재하면 문자열 추가 -> 배열 합
            closet[Type] += [Kind]

    for key, value in closet.items():
        answer *= (len(value) + 1)
        
    return answer -1