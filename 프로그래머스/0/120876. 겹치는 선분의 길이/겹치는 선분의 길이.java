//전체탐색(브루트포스) 알고리즘
//다시풀기

class Solution {
    public int solution(int[][] lines) {
        //범위 -100~100 -> 0~200 크기 정하기(음수 좌표 해결)
        //점-점 겹치는 경우(끝점포함x) -> for(i=start; <end; ++)
        //3개가 동시에 겹친다. -> 겹치는게 2개 이상이면 갯수++
        int[] arr = new int[201]; // -100 ~ 100 → 201칸
        int answer = 0;

        for (int i = 0; i < lines.length; i++) {
            int start = lines[i][0] + 100;
            int end = lines[i][1] + 100;

            for (int j = start; j < end; j++) {
                arr[j]++;
            }
        }

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 2) {
                answer++;
            }
        }

        return answer;
    }
}