import java.util.*;

public class Main {

    static class Node implements Comparable<Node>{
        int r;
        int c;
        int count;
        int min;

        Node(int r, int c, int count, int min){
            this.r = r;
            this.c = c;
            this.count = count;
            this.min = min;
        }

        @Override
        public int compareTo(Node o){
            //일단 min은 오름차순으로 가져가고 count는 내림차순? 그게 맞는듯?
            if(this.min == o.min) return o.count - this.count;
            return this.min - o.min;
        }
    }

    static int[][] grid;
    static int n;
    static int k;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = scanner.nextInt();
        // Please write your code here.
        //아 어차피 k는 100이라 최소값만 가져가면 되는구나 결국
        //일단 k만큼만 찾으면돼 더 안가고
        //시작은 각 노드부터 시작하고 bfs돌리면 될듯? 1만 * k -> 1만 * 100 100만 ㅇㅋ
        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int min = search(i, j);
                if(min == Integer.MAX_VALUE) continue;
                // System.out.println(min);
                answer = Math.min(answer, min); 
            }
        }

        if(answer == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(answer);
    }
    
    static int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    public static int search(int r, int c){
    
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(r, c, 1, 0));

        while(!pq.isEmpty()){
            Node cur = pq.poll();

            if(cur.count == k) return cur.min;

            for(int i = 0; i < 4; i++){
                int nr = cur.r + dir[i][0];
                int nc = cur.c + dir[i][1];

                if(nr >= 0 && nr < n && nc >= 0 && nc < n){
                    if(grid[cur.r][cur.c] < grid[nr][nc]){
                    
                        int dif = grid[nr][nc] - grid[cur.r][cur.c];
                        pq.add(new Node(nr, nc, cur.count + 1, Math.max(cur.min, dif)));
                    }
                }
            }
        }

        return Integer.MAX_VALUE;
    }
}
