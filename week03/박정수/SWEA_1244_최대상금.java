import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int C;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char[] num = st.nextToken().toCharArray();
            N = num.length;
            C = Integer.parseInt(st.nextToken());

            String result = find(num);
            sb.append("#").append(test_case).append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static String find(char[] arr) {
        Set<String> set = new HashSet<>();
        set.add(new String(arr));

        for (int i = 0; i < C; i++) {
            Set<String> cur = new HashSet<>();
            for (String s : set) {
                char[] num = s.toCharArray();
                for (int k = 0; k < N - 1; k++) {
                    for (int j = k + 1; j < N; j++) {
                        swap(num, k, j);
                        cur.add(new String(num));
                        swap(num, k, j);
                    }
                }
            }
            set = cur;
        }

        List<String> list = new ArrayList<>(set);
        list.sort((a, b) -> {
            return b.compareTo(a);
        });

        return list.get(0);
    }

    public static void swap(char[] arr, int a, int b) {
        char temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
