class Solution {
    public int[] solution(int[] num_list) {
        int l = num_list.length;
        List<Integer> list = new ArrayList<>();
        for(i : num_list){
            list.add(i);
        }
        if(num_list[l-1]>num_list[l-2]){
            list.add(num_list[l-1]-num_list[l-2]);
        }else{
            list.add(num_list[l-1]*2);
        }
        return list;
    }
}