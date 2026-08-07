import java.util.*;

class Solution
{	
   public static class Node{
       int idx;
       int val;
       
       Node(int idx, int val){
           this.idx = idx;
           this.val = val;
       }
   }
   
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            
            Queue<Node> drum = new LinkedList<>();
            Queue<Node> wait = new LinkedList<>();
            
            for(int i = 0; i < M; i++) {
                int num = sc.nextInt();
                if(drum.size() < N) drum.add(new Node(i + 1, num));
                else wait.add(new Node(i + 1, num));
            }
            
            while(drum.size() != 1) {
                Node node = drum.poll();
                if(node.val / 2 == 0) {
                    if(!wait.isEmpty()) drum.add(wait.poll());
                }else {
                    drum.add(new Node(node.idx, node.val /2));
                }
            }
            
           System.out.println("#" + test_case + " " + drum.poll().idx);
        }
    }
}