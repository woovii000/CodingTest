class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if(ineq==">" && eq=="="){return n>=m ? 1:0;}
        else if(ineq=="<" && eq=="<"){return n<=m ? 1:0;}
        else if(ineq==">" && eq=="!"){return n>m ? 1:0;}
        else if(ineq=="<" && eq=="!"){return n<m ? 1:0;}
    }
}