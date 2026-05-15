class Solution {
    public int solution(int[] common) {
        int answer = common[0];
        if(common[0] - common[1] == common[1] - common[2]){
            int plus = common[1] - common[0]; 
            answer += common.length*plus;
        } else {
            int count=0;
            double mul = common[1]/common[0];
            while(count != common.length){
                answer *= mul;
                count++;
            }
        }
        return answer;
    }
}