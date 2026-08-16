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

            List<Time> times = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                times.add(new Time(start, end));
            }

            Collections.sort(times);

            boolean[] hour = new boolean[25];
            int result = 0;
            for (Time time : times) {
                boolean isOk = true;
                boolean[] newHour = hour.clone();
                for (int start = time.start; start < time.end; start++) {
                    if (hour[start]) {
                        isOk = false;
                        break;
                    } else {
                        hour[start] = true;
                    }
                }

                if (isOk) {
                    result++;
                } else {
                    hour = newHour;
                    continue;
                }
            }
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }
}
