import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.next();
        int K = scanner.nextInt();
        int M = scanner.nextInt();
        // Please write your code here.
        //k이상이 M번 반복 
        //아 어차피 K만 반복이 된다면 어차피 K + 1이상은 의미가 없구나
        Map<Long, Integer> map = new HashMap<>();
        for(int i = 0; i < S.length() - K; i++){
            Long key = Long.parseLong(S.substring(i, i +K), 2);
             
            map.put(key, map.getOrDefault(key, 0) + 1);         
        }

        int answer = 0;
        for(int val : map.values()){
            if(val >= M){ answer = 1; break;}

        }
        System.out.println(answer);
    }
}
