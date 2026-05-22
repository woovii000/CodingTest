class Solution {
    public int solution(int a, int b) {
        String A = String.valueOf(a);
        String B = String.valueOf(b);
        if( Integer.parseInt(A+B) >= Integer.parseInt(B+A)){ return Integer.parseInt(A+B); }
        else { return Integer.parseInt(B+A);}
    }
}