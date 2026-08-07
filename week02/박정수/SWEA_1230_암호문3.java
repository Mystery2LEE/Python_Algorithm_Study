import java.util.*;

public class Solution {
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int T = 10;
		
		for(int test_case = 1; test_case <= T; test_case++) {
			int N = sc.nextInt();
			
			List<Integer> list = new LinkedList<>();
			for(int i = 0; i < N; i++) list.add(sc.nextInt());
			
			// 명령어 수 
			int M = sc.nextInt();
			
			for(int i = 0; i < M; i++) {
				String s = sc.next();
				if(s.equals("I")) {
					int x = sc.nextInt();
					int y = sc.nextInt();
					List<Integer> newList = new ArrayList<>();
					for(int j = 0; j < y; j++) {
						newList.add(sc.nextInt());
					}
					
					if(x >= list.size()) list.addAll(newList);
					else list.addAll(x, newList);
					
				}else if(s.equals("D")) {
					int x = sc.nextInt();
					int y = sc.nextInt();
					for(int j = 0; j < y; j++) {
						//이거 인덱스 초과할 가능성 없음????? 흠 
						list.remove(x);
					}
				}else {
					int y = sc.nextInt();
					for(int j = 0; j < y; j++) { 
						list.add(sc.nextInt());
					}
				}
				
			}
			
			System.out.print("#" + test_case + " ");
			for(int i = 0;i<10; i++) {
				System.out.print(list.get(i) + " ");
			}
			System.out.println();
		}
	}
}
