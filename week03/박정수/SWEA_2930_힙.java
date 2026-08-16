import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = Integer.parseInt(br.readLine());

            StringBuilder result = new StringBuilder();

            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                int cmd = Integer.parseInt(st.nextToken());

                if (cmd == 1) {
                    int num = Integer.parseInt(st.nextToken());
                    pq.add(num);
                } else {
                    if (pq.isEmpty())
                        result.append(-1).append(" ");
                    else
                        result.append(pq.poll()).append(" ");
                }
            }

            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
