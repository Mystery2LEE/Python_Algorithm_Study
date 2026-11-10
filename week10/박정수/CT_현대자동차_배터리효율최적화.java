import java.util.*;

public class Main {
    static int N, M;
    static int[][] board;
    static int[] dr = { -1, 1, 0, 0 };
    static int[] dc = { 0, 0, -1, 1 };
    // key: (B-A 오프셋), value: 붙일 3칸 패턴들 (A 기준 상대좌표)
    static HashMap<String, List<int[][]>> pat = new HashMap<>();
    static int[][] cur = new int[5][2];
    static HashSet<String> seen;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        board = new int[N][M];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                board[i][j] = sc.nextInt();

        // 1. 오프셋별 3칸 패턴 미리 구하기
        for (int r = -4; r <= 4; r++) {
            for (int c = -4; c <= 4; c++) {
                if (Math.abs(r) + Math.abs(c) == 0 || Math.abs(r) + Math.abs(c) > 4)
                    continue;
                List<int[][]> list = new ArrayList<>();
                seen = new HashSet<>();
                cur[0][0] = 0;
                cur[0][1] = 0;
                cur[1][0] = r;
                cur[1][1] = c;
                build(2, list);
                pat.put(r + "," + c, list);
            }
        }

        // 2. 4중 for문으로 A, B 고르기
        int max = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = i; k < N; k++) {
                    for (int l = (k == i ? j + 1 : 0); l < M; l++) {
                        List<int[][]> list = pat.get((k - i) + "," + (l - j));
                        if (list == null)
                            continue; // 거리 4 초과

                        // 3. 보드 위에 올려서 후보 모으기
                        List<int[]> cand = new ArrayList<>();
                        for (int[][] p : list) {
                            int[] ids = new int[3];
                            boolean ok = true;
                            for (int t = 0; t < 3; t++) {
                                int r = i + p[t][0], c = j + p[t][1];
                                if (r < 0 || r >= N || c < 0 || c >= M) {
                                    ok = false;
                                    break;
                                }
                                ids[t] = r * M + c;
                            }
                            if (ok)
                                cand.add(ids);
                        }

                        // 4. 서로 안 겹치는 두 후보 고르기
                        int base = board[i][j] + board[k][l];
                        for (int a = 0; a < cand.size(); a++) {
                            for (int b = a + 1; b < cand.size(); b++) {
                                if (disjoint(cand.get(a), cand.get(b))) {
                                    max = Math.max(max, base + sum(cand.get(a)) + sum(cand.get(b)));
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println(max);
    }

    // A, B에서 3칸 붙이기 (고른 칸 전체에서 뻗음)
    static void build(int cnt, List<int[][]> list) {
        if (cnt == 5) {
            if (!connected())
                return;
            int[][] p = { cur[2].clone(), cur[3].clone(), cur[4].clone() };
            Arrays.sort(p, (x, y) -> x[0] != y[0] ? x[0] - y[0] : x[1] - y[1]);
            if (seen.add(Arrays.deepToString(p)))
                list.add(p);
            return;
        }
        for (int t = 0; t < cnt; t++) {
            for (int d = 0; d < 4; d++) {
                int nr = cur[t][0] + dr[d], nc = cur[t][1] + dc[d];
                boolean used = false;
                for (int u = 0; u < cnt; u++)
                    if (cur[u][0] == nr && cur[u][1] == nc)
                        used = true;
                if (used)
                    continue;
                cur[cnt][0] = nr;
                cur[cnt][1] = nc;
                build(cnt + 1, list);
            }
        }
    }

    static boolean connected() {
        boolean[] vis = new boolean[5];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        vis[0] = true;
        int count = 1;
        while (!q.isEmpty()) {
            int x = q.poll();
            for (int o = 0; o < 5; o++) {
                if (vis[o])
                    continue;
                if (Math.abs(cur[x][0] - cur[o][0]) + Math.abs(cur[x][1] - cur[o][1]) == 1) {
                    vis[o] = true;
                    q.add(o);
                    count++;
                }
            }
        }
        return count == 5;
    }

    static boolean disjoint(int[] x, int[] y) {
        for (int a : x)
            for (int b : y)
                if (a == b)
                    return false;
        return true;
    }

    static int sum(int[] ids) {
        int s = 0;
        for (int id : ids)
            s += board[id / M][id % M];
        return s;
    }
}