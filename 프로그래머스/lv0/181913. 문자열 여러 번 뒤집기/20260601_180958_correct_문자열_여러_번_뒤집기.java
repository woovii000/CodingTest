import java.util.Arrays;

class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] answer = my_string.toCharArray();
        for(int i=0; i<queries.length; i++){
            for(int j=0; j<(queries[i][1]-queries[i][0]+1)/2; j++){
                char c = 'a';
                c = answer[queries[i][0]+j]; 
                answer[queries[i][0]+j] = answer[queries[i][1]-j];
                answer[queries[i][1]-j] = c;
            }
        }
        String a = "";
        for(int i=0; i<answer.length; i++){
            a += answer[i];
        }
        return a;
    }
}