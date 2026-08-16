import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int[] boxs = new int[M];
            int[] person = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                boxs[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                person[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(boxs);
            Arrays.sort(person);

            int result = 0;
            int boxIdx = M - 1;
            int personIdx = N - 1;
            while (personIdx >= 0 && boxIdx >= 0) {
                int max = person[personIdx];
                while (boxIdx >= 0 && max < boxs[boxIdx])
                    boxIdx--;
                if (boxIdx >= 0) {
                    result += boxs[boxIdx];
                    boxIdx--;
                    personIdx--;
                }
            }
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
