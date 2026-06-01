import java.util.Arrays;

class Solution {
    public String solution(String my_string, int[][] queries) {
        String[] answer = new String[my_string.length()];
        for(int i=0; i<answer.length; i++){
            answer[i] = my_string.valueOf(i);
        }
        for(int i=0; i<queries.length; i++){
            for(int j=0; j<(queries[i][1]-queries[i][0]+1)/2; j++){
                int temp = 0;
                temp = answer[queries[i][0]+i]; 
                answer[queries[i][0]+i] = answer[queries[i][1]-i];
                answer[queries[i][1]-i] = temp;
            }
        }
        return Arrays.toString(answer);
    }
}