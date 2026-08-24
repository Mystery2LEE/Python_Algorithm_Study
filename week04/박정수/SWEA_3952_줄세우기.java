import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            List<Integer>[] graph = new ArrayList[N + 1];
            int[] indegree = new int[N + 1];

            for (int i = 0; i <= N; i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph[from].add(to);
                // 위상정
                indegree[to]++;

            }

            boolean[] visited = new boolean[N + 1];
            Queue<Integer> q = new LinkedList<>();
            for (int i = 1; i <= N; i++) {
                if (indegree[i] == 0)
                    q.add(i);
            }

            StringBuilder sb = new StringBuilder();
            while (!q.isEmpty()) {
                int cur = q.poll();
                sb.append(cur).append(" ");
                // 이전노드들을 전부 방문 했는지 확인필요
                for (int node : graph[cur]) {
                    indegree[node]--;
                    if (!visited[node] && indegree[node] == 0) {
                        q.add(node);
                    }
                }
            }

            System.out.println("#" + test_case + " " + sb.toString());
        }
    }
}
