package basic;
//this is the code for finding the second largest element in the array without sorting the array
import java.util.List;

public class secondlargest {
    class Solution {
    public int print2largest(List<Integer> arr) {
        //below code is for converting the list to array
        Integer[] arr1=arr.toArray(new Integer[0]);
        int n=arr1.length;
        int fe=arr1[0];
        int se=-1;
        for(int i=1;i<n;i++)
        {
            if(fe<arr1[i])
            {
                se=fe;
                fe=arr1[i];
            }
            else if(fe>arr1[i]&&arr1[i]>se){
                se=arr1[i];
            }
        }
        return se;
    }
}
}
