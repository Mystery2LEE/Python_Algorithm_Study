import java.util.*;
import java.io.*;

import java.io.*;
import java.util.*;

public class Solution {

    static List<Integer>[] graph;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            graph = new ArrayList[V + 1];
            for (int i = 0; i <= V; i++) {
                graph[i] = new ArrayList<>();
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph[from].add(to);
                graph[to].add(from);
            }

            int count = 0;
            boolean[] visited = new boolean[V + 1];
            for (int i = 1; i <= V; i++) {
                if (visited[i])
                    continue;
                count++;
                bfs(i, visited);
            }

            result.append("#").append(test_case).append(" ").append(count).append("\n");
        }

        System.out.println(result.toString());
    }

    public static void bfs(int start, boolean[] visited) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int node : graph[cur]) {
                if (visited[node])
                    continue;
                visited[node] = true;
                q.add(node);
            }
        }
    }
}
