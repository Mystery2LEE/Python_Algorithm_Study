import java.util.*;

class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        List<Integer> list = new ArrayList<>();
        list.add(50000);
        list.add(10000);
        list.add(5000);
        list.add(1000);
        list.add(500);
        list.add(100);
        list.add(50);
        list.add(10);

        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int money = sc.nextInt();

            Map<Integer, Integer> map = new HashMap<>();

            for (int n : list) {
                if (money / n > 0) {
                    map.put(n, money / n);
                    money %= n;
                }
            }

            StringBuilder sb = new StringBuilder();
            for (int n : list) {
                sb.append(map.getOrDefault(n, 0)).append(" ");
            }
            System.out.println("#" + test_case + "\n" + sb.toString());
        }
    }
}