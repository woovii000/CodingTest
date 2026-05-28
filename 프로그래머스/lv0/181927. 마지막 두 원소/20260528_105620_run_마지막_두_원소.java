import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(int[] num_list) {
        int l = num_list.length;
        String answer = "";
        for(int i=0; i<l; i++){
            answer += num_list[i];
        }
        if(num_list[l-1]>num_list[l-2]){
            answer += num_list[l-1]-num_list[l-2];
        }else{
            answer += num_list[l-1]*2;
        }
        return Array.toString(answer);
    }
}