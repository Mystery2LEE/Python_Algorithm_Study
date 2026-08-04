import java.util.*;

public class Solution {
    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);

        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {

        	int N = sc.nextInt();
        	int[][] arr = new int[N][100];
        	for(int i = 0; i < N; i++) {
        		int num = sc.nextInt();
        		for(int j = 0; j < num; j++) {
        			arr[i][j] = 1;
        		}
        	}
        	int max = 0;
        	for(int i = N -1; i >=0; i--) {
        		for(int j= 99; j >= 0; j--) {
        			if(arr[i][j] == 0) continue;
        			int count = 1;
        			while(i + count < N && arr[i + count][j] == 0) {
        				count++;
        			}
        			arr[i][j] = 0;
        			arr[i + count - 1][j] = 1;
        			max = Math.max(max, count - 1);
        		}
        	}
            System.out.println("#" + test_case + " " + max);
        }
    }
}