import java.util.*;
import java.io.*;

public class Solution {
	
	public static void main(String args[]) throws IOException{
		Scanner sc =new Scanner(System.in);
		
		int T = sc.nextInt();
		sc.nextLine(); //개행 제거
		for(int test_case = 1; test_case <= T; test_case++) {
			String s = sc.nextLine();
			Stack<Character> stack = new Stack<>();
			boolean ok = true; 
			for(int i = 0; i < s.length(); i++) {
				char c = s.charAt(i);
				if(c == '(' || c== '{') {
					stack.push(c);
				} else if( c == ')' ||  c == '}') {
					if(stack.isEmpty()) {
						ok = false;
						break;
					}
					
					char in = stack.pop();
					if((in == '{' && c ==')') || (in == '(' && c == '}')) {
						ok = false;
						break;
					}
				} 
			}
			
			if(!stack.isEmpty()) ok = false;
			System.out.println("#" + test_case + " " + (ok ? 1 : 0));
		}
	}
}
