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
            int N = sc.nextInt();
           List<String> list = new ArrayList<>();
           for(int i = 0; i <N; i++){
                String s = sc.next();
                list.add(s);
           }
            //여기서 홀수면 5 / 2
            Queue<String>  front= new LinkedList<>();
           Queue<String> back = new LinkedList<>();
            
            if(N % 2 == 1) N++;
            
            for(int i = 0; i <N / 2; i++){
                front.add(list.get(i));
            }
            
            for(int i = N/2; i <list.size(); i++){
                back.add(list.get(i));
            }
            
            List<String> answer = new ArrayList<>();
            
            while(!front.isEmpty() || !back.isEmpty()) {
                if(!front.isEmpty()) answer.add(front.poll());
                if(!back.isEmpty()) answer.add(back.poll());
            }
            
            StringBuilder sb = new StringBuilder();
            for(String s : answer) {
                sb.append(s);
                sb.append(" ");
            }
            
            System.out.println("#" + test_case + " " + sb.toString());
        }
    }
}