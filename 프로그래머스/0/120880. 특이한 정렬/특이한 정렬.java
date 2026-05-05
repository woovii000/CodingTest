//다시 풀 것
class Solution {
    public int[] solution(int[] numlist, int n) {

        for(int i = 0; i < numlist.length; i++){
            for(int j = i + 1; j < numlist.length; j++){

                int diffI = Math.abs(numlist[i] - n);
                int diffJ = Math.abs(numlist[j] - n);

                if(diffI > diffJ || (diffI == diffJ && numlist[i] < numlist[j])){
                    int temp = numlist[i];
                    numlist[i] = numlist[j];
                    numlist[j] = temp;
                }
            }
        }

        return numlist;
    }
}