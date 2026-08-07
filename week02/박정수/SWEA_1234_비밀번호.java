import java.util.*;

class Solution
 {
 	public static void main(String args[]) throws Exception
 	{
 		Scanner sc = new Scanner(System.in);
 		int T;
 		T=10;

 		for(int test_case = 1; test_case <= T; test_case++) {
 			int N = sc.nextInt();
 			String s = sc.next();
 			
 			Stack<Integer> stack = new Stack<>();
 			for(int i = 0; i < s.length(); i++) {
 				int num = s.charAt(i) - '0';
 				
 				if(stack.isEmpty()) {
 					stack.add(num);
 					continue;
 				}
 				
 				if(stack.peek() == num) stack.pop();
 				else stack.add(num);
 			}
            
 			StringBuilder sb = new StringBuilder();
 			while(!stack.isEmpty()) sb.append(stack.pop());
            System.out.println("#" + test_case + " " + sb.reverse().toString());
 		}
 	}
 }