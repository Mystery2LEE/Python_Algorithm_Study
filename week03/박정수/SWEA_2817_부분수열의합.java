import java.io.*;
import java.util.*;

public class Solution {
    // 하루에 최대한 예약을 많이 받는법이란?
    public static class Time implements Comparable<Time> {
        int start;
        int end;

        Time(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Time o) {
            return this.end - o.end;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            Map<Integer, Integer> map = new HashMap<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(st.nextToken());
                List<Integer> keys = new ArrayList<>(map.keySet());
                keys.sort((a, b) -> {
                    return b - a;
                });
                for (int key : keys) {
                    map.put(key + num, map.get(key) + map.getOrDefault(key + num, 0));
                }
                map.put(num, map.getOrDefault(num, 0) + 1);
            }

            int result = map.getOrDefault(K, 0);
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
