class Solution {
    public int solution(int a, int b) {
        String A = String.valueOf(a);
        String B = String.valueOf(b);
        if(Integer.parseInt(A+B) >= 2*a*b){ return Integer.parseInt(A+B); }
        else{ return 2*a*b; }
    }
}