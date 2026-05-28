class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for(int i=0; queries.length; i++){
            answer[i] = queries[i][1];
        }
        return answer;
    }
}