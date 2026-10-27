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
        //일단 k만큼만 찾으면돼 더 안가고 왜안되지... 
        int answer = search();

        if(answer == Integer.MAX_VALUE) answer = -1;
        System.out.println(answer);
    }
    
    static int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    public static int search(){
    
        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean[][][] visited = new boolean[n][n][k + 1];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                pq.add(new Node(i, j, 1, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (visited[cur.r][cur.c][cur.count]) continue;
            visited[cur.r][cur.c][cur.count] = true;

            if (cur.count == k) return cur.min;   // 처음 도달한 게 최적

            for (int[] d : dir) {
                int nr = cur.r + d[0], nc = cur.c + d[1];
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if (grid[cur.r][cur.c] >= grid[nr][nc]) continue;
                if (visited[nr][nc][cur.count + 1]) continue;

                int dif = grid[nr][nc] - grid[cur.r][cur.c];
                pq.add(new Node(nr, nc, cur.count + 1, Math.max(cur.min, dif)));
            }
        }

        return -1;
    }
}

