import java.util.Collections;
import java.util.List;
import java.util.ArrayList;


class Solution {
    public int[] solution(String my_string) {
        List<Integer> list = new ArrayList<>();
        for(int i=0; i<my_string.length(); i++){
            if('0'<=my_string.charAt(i)&&my_string.charAt(i)<='9')
            list.add((int)(my_string.charAt(i)-'0'));
        }
        Collections.sort(list);
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}