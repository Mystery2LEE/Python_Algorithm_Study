import java.util.*;

class UserSolution {
	//마지막에 공격했던게 사정거리에 있다면 공격대상 유지 이거 어캐함?????
	public static class Node{
		//체력있어야되고....
		int idx;
		int hp;
		Node(int idx, int hp){
			this.idx = idx;
			this.hp = hp;
		}
	}
	
	public static class Tower{
		//스캔 가능한 목록 
		List<Integer> area;
		int remainTime;
		int interval;
		int lastAttack;
		
		Tower(int remainTime, int interval, int lastAttack){
			this.area = new ArrayList<>();
			this.remainTime = remainTime;
			this.interval = interval;
			this.lastAttack = lastAttack;
		}
	}
	static int N;
	static int[][]map;
	static List<int[]> points;
	static int[] start;
	static int[] end;
	static int[][] move = new int[][] {{-1,0},{1,0},{0,1},{0,-1}};
	static List<Tower> towers;
	static Node[] roads;
	void init(int N, int mMap[][]){
		this.N= N;
		map = new int[N][N];
		points = new ArrayList<>();
		towers = new ArrayList<>();
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				map[i][j] = mMap[i][j];
				if(map[i][j] == 2) start = new int[] {i,j};
				if(map[i][j] == 3) end = new int[] {i,j};
			}
		}
		
		Queue<int[]> q = new LinkedList<>();
		boolean visited[][] = new boolean[N][N];
		q.add(start);
		visited[start[0]][start[1]] = true;
		
		while(!q.isEmpty()) {
			int[] point = q.poll();
			points.add(point);
			if(point[0] == end[0] && point[1] == end[1]) {
				break;
			}
			
			for(int i = 0; i < 4; i++) {
				int nextR = point[0] + move[i][0];
				int nextC = point[1] + move[i][1];
				if(nextR >= 0 && nextR < N && nextC >= 0 && nextC < N && !visited[nextR][nextC]
						&& map[nextR][nextC] != 0) {
					visited[nextR][nextC] = true;
					int[] nextPoint = new int[] {nextR, nextC};
					q.add(nextPoint);
				}
			}
		}
		
		roads = new Node[points.size()];
	}
	
	void addTower(int mRow, int mCol, int mInterval)
	{
		//tower가 지켜보고있는 point들 탐색??????????????????????? 모든 타워의 공격거리는 3
		//완탐 합시더
		Tower tower = new Tower(0, mInterval, -1);
		for(int i = 0; i < points.size(); i++) {
			int dist = Math.abs(mRow - points.get(i)[0]) + Math.abs(mCol - points.get(i)[1]);
			if(dist <= 3) {
				tower.area.add(i);
			}	
		}
		towers.add(tower);
	}

	void runSimulation(int M, int mInterval, int mHP, int mRetTs[], int mRetHP[]) {
		int time = 0;
		int curIdx = 0;
		int sum = 0;
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
			//0번째 인덱스는 hp , 1번째는 인덱스 인덱스가 크면 먼저 나오아야ㅕ함 
			if(a[0] == b[0]) return b[1] - a[1];
				return a[0] - b[0];
		}) ;
		
		for (Tower tower : towers) {
		    tower.lastAttack = -1;
		    tower.remainTime = 0;
		}
		
		while(true) {
			//우선 공격대상 먼저 확인..해야함
			List<Integer> attacked = new ArrayList<>();
			//우선 순위 
			//1. 이전에 공격한 노드 
			//2. 체력이 적은거
			//3. 거리가 가장 먼거?
			for(Tower tower : towers) {
				if(tower.remainTime == 0){
					//여기서 이제 우선순위해서 공격 대상 선택해야되는거고
					pq.clear();
					for(int area : tower.area) {
						//이게 이제 몇번째 도로에 node가 있고 뭘 공격해야할지 선택해야함
						Node node = roads[area];
						if(node == null) continue;
						//노드가 존재해
						if(node.idx == tower.lastAttack) {
							pq.add(new int[] {0, area, node.idx});
							break;
						}
						pq.add(new int[] {node.hp, area, node.idx});
					}
					
					if(pq.size() > 0) {
						int[] info = pq.poll();
						attacked.add(info[1]);
						tower.lastAttack = info[2];
						tower.remainTime = tower.interval - 1;
					}else {
						tower.lastAttack = -1;
					}
				}else {
					tower.remainTime--;
				}
			}
		
			//공격하고 이제 시간에 맞줘서 옆으로 하나씩 이동시켜야하나?ㅇㅇ
			for(int idx : attacked) {
				Node node = roads[idx];
				if(node == null) continue;
				node.hp--;
				if(node.hp <= 0) {
					sum++;
					roads[idx] = null;
					mRetTs[node.idx] = time;
					mRetHP[node.idx] = 0;
				}
			}
			
			//옆으로 하나씩 이동 ㄱㄱ
			if(time != 0 && time % mInterval == 0) {
				// 1. 한 칸씩 전진
				for (int i = roads.length - 2; i >= 0; i--) {
				    if (roads[i] != null) {
				        roads[i + 1] = roads[i];
				        roads[i] = null;
				    }
				}
				
				// 2, 이미 도착지에 있던거 보
				if (roads[roads.length - 1] != null) {
				    Node node = roads[roads.length - 1];
				    roads[roads.length - 1] = null;
				    sum++;
				    mRetTs[node.idx] = time;
				    mRetHP[node.idx] = node.hp;
				}

				// 3 새롭ㄱ 스폰
				if (curIdx < M) {
				    roads[0] = new Node(curIdx, mHP);
				    curIdx++;
				}
			}
			
//			for(int i = 0; i < roads.length; i++) {
//				System.out.print((roads[i] == null ? 0 : roads[i].hp) + " " );
//			}
//			System.out.println();
			if(sum == M) break;
			time++;
		}
		
	}
}
