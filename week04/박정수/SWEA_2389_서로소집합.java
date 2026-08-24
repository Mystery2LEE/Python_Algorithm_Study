import java.io.*;
import java.util.*;

public class Solution {

    static int[] node;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringBuilder answer = new StringBuilder();

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            node = new int[N + 1];
            for (int i = 0; i <= N; i++) {
                node[i] = i;
            }
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                String cmd = st.nextToken();
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if (cmd.equals("0")) {
                    union(a, b);
                } else {
                    if (find(a) == find(b))
                        answer.append(1);
                    else
                        answer.append(0);
                }
            }

            result.append("#").append(test_case).append(" ").append(answer.toString()).append("\n");
        }

        System.out.println(result.toString());
    }

    public static int find(int a) {
        if (node[a] == a)
            return a;
        return node[a] = find(node[a]);
    }

    public static boolean union(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        node[b] = a;
        return true;
    }
}
