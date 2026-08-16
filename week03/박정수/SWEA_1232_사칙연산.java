import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = 10;

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            List<Integer>[] nodes = new ArrayList[N + 1];
            for (int i = 0; i <= N; i++) {
                nodes[i] = new ArrayList<>();
            }
            String[] arr = new String[N + 1];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int node = Integer.parseInt(st.nextToken());

                String oper = st.nextToken();
                arr[node] = oper;
                if (oper.equals("+") || oper.equals("-") || oper.equals("*") || oper.equals("/")) {
                    int leftChild = Integer.parseInt(st.nextToken());
                    int rightChild = Integer.parseInt(st.nextToken());
                    nodes[node].add(leftChild);
                    nodes[node].add(rightChild);
                }
            }

            int result = dfs(arr, nodes, 1);

            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static int dfs(String[] arr, List<Integer>[] nodes, int start) {
        String s = arr[start];
        if (!s.equals("+") && !s.equals("-") && !s.equals("*") && !s.equals("/")) {
            return Integer.parseInt(s);
        }
        int left = nodes[start].get(0);
        int right = nodes[start].get(1);
        if (s.equals("+"))
            return dfs(arr, nodes, left) + dfs(arr, nodes, right);
        else if (s.equals("-"))
            return dfs(arr, nodes, left) - dfs(arr, nodes, right);
        else if (s.equals("*"))
            return dfs(arr, nodes, left) * dfs(arr, nodes, right);
        else
            return dfs(arr, nodes, left) / dfs(arr, nodes, right);
    }
}
