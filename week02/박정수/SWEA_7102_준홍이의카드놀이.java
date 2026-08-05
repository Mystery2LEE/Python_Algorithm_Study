import java.util.*;
public class Solution {
    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);

        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {

        	int N = sc.nextInt();
        	int M = sc.nextInt();
        	
        	Map<Integer, Integer> map = new HashMap<>();
        	
        	for(int i = 1; i <= N; i++) {
        		for(int j = 1; j <= M; j++) {
        			map.put(i + j, map.getOrDefault(i + j, 0) + 1);
        		}
        	}
        	
        	List<Integer> list = new ArrayList<>(map.values());
        	Collections.sort(list);
        	int max = list.get(list.size() - 1);
        	
        	List<Integer> answer = new ArrayList<>();
        	
        	for(int key : map.keySet()) {
        		if(map.get(key) == max) answer.add(key);
        	}
        	
        	Collections.sort(answer);
        	
            System.out.print("#" + test_case + " ");

            for (int num : answer) {
                System.out.print(num + " ");
            }

            System.out.println();
        }
    }
}