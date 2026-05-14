class Solution {
    public int solution(int M, int N) {
        //MN 중에 작은 애를 먼저 자르고 그만큼 자른 수
        //((큰수-1)*작은수+1)
        // if(M==N) {
        //     return M*N-1;
        // }else {
        //     int max = Math.max(M, N);
        //     int min = Math.min(M, N);
        //     return (min-1)+(max-1)*min;           
        // }
        return M*N-1;
    }
}