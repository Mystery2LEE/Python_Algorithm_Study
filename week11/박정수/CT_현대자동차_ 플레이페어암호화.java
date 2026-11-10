import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String msg = sc.next();
        String key = sc.next();
        // Please write your code here.
        Character[][] arr = new Character[5][5];
        // 5*5채우기
        // 1. 우선 Set에 없는 것들을 먼저 채우기
        // 2. 남은 알파벳 채우기 JI 조심
        Set<Character> set = new HashSet<>();
        char[] chars = key.toCharArray();
        int size = chars.length;
        int k = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                while (k < size && set.contains(chars[k]))
                    k++;
                if (k >= size)
                    continue;
                set.add(chars[k]);
                arr[i][j] = chars[k];
            }
        }

        k = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] != null)
                    continue;
                while (k < 26 && (set.contains((char) ('A' + k)) || (char) ('A' + k) == 'J'))
                    k++;
                if (k >= 26)
                    continue;
                set.add((char) ('A' + k));
                arr[i][j] = (char) ('A' + k);
            }
        }

        // //일단
        // for(int i = 0; i < 5; i++){
        // for(int j = 0; j < 5; j++){
        // System.out.print(arr[i][j] + " ");
        // }
        // System.out.println();
        // }

        // 2. 키로 채워진 맵에서 S를 두 글자씩 나누기
        Queue<Character> q = new LinkedList<>();
        for (char c : msg.toCharArray())
            q.add(c);
        StringBuilder sb = new StringBuilder();

        while (!q.isEmpty()) {
            char c = q.poll();
            // 2.1 마지막 문자열일때 뒤에 X추가
            if (q.isEmpty()) {
                sb.append(c);
                sb.append('X');
                break;
            }

            // 마지막 문자열과 다르면 그대로 추가
            if (c != q.peek()) {
                sb.append(c);
                sb.append(q.poll());
                continue;
            }

            // 마지막 문자열과 동일하면 가운데에 X 단, 양쪽이 X이면 Q로 추
            if (c == q.peek()) {
                if (c == 'X') {
                    sb.append(c);
                    sb.append('Q');
                    continue;
                }
                sb.append(c);
                sb.append('X');
            }
        }

        // 3. 같은행 같은 열, 다를때 나눠서 진행
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < sb.length(); i += 2) {
            int[] points1 = find(arr, sb.charAt(i));
            int[] points2 = find(arr, sb.charAt(i + 1));

            if (points1[0] == points2[0]) {
                points1[1] = (points1[1] + 1) % 5;
                points2[1] = (points2[1] + 1) % 5;
                answer.append(arr[points1[0]][points1[1]]);
                answer.append(arr[points2[0]][points2[1]]);
                continue;
            }

            if (points1[1] == points2[1]) {
                points1[0] = (points1[0] + 1) % 5;
                points2[0] = (points2[0] + 1) % 5;
                answer.append(arr[points1[0]][points1[1]]);
                answer.append(arr[points2[0]][points2[1]]);
                continue;
            }

            int temp = points1[1];
            points1[1] = points2[1];
            points2[1] = temp;
            answer.append(arr[points1[0]][points1[1]]);
            answer.append(arr[points2[0]][points2[1]]);

        }

        System.out.println(answer.toString());
    }

    public static int[] find(Character[][] arr, char c) {
        int[] points = new int[2];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] == c) {
                    points[0] = i;
                    points[1] = j;
                }
            }
        }

        return points;
    }
}