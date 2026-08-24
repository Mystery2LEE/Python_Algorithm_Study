import java.util.*;

class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int K = sc.nextInt();

            // 잠만 정렬을 하던 안하던 상관이 없나....????
            int[] bupi = new int[N];
            int[] value = new int[N];
            int[] score = new int[K + 1];

            for (int i = 0; i < N; i++) {
                bupi[i] = sc.nextInt();
                value[i] = sc.nextInt();

            }

            for (int i = 0; i < N; i++) {
                for (int j = K; j >= bupi[i]; j--) {
                    score[j] = Math.max(score[j], score[j - bupi[i]] + value[i]);
                }
            }

            int max = 0;
            for (int i = 0; i <= K; i++) {
                max = Math.max(max, score[i]);
            }
            System.out.println("#" + test_case + " " + max);
        }
    }
}
