import java.util.*;
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] A = new int[N];
            int[] B = new int[M];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++)
                A[i] = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++)
                B[i] = Integer.parseInt(st.nextToken());

            Arrays.sort(A);
            int total = 0;
            for (int i = 0; i < M; i++) {
                if (binarySearch(0, N - 1, B[i], A))
                    total++;
            }

            result.append("#").append(test_case).append(" ").append(total).append("\n");
        }

        System.out.println(result.toString());
    }

    public static boolean binarySearch(int l, int r, int target, int[] arr) {
        // 초기값 : -1 1일때 왼쪽 0일때 오른쪽
        int isLeft = -1;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (arr[mid] == target)
                return true;

            if (arr[mid] < target) {
                // 만약 이전이 오른쪽이었다면 break
                if (isLeft == 0)
                    break;
                isLeft = 0;
                l = mid + 1;
            } else {
                if (isLeft == 1)
                    break;
                isLeft = 1;
                r = mid - 1;
            }
        }

        return false;
    }
}
