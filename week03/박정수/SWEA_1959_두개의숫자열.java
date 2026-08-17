import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] arrN = new int[N];
            int[] arrM = new int[M];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arrN[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                arrM[i] = Integer.parseInt(st.nextToken());
            }

            long result = findMax(arrN, arrM);

            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static long findMax(int[] arr1, int[] arr2) {
        int N = arr1.length;
        int M = arr2.length;
        if (N > M)
            return findMax(arr2, arr1);

        long result = Long.MIN_VALUE;

        for (int i = 0; i <= M - N; i++) {
            long sum = 0;
            for (int j = 0; j < N; j++) {
                sum += arr1[j] * arr2[i + j];
            }
            result = Math.max(result, sum);
        }

        return result;
    }
}
