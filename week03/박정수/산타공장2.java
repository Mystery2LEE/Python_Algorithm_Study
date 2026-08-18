import java.util.*;
import java.io.*;

public class Main {
    /***
     * 선물 공장
     * 각 벨트의 정보와 선물의 정보를 조회할 수 있는 기능들을 추가하여 새로운 공장을 만들고자 함.
     * 1. 공장 설립 - 선물 공장에 n개의 벨트를 설치, m개의 물건을 준비한다.
     * m개의 선물의 번호는 오름차순으로 벨트에 쌓인다.
     *
     * 2. 물건 모두 옮기기
     * m src 벨트에 있는 선물들을 -> m-dst 번째 벨트의 선물들로 옮긴다.
     * 옮겨진 선물들은 m dst 벨트 앞에 위치한다.
     * 만약 m-src가 비어있을 경우 옮기기 x
     * 그리고 옮긴 후 m-dst의 선물들 개수 출력
     *
     * 3. 앞 물건만 교체하기
     * m-src벨트에 있는 선물 중 -> m-dst번째 벨트의 선물들 중 가장 앞에 있는 선물과 교체
     * 둘 중 하나의 벨트에 선물이 없다면 교체X 해당 선물을 옮기기만 한다. -> 옮긴 후 m-dst 번째 벨트에 있는 선물 출력
     *
     * 4. 물건 나누기
     * m-src번째 선물의 개수를 n개라고 하면 가장 앞에서 floor(n/2) 번째까지 있는 선물을 m-dst로 옮김.
     * 만약 m-src벨트에 선물이 1개인 경우에는 선물을 옮기지 않는다. --> 옮긴 뒤 m-dst 선물 개수 출력 (head로 넣음)
     *
     * 5. 선물 정보 얻기
     * 해당 선물의 앞 선물 번호 a와 뒤 선물 b일 때 a + 2*b를 출력한다.
     * 만약 앞 선물 x -> a = -1, 뒤 x -> b = -1
     *
     * 6. 벨트 정보 얻기
     * 벨트의 맨 앞 선물 a, 맨 뒤 선물 b, 해당 라인의 선물 개수 c -> a + 2*b + 3*c 출력
     * 선물이 없는 경우 a, b = -1
     */

    public static class Belt {
        Box head;
        Box tail;
        int size;

        Belt(Box head, Box tail, int size) {
            this.head = head;
            this.tail = tail;
            this.size = size;
        }
    }

    public static class Box {
        int box;
        Box prev;
        Box next;

        Box(int box, Box prev, Box next) {
            this.box = box;
            this.prev = prev;
            this.next = next;
        }
    }

    static Belt[] belts;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int Q = Integer.parseInt(br.readLine());

        Map<Integer, Box> map = new HashMap<>();

        for (int c = 0; c < Q; c++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());

            if (command == 100) {
                int beltSize = Integer.parseInt(st.nextToken());
                int totalBox = Integer.parseInt(st.nextToken());

                belts = new Belt[beltSize + 1];

                // 벨트 초기화
                for (int i = 1; i <= beltSize; i++) {
                    Box head = new Box(0, null, null);
                    belts[i] = new Belt(head, head, 0);
                }

                // 벨트에 박스 넣기 (넣을 때마다 벨트의 tail, size 업데이트 필요)
                for (int i = 1; i <= totalBox; i++) {
                    int beltNum = Integer.parseInt(st.nextToken());
                    Belt belt = belts[beltNum];
                    Box box = new Box(i, belt.tail, null);
                    belt.tail.next = box;
                    belt.tail = box;
                    belt.size++;
                    map.put(i, box);
                }

            } else if (command == 200) {
                int src = Integer.parseInt(st.nextToken());
                int dst = Integer.parseInt(st.nextToken());
                Belt srcBelt = belts[src];
                Belt dstBelt = belts[dst];

                // src의 헤더는 동일하게 두고 src.next가 있는지 확인
                // src.next의 Node와 tail의 Node를 꺼내고
                // dst의 head.next를 src.next를 바라보게 하고
                // tail.next가 원본 dst의 head.next를 바라보게 하면 된다.
                if (srcBelt.size == 0) {
                    sb.append(dstBelt.size).append('\n');
                    continue;
                }

                Box temp = dstBelt.head.next;
                dstBelt.head.next = srcBelt.head.next;
                dstBelt.head.next.prev = dstBelt.head;
                srcBelt.tail.next = temp;
                if (temp != null)
                    temp.prev = srcBelt.tail;
                else {
                    dstBelt.tail = srcBelt.tail;

                }

                // 옮긴 후 크기 맞춰주기
                dstBelt.size += srcBelt.size;
                srcBelt.size = 0;

                // 헤더 초기화
                srcBelt.head.next = null;
                srcBelt.tail = srcBelt.head;

                sb.append(dstBelt.size).append('\n');

            } else if (command == 300) {
                int src = Integer.parseInt(st.nextToken());
                int dst = Integer.parseInt(st.nextToken());
                Belt srcBelt = belts[src];
                Belt dstBelt = belts[dst];

                if (srcBelt.head.next != null && dstBelt.head.next != null) {
                    // 두 개 바꿔야 하는 경우 (size가 1이라면 tail도 변경)
                    Box srcBox = srcBelt.head.next;
                    Box srcNextBox = srcBelt.head.next.next;
                    Box dstBox = dstBelt.head.next;
                    Box dstNextBox = dstBelt.head.next.next;

                    dstBelt.head.next = srcBox;
                    srcBelt.head.next = dstBox;
                    dstBelt.head.next.prev = dstBelt.head;
                    srcBelt.head.next.prev = srcBelt.head;

                    if (srcBelt.size == 1) {
                        srcBelt.head.next.next = null;
                        srcBelt.tail = srcBelt.head.next;
                    } else {
                        srcBelt.head.next.next = srcNextBox;
                        srcBelt.head.next.next.prev = srcBelt.head.next;
                    }

                    if (dstBelt.size == 1) {
                        dstBelt.head.next.next = null;
                        dstBelt.tail = dstBelt.head.next;
                    } else {
                        dstBelt.head.next.next = dstNextBox;
                        dstBelt.head.next.next.prev = dstBelt.head.next;
                    }

                } else if (srcBelt.head.next == null && dstBelt.head.next != null) {
                    // src는 비어있고 dst가 있을 때: dst 앞에서 하나만 꺼내오기
                    Box dstBox = dstBelt.head.next;
                    if (dstBelt.size > 1) {
                        Box dstNextBox = dstBelt.head.next.next;
                        dstNextBox.prev = dstBelt.head;
                        dstBelt.head.next = dstNextBox;
                    } else {
                        dstBelt.head.next = null;
                        dstBelt.tail = dstBelt.head;
                    }
                    srcBelt.head.next = dstBox;
                    srcBelt.head.next.next = null;
                    srcBelt.head.next.prev = srcBelt.head;
                    srcBelt.tail = srcBelt.head.next;
                    srcBelt.size++;
                    dstBelt.size--;

                } else if (srcBelt.head.next != null && dstBelt.head.next == null) {
                    // src가 있고 dst는 비어있을 때: src 앞에서 하나만 꺼내서 dst로
                    Box srcBox = srcBelt.head.next;
                    if (srcBelt.size > 1) {
                        Box srcNextBox = srcBelt.head.next.next;
                        srcNextBox.prev = srcBelt.head;
                        srcBelt.head.next = srcNextBox;
                    } else {
                        srcBelt.head.next = null;
                        srcBelt.tail = srcBelt.head;
                    }
                    dstBelt.head.next = srcBox;
                    dstBelt.head.next.next = null;
                    dstBelt.head.next.prev = dstBelt.head;
                    dstBelt.tail = dstBelt.head.next;
                    dstBelt.size++;
                    srcBelt.size--;

                } else {
                    // 둘 다 없는 경우는 무시
                    sb.append(dstBelt.size).append('\n');
                    continue;
                }

                sb.append(dstBelt.size).append('\n');

            } else if (command == 400) {
                int src = Integer.parseInt(st.nextToken());
                int dst = Integer.parseInt(st.nextToken());
                Belt srcBelt = belts[src];
                Belt dstBelt = belts[dst];

                int midSize = srcBelt.size / 2;
                if (midSize < 1) {
                    sb.append(dstBelt.size).append('\n');
                    continue;
                }

                Box midBox = srcBelt.head;
                for (int i = 0; i < midSize; i++) {
                    midBox = midBox.next;
                }

                // src.head.next 부터 src.mid 까지 dst 앞으로 옮기기
                Box midNext = midBox.next;
                Box first = srcBelt.head.next;

                srcBelt.head.next = midNext; // src는 절반 뒤부터 연결
                midNext.prev = srcBelt.head;

                // dst 연결 (dst가 0일 때 tail 업데이트)
                if (dstBelt.size != 0) {
                    midBox.next = dstBelt.head.next;
                    dstBelt.head.next.prev = midBox;
                }
                midBox.next = dstBelt.head.next;
                dstBelt.head.next = first;
                first.prev = dstBelt.head;
                if (dstBelt.size == 0)
                    dstBelt.tail = midBox;

                srcBelt.size -= midSize;
                dstBelt.size += midSize;

                sb.append(dstBelt.size).append('\n');

            } else if (command == 500) {
                int boxNum = Integer.parseInt(st.nextToken());
                Box box = map.get(boxNum);
                int a = box.prev.box != 0 ? box.prev.box : -1;
                int b = box.next != null ? box.next.box : -1;
                sb.append(a + b * 2).append('\n');

            } else if (command == 600) {
                int beltNum = Integer.parseInt(st.nextToken());
                Belt belt = belts[beltNum];
                int front = belt.head.next != null ? belt.head.next.box : -1;
                int end = front == -1 ? -1 : belt.tail.box;
                sb.append(front + end * 2 + belt.size * 3).append('\n');
            }
            // printAllBox(belts);
        }
        System.out.println(sb.toString());
    }

    public static void printAllBox(Belt[] belts) {
        System.out.println("-------------------------");
        for (int i = 1; i < belts.length; i++) {
            Box cur = belts[i].head.next;
            System.out.print(i + " : ");
            while (cur != null) {
                System.out.print(cur.box + " ");
                cur = cur.next;
            }
            System.out.println();
            cur = belts[i].tail;
            while (cur != null) {
                System.out.print(cur.box + " ");
                cur = cur.prev;
            }
            System.out.println(" size : " + belts[i].size);
            System.out.println(" tail : " + belts[i].tail.box);
            System.out.println();
        }
    }
}
