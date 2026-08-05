import java.util.*;

public class Solution
{	
	
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{	
			int N = sc.nextInt();
			int M = sc.nextInt();
			int K = sc.nextInt();
			
			//시작 위치 맨 앞 구슬
			//장인 다음 규칙 사용해서 구슬 끼원허음
			//현재 작업 위치에서 M칸 앞으로 그자리에 새구슬을 끼워넣음 (위치 지정) 
			//새 구슬에 새길 숫자는 바로 앞 칸의 구슬 숫자와 그자리에서 뒤로 밀려나는 구슬 숫자를 더한 값이다. (값 지정)
			// 이제 새로 끼운 구슬 위치가 다음 작업의 위치가 됨
			//M칸을 세는 도중 줄의 마지막 구슬을 지나면 남은 칸 수는 맨앞 구슬부터 샌다 .
			//만약 정확히 줄의 끝을 지나서 다시 처음에 닿아
			
			List<Integer> list = new LinkedList<>();
			
			for(int i = 0; i < N; i++) {
				list.add(sc.nextInt());
			}
			
			//기준점에서 시작
			int start = 0;
			for(int i = 0; i < K; i++) {
				int nextStart = (start + M) % list.size();
				
				if(nextStart != 0) {
					int value = list.get(nextStart - 1) + list.get(nextStart);
					list.add(nextStart, value);
				}else {
					//0이면 마지막 + 
					list.add(list.get(0) + list.get(list.size() - 1));
					start = list.size() - 1;
					continue;
				}
				
				start = nextStart;
			}
			
			StringBuilder sb = new StringBuilder();
			for(int i = list.size() -1; i >= list.size() - 10; i--) {
				if(i >= 0) {
					sb.append(list.get(i));
					sb.append(" ");
				}else break;
			}
			System.out.println("#" + test_case + " " + sb.toString());
		}
	}
} 