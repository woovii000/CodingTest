class Solution {
    public int solution(int a, int b) {
        String A = Character.toString(a);
        String B = Character.toString(b);
        String C = A+B;
        String D = B+A;
        if(Integer.parseInt(C) >= Integer.parseInt(D)){ return Integer.parseInt(D); }
        else { return Integer.parseInt(D);}
    }
}