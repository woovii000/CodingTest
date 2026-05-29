import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        List<Integer> num = new ArrayList<>();
        num.append(n)
        while(n != 1){
            if(n%2==0){ n /= 2; }
            else{n = 3*n+1;}
            num.append(n)
        }
        int[] answer = new int[num.size()];       
        for(int i = 0; i < num.size(); i++){
            arr[i] = num.get(i);
        }
        return answer;
    }
}