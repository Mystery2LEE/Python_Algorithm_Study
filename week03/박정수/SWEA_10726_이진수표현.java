import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        String on = "ON";
        String off = "OFF";
        for (int test_case = 1; test_case <= T; test_case++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            // 이진수 표현의 마지막 N비트가 모두 1인지 확인
            String status = on;
            for (int i = 0; i < N; i++) {
                if ((M >> i) % 2 == 0) {
                    status = off;
                    break;
                }
            }
            sb.append("#").append(test_case).append(" ").append(status).append("\n");
        }

        System.out.println(sb.toString());
    }
}