class Solution {
    int solution(int[][] land) {
        int answer = 0;
        int width = land[0].length;
        int height = land.length;
        int[][] dp = new int[height + 1][width];
        //dp값 전체 계산
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                int temp = land[i][j];
                for(int k = 0; k < width; k++){
                    if(k == j) continue;
                    dp[i + 1][j] = Math.max(dp[i + 1][j], temp + dp[i][k]);
                }
            }
        }
        
        //가장 아래행에 맥스값 찾기
        for(int i = 0; i < width; i++){
            answer = Math.max(answer, dp[height][i]);
        }
        return answer;
    }
}