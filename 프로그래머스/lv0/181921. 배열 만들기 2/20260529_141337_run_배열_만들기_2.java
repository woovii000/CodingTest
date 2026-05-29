import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> num = new ArrayList<>();
        for(int i=l; i<=r; i++){
            if(String.valueOf(i).contains("0", "5")){
                
            }
        }
        int[] answer = new int[num.size()];
        for(int i=0; i<num.size(); i++){
            answer[i] = num.get(i);
        }
        return answer;
    }
}