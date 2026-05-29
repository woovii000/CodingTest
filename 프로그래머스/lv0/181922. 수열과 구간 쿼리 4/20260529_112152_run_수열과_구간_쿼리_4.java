class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr.copy();
        for(int i=0; i<queries.length; i++){
            if(i%queries[i][2]==0){
                answer[i] += 1;
            }
        }
        return answer;
    }
}