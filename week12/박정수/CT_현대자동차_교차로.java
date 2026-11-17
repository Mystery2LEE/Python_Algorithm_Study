import java.io.*;
import java.util.*;

class Main {
    //
    public static class Car implements Comparable<Car> {
        int num;
        int time;
        String road;

        Car(int num, int time, String road) {
            this.num = num;
            this.time = time;
            this.road = road;
        }

        @Override
        public int compareTo(Car o) {
            // A -> D, B -> A, C -> B, D -> C
            // if(this.time == o.time) return this.road.compareTo(o.road);
            return this.time - o.time;
        }
    }

    static Queue<Car> roadA;
    static Queue<Car> roadB;
    static Queue<Car> roadC;
    static Queue<Car> roadD;
    static int[] answer;

    public static void main(String[] args) throws Exception {
        // A,B,C,D 큐에 하나씩 넣어
        // 각 이전 타임 고려하면서. 이전 상황에 대한 정보를 넣어야하지않냐?0초면 그냥 추가만진행하고 1초면 하나빼야되고 이런식으로 해야될거같은데
        // 갑자기 3초차이면 FOR문만큼 돌리고 ? 갑자기 10억 나오면? ??? 아니 ㅅ 아 어차피
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        answer = new int[N];
        Arrays.fill(answer, -1);
        PriorityQueue<Car> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            String road = st.nextToken();
            pq.add(new Car(i, t, road));
        }
        roadA = new LinkedList<>();
        roadB = new LinkedList<>();
        roadC = new LinkedList<>();
        roadD = new LinkedList<>();

        while (!pq.isEmpty()) {
            Car cur = pq.poll();
            int curTime = cur.time;

            // System.out.println("cur : " + cur.time + " " + cur.road + " " + cur.num);
            insertRoad(cur);
            while (!pq.isEmpty() && cur.time == pq.peek().time) {
                insertRoad(pq.poll());
            }

            int nextTime = pq.isEmpty() ? Integer.MAX_VALUE : pq.peek().time;
            while (curTime < nextTime) {
                List<Car> list = new ArrayList<>();
                if (!roadA.isEmpty()) {
                    list.add(roadA.peek());
                }
                if (!roadB.isEmpty()) {
                    list.add(roadB.peek());
                }
                if (!roadC.isEmpty()) {
                    list.add(roadC.peek());
                }
                if (!roadD.isEmpty()) {
                    list.add(roadD.peek());
                }
                // 만약 전부 차있으면 break;
                // 이전 시간 비교해서 그 시간동안 WHILE 돌려야하나???/??????//????????/
                // 그러니까 a와 d가 문제잖아 a와 d를 비교를 하면 되지않냐????
                // 0 , 1, 2, 3 ->
                // System.out.print("------------" + curTime + "------------" );
                // for(int i = 0; i < list.size(); i++) {
                // System.out.print(list.get(i).road + " ");
                // }
                // System.out.println();
                int size = list.size();
                if (size == 4)
                    break;

                else if (size == 3) {
                    // 하나만 빈경우,
                    Car car = list.get(0);
                    if (list.get(0).road.equals("A") && list.get(2).road.equals("D")) {
                        if (list.get(1).road.equals("C"))
                            car = list.get(1);
                        else
                            car = list.get(2);
                    }
                    // System.out.println(car.num);
                    removeCar(car);
                    answer[car.num] = curTime;
                }

                else if (size == 2) {
                    Car car1 = list.get(0);
                    Car car2 = list.get(1);
                    // System.out.println("size2" + car1.road + " " + car2.road);
                    if ((car1.road.equals("A") && car2.road.equals("C"))
                            || (car1.road.equals("B") && car2.road.equals("D"))) {
                        removeCar(car1);
                        // System.out.println(car1.num + car2.num);

                        answer[car1.num] = curTime;
                        removeCar(car2);
                        answer[car2.num] = curTime;
                    } else {
                        // 여기 뭔가 꼬였는데;
                        if (car1.road.equals("A") && car2.road.equals("D")) {
                            answer[car2.num] = curTime;
                            removeCar(car2);
                        } else {
                            answer[car1.num] = curTime;
                            removeCar(car1);
                        }
                        // System.out.println(car1.num);
                    }
                }

                else if (size == 1) {
                    Car car = list.get(0);
                    // System.out.println(car.num);
                    removeCar(car);
                    answer[car.num] = curTime;
                }

                else if (size == 0)
                    break;

                curTime++;
            }
            // Queue에 있는 것들 계산
            // A -> D, B -> A, C -> B, D -> C
            // 일단 a, b, c, d에 전부 있으면 제거

        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(answer[i]).append("\n");
        }
        System.out.println(sb.toString());
    }

    public static void insertRoad(Car c) {
        switch (c.road) {
            case "A": {
                roadA.add(c);
                break;
            }

            case "B": {
                roadB.add(c);
                break;
            }

            case "C": {
                roadC.add(c);
                break;
            }

            case "D": {
                roadD.add(c);
                break;
            }
        }
    }

    public static void removeCar(Car c) {
        // System.out.println("remove : " + c.road);
        switch (c.road) {
            case "A": {
                roadA.poll();
                break;
            }

            case "B": {
                roadB.poll();
                break;
            }

            case "C": {
                roadC.poll();
                break;
            }

            case "D": {
                roadD.poll();
                break;
            }
        }
    }
}
