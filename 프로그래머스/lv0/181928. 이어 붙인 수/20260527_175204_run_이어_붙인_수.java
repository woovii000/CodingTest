class Solution {
    public int solution(int[] num_list) {
        String odd = "";
        String even = "";
        String answer = "";
        for(int i=0; i<num_list.length; i++){
            if(i%2==0){
                even += char(num_list[i]);
            }else{
                odd += char(num_list[i]);
            }   
        }
        answer = even+odd;
        return (int)answer;
    }
}