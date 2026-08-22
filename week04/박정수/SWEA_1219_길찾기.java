import java.util.*;
import java.io.*;

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = 10;

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int test_num = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            List<Integer>[] graph = new ArrayList[100];
            for (int i = 0; i < 100; i++) {
                graph[i] = new ArrayList<>();
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph[from].add(to);
            }

            boolean[] visited = new boolean[100];
            Queue<Integer> q = new LinkedList<>();
            q.add(0);
            visited[0] = true;

            int ok = 0;
            while (!q.isEmpty()) {
                int cur = q.poll();

                if (cur == 99) {
                    ok = 1;
                    break;
                }

                for (int node : graph[cur]) {
                    if (visited[node])
                        continue;
                    visited[node] = true;
                    q.add(node);
                }
            }

            result.append("#").append(test_case).append(" ").append(ok).append("\n");
        }

        System.out.println(result.toString());
    }
}
