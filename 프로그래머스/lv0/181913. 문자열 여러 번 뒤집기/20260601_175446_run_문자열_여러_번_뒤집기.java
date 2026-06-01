import java.util.Arrays;

class Solution {
    public String solution(String my_string, int[][] queries) {
        String[] answer = new String[my_string.length()];
        for(int i=0; i<answer.length; i++){
            answer[i] = my_string.charAt(i);
        }
        for(int i=0; i<queries.length; i++){
            for(int j=0; j<(queries[i][1]-queries[i][0]+1)/2; j++){
                String ch = "";
                c = answer[queries[i][0]+j]; 
                answer[queries[i][0]+j] = answer[queries[i][1]-j];
                answer[queries[i][1]-j] = ch;
            }
        }
        return Arrays.toString(answer);
    }
}