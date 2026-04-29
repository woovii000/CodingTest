class Solution {
    public int solution(String[] babbling) {
        String[] word = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        for(int i=0; i<babbling.length; i++){
            String temp = babbling[i];//babbling 값 복사
            while(temp.length() > 0){ //길이가 0면 해당단어 제거 완료
                boolean matched = false; //해당하는지 확인
                
                for(String str : word){
                    if(temp.startsWith(str)){ //str로 시작하는지*
                        temp = temp.substring(str.length()); //첨부터 길이만큼 제거
                        matched = true; //해당함
                        break;
                    }
                }
                
                if(!matched){ //해당하지 않다면?
                    break;
                }
            }
            
            if(temp.length() == 0){
                answer++;
            }
        }
        return answer;
    }
}