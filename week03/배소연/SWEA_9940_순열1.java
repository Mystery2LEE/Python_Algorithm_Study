import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());

            Set<Integer> set = new HashSet<>();
            boolean isOk = true;

            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(st.nextToken());

                if (num < 1 || num > N) {
                    isOk = false;
                }

                if (!set.add(num)) {
                    isOk = false;
                }
            }

            if (isOk) {
                System.out.println("#" + tc + " Yes");
            } else {
                System.out.println("#" + tc + " No");
            }
        }
    }
}