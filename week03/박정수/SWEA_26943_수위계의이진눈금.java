import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            double target = Double.parseDouble(br.readLine());

            StringBuilder result = new StringBuilder();

            double h = 0.0;
            double cur = 1;
            boolean find = false;
            for (int i = 0; i < 12; i++) {
                cur /= 2;
                if (target >= h + cur) {
                    h += cur;
                    result.append(1);
                } else {
                    result.append(0);
                }
                if (h == target) {
                    find = true;
                    break;
                }
            }

            sb.append("#").append(test_case).append(" ").append(find ? result : "overflow").append("\n");
        }

        System.out.println(sb);
    }
}
