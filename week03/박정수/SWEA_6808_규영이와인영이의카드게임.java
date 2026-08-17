import java.io.*;
import java.util.*;

public class Solution {

    static int N;
    static int win;
    static int lose;
    static boolean[] visited;
    static List<Integer> cards1;
    static List<Integer> cards2;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            N = 9;

            visited = new boolean[19];
            win = 0;
            lose = 0;
            cards1 = new ArrayList<>();
            cards2 = new ArrayList<>();

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(st.nextToken());
                cards1.add(num);
                visited[num] = true;
            }

            for (int i = 1; i < 19; i++) {
                if (!visited[i])
                    cards2.add(i);
            }

            dfs(0, 0, 0);

            sb.append("#").append(test_case).append(" ").append(win).append(" ").append(lose).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void dfs(int idx, int score1, int score2) {
        if (idx == N) {
            if (score1 > score2)
                win++;
            else if (score1 < score2)
                lose++;
            return;
        }

        int card1 = cards1.get(idx);
        for (int i = 0; i < 9; i++) {
            int card2 = cards2.get(i);
            if (!visited[card2]) {
                visited[card2] = true;
                if (card1 > card2)
                    dfs(idx + 1, score1 + card1 + card2, score2);
                else
                    dfs(idx + 1, score1, score2 + card1 + card2);
                visited[card2] = false;
            }
        }
    }
}
