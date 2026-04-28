import java.util.Set;
import java.util.HashSet;
class Solution {
    public int solution(int a, int b) {
        //분모의 소인수 2 or 5인지 확인
        //기약분수 -> GCD - 유클리드 호제법
        int bg = b;
        int sm = a;
        int rest = 1;
        while(rest!=0){ //b%a = 몫(b/a) + 나머지(b%a)
            rest = bg % sm;
            bg = sm;
            sm = rest;
        }
        b = b/bg; //기약분수
        Set<Integer> num = new HashSet<>();
        int i=2;
        int answer = 1;
        while(b!=1){
            if(b%i==0){
                b = b/i;
                num.add(i);
            }else{
                i++;   
            }
        }
        for(Integer kkk : num){
            if(kkk != 2 && kkk != 5) answer = 2;
        }
        return answer;
    }
}