class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int min_value = 1000000;
        for(int i=0; i<queries.length; i++){
            for(int j=queries[i][0]; j<=queries[i][1]; j++){
                   if(queries[i][2]<arr[j]){
                       min_value = Math.min(min_value,arr[j]);
                   }
                }
            }
            if(min_value != queries[i][2]){
                answer[i] = min_value;
            }else{
                answer[i] = -1;
            }
        }
        return answer;
    }
}