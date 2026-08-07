import java.util.*;

public class Solution {
	static int N;
	
	static class Node{
		int val;
		Node next;
		
		Node(){
			
		}
		
		Node(int val, Node next){
			this.val = val;
			this.next = next;
		}
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			
			Node head = new Node();
			
			for(int i = 0; i < N; i++) {
				int c = sc.nextInt();
				int id = sc.nextInt();
				Node node = new Node(id, null);
				if(c == 1) {
					//앞에 추가 
					Node next = head.next;
					head.next = node;
					node.next = next;
				}else {
					//뒤에 노드는 어캐 추적하지
					Node cur = head;
					while(cur.next != null) {
						cur = cur.next;
					}
					cur.next = node;
				}
			}
			
			StringBuilder sb = new StringBuilder();
			while(head.next != null) {
				head = head.next;
				sb.append(head.val);
				sb.append(" ");
			}
			System.out.println("#"+test_case+" " + sb.toString());
		}
	}
}
