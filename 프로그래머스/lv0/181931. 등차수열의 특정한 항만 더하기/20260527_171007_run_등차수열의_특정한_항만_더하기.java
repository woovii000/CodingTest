class Solution {
    public int solution(int a, int d, boolean[] included) {
        int sum = 0;
        for(int i=0; i<boolean.size(); i++){
            if(boolean[i]){
                sum += a+i*d;
            }
        }
        return sum;
    }
}