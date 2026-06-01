class Solution {
    public int solution(String number) {
        int sum = 0;
        for(int i=0; i<number.length(); i++){
            sum += (int)(number.chatAt(i)-'0');
        }
        return sum%9;
    }
}