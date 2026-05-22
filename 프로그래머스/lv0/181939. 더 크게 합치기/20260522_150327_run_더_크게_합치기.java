class Solution {
    public int solution(int a, int b) {
        String[] A = String.valueOf(a);
        String[] B = String.valueOf(b);
        String C = "";
        String D = "";
        for(int i=0; i<A.length(); i++){
            C += A[i];
        }
        for(int i=0; i<B.length(); i++){
            C += B[i];
            D += A[i];
        }
        for(int i=0; i<B.length(); i++){
            C += B[i];
        }
        
        if(Integer.parseInt(C) >= Integer.parseInt(D)){ return Integer.parseInt(D); }
        else { return Integer.parseInt(D);}
    }
}