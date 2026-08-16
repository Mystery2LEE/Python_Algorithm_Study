import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int M;
    static int result;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        Map<String, Integer> map = new HashMap<>();
        map.put("0001101", 0); // 0
        map.put("0011001", 1); // 1
        map.put("0010011", 2); // 2
        map.put("0111101", 3); // 3
        map.put("0100011", 4); // 4
        map.put("0110001", 5); // 5
        map.put("0101111", 6); // 6
        map.put("0111011", 7); // 7
        map.put("0110111", 8); // 8
        map.put("0001011", 9); // 9

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            String[] secret = new String[N];
            String codeLine = "";
            for (int i = 0; i < N; i++) {
                secret[i] = br.readLine();
                if (secret[i].contains("1"))
                    codeLine = secret[i];
            }

            codeLine = new StringBuilder(codeLine).reverse().toString().replaceFirst("[0]+", "");
            codeLine = new StringBuilder(codeLine).reverse().toString().substring(codeLine.length() - 56,
                    codeLine.length());
            int sum = 0;
            int valid = 0;
            for (int i = 0; i < 8; i++) {
                String sub = codeLine.substring(i * 7, (i + 1) * 7);
                int num = map.get(sub);
                sum += num;
                if (i % 2 == 0)
                    valid += (num * 3);
                else
                    valid += num;
            }

            int result = valid % 10 == 0 ? sum : 0;
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
