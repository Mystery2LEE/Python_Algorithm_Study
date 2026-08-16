import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);

            String isYes = "Yes";
            for (int i = 0; i < N; i++) {
                if (i + 1 != arr[i]) {
                    isYes = "No";
                    break;
                }
            }
            System.out.println("#" + test_case + " " + isYes);
        }
    }
}