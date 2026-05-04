class Solution {
    public int solution(int i, int j, int k) {
        int count = 0;
        String nums = "";
        //숫자 -> 문자열 변환. 첨부터 k있는지 검사. 있으면 count++;
        for(int a=i; a<=j; a++){
            nums += String.valueOf(a);
        }
        for(int b=0; b<nums.length(); b++){
            if(String.valueOf(nums.charAt(b)).equals(String.valueOf(k))) {
                count++;
            }
        }
        return count;
    }
}