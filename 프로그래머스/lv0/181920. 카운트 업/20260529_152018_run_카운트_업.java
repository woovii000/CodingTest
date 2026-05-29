import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int start_num, int end_num) {
        List<Integer> num = new ArrayList<>();
        for(int i=start_num; i<=end_num; i++){
            num.add(i);
        }
        int[] answer = new int[num.size()];
        for(int i=0; i<num.size(); i++){
            answer[i] = num.get(i);
        }
        return answer;
    }
}