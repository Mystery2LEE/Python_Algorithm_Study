import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int count = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            count = 0;
            boolean[][] visited = new boolean[N][N];
            dfs(0, visited);

            sb.append("#").append(test_case).append(" ").append(count).append("\n");
        }

        System.out.println(sb.toString());
    }

    static int[][] dir = { { -1, 0 }, { -1, -1 }, { -1, 1 }, { 1, 0 }, { 1, -1 }, { 1, 1 }, { 0, 1 }, { 0, -1 } };

    public static void dfs(int row, boolean[][] visited) {
        if (row == N) {
            count++;
            return;
        }
        boolean[][] prevVisited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            prevVisited[i] = visited[i].clone();
        }

        for (int i = 0; i < N; i++) {
            if (visited[row][i])
                continue;

            for (int j = 0; j < 8; j++) {
                int nextRow = row;
                int nextCol = i;
                while (nextRow >= 0 && nextRow < N && nextCol >= 0 && nextCol < N) {
                    visited[nextRow][nextCol] = true;
                    nextRow += dir[j][0];
                    nextCol += dir[j][1];
                }
            }

            dfs(row + 1, visited);
            for (int j = 0; j < N; j++) {
                visited[j] = prevVisited[j].clone();
            }

        }

    }
}
