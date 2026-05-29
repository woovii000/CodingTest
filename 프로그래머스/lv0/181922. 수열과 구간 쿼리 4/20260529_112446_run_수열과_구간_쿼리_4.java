import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        for(int i=0; i<queries.length; i++){
            if(i%queries[i][2]==0){
                answer[i] += 1;
            }
        }
        return answer;
    }
}