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
            int B = Integer.parseInt(st.nextToken());
            List<Integer> list = new ArrayList<>();

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int h = Integer.parseInt(st.nextToken());
                int size = list.size();
                list.add(h);
                for (int j = 0; j < size; j++) {
                    list.add(list.get(j) + h);
                }
            }

            Collections.sort(list);

            int result = 0;
            for (int num : list) {
                if (num >= B) {
                    result = (num - B);
                    break;
                }
            }
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
