import java.util.*;
import java.io.*;

import java.io.*;
import java.util.*;

public class Solution {
    static class Node implements Comparable<Node> {
        int r;
        int c;
        int cost;

        Node(int r, int c, int cost) {
            this.r = r;
            this.c = c;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    static int[][] move = new int[][] { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } };
    static int[][] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());

            arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] dist = new int[N][N];
            for (int i = 0; i < N; i++) {
                Arrays.fill(dist[i], Integer.MAX_VALUE);
            }

            PriorityQueue<Node> pq = new PriorityQueue<>();
            pq.add(new Node(0, 0, 0));
            dist[0][0] = 0;

            while (!pq.isEmpty()) {
                Node cur = pq.poll();
                int curR = cur.r;
                int curC = cur.c;
                int curCost = cur.cost;

                if (dist[curR][curC] < curCost)
                    continue;

                if (curR == N - 1 && curC == N - 1)
                    break;

                for (int i = 0; i < 4; i++) {
                    int nextR = curR + move[i][0];
                    int nextC = curC + move[i][1];
                    if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < N) {
                        int add = 0;
                        if (arr[nextR][nextC] <= arr[curR][curC])
                            add += 1;
                        else
                            add += (arr[nextR][nextC] - arr[curR][curC] + 1);
                        if (dist[nextR][nextC] > dist[curR][curC] + add) {
                            dist[nextR][nextC] = dist[curR][curC] + add;
                            pq.add(new Node(nextR, nextC, dist[nextR][nextC]));
                        }
                    }
                }
            }

            result.append("#").append(test_case).append(" ").append(dist[N - 1][N - 1]).append("\n");
        }

        System.out.println(result.toString());
    }
}
