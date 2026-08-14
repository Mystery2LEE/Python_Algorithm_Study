T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    dump_count = int(input())
    boxes = list(map(int, input().split()))
    
    
    def flatten(boxes):
        boxes.sort(reverse=True)
        boxes[0] -= 1
        boxes[99] += 1
        boxes.sort(reverse=True)
        
    while dump_count:
        flatten(boxes)
        if boxes[0] - boxes[99] < 2:
            break
        dump_count -= 1
        
            
        
    print(f'#{test_case} {boxes[0] - boxes[99]}')