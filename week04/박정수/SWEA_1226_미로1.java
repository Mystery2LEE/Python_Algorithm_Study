import java.util.*;

class Solution {

    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);

        // int T = sc.nextInt();

        for (int test_case = 1; test_case <= 10; test_case++) {
            int testcase = sc.nextInt();
            int N = 16;

            int[][] arr = new int[N][N];
            boolean[][] visited = new boolean[N][N];

            int startX = -1;
            int startY = -1;
            int endX = -1;
            int endY = -1;

            for (int i = 0; i < N; i++) {
                String s = sc.next();
                for (int j = 0; j < N; j++) {
                    int n = s.charAt(j) - '0';
                    if (n == 2) {
                        startX = i;
                        startY = j;
                    }

                    if (n == 3) {
                        endX = i;
                        endY = j;
                    }

                    arr[i][j] = n;
                }
            }

            boolean find = false;

            Queue<int[]> q = new LinkedList<>();
            q.add(new int[] { startX, startY });
            visited[startX][startY] = true;

            int[][] dir = new int[][] { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
            while (!q.isEmpty()) {
                int[] point = q.poll();
                int x = point[0];
                int y = point[1];

                if (endX == x && endY == y) {
                    find = true;
                    System.out.println("#" + test_case + " " + 1);
                    break;
                }

                for (int i = 0; i < 4; i++) {
                    int nextX = x + dir[i][0];
                    int nextY = y + dir[i][1];

                    if (nextX >= 0 && nextX < N && nextY >= 0 && nextY < N && !visited[nextX][nextY]) {
                        if (arr[nextX][nextY] == 0 || arr[nextX][nextY] == 3) {
                            visited[nextX][nextY] = true;
                            q.add(new int[] { nextX, nextY });
                        }
                    }
                }
            }

            if (!find)
                System.out.println("#" + test_case + " " + 0);
        }

        sc.close(); // 사용이 끝난 스캐너 객체를 닫습니다.
    }
}
