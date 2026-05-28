class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for(int i=0; i<queries.length; i++){
            int min_value = Integer.MAX_VALUE;
            for(int j=queries[i][0]; j<=queries[i][1]; j++){
               if(queries[i][2]<arr[j])
                   min_value = Math.min(min_value,arr[j]);
            }
            if(min_value == Integer.MAX_VALUE){ answer[i] = -1; }
            else{ answer[i] = min_value; }   
        }
        return answer;
    }
}