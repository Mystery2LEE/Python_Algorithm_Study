import java.util.*;

class UserSolution {
    // 상, 우, 하, 좌
    static int[][] move = new int[][] { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    // group은 0부터 시작
    static int groupNumber = 0;
    static List<Ice>[][] map;
    static int N;
    static Map<Integer, Integer> moveMap;

    public class Ice {
        int group;
        int height;
        int dir;

        Ice(int group, int height, int dir) {
            this.group = group;
            this.height = height;
            this.dir = dir;
        }
    }

    private final static int MAX_N = 100;

    static class RESULT {
        int[][] heights;

        RESULT() {
            heights = new int[MAX_N][MAX_N];
        }
    }

    // 각 빙하를 알고있어야하고.... 각 좌표마다 객체를 넣어야하나..?
    // 그러면 각 객체에 필요한 값은 좌표, 방향..................
    void init(int N, int M, int mIceBlock[][], int mIceGroup[][]) {
        this.N = N;
        map = new LinkedList[N][N];
        moveMap = new HashMap<>();
        groupNumber = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = new LinkedList<>();
            }
        }

        boolean visited[][] = new boolean[N][N];

        for (int i = 0; i < M; i++) {
            groupNumber++;
            int x = mIceGroup[i][1];
            int y = mIceGroup[i][0];
            int dir = mIceGroup[i][2];

            moveMap.put(groupNumber, dir);

            Queue<int[]> q = new LinkedList<>();
            q.add(new int[] { x, y });
            visited[x][y] = true;
            // 이거 얼음 번호도 필요한가 흠
            while (!q.isEmpty()) {
                int[] point = q.poll();
                int curX = point[0];
                int curY = point[1];

                map[curX][curY].add(new Ice(groupNumber, mIceBlock[curX][curY], dir));

                for (int d = 0; d < 4; d++) {
                    int nextX = (N + curX + move[d][0]) % N;
                    int nextY = (N + curY + move[d][1]) % N;
                    // 벽은 신경 안쓰고..
                    if (mIceBlock[nextX][nextY] != 0 && !visited[nextX][nextY]) {
                        q.add(new int[] { nextX, nextY });
                        visited[nextX][nextY] = true;
                    }
                }
            }
        }
        return;

    }

    RESULT oneYearLater() {
        RESULT res = new RESULT();
        // 1. 융해
        // 10만

        List<int[]> removed = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j].isEmpty())
                    continue;
                else {
                    for (int d = 0; d < 4; d++) {
                        int x = (N + i + move[d][0]) % N;
                        int y = (N + j + move[d][1]) % N;
                        if (map[x][y].isEmpty()) {
                            Ice ice = map[i][j].get(0);
                            ice.height--;
                            if (ice.height == 0)
                                removed.add(new int[] { i, j });
                            break;
                        }
                    }
                }
            }
        }

        for (int[] remove : removed) {
            map[remove[0]][remove[1]].remove(0);
        }

        // 분리됐을 경우 그룹아이디를 증가
        boolean visited[][] = new boolean[N][N];
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] || map[i][j].isEmpty())
                    continue;
                Ice ice = map[i][j].get(0);
                if (set.contains(ice.group)) {
                    groupNumber++;
                    moveMap.put(groupNumber, ice.dir);
                    check(i, j, visited, groupNumber);
                }
                set.add(ice.group);
                check(i, j, visited, ice.group);
            }
        }

        // 2. 이동
        // 어차피 첫벗째 인덱스에 있는것들만 옮기면 된다............
        List<Ice>[][] movedMap = new LinkedList[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                movedMap[i][j] = new LinkedList<>();
            }
        }
        // for(int i = 0; i < N; i++) {
        // for(int j = 0; j < N; j++) {
        // if(map[i][j].isEmpty()) System.out.print(0 + " ");
        // else System.out.print(map[i][j].get(0).group + " ");
        // }
        // System.out.println();
        // }
        // System.out.println("--------------------------");

        // 왜 오른쪽으로 이동함??/?
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j].isEmpty())
                    continue;
                Ice ice = map[i][j].get(0);
                int nextX = (N + i + move[ice.dir][0]) % N;
                int nextY = (N + j + move[ice.dir][1]) % N;
                movedMap[nextX][nextY].add(ice);
            }
        }

        map = movedMap;
        //
        // System.out.println("--------------------------");
        // for(int i = 0; i < N; i++) {
        // for(int j = 0; j < N; j++) {
        // if(map[i][j].isEmpty()) System.out.print(0+" ");
        // else System.out.print(map[i][j].get(0).group+" ");
        // }
        // System.out.println();
        // }
        // System.out.println("--------------------------");

        // 3 병합
        // 인접한 노드가 있는지 그리고 겹친 노드들이 있는지 체크.......
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] || map[i][j].isEmpty())
                    continue;
                // cell merge
                merge(i, j, visited);
            }
        }
        // 리턴 부분

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!map[i][j].isEmpty())
                    res.heights[i][j] = map[i][j].get(0).height;
            }
        }

        // System.out.println("--------------------------");
        // for(int i = 0; i < N; i++) {
        // for(int j = 0; j < N; j++) {
        // if(map[i][j].isEmpty()) System.out.print(0+" ");
        // else System.out.print(map[i][j].get(0).height+" ");
        // }
        // System.out.println();
        // }
        // System.out.println("--------------------------");

        return res;
    }

    public void merge(int r, int c, boolean[][] visited) {
        // 부피
        Map<Integer, Integer> bupi = new HashMap<>();

        // 면적
        Map<Integer, Integer> size = new HashMap<>();

        Queue<int[]> q = new LinkedList<>();

        List<int[]> points = new ArrayList<>();
        q.add(new int[] { r, c });
        points.add(new int[] { r, c });
        visited[r][c] = true;

        while (!q.isEmpty()) {
            int[] point = q.poll();
            int curX = point[0];
            int curY = point[1];

            for (Ice ice : map[curX][curY]) {
                int group = ice.group;
                bupi.put(group, bupi.getOrDefault(group, 0) + ice.height);
                size.put(group, size.getOrDefault(group, 0) + 1);
            }

            for (int i = 0; i < 4; i++) {
                int nextX = (N + curX + move[i][0]) % N;
                int nextY = (N + curY + move[i][1]) % N;

                if (!visited[nextX][nextY] && !map[nextX][nextY].isEmpty()) {
                    visited[nextX][nextY] = true;
                    points.add(new int[] { nextX, nextY });
                    q.add(new int[] { nextX, nextY });
                }
            }
        }

        // 만약에 이어진게 있다면 map 사이즈가 무조건 2 이상

        // 1이면 바로 리턴;
        if (bupi.size() <= 1)
            return;

        Set<Integer> keySet = new HashSet<>();
        int max = 0;
        int minSize = Integer.MAX_VALUE;

        for (int key : bupi.keySet()) {
            if (bupi.get(key) > max) {
                keySet.clear();
                keySet.add(key);
                max = bupi.get(key);
                minSize = size.get(key);
            } else if (bupi.get(key) == max) {
                if (size.get(key) < minSize) {
                    keySet.clear();
                    keySet.add(key);
                    minSize = size.get(key);
                } else if (size.get(key) == minSize) {
                    keySet.add(key);
                }
            }
        }

        if (keySet.size() == 1) {
            int group = -1;
            for (int key : keySet)
                group = key;
            spread(r, c, group);
            return;
        }

        points.sort((a, b) -> {
            if (a[0] == b[0])
                return a[1] - b[1];
            return a[0] - b[0];
        });

        for (int[] point : points) {
            int x = point[0];
            int y = point[1];
            for (Ice ice : map[x][y]) {
                if (keySet.contains(ice.group)) {
                    spread(r, c, ice.group);
                    return;
                }
            }
        }
        return;
    }

    public void spread(int r, int c, int group) {
        boolean visited[][] = new boolean[N][N];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] { r, c });
        visited[r][c] = true;

        while (!q.isEmpty()) {
            int[] point = q.poll();
            int curX = point[0];
            int curY = point[1];

            int max = 0;
            for (Ice ice : map[curX][curY]) {
                max = Math.max(max, ice.height);
            }

            map[curX][curY].clear();
            map[curX][curY].add(new Ice(group, max, moveMap.get(group)));

            for (int i = 0; i < 4; i++) {
                int nextX = (N + curX + move[i][0]) % N;
                int nextY = (N + curY + move[i][1]) % N;

                if (!visited[nextX][nextY] && !map[nextX][nextY].isEmpty()) {
                    q.add(new int[] { nextX, nextY });
                    visited[nextX][nextY] = true;
                }
            }
        }

        return;
    }

    public void check(int r, int c, boolean[][] visited, int group) {

        Queue<int[]> q = new LinkedList<>();

        q.add(new int[] { r, c });
        visited[r][c] = true;

        while (!q.isEmpty()) {
            int[] point = q.poll();
            int curX = point[0];
            int curY = point[1];

            Ice curIce = map[curX][curY].get(0);
            curIce.group = group;

            for (int i = 0; i < 4; i++) {
                int nextX = (N + curX + move[i][0]) % N;
                int nextY = (N + curY + move[i][1]) % N;

                if (!visited[nextX][nextY] && !map[nextX][nextY].isEmpty()) {
                    visited[nextX][nextY] = true;
                    q.add(new int[] { nextX, nextY });
                }
            }
        }

        return;
    }
}
