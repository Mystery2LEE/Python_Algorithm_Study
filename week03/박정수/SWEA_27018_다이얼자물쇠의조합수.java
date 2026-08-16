import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int S;
    static int result;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            S = Integer.parseInt(st.nextToken());
            result = 0;
            dfs(0, 0);
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void dfs(int count, int sum) {
        if (sum > S)
            return;

        if (count == N) {
            if (sum == S) {
                result++;
            }
            return;
        }

        for (int i = 0; i <= 9; i++) {
            dfs(count + 1, sum + i);
        }
    }
}
