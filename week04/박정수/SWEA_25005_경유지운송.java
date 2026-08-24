import java.util.*;

class UserSolution {
    static class Node implements Comparable<Node> {
        int to;
        int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return o.cost - this.cost;
        }
    }

    static List<Node>[] graph;
    static int N;

    public void init(int N, int K, int sCity[], int eCity[], int mLimit[]) {
        this.N = N;
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < K; i++) {
            int from = sCity[i];
            int to = eCity[i];
            int cost = mLimit[i];

            graph[from].add(new Node(to, cost));
            graph[to].add(new Node(from, cost));
            // roads.add(new Road(from, to ,cost));
        }

        return;
    }

    public void add(int sCity, int eCity, int mLimit) {
        graph[sCity].add(new Node(eCity, mLimit));
        graph[eCity].add(new Node(sCity, mLimit));
        return;
    }

    public int calculate(int sCity, int eCity, int M, int mStopover[]) {

        int MAX = Integer.MAX_VALUE;

        boolean visited[] = new boolean[N];
        PriorityQueue<Node> pq = new PriorityQueue<>();
        visited[sCity] = true;
        pq.addAll(graph[sCity]);

        while (!pq.isEmpty()) {
            // 일단 연결된 노드로 부터 가장 큰 노선 꺼내옴
            Node cur = pq.poll();
            if (visited[cur.to])
                continue;
            visited[cur.to] = true;

            MAX = Math.min(MAX, cur.cost);

            if (visited[eCity]) {
                boolean isConnected = true;
                for (int i = 0; i < M; i++) {
                    if (!visited[mStopover[i]]) {
                        isConnected = false;
                        break;
                    }
                }

                if (isConnected)
                    return MAX;
            }

            for (Node next : graph[cur.to]) {
                if (visited[next.to])
                    continue;
                pq.add(next);
            }
        }

        return -1;
    }
}