import java.util.*;

public class Solution
{
	public static void main(String args[]) throws Exception
	{
//		 System.out.println("Hello World");
		Scanner sc = new Scanner(System.in);
		
		int T = 10;
		
		for(int test_case = 1; test_case <= T; test_case++) {
			
			int N = sc.nextInt();
			
			String s = sc.next();
			
			Stack<Character> stack = new Stack<>();
			
			boolean find = true;
			
			for(int i = 0; i < N; i++) {
				char c = s.charAt(i);
				if(c == '[' || c == '{' || c == '(' || c == '<') {
					stack.add(c);
				}else {
					if(stack.isEmpty()) {
						System.out.println("#" + test_case+ " " + 0);
						find = false;
						break;
					}
					
					char stackC = stack.pop();
					if((stackC == '[' && c == ']') || 
						(stackC == '{' && c == '}')	||
						(stackC == '(' && c == ')') ||
						(stackC == '<' && c == '>')) {
						continue;
					}else {
						System.out.println("#" + test_case+ " " + 0);
						find = false;
						break;
					}
				}
			}
			
			if(find)  System.out.println("#" + test_case+ " " + 1);
		}
	}
}