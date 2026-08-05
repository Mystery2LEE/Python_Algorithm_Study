import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
	
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
	
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int K = sc.nextInt();
            Stack<Integer> stack = new Stack<>();
            for(int i = 0; i < K; i++){
                int num = sc.nextInt();
                if(num == 0){
                    stack.pop();
                }else{
                    stack.push(num);
                }
            }

            int sum = 0;
            while(!stack.isEmpty()){
                sum += stack.pop();
            }
		}
	}
}