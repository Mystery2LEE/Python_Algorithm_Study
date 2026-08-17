import java.io.*;
import java.util.*;

public class Solution {

    public static class Node implements Comparable<Node> {
        int to;
        int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    static List<Node>[] nodes;
    static int[] start = new int[2];
    static int[] end = new int[2];
    static boolean[] visited;
    static int result;
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            N = Integer.parseInt(br.readLine()) + 2;
            result = Integer.MAX_VALUE;
            int[][] points = new int[N][N];
            nodes = new ArrayList[N];
            visited = new boolean[N];
            for (int i = 0; i < N; i++) {
                nodes[i] = new ArrayList<>();
            }

            StringTokenizer st = new StringTokenizer(br.readLine());

            // start[0] = Integer.parseInt(st.nextToken());
            // start[1] = Integer.parseInt(st.nextToken());
            // end[0] = Integer.parseInt(st.nextToken());
            // end[1] = Integer.parseInt(st.nextToken());

            for (int i = 0; i < N; i++) {
                points[i][0] = Integer.parseInt(st.nextToken());
                points[i][1] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (i == j)
                        continue;
                    int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                    nodes[i].add(new Node(j, dist));
                }
            }

            for (int i = 0; i < N; i++) {
                Collections.sort(nodes[i]);
            }

            visited[0] = true;
            dfs(0, 0, 0);

            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void dfs(int node, int count, int cost) {
        if (cost >= result)
            return;

        if (count == N - 1 && node == 1) {
            result = Math.min(result, cost);
            return;
        } else if (count == N - 1 || node == 1) {
            return;
        }

        for (Node o : nodes[node]) {
            if (!visited[o.to]) {
                visited[o.to] = true;
                dfs(o.to, count + 1, cost + o.cost);
                visited[o.to] = false;
            }
        }
    }
}
