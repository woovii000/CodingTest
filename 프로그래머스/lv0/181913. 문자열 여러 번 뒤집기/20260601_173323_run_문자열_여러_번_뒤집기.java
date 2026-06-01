class Solution {
    public String solution(String my_string, int[][] queries) {
        String[] answer = new String[my_string.length()];
        for(int i=0; i<my_string.length(); i++){
            answer[i] = my_string.charAt(i);
        }
        for(int i=0; i<queries.length; i++){
            for(int j=0; j<queries[1]-queries[0]+1; j++){
                int temp = 0;
                temp = answer[queries[0]+i]; 
                answer[queries[0]+i] = answer[queries[1]-i];
                answer[queries[1]-i] = temp;
            }
        }
        return Arrays.toString(answer);
    }
}