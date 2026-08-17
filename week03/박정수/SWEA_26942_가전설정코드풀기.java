import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            StringBuilder result = new StringBuilder();
            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(String.valueOf(s.charAt(i)), 16);
                StringBuilder sb2 = new StringBuilder();

                while (num > 0) {
                    if (num % 2 == 0)
                        sb2.append(0);
                    else
                        sb2.append(1);
                    num /= 2;
                }

                while (sb2.length() < 4) {
                    sb2.append(0);
                }

                result.append(sb2.reverse().toString());
            }

            sb.append("#").append(test_case).append(" ").append(result.toString()).append("\n");
        }

        System.out.println(sb.toString());
    }
}