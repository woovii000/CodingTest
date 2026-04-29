class Solution {
    public String solution(String[] id_pw, String[][] db) {
        //2중 for - 둘다 일치 "login", 둘다x "fail", pwx "wrong pw"
        String answer = ""; 
        for(int j=0; j<db.length; j++){ 
            if(id_pw[0].equals(db[j][0]) && id_pw[1].equals(db[j][1])){
                answer = "login";
            }else if(id_pw[0].equals(db[j][0]) && !id_pw[1].equals(db[j][1])){
                answer = "wrong pw";
            }else if(!id_pw[0].equals(db[j][0]) && !id_pw[1].equals(db[j][1])){
                answer = "fail";
            }
        }
        return answer;
    }
}