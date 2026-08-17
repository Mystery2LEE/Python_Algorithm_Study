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

            // 0 w : 1, : b, 2 : r
            int[][] arr = new int[N][3];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                String s = st.nextToken();
                for (int j = 0; j < M; j++) {
                    char c = s.charAt(j);
                    if (c == 'W')
                        arr[i][0]++;
                    else if (c == 'B')
                        arr[i][1]++;
                    else if (c == 'R')
                        arr[i][2]++;
                }
            }

            int result = Integer.MAX_VALUE;

            for (int i = 0; i < N - 2; i++) {
                int white = 0;
                for (int w = 0; w <= i; w++) {
                    white += M - arr[w][0];
                }

                for (int j = i + 1; j < N - 1; j++) {
                    int blue = 0;
                    for (int b = i + 1; b <= j; b++) {
                        blue += M - arr[b][1];
                    }

                    int red = 0;
                    for (int k = j + 1; k < N; k++) {
                        red += M - arr[k][2];
                    }
                    result = Math.min(result, white + blue + red);
                }
            }
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
