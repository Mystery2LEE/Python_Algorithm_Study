import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            int V1 = Integer.parseInt(st.nextToken());
            int V2 = Integer.parseInt(st.nextToken());

            int[] nodes = new int[V + 1];
            List<Integer>[] tree = new ArrayList[V + 1];

            for (int i = 0; i <= V; i++) {
                tree[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int v1 = Integer.parseInt(st.nextToken());
                int v2 = Integer.parseInt(st.nextToken());
                nodes[v2] = v1;
                tree[v1].add(v2);
            }

            // 뒤에서부터 시작해서 nodes의 연결되는 간선들을 찾기.
            Stack<Integer> v1Nodes = new Stack<>();
            Stack<Integer> v2Nodes = new Stack<>();
            linkNode(nodes, v1Nodes, V1);
            linkNode(nodes, v2Nodes, V2);
            int commonParent = 1;
            while (v1Nodes.peek().equals(v2Nodes.peek())) {
                commonParent = v1Nodes.pop();
                v2Nodes.pop();
            }

            int count = childCount(tree, commonParent);
            sb.append("#").append(test_case).append(" ")
                    .append(commonParent)
                    .append(" ")
                    .append(count)
                    .append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void linkNode(int[] nodes, Stack<Integer> link, int v) {
        while (nodes[v] != 0) {
            link.add(v);
            v = nodes[v];
        }
    }

    public static int childCount(List<Integer>[] tree, int start) {
        int count = 0;
        Queue<Integer> q = new LinkedList<>();

        q.add(start);

        while (!q.isEmpty()) {
            int node = q.poll();
            count++;
            for (int child : tree[node]) {
                q.add(child);
            }
        }

        return count;
    }
}