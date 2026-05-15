class Solution {
    public int[] solution(int num, int total) {
        //i+0 i+1 i+2 i+3 ... i+num-1
        //= i*num + (0~num-1 합)
        int sum = 0; 
        for(int i=0; i<num; i++){ sum += i; }
        int n = (total-sum) / num;
        int[] answer = new int[num];
        for(int i=0; i<num; i++){
            answer[i] = n + i;
        }
        return answer;
    }
}