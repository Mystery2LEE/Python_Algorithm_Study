class Solution {
    boolean[] visit = null;
    int answer = 0;
    public int solution(int k, int[][] dungeons) {
        visit = new boolean[dungeons.length];
        dfs(k, 0, dungeons);
        return answer;
    }
    
    public void dfs(int k, int count, int[][] dungeons){
        answer = Math.max(answer, count);
        
        for(int i = 0 ; i < dungeons.length; i++){
            if(!visit[i] && k >= dungeons[i][0]){
                visit[i] = true;
                dfs(k - dungeons[i][1], count + 1, dungeons);
                visit[i] = false;
            }
        }
    }
}