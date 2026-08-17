import java.io.*;
import java.util.*;

public class Solution {
    static StringBuilder result;
    static String[] nodes;
    static List<Integer>[] tree;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = 10;

        for (int test_case = 1; test_case <= T; test_case++) {
            result = new StringBuilder();
            int N = Integer.parseInt(br.readLine());
            nodes = new String[N + 1];
            tree = new ArrayList[N + 1];

            for (int i = 0; i <= N; i++) {
                tree[i] = new ArrayList<>();
            }

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int node = Integer.parseInt(st.nextToken());
                String s = st.nextToken();

                nodes[node] = s;
                while (st.hasMoreTokens()) {
                    int num = Integer.parseInt(st.nextToken());
                    tree[node].add(num);
                }
            }

            dfs(1);

            sb.append("#").append(test_case).append(" ").append(result.toString()).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void dfs(int node) {
        if (tree[node].isEmpty()) {
            result.append(nodes[node]);
            return;
        }

        if (tree[node].size() >= 1)
            dfs(tree[node].get(0));
        result.append(nodes[node]);
        if (tree[node].size() > 1)
            dfs(tree[node].get(1));
    }
}
