
// import java.util.PriorityQueue;
// class Oct_14 {
//     public long maxKelements(int[] nums, int k) {
//         PriorityQueue<Integer> pq = new PriorityQueue<>();
//         for(int i:nums){
//             pq.offer(i);
//         }
//         long res=0;
//         for(int i=0;i<k;i++){
//             int curr=pq.poll();
//             res+=(int)curr;
//             pq.offer((int)((long)curr+2)/3);
//         }
//         return res;
//     }
// }