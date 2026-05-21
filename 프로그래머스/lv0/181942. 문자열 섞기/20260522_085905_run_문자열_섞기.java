class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        for(int i=0; i<str1.length(); i++){
            answer += str1[i];
            answer += str2[i];
        }
        return answer;
    }
}