import java.util.*;
import java.io.*;

class Main {
    static int N;
    static int[] play;
    static int[] rank;
    static int[][] participant;
    static int[][] answer;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        answer = new int[4][N];
        participant = new int[4][N];

        for (int i = 0; i < 4; i++) {
            play = new int[3001];
            rank = new int[3001];
            if (i != 3)
                st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                if (i == 3)
                    break;
                int score = Integer.parseInt(st.nextToken());
                participant[i][j] = score;
                participant[3][j] += score;
                play[score]++;
            }

            if (i == 3) {
                for (int j = 0; j < N; j++) {
                    play[participant[i][j]]++;
                }
            }

            setRank(i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(answer[i][j]).append(" ");
            }
            System.out.println(sb.toString());
            sb = new StringBuilder();
        }
    }

    public static void setRank(int n) {
        int curRank = 1;
        for (int i = 3000; i >= 0; i--) {
            if (play[i] == 0)
                continue;

            rank[i] = curRank;
            curRank += play[i];
        }

        for (int i = 0; i < N; i++) {
            answer[n][i] = rank[participant[n][i]];
        }
    }
}
