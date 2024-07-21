package basic;

public class largestelement {
    class Solution {
        public static int largest(int n, int[] arr) {
            int m=arr[0];
            for(int i=1;i<n;i++){
                if (m < arr[i])
                m = arr[i];
            }
            return m;
        }
    }
    
}
