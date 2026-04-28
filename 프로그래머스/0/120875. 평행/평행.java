class Solution {
    public int solution(int[][] dots) {
        //각 선분의 기울기 동일 시, 1 / 모든 경우x -> 0
        int lean = 0;
        //케이스 별로(12-34/13-24/14-23) 기울기 확인(모두 구해야할까?)
        double lna1 = (double)(dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0]);
        double lnb1 = (double)(dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0]);
        double lna2 = (double)(dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0]);
        double lnb2 = (double)(dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0]);
        double lna3 = (double)(dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0]);
        double lnb3 = (double)(dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0]);
        if((lna1==lnb1) || (lna2==lnb2) || (lna3==lnb3)){
            lean = 1;
        }
        return lean;
    }
}