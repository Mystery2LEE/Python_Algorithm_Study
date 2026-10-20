class Solution {
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(numbers.length, 0, numbers, target);
        return answer;
    }
    
    public void dfs(int count, int sum ,int[] numbers, int target){
        if(count == 0){
            if(sum == target) answer++;
            return;
        }
        count--;
        int plus = sum + numbers[count];
        int minus = sum - numbers[count];
        dfs(count, plus, numbers, target);
        dfs(count, minus, numbers, target); 
    }
}