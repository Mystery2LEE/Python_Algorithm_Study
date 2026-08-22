import java.util.*;
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            List<Integer>[] graph = new ArrayList[V + 1];
            for (int i = 0; i <= V; i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph[from].add(to);
                graph[to].add(from);
            }

            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int G = Integer.parseInt(st.nextToken());

            boolean[] visited = new boolean[V + 1];
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[] { S, 0 });
            visited[S] = true;

            int count = 0;
            while (!q.isEmpty()) {
                int[] info = q.poll();

                if (info[0] == G) {
                    count = info[1];
                    break;
                }

                for (int node : graph[info[0]]) {
                    if (visited[node])
                        continue;
                    visited[node] = true;
                    q.add(new int[] { node, info[1] + 1 });
                }
            }

            result.append("#").append(test_case).append(" ").append(count).append("\n");
        }

        System.out.println(result.toString());
    }
}
