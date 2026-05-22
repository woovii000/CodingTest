class Solution {
    public String solution(String my_string, int k) {
        String answer = "";
        for(int i=0; i<k; i++){
            for(int j=0; i<my_string.length(); j++){
                answer += my_string[j];
            }
        }
        return answer;
    }
}