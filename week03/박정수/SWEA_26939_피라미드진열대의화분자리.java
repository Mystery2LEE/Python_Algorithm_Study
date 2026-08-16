import java.io.*;
import java.util.*;

public class Solution {
    static int n;
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            N = Integer.parseInt(br.readLine());
            n = 1;

            int[] arr = new int[N + 1];
            dfs(arr, 1);
            sb.append("#").append(test_case).append(" ").append(arr[1]).append(" ").append(arr[N / 2]).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void dfs(int[] arr, int num) {
        if (num > N)
            return;

        if (num * 2 > N && num * 2 + 1 > N) {
            arr[num] = n++;
            return;
        }
        dfs(arr, num * 2);
        arr[num] = n++;
        dfs(arr, num * 2 + 1);
    }
}
