import java.util.*;

class Solution {
    static int[][] dir = new int[][] { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

    static class Node implements Comparable<Node> {
        int x;
        int y;
        int cost;

        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int[][] arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                String s = sc.next();
                for (int j = 0; j < N; j++) {
                    arr[i][j] = s.charAt(j) - '0';
                }
            }

            int[][] dist = new int[N][N];
            for (int i = 0; i < N; i++) {
                Arrays.fill(dist[i], Integer.MAX_VALUE);
            }

            PriorityQueue<Node> pq = new PriorityQueue<>();
            dist[0][0] = 0;
            pq.add(new Node(0, 0, 0));

            while (!pq.isEmpty()) {
                Node node = pq.poll();
                int x = node.x;
                int y = node.y;
                int cost = node.cost;

                if (x == N - 1 && y == N - 1)
                    break;

                if (cost > dist[x][y])
                    continue;

                for (int i = 0; i < 4; i++) {
                    int nextX = x + dir[i][0];
                    int nextY = y + dir[i][1];

                    if (nextX >= 0 && nextX < N && nextY >= 0 && nextY < N) {
                        if (dist[nextX][nextY] > cost + arr[nextX][nextY]) {
                            dist[nextX][nextY] = cost + arr[nextX][nextY];
                            pq.add(new Node(nextX, nextY, dist[nextX][nextY]));
                        }
                    }
                }
            }

            System.out.println("#" + test_case + " " + dist[N - 1][N - 1]);
        }
    }
}