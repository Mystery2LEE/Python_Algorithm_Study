import java.util.*;
import java.io.*;

public class Solution {
    static int[][] dir = new int[][] { { -1, 0 }, { 0, 1 }, { 0, -1 }, { 1, 0 } };

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder();

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            int[][] arr = new int[N][N];

            int sr = -1;
            int sc = -1;
            int er = -1;
            int ec = -1;

            for (int i = 0; i < N; i++) {
                String s = br.readLine();
                for (int j = 0; j < N; j++) {
                    arr[i][j] = s.charAt(j) - '0';
                    if (arr[i][j] == 2) {
                        sr = i;
                        sc = j;
                    }

                    if (arr[i][j] == 3) {
                        er = i;
                        ec = j;
                    }
                }
            }
            int count = 0;
            boolean[][] visited = new boolean[N][N];
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[] { sr, sc, 0 });

            while (!q.isEmpty()) {
                int[] info = q.poll();
                int curR = info[0];
                int curC = info[1];
                int curT = info[2];

                if (curR == er && curC == ec) {
                    count = curT - 1;
                    break;
                }

                for (int i = 0; i < 4; i++) {
                    int nextR = curR + dir[i][0];
                    int nextC = curC + dir[i][1];
                    if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < N && arr[nextR][nextC] != 1
                            && !visited[nextR][nextC]) {
                        visited[nextR][nextC] = true;
                        q.add(new int[] { nextR, nextC, curT + 1 });
                    }
                }

            }

            result.append("#").append(test_case).append(" ").append(count).append("\n");
        }

        System.out.println(result.toString());
    }
}
