package com.foundation.ds.array;

import java.util.ArrayList;
import java.util.List;

public class ContinuousMemory {

    public static List<Integer> getSubArraySum(int[] array, int reqSum) {
      List<Integer> result = new ArrayList<>();

      int start=0,end=0,sum=0;

      while(end < array.length){

          if(sum < reqSum)
            sum+=array[end++];

          while(sum>reqSum){
              sum-=array[start++];
          }
          if(sum==reqSum){
              break;
          }

      }
      result.add(start+1);
      result.add(end);

      return result;

    }
}
