class Solution {
    public int solution(int n) {
        //규칙 찾기-> 없어. 그냥 찾아
        int num=0;
        int count=0;
        while(count<n){ //*
            num++;  //*
            //숫자- 3의배수 || 3이 포함됨
            if(num%3==0 || String.valueOf(num).contains("3")){
                continue;
            }
            count++; //*
        }
        return num;
    }
}